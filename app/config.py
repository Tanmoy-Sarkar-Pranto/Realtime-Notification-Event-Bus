from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/notifications"
    rabbitmq_url: str = "amqp://guest:guest@localhost:5672/"
    redis_url: str = "redis://localhost:6379"

    rate_limit_requests: int = 100
    rate_limit_window: int = 60

    ws_heartbeat_interval: int = 30
    ws_heartbeat_timeout: int = 10


settings = Settings()
