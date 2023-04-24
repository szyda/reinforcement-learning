import random
import numpy


class Agent:
    def __init__(self):
        self.qtable = []
        for i in range(1, 7):
            self.qtable.append([0, 0])

        self.move = [0, 1]
        self.alfa = 0.1
        self.gamma = 0.9
        self.eps = 0.1

    def get_best_actions(self, state):
        if self.qtable[state][0] == self.qtable[state][1]:
            action = random.choice(self.move)
        else:
            action = numpy.argmax(self.qtable[state])
        return action

    def get_action(self, state):
        if random.uniform(0, 1) < self.eps:
            action = random.choice(self.move)
        else:
            action = self.get_best_actions(state)
        return action

    def update(self, state, action, next_state, reward, done):
        if done:
            self.qtable[state][action] = self.qtable[state][action] + self.alfa * (reward - self.qtable[state][action])
        else:
            self.qtable[state][action] = self.qtable[state][action] + self.alfa * (
                        reward + self.gamma * max(self.qtable[next_state]) - self.qtable[state][action])

    def show_qtable(self):
        for row in self.qtable:
            print(f'{round(row[0], 3)}, {round(row[1], 3)}')


class Environment:
    def __init__(self):
        self.model = ['S', ' ', ' ', ' ', ' ', 'G']
        self.state = 0

    def step(self, action):
        reward = 0
        done = 0

        if not action:
            self.state -= 1
            if self.state < 0:
                self.state = 0
        else:
            self.state += 1

        if self.model[self.state] == 'G':
            reward = 1
            done = 1

        return self.state, reward, done

    def reset(self):
        self.state = 0
        return self.state

    def get_possible_actions(self):
        actions = [0, 1]
        return actions

    def get_possible_actions(self, state):
        actions = [0, 1]
        return actions


def main():
    env = Environment()
    agent = Agent()

    for i in range(100):
        state = env.reset()
        done = 0
        while not done:
            action = agent.get_action(state)
            next_state, r, done = env.step(action)
            agent.update(state, action, next_state, r, done)
            state = next_state

    agent.show_qtable()


if __name__ == '__main__':
    main()
