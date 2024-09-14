compile-requirements:
	@pip-compile --no-strip-extras --quiet --resolver=backtracking --generate-hashes --allow-unsafe --output-file=requirements/base.txt requirements/base.in

test:
	pytest . --cov