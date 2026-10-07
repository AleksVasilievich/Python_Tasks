from enum import Enum


class Operation(Enum):
    """Доступные операции калькулятора."""

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

    @classmethod
    def from_code(cls, code: int) -> "Operation":
        try:
            return cls(code)
        except ValueError:
            raise ValueError(f"Неизвестная команда: {code}. Ожидается 1-4.")