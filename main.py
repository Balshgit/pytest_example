import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from learning_pytest.app.dto import CatDataDTO
from learning_pytest.app.api_scrapper import AsyncNetScrapper
from learning_pytest.app.file_repository import FileRepository
from learning_pytest.app.constants import DATA_DIR


@dataclass
class Application:
    net_scrapper: AsyncNetScrapper
    file_repository: FileRepository

    def save_cat_facts_to_csv(self, filename: str):
        data = self.net_scrapper.run()
        self.file_repository.save_data_to_csv(filename, data)

    def get_cats_facts_from_web(self):
        return self.net_scrapper.run()

    def load_cat_facts_from_csv(self, filename: str) -> list[str]:
        return self.file_repository.load_data_from_csv(filename=filename)


def get_app() -> Application:
    return Application(
        net_scrapper=AsyncNetScrapper(),
        file_repository=FileRepository(),
    )

def run():
    app = get_app()
    app.save_cat_facts_to_csv(filename=DATA_DIR.joinpath("cats_facts.csv"))
    print(app.load_cat_facts_from_csv(filename=DATA_DIR.joinpath("cats_facts.csv")))


if __name__ == "__main__":
    run()