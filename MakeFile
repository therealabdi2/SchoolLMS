ROOT_DIR:=./
SRC_DIR:=./src
VENV_BIN_DIR:="venv/bin"

VIRTUALENV:=$(shell which virtualenv)

REQUIREMENTS_DIR:="requirements"
REQUIREMENTS_LOCAL:="$(REQUIREMENTS_DIR)/local.txt"

PIP:="$(VENV_BIN_DIR)/pip"
FLAKE8:="$(VENV_BIN_DIR)/flake8"
ISORT:="$(VENV_BIN_DIR)/isort"

CMD_FROM_VENV:=". $(VENV_BIN_DIR)/activate; which"
PYTHON=$(shell "$(CMD_FROM_VENV)" "python")

define create-venv
virtualenv venv -p python3
endof

venv:
    @$(create-venv)
    @$(PIP) install -r $(REQUIREMENTS_LOCAL)

fix: venv
    @$(FLAKE8) src
    @$(ISORT) -rc -c src