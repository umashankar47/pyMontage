from datetime import datetime
from pathlib import Path

class OutputManager:
    def __init__(self, config):
        self.config = config

    def get_unique_path(self) -> Path:
        folder = Path(self.config.output_folder)
        folder.mkdir(parents=True, exist_ok=True)

        stem = Path(self.config.output_name).stem
        suffix = Path(self.config.output_name).suffix
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        candidate = folder / f"{stem}_{timestamp}{suffix}"

        counter = 1
        while candidate.exists():
            candidate = folder / f"{stem}_{timestamp}_{counter}{suffix}"
            counter += 1

        return candidate