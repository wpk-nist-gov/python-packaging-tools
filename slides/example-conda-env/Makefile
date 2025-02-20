.PHONY: lock-example create-example-env all
lock-example:  ## create example conda-lock file
	@-rm py312-example-env-lock.yml
	conda-lock lock -f py312-example-env.yaml --lockfile py312-example-env-lock.yml -p osx-64

create-example-env:
	micromamba create -n python-packaging-tools-example-dev  -f py312-example-env-lock.yml -y


all: lock-example create-example-env
