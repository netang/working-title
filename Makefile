build:
	docker-compose -f deployment/docker-compose.yaml build

up:
	docker-compose -f deployment/docker-compose.yaml up -d

down:
	docker-compose -f deployment/docker-compose.yaml down

ps:
	docker-compose -f deployment/docker-compose.yaml ps