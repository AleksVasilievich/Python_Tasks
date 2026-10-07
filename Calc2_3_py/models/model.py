from models.operation import Operation
from base.calc import Calc


class Model(Calc):
    """Чистая логика расчёта. Никакого ввода/вывода."""

    def __init__(self) -> None:
        pass

    def calculate(self, op: Operation, a: float, b: float) -> float:
        """Возвращает ЧИСЛО, а не строку.

        Форматирование — задача View/Log, не Model.
        """
        match op:
            case Operation.ADD:
                return a + b
            case Operation.SUB:
                return a - b
            case Operation.MUL:
                return a * b
            case Operation.DIV:
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно.")
                return a / b
        raise ValueError(f"Неподдерживаемая операция: {op}")