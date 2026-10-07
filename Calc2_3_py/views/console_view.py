from base.calc import Calc


class ConsoleView(Calc):
    """Ввод данных от пользователя с проверками."""

    def __init__(self) -> None:
        pass

    def read_float(self, prompt: str) -> float:
        """Читает число с повторным запросом при ошибке."""
        while True:
            raw = input(prompt).strip()
            try:
                return float(raw)
            except ValueError:
                print(f"  ⚠ '{raw}' — не число. Попробуйте ещё раз.")

    def read_command(self) -> int:
        """Читает команду (целое 1-4)."""
        while True:
            raw = input("Введите команду: ").strip()
            try:
                return int(raw)
            except ValueError:
                print(f"  ⚠ '{raw}' — не целое число.")