from dataclasses import dataclass
import json


class StorageCall:
    def __init__(self, data: dict, data_selection: dict = None) -> None:
        self.data: dict = data
        self.data_selection: dict = data if data_selection is None else data_selection

    def get(self, path: str) -> 'StorageCall':
        if path not in self.data_selection:
            self.data_selection[path] = {}

        return StorageCall(self.data, self.data_selection.get(path))

    def add(self, key: str, value: dict, save: bool = True):
        self.data_selection[key] = value
        if save:
            save_data(self.data)

    def add_all(self, values: list[dict]):
        for value in values:
            self.add(*value[:2], save=False)

        save_data(self.data)

    def remove(self, key: str):
        if key in self.data_selection:
            self.data_selection.pop(key)
            save_data(self.data)

    def edit(self, key: str, new_value: str):
        self.data_selection[key] = new_value
        save_data(self.data)

    def as_dict(self) -> dict:
        return self.data_selection


def get_data():
    with open("save.json", "r", encoding="utf-8-sig") as f:
        data = json.load(f)


    return data


def save_data(data: dict):
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def storage():
    data = get_data()
    return StorageCall(data, data)
