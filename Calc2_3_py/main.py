# Этот Калькулятор был создан на основе Calc2_2_py
# Принципы, применённые здесь
# Single Responsibility — каждый класс делает одно.
# Open/Closed — новая операция = правка Enum и Model, остальное не трогается.
# Dependency Injection — зависимости передаются снаружи, а не создаются внутри.
# Fail gracefully — ошибки ловятся, пользователь видит сообщение, программа продолжает работу.
# Слои знают только «вниз» — Controller → Model/View/Log, а не наоборот.
# Тестируемость — Model.calculate и Output.run_once можно протестировать в изоляции.
# Явное лучше неявного — типы, имена, Enum, ABC.

from models.model import Model
from views.console_view import ConsoleView
from views.show import Show
from services.log import Log
from controllers.output import Output


def main() -> None:
    Show.menu()

    view = ConsoleView()
    model = Model()
    log = Log()
    controller = Output(view, model, log)

    while True:
        try:
            controller.run_once()
        except (KeyboardInterrupt, EOFError):
            print("\nВыход.")
            break

        again = input("Ещё раз? (y/n): ").strip().lower()
        if again != "y":
            print("До свидания.")
            break


if __name__ == "__main__":
    main()