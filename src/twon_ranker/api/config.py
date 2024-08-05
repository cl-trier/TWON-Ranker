import typing
import pathlib


class Config:
    title: str = "TWON Ranker API"
    version: str = "0.0.6"

    trust_origins: typing.List[str] = [
        "http://localhost:5173",
        "http://localhost:8000",
    ]

    docs_path: str = pathlib.Path(__file__).parent.resolve() / "docs"
    log_path: str = ".logs/"

    def __init__(self) -> None:
        self.log_path = f"{self.log_path}/{self.version}"
        pathlib.Path(self.log_path).mkdir(parents=True, exist_ok=True)
