from pathlib import Path
import os


def get_app_data_path() -> Path:
    android_path = Path("/data/user/0/com.flet.app/files")

    if android_path.exists():
        base_path = android_path
    else:
        base_path = Path.home() / ".dulceria"

    data_dir = base_path / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    return data_dir