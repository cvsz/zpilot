"""Static contract tests for independent review and safe rollout behavior."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github/workflows/request-independent-review.yml").read_text(encoding="utf-8")
ROLLOUT = (ROOT / "scripts/rollout-independent-review.sh").read_text(encoding="utf-8")


class IndependentReviewWorkflowTests(unittest.TestCase):
    def test_review_request_is_refreshed_on_head_updates(self):
        self.assertIn("synchronize", WORKFLOW)
        self.assertIn("pull_request_review:", WORKFLOW)
        self.assertIn("[submitted, dismissed]", WORKFLOW)

    def test_gate_requires_distinct_reviewer_on_exact_head(self):
        self.assertIn("verify-independent-approval:", WORKFLOW)
        self.assertIn("vars.INDEPENDENT_REVIEWER", WORKFLOW)
        self.assertIn("HEAD_SHA:", WORKFLOW)
        self.assertIn('.state == "APPROVED"', WORKFLOW)
        self.assertIn(".commit_id == $sha", WORKFLOW)
        self.assertIn("PR_AUTHOR", WORKFLOW)
        self.assertIn("gh api --paginate --slurp", WORKFLOW)
        self.assertIn("jq -e", WORKFLOW)
        self.assertNotIn("--slurp --jq", WORKFLOW)
        self.assertNotIn("policedbc", WORKFLOW)
        self.assertNotIn("actions/checkout", WORKFLOW)

    def test_permissions_are_scoped(self):
        self.assertIn("pull-requests: read", WORKFLOW)
        self.assertIn("pull-requests: write", WORKFLOW)
        self.assertNotIn("contents: write", WORKFLOW)

    def test_cross_repository_rollout_is_disabled(self):
        self.assertIn("Cross-repository workflow rollout is disabled", ROLLOUT)
        self.assertIn("exit 2", ROLLOUT)
        self.assertNotIn("gh api", ROLLOUT)
        self.assertNotIn("gh repo clone", ROLLOUT)
        self.assertNotIn("git push", ROLLOUT)


if __name__ == "__main__":
    unittest.main()
