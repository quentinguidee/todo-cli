import json
from typing import NoReturn, Optional
import os


SAVE_FILENAME = "save.json"


class StorageCall:
    def __init__(self, data: dict, data_selection: Optional[dict] = None, allow_save: bool = True):
        self.data: dict = data
        self.data_selection: dict = data if data_selection is None else data_selection
        self.allow_save = allow_save

    def get(self, path: str) -> 'StorageCall':
        if path not in self.data_selection:
            self.data_selection[path] = {}

        return StorageCall(self.data, self.data_selection.get(path), allow_save=self.allow_save)

    def add(self, key: str, value: dict, save: bool = True) -> NoReturn:
        self.data_selection[key] = value
        if save:
            self.save()

    def add_all(self, values: list[dict]) -> NoReturn:
        for value in values:
            self.add(*value[:2], save=False)

        self.save()

    def remove(self, key: str) -> NoReturn:
        if key in self.data_selection:
            self.data_selection.pop(key)
            self.save()

    def edit(self, key: str, new_value: str) -> NoReturn:
        self.data_selection[key] = new_value
        self.save()

    def as_dict(self) -> dict:
        return self.data_selection

    def save(self) -> NoReturn:
        if self.allow_save:
            save_data(SAVE_FILENAME, self.data)


def get_data(filename: str):
    if not os.path.exists(filename):
        save_data(filename, {})

    with open(filename, encoding="utf-8-sig") as f:
        data = json.load(f)

    return data


def save_data(filename: str, data: dict) -> NoReturn:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def storage() -> StorageCall:
    data = get_data(SAVE_FILENAME)
    return StorageCall(data)
