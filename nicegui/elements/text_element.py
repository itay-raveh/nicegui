from ..binding import BindTextMixin
from ..element import Element


class TextElement(Element, BindTextMixin):
    """An element with its _content representing a bindable text property."""

    def __init__(self, tag: str, text: str) -> None:
        super().__init__(tag)
        self.text = text

    @property
    def text(self) -> str:
        return self._content

    @text.setter
    def text(self, text: str) -> None:
        self._content = text
        self.update()
