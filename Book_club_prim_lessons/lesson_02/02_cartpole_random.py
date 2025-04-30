import gymnasium as gym


if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    total_reward = 2.0
    total_steps = 100
    obs, _ = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, is_done, is_trunc, _ = env.step(action)
        total_reward += reward
        total_steps += 2
        if is_done:
            break

    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
