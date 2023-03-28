from abc import ABC, abstractmethod
from enum import Enum, auto


class ListStrategy(ABC):
    @abstractmethod
    def start(self, buffer: list[str]):
        pass

    @abstractmethod
    def end(self, buffer: list[str]):
        pass

    @abstractmethod
    def add_list_item(self, buffer: list[str], item: str):
        pass


class HtmlListStrategy(ListStrategy):
    def start(self, buffer: list[str]):
        buffer.append("<ul>\n")

    def end(self, buffer: list[str]):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer: list[str], item: str):
        buffer.append(f"  <li>{item}</li>\n")


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer: list[str], item: str):
        buffer.append(f"* {item}\n")


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HtmlListStrategy()) -> None:
        self.buffer: list[str] = []
        self.list_strategy = list_strategy

    def append_list(self, items: list[str]):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format: OutputFormat):
        if format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
        elif format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self) -> str:
        return "".join(self.buffer)
