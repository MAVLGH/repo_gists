.PHONY: pyenv_install virtual_env_install reqs_install

pyenv_install:
	sudo ./install_pyenv.sh

virtual_env_install:
	pyenv install 3.11.4
	pyenv virtualenv 3.11.4 gists

reqs_install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip freeze > reqs_freeze.txt

run_solution:
	python flask_download_data.py