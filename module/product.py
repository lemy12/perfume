class Product:

    def __init__(self, name, comp):
        self.name = name
        self.comp = comp

    def return_data(self):
        return {"name": self.name, "comp": self.comp}
