from pathlib import Path
from typing import List


class Config:
    title: str = 'TWON Ranker API'
    version: str = '0.0.1'

    trust_origins: List[str] = [
        'http://localhost:5173',
        'http://localhost:8000',
    ]

    docs_path: str = './api/docs'
    log_path: str = './api/logs/responses'

    def __init__(self) -> None:
        self.log_path = f'{self.log_path}/{self.version}'
        Path(self.log_path).mkdir(parents=True, exist_ok=True)
