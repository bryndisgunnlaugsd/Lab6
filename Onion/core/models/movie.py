from dataclasses import dataclass

@dataclass
class Movie:
    name: str
    description: str
    imbd_url: str
    id: int = None