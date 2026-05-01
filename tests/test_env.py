from dotenv import load_dotenv
import os
from pathlib import Path

env_path = path(_file_).parent.parent / "Data" / "Raw" / ".env"
print(f"searching.. at: {env_path.absolute()}")

load_dotenv(env_path)

model = os.getenv("QWEN_MODEL")
print(f"QWEN_MODEL: {model}")
