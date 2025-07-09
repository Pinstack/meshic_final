from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, ValidationError
import os
import yaml

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "..",
    "..",
    "configs",
    "config.yaml",
)
CONFIG_PATH = os.path.abspath(CONFIG_PATH)


class DiscoveryConfig(BaseSettings):
    database_url: Optional[str] = Field(default=None, validation_alias="database_url")
    tile_server: str = Field(
        "https://tiles.suhail.ai/maps/{region}/{z}/{x}/{y}.vector.pbf"
    )
    zoom10: int = 10
    zoom12: int = 12
    zoom15: int = 15
    max_radius: int = 30
    concurrency: int = 20
    model_config = SettingsConfigDict(env_prefix="DISCOVERY_", extra="ignore")


def get_discovery_config() -> DiscoveryConfig:
    print("[DEBUG] CONFIG_PATH:", CONFIG_PATH)
    if not os.path.exists(CONFIG_PATH):
        return DiscoveryConfig()
    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    print("[DEBUG] Raw YAML data:", data)
    try:
        # Merge top-level keys (e.g., database_url) with discovery section
        merged = {
            **{k: v for k, v in data.items() if k != "discovery"},
            **data.get("discovery", {}),
        }
        # Using DiscoveryConfig defaults if required fields are missing
        if "tile_server" not in merged:
            merged["tile_server"] = DiscoveryConfig.model_fields["tile_server"].default
        if "zoom10" not in merged:
            merged["zoom10"] = DiscoveryConfig.model_fields["zoom10"].default
        if "zoom12" not in merged:
            merged["zoom12"] = DiscoveryConfig.model_fields["zoom12"].default
        if "zoom15" not in merged:
            merged["zoom15"] = DiscoveryConfig.model_fields["zoom15"].default
        if "max_radius" not in merged:
            merged["max_radius"] = DiscoveryConfig.model_fields["max_radius"].default
        if "concurrency" not in merged:
            merged["concurrency"] = DiscoveryConfig.model_fields["concurrency"].default
        print("[DEBUG] Merged config for DiscoveryConfig:", merged)
        return DiscoveryConfig(**merged)  # type: ignore
    except ValidationError as e:
        print("Config validation error:", e)
        return DiscoveryConfig()
