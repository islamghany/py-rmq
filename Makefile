# Check to see if we can use ash, in Alpine images, or default to BASH.
SHELL_PATH = /bin/ash
SHELL = $(if $(wildcard $(SHELL_PATH)),/bin/ash,/bin/bash)


run:
	@python3 main.py


## Venv
create-venv:
	@python3 -m venv --prompt=rmq .venv
	@source ./.venv/bin/activate
	@pip install -r requirements.txt

deactivate:
	@deactivate
delete-venv:
	@rm -rf ./.venv

## mkvirtualenv

create-mkvirtualenv:
	@mkvirtualenv --python=/usr/bin/python3 rmq
	@workon rmq
	@pip install -r requirements.txt
delete-mkvirtualenv:
	@rmvirtualenv rmq

