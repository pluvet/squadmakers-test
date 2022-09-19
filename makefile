test:
	pytest -s -m "not integration"

test-integration:
	pytest -s