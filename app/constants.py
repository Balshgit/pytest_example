from pathlib import Path

BASE_URL = "https://catfact.ninja"

BASE_SCRIPT_DIR = Path(__file__).resolve(strict=True).parent.parent
DATA_DIR = BASE_SCRIPT_DIR.joinpath("data")
DATA_DIR.mkdir(exist_ok=True)