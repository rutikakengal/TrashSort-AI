from environment.env import TrashSortingEnv
from environment.models import SimpleModel
from tasks.easy import evaluate as easy_eval
from tasks.medium import evaluate as medium_eval
from tasks.hard import evaluate as hard_eval

env = TrashSortingEnv()
model = SimpleModel()

easy_score = easy_eval(env, model)
medium_score = medium_eval(env, model)
hard_score = hard_eval(env, model)

print("Easy Score:", easy_score)
print("Medium Score:", medium_score)
print("Hard Score:", hard_score)

final_score = (easy_score + medium_score + hard_score) / 3
print("Final Score:", final_score)