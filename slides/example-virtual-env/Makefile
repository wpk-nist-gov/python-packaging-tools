.PHONY: lock-example create-example-env install-kernel all
lock-example:
	uv pip compile -U --universal example-env.txt -o requirements.txt

create-example-env:
	uv venv .venv -p 3.12
	uv pip sync -p .venv/bin/python requirements.txt

install-kernel:
	uv run --python=.venv/bin/python -m ipykernel install --user \
	--name python-packaging-tools-example-dev \
    --display-name "Python [venv: python-packaging-tools-example-dev]"

all: lock-example create-example-env install-kernel
