import csv
from dataclasses import dataclass

from learning_pytest.app.dto import CatDataDTO


@dataclass
class FileRepository:

    @staticmethod
    def save_data_to_csv(filename: str, data: list[CatDataDTO]):
        with open(filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=[
                    "fact",
                    "length",
                ],
                delimiter=";",
            )
            writer.writeheader()

            for row in data:
                writer.writerow(
                    {
                        "fact": row.fact,
                        "length": row.length,
                    }
                )

    @staticmethod
    def load_data_from_csv(filename: str) -> list[str]:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

            return [
                f"{row['fact']};{row['length']}"
                for row in reader
            ]