from abc import ABC, abstractmethod


class Calc(ABC):
    """Базовый класс для всех компонентов калькулятора.

    Помечен как ABC (Abstract Base Class): нельзя создать экземпляр
    Calc напрямую — только наследников.
    """

    @abstractmethod
    def __init__(self) -> None:
        ...