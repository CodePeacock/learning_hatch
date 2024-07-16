import asyncio
import sys
from dataclasses import dataclass
from loguru import logger
import os
import yaml

DEFAULT_CONFIG_FILE_FOLDER = f"{os.path.expanduser('~')}/.config/article_improver"
DEFAULT_CONFIG_FILE = "config.yaml"

FIELD_OPEN_AI_KEY = "open_ai_key"


@dataclass()
class Config:
    open_ai_key: str


def _read_config(config_file_folder: str, config_file: str) -> Config:
    file = (
        f"{config_file_folder}/{config_file}"
        if config_file_folder
        else f"{DEFAULT_CONFIG_FILE_FOLDER}/{DEFAULT_CONFIG_FILE}"
    )

    with open(file) as f:
        config_json = yaml.safe_load(f)
        return Config(config_json[FIELD_OPEN_AI_KEY])


def init(
    config_file_folder: str = None, config_file: str = None
) -> tuple[Config, asyncio.AbstractEventLoop]:
    logger.remove()
    logger.add(sys.stderr, format="{message}", level="INFO")
    try:
        cfg = _read_config(config_file_folder, config_file)
    except FileNotFoundError:
        print(f"No valid configuration file!, {FileNotFoundError}")
        cfg = None

    return (cfg, asyncio.get_event_loop_policy().get_event_loop())
