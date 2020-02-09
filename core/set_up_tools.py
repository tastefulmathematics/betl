import random
import uuid


class SetUpTools:

    def __init__(self, name, user=""):
        self.name = name
        self.user = user or self.unique_key("user")

    def unique_key(self, key=""):
        return f"{uuid.uuid4().hex}_{self.name}_{key}"

    @staticmethod
    def unique_id(low=1, high=1000000000):
        return random.randrange(low, high)
