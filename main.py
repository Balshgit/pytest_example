from dataclasses import dataclass

from learning_pytest.app.api_scrapper import AsyncNetScrapper
from learning_pytest.app.dto import CatDataDTO
from learning_pytest.app.file_repository import FileRepository


@dataclass
class Application:
    net_scrapper: AsyncNetScrapper
    file_repository: FileRepository

    def save_cats_facts_to_csv(self, file_name: str):
        data = self.net_scrapper.run()
        self.file_repository.save_data_to_csv(file_name, data)

    def print_cats_facts(self):
        print(self.net_scrapper.run())

def get_app() -> Application:
    return Application(
        net_scrapper=AsyncNetScrapper(),
        file_repository=FileRepository(),
    )

app = get_app()
app.print_cats_facts()
app.save_cats_facts_to_csv("cats_facts.csv")