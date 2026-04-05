import gradio as gr
from environment.env import TrashSortingEnv
from environment.models import SimpleModel

env = TrashSortingEnv()
model = SimpleModel()

def run_demo():
    scores = []

    for _ in range(20):
        state = env.reset()
        action = model.predict(state)
        _, reward, _, _ = env.step(action)
        scores.append(reward)

    return f"Score: {sum(scores)/len(scores):.2f}"

gr.Interface(fn=run_demo, inputs=[], outputs="text", title="TrashSort AI").launch()
