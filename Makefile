.PHONY: validate test viewer

validate:
	python3 code/project-dev/scripts/validate_structure.py

test:
	cd code/project-dev && python3 -m pytest

viewer:
	cd code/project-dev/analyses/preprint_figures/take1 && python3 server.py 8767
