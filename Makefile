style:
	flake8 .

types:
	mypy .

tests:
	python -m pytest .

run:
	python -m main

check:
	make -j3 style types tests