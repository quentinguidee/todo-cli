from unittest.case import TestCase

from storage import StorageCall


def get_sample_data():
    return {
        "1_1": {
            "2_1": {
                "3_1": "value_A",
                "3_2": "value_B"
            }
        },
        "1_2": {
            "2_2": {
                "3_3": "value_C",
                "3_4": "value_D"
            }
        },
    }


class TestStorage(TestCase):
    def test_get(self):
        data = get_sample_data()

        result = StorageCall(data).get("1_2").get("2_2").as_dict()
        expect = {'3_3': 'value_C', '3_4': 'value_D'}

        self.assertDictEqual(result, expect)

    def test_get_none(self):
        data = get_sample_data()

        result = StorageCall(data).get("1_3").get("2_3").as_dict()
        expect = {}

        self.assertDictEqual(result, expect)

    def test_add(self):
        data = get_sample_data()
        expect = get_sample_data()
        expect["1_2"]["2_3"] = {"3_5": "Test"}

        StorageCall(data).get("1_2").add("2_3", {"3_5": "Test"})

        self.assertDictEqual(data, expect)

    def test_add_none(self):
        data = get_sample_data()
        expect = get_sample_data()
        expect["1_3"] = {"2_3": {"3_5": "Test"}}

        StorageCall(data).get("1_3").add("2_3", {"3_5": "Test"})

        self.assertDictEqual(data, expect)

    def test_remove(self):
        data = get_sample_data()
        expect = get_sample_data()
        expect["1_2"].pop("2_2")

        StorageCall(data).get("1_2").remove("2_2")

        self.assertDictEqual(data, expect)

    def test_remove_none(self):
        data = get_sample_data()

        StorageCall(data).get("1_3").remove("2_3")

    def test_edit(self):
        data = get_sample_data()

        StorageCall(data).get("1_2").get("2_2").edit("3_3", "value_E")

        self.assertEqual(data.get("1_2").get("2_2").get("3_3"), "value_E")

    def test_edit_none(self):
        data = get_sample_data()

        StorageCall(data).get("1_3").get("2_2").edit("3_3", "value_E")

        self.assertEqual(data.get("1_3").get("2_2").get("3_3"), "value_E")

    def test_add_all(self):
        data = get_sample_data()
        expect = get_sample_data()
        expect["1_3"] = {
            "2_3": {
                "3_5": "value_E",
                "3_6": "value_F"
            },
            "2_4": {
                "3_7": "value_G",
                "3_8": "value_H"
            }
        }

        StorageCall(data).get("1_3").add_all([
            ("2_3", {
                "3_5": "value_E",
                "3_6": "value_F"
            }),
            ("2_4", {
                "3_7": "value_G",
                "3_8": "value_H"
            }),
        ])

        self.assertDictEqual(data, expect)
