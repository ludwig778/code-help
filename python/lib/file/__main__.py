from . import FileConverter


if __name__ == "__main__":
    fc = FileConverter()
    data = {
        "test": ["ok", "lmao"],
        "okkkk": 3
    }

    print()

    fc.to_json("test.json", data)
    fc.from_json("test.json")

    print()

    fc.to_ini(
        "test.ini",
        {
            "default": {
                "test": "ok",
                "lmao": 33
            },
            "section1": {
                "parametre1": "valeur",
                #"parametre2": [1, 2, 3]
            }
        }
    )
    fc.from_ini("test.ini")

    print()

    fc.to_csv("test.csv", data)
    fc.from_csv("test.csv")

    print()

    fc.to_yaml("test.yaml", data)
    fc.from_yaml("test.yaml")

