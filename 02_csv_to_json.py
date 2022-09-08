import csv
import json


def read_csv(name_file: str) -> list:
    with open(name_file, mode="r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)


def write_json(name_file: str, data: dict) -> None:
    with open(name_file, mode="w", encoding="utf-8-sig") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    try:
        data = read_csv("example.csv")
    except Exception as err:
        print(f"Something happened: {err}")

    data_dict = {
        "dates": [row[0] for row in data],
        "fruits": [row[1] for row in data],
        "numbers": [row[2] for row in data],
    }

    try:
        write_json("example.json", data_dict)
    except Exception as err:
        print(f"Something happened: {err}")
