from pydantic_settings import BaseSettings


class AIConfig(BaseSettings):
    SYSTEM_ROLE: str = """
        You are a professional code reviewer that reviews code of the vacancy candidates 
        on Github and gives feedback on it.
    """
    MODEL_NAME: str = 'gpt-4-turbo'
    TEMPERATURE: float = 0.0
