from extraction import *
import json


if __name__ == "__main__":
    db = get_product_data()
    with open("database.json", "w") as fWrite:
        json.dump(db, fWrite, indent=4)
