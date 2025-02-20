.PHONY: lock-example create-example-env all
lock-example:  ## create example conda-lock file
	conda-lock lock --update -f py312-example-env.yaml --lockfile py312-example-env-lock.yml

create-example-env:
	micromamba create -n python-packaging-tools-example-env  -f py312-example-env-lock.yml


all: lock-example create-example-env
