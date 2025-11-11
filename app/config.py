# app/config.py
from pathlib import Path
from dynaconf import Dynaconf

ROOT = Path(__file__).resolve().parent.parent

settings = Dynaconf(
    settings_files=[str(ROOT / "settings.toml"), str(ROOT / "secrets.toml")],
    environments=True,
    env_switcher="ENV_FOR_DYNACONF",
    load_dotenv=True,
)