import os
import yaml

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "configs",
    "config.yaml",
)

_DEFAULT_DISCOVERY_CONFIG = {
    "tile_server": "https://tiles.suhail.ai/maps/{region}/{z}/{x}/{y}.vector.pbf",
    "zoom10": 10,
    "zoom12": 12,
    "zoom15": 15,
    "max_radius": 30,
    "concurrency": 20,
}


def get_discovery_config():
    if not os.path.exists(CONFIG_PATH):
        return _DEFAULT_DISCOVERY_CONFIG.copy()
    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    return data.get("discovery", _DEFAULT_DISCOVERY_CONFIG)
