install:
	poetry install

check:
	poetry check

build:
	poetry build

package-install:
	pip install --user dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 validator tests

test:
	poetry run pytest
