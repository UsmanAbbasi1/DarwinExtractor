from pydantic.env_settings import BaseSettings
from pydantic.fields import Field


class DarwinConfig(BaseSettings):
    # TODO: The token will come from environment variable, never ever store secret and tokens in the code. This is
    #  for the sake of this task only. In production code, secrets should alwasy come from environment variables.
    access_token: str = Field(default="c570fb40-f784-3dd8-b784-ab29c2115986", env="ACCESS_TOKEN")
