from dataclasses import dataclass


@dataclass(slots=True)
class CatDataDTO:
    fact: str
    length: int