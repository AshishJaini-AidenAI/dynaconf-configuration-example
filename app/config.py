# app/config.py
from pathlib import Path
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[str(Path(__file__).parent.parent / "settings.toml")],
    environments=True,
    load_dotenv=True,
    env_switcher="ENV_FOR_DYNACONF",
)