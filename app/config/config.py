from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config import AIConfig
from app.config.github import GitHubConfig


class Config(BaseSettings):
    HOST: str
    PORT: int
    DEBUG: bool
    REDIS_HOST: str
    REDIS_PORT: int = 6379
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    ai: AIConfig = AIConfig()
    gh: GitHubConfig = GitHubConfig()


settings = Config()
