import random

class SimpleModel:
    def __init__(self):
        self.knowledge = {
            "plastic": "plastic",
            "paper": "paper",
            "metal": "metal",
            "organic": "organic"
        }

    def predict(self, state):
        if random.random() < 0.7:
            return self.knowledge.get(state, random.choice(list(self.knowledge.values())))
        return random.choice(list(self.knowledge.values()))