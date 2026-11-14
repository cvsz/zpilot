"""Tests for ZPilot GitHub administration prerequisites."""

import unittest
from unittest.mock import patch

from scripts.github_admin import (
    DEFAULT_REPO,
    REQUIRED_CHECKS,
    configured_independent_reviewer,
    protection_payload,
    validate_independent_reviewer,
)


class IndependentReviewerAdminTests(unittest.TestCase):
    def test_zpilot_default_and_required_checks_are_current(self):
        self.assertEqual(DEFAULT_REPO, "cvsz/zpilot")
        self.assertIn("repository-baseline", REQUIRED_CHECKS)
        self.assertIn("Analyze GitHub Actions and Python", REQUIRED_CHECKS)
        self.assertIn("dependency-review", REQUIRED_CHECKS)
        self.assertIn("secret-scan", REQUIRED_CHECKS)
        self.assertIn("verify-independent-approval", REQUIRED_CHECKS)
        payload = protection_payload()
        self.assertEqual(set(REQUIRED_CHECKS), set(payload["required_status_checks"]["contexts"]))
        self.assertTrue(payload["required_status_checks"]["strict"])

    def test_review_policy_keeps_review_and_codeowner_requirements(self):
        reviews = protection_payload()["required_pull_request_reviews"]
        self.assertGreaterEqual(reviews["required_approving_review_count"], 1)
        self.assertTrue(reviews["require_code_owner_reviews"])
        self.assertTrue(reviews["dismiss_stale_reviews"])
        self.assertTrue(reviews["require_last_push_approval"])

    def test_reviewer_must_be_valid_and_distinct_from_owner(self):
        self.assertEqual(validate_independent_reviewer("cvsz/zpilot", "reviewer-account"), "reviewer-account")
        for reviewer in ("", "invalid/login", "cvsz", "bad name"):
            with self.subTest(reviewer=reviewer), self.assertRaises(ValueError):
                validate_independent_reviewer("cvsz/zpilot", reviewer)

    @patch("scripts.github_admin.gh_api")
    def test_configured_reviewer_reads_repository_variable(self, gh_api):
        gh_api.return_value = {"variables": [
            {"name": "OTHER_VARIABLE", "value": "unused"},
            {"name": "INDEPENDENT_REVIEWER", "value": "reviewer-account"},
        ]}
        self.assertEqual(configured_independent_reviewer("cvsz/zpilot"), "reviewer-account")
        gh_api.assert_called_once_with("GET", "repos/cvsz/zpilot/actions/variables?per_page=100")

    @patch("scripts.github_admin.gh_api")
    def test_missing_reviewer_variable_is_not_assumed(self, gh_api):
        gh_api.return_value = {"variables": []}
        self.assertIsNone(configured_independent_reviewer("cvsz/zpilot"))


if __name__ == "__main__":
    unittest.main()
