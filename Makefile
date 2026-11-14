PYTHON ?= python3

.PHONY: help validate test lint discover ci

help:
	@printf '%s\n' 'make validate  - Validate repository structure and links' \
		'make test      - Run unit tests' \
		'make lint      - Compile Python sources' \
		'make discover  - Run read-only repository discovery' \
		'make ci        - Run all local checks'

validate:
	$(PYTHON) scripts/validate_repo.py

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m compileall -q zpilot.py scripts tests

discover:
	$(PYTHON) zpilot.py --discover-only --json

ci: validate lint test discover
