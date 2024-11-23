from pydantic_settings import BaseSettings, SettingsConfigDict


class GitHubConfig(BaseSettings):
    GITHUB_API_URL: str = 'https://api.github.com'
    GITHUB_API_KEY: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
