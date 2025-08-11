# Makefile for PyConc - Python Concurrency Examples

.PHONY: help install install-dev test test-coverage lint format clean run-example

# Default target
help:
	@echo "PyConc - Python Concurrency Examples"
	@echo "===================================="
	@echo ""
	@echo "Available targets:"
	@echo "  install         Install the package in development mode"
	@echo "  install-dev     Install with development dependencies"
	@echo "  test            Run all tests"
	@echo "  test-coverage   Run tests with coverage report"
	@echo "  lint            Run linting checks"
	@echo "  format          Format code with black"
	@echo "  clean           Clean build artifacts"
	@echo "  run-example     Run a specific example (use EXAMPLE=<name>)"
	@echo ""
	@echo "Examples:"
	@echo "  make run-example EXAMPLE=deadlock"
	@echo "  make run-example EXAMPLE=threadpool-polling-adaptive"
	@echo "  make test"
	@echo "  make lint"

# Install the package
install:
	pip3 install -e .

# Install with development dependencies
install-dev:
	pip3 install -e ".[dev]"

# Run all tests
test:
	python3 -m pytest tests/ -v

# Run tests with coverage
test-coverage:
	python3 -m pytest tests/ --cov=examples --cov-report=html --cov-report=term-missing

# Run linting checks
lint:
	python3 -m flake8 examples/ pyconc.py tests/
	python3 -m mypy examples/ pyconc.py

# Format code
format:
	python3 -m black examples/ pyconc.py tests/

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf examples/__pycache__/
	rm -rf examples/*/__pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Run a specific example
run-example:
	@if [ -z "$(EXAMPLE)" ]; then \
		echo "Error: Please specify an example with EXAMPLE=<name>"; \
		echo "Available examples:"; \
		python3 pyconc.py -h; \
		exit 1; \
	fi
	python3 pyconc.py -e $(EXAMPLE)

# Quick test of all examples (short duration)
test-all-examples:
	@echo "Testing all examples with short duration..."
	@for example in deadlock livelock starvation threadpool; do \
		echo "Testing $$example..."; \
		python3 pyconc.py -e $$example -d 1 || exit 1; \
	done
	@echo "All basic examples passed!"

# Development workflow
dev: install-dev format lint test

# Show project structure
structure:
	@echo "Project Structure:"
	@find . -name "*.py" -type f | sort

# Show available examples
examples:
	@echo "Available Examples:"
	@python3 pyconc.py -h 