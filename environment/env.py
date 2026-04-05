import random

class TrashSortingEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.trash_types = ["plastic", "paper", "metal", "organic"]
        self.state = random.choice(self.trash_types)
        self.done = False
        return self.state

    def step(self, action):
        reward = 0

        if action == self.state:
            reward = 1
        else:
            reward = -1

        self.state = random.choice(self.trash_types)
        self.done = False

        return self.state, reward, self.done, {}