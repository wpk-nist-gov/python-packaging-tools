.PHONY: lock-example create-example-env install-kernel all
lock-example:
	uv pip compile --universal example-env.txt -o requirements.txt

create-example-env:
	uv venv .venv -p 3.12
	uv pip install -r requirements.txt

install-kernel:
	uv run python -m ipykernel install --user \
	--name python-packaging-tools-dev \
    --display-name "Python [venv: python-packaging-tools-dev]"

all: lock-example create-example-env install-kernel
