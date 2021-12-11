start:
	docker-compose up --build

start-detach:
	docker-compose up --build --detach

migrations:
	docker exec -it docker_hw_hcs_1 python manage.py makemigrations

migrate:
	docker exec -it docker_hw_hcs_1 python manage.py migrate

clone-database:
	docker exec -it docker_hw_hcs_1 python manage.py loaddata mydata.json

stop:
	docker-compose stop

