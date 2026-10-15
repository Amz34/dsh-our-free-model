test:
	python3 -m unittest discover -s tests -q

verify:
	python3 -m py_compile dsh_plugin/*.py tests/*.py
