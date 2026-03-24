from textual.app import App, ComposeResult

from view.item.DictionaryViewerItem import DictionaryViewerItem
from view.item.LabelItem import LabelItem
from view.item.StringViewerItem import StringViewerItem


class CursusxViewerApp(App):
    _my_dictionary_items: list[DictionaryViewerItem]
    _my_label_items: list[LabelItem]
    _my_string_items: list[StringViewerItem]

    def __init__(self, dictionary_items: list[DictionaryViewerItem],
                 label_items: list[LabelItem],
                 string_viewer_items: list[StringViewerItem], **kwargs):
        super().__init__(**kwargs)
        self._my_dictionary_items = dictionary_items
        self._my_label_items = label_items
        self._my_string_items = string_viewer_items

    def compose(self) -> ComposeResult:
        for item in self._my_dictionary_items:
            yield item
        for item in self._my_label_items:
            yield item
        for item in self._my_string_items:
            yield item
