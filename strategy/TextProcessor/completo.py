from abc import ABC, abstractmethod
from enum import Enum, auto


class ListStrategy(ABC):
    def start(self, buffer: list[str]):
        pass

    def end(self, buffer: list[str]):
        pass

    def add_list_item(self, buffer: list[str], item: str):
        pass

class HtmlListStrategy(ListStrategy):
    def start(self, buffer: list[str]):
        pass

    def end(self, buffer: list[str]):
        pass

    def add_list_item(self, buffer: list[str], item: str):
        pass
    
class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer: list[str], item: str):
        pass


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()

class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HtmlListStrategy()) -> None:
        self.buffer: list[str] = []
        self.list_strategy = list_strategy

    def append_list(self, items: list[str]):
        pass

    def set_output_format(self, format: OutputFormat):
        pass
    
    def clear(self):
        self.buffer.clear()

    def __str__(self) -> str:
        return "".join(self.buffer)