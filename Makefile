.PHONY: start

start:
	@echo "Starting bot and API..."
	@trap "make stop" INT TERM EXIT; \
	uv run python3 -m src.bot.bot & \
	uv run python3 -m src.api.main & \
	wait
