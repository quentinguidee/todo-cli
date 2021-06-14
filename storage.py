from dataclasses import dataclass
import json


class StorageCall:
    def __init__(self, data: dict, data_selection: dict = None, allow_save: bool = True) -> None:
        self.data: dict = data
        self.data_selection: dict = data if data_selection is None else data_selection
        self.allow_save = allow_save

    def get(self, path: str) -> 'StorageCall':
        if path not in self.data_selection:
            self.data_selection[path] = {}

        return StorageCall(self.data, self.data_selection.get(path), allow_save=self.allow_save)

    def add(self, key: str, value: dict, save: bool = True):
        self.data_selection[key] = value
        if save:
            self.save()

    def add_all(self, values: list[dict]):
        for value in values:
            self.add(*value[:2], save=False)

        self.save()

    def remove(self, key: str):
        if key in self.data_selection:
            self.data_selection.pop(key)
            self.save()

    def edit(self, key: str, new_value: str):
        self.data_selection[key] = new_value
        self.save()

    def as_dict(self) -> dict:
        return self.data_selection

    def save(self):
        if self.allow_save:
            save_data("save.json", self.data)


def get_data(filename: str):
    with open(filename, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    return data


def save_data(filename: str, data: dict):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def storage():
    data = get_data("save.json")
    return StorageCall(data)
