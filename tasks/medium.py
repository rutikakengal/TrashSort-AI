def evaluate(env, model, episodes=50):
    score = 0

    for _ in range(episodes):
        state = env.reset()
        action = model.predict(state)
        _, reward, _, _ = env.step(action)
        score += reward

    return score / episodes