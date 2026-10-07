from pathlib import Path
from datetime import datetime


class Log:
    """Пишет результаты в файл и дублирует в консоль.

    Путь можно задать при создании; по умолчанию — рядом с проектом.
    """

    def __init__(self, path: Path | None = None, echo: bool = True) -> None:
        self._path = path or (Path(__file__).resolve().parent.parent / "calc.log")
        self._echo = echo
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, text: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {text}"
        if self._echo:
            print(text)
        with self._path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")