.PHONY: run, svl, test

run:
	docker-compose exec python bash -c "cd src && python simulate.py | python -m json.tool"

svl:
	docker-compose exec python bash -c "cd src && serverless invoke local -f fetch -d '{\"guid\": \"CDF001B001B\", \"profile\": \"5F5DA2E8-D4EF-45FA-AB7B-F49A6A3226DE\", \"platform\": \"web\", \"fields\":\"metadata,urls\"}'"

test:
	docker-compose exec python bash -c "cd src/fetchFunction && pytest"