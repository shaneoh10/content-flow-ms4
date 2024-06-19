VENV = .venv

collectstatic:
	. $(VENV)/bin/activate && python3 manage.py collectstatic --noinput

createsuperuser:
	. $(VENV)/bin/activate && python3 manage.py createsuperuser

makemigrations:
	. $(VENV)/bin/activate && python3 manage.py makemigrations

migrate:
	. $(VENV)/bin/activate && python3 manage.py migrate

serve:
	. $(VENV)/bin/activate && python3 manage.py runserver

test:
	. $(VENV)/bin/activate && python3 manage.py test
