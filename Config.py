import json


class Config:
    file = None
    f = None

    def __init__(self, file: str):
        self.file = file
        self.reload()

    def reload(self):
        self.f = open(self.file, "r")

    def getvalue(self, key):
        return json.loads(self.f.read())[key]
