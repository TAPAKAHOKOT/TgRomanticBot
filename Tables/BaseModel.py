class BaseModel:
    def get_class(self):
        return BaseModel

    def get_table(self):
        return self.get_class().__table__
