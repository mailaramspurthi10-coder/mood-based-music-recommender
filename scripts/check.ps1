$ErrorActionPreference = "Stop"

python -m ruff format --check backend
python -m ruff check backend
python -m mypy backend
python -m vulture backend
python -m bandit -c pyproject.toml -r backend
python -m pylint backend
python -m flake8 backend
python -m semgrep --config .semgrep.yml backend

Write-Host "All developer checks passed."
