up:
	docker-compose up

test: up
	docker-compose exec webapp python3 /app/manage.py test
