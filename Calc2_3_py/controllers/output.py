from models.model import Model
from models.operation import Operation
from views.console_view import ConsoleView
from services.log import Log


class Output:
    """Связывает View, Model и Log. Здесь живёт сценарий работы."""

    def __init__(self, view: ConsoleView, model: Model, log: Log) -> None:
        self._view = view
        self._model = model
        self._log = log

    def run_once(self) -> None:
        """Один цикл: команда → два числа → расчёт → лог."""
        try:
            code = self._view.read_command()
            op = Operation.from_code(code)
        except ValueError as e:
            print(f"  ⚠ {e}")
            return

        a = self._view.read_float("Первое число: ")
        b = self._view.read_float("Второе число: ")

        try:
            result = self._model.calculate(op, a, b)
        except (ZeroDivisionError, ValueError) as e:
            print(f"  ⚠ {e}")
            return

        text = self._format(op, a, b, result)
        self._log.write(text)

    @staticmethod
    def _format(op: Operation, a: float, b: float, result: float) -> str:
        symbol = {
            Operation.ADD: "+",
            Operation.SUB: "-",
            Operation.MUL: "*",
            Operation.DIV: "/",
        }[op]
        return f"{a} {symbol} {b} = {result}"