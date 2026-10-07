from models.operation import Operation


class Show:
    """Печатает меню и подсказки."""

    @staticmethod
    def menu() -> None:
        print("=" * 40)
        print("Калькулятор")
        print("=" * 40)
        print("Доступные команды:")
        for op in Operation:
            print(f"  {op.value} — {Show._ru_name(op)}")
        print("=" * 40)

    @staticmethod
    def _ru_name(op: Operation) -> str:
        names = {
            Operation.ADD: "сложить",
            Operation.SUB: "вычесть",
            Operation.MUL: "умножить",
            Operation.DIV: "делить",
        }
        return names[op]