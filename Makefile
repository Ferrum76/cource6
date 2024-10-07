migrate: migrations
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

run:
	python3 manage.py runserver


csu:
	python3 manage.py csu


send_mail:
	python3 manage.py send_mail