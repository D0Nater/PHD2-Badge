.PHONY: lint
lint:
	mypy --install-types --non-interactive --config-file setup.cfg .
	flake8 .

.PHONY: style
style:
	black . --check --diff
	isort . -c --diff

.PHONY: format
format:
	black .
	isort .

.PHONY: ftest
ftest: format test

.PHONY: flint
flint: format lint
