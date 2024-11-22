from pydantic_settings import BaseSettings


class GitHubConfig(BaseSettings):
    GITHUB_API_URL: str = 'https://api.github.com'
    GITHUB_API_KEY: str
