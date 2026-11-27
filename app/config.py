from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
     """Application settings, read from environment variables or a .env file."""

     model_config = SettingsConfigDict(env_file=".env" , extra="ignore") #Ignore Here Removes Extra Variables if present in .env file insteal of giveing error

     search_engine_url : str = "http://localhost:8000"
     search_engine_api_key : str = "" 
     ollama_host : str = "http://localhost:11434"
     model_name : str = "phi3:mini"
     top_k : int = 3 
     request_timeout : int = 30

@lru_cache
def get_settings() -> Settings:
    return Settings()