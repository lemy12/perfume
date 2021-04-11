import module.extraction
import json


if __name__ == "__main__":
    db = []
    with open("database_new.json", "w") as fWrite:
        links = module.extraction.get_products_links()
        for each in links:
            product_data = module.extraction.get_product_data(each)
            if product_data:
                db.append(product_data.return_data())
        json.dump(db, fWrite, indent=4)
