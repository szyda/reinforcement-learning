import random
import numpy

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

class Agent:
    def __init__(self):
        self.qtable = {}
        self.move = [LEFT, RIGHT, UP, DOWN]
        self.alfa = 0.1
        self.gamma = 0.9
        self.eps = 0.1

    def get_best_actions(self, state):
        if state not in self.qtable:
            self.qtable[state] = [0, 0, 0, 0]

        if self.qtable[state][0] == self.qtable[state][1] == self.qtable[state][2] == self.qtable[state][3]:
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
        if state not in self.qtable:
            self.qtable[state] = [0, 0, 0, 0]

        if next_state not in self.qtable:
            self.qtable[next_state] = [0, 0, 0, 0]

        if done:
            self.qtable[state][action] = self.qtable[state][action] + self.alfa * (reward - self.qtable[state][action])

        else:
            self.qtable[state][action] = self.qtable[state][action] + self.alfa * (
                        reward + self.gamma * max(self.qtable[next_state]) - self.qtable[state][action])

    def show_qtable(self):
        for row in self.qtable:
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')


class Environment:
    def __init__(self, width, height):
        self.model = []
        self.state = (0, 0)
        self.width = width
        self.height = height
        self.x = random.randint(0, self.width - 1)
        self.y = random.randint(0, self.height - 1)

        for i in range(self.height):
            self.model.append([' '] * self.width)

    def generate_goal(self):
        self.model[self.x][self.y] = 'X'

    def show_environment(self):
        for row in self.model:
            print(row)

    def step(self, action):
        reward = 0
        done = 0

        if action == LEFT:
            self.state = (self.state[0] - 1, self.state[1])

        elif action == RIGHT:
            self.state = (self.state[0] + 1, self.state[1])

        elif action == UP:
            self.state = (self.state[0], self.state[1] + 1)

        elif action == DOWN:
            self.state = (self.state[0], self.state[1] - 1)

        if self.state[0] < 0 or self.state[0] > self.width - 1 or self.state[1] < 0 or self.state[1] > self.height - 1:
            done = 1
            reward = -1

        elif self.model[self.state[0]][self.state[1]] == 'X':
            reward = 1
            done = 1

        return (self.state, self.x, self.y), reward, done

    def reset(self):
        self.state = (0, 0)
        self.x = random.randint(0, self.width - 1)
        self.y = random.randint(0, self.height - 1)
        return (self.state, self.x, self.y)

    def get_possible_actions(self):
        actions = [LEFT, RIGHT, UP, DOWN]
        return actions

    def get_possible_actions(self, state):
        actions = [LEFT, RIGHT, UP, DOWN]
        return actions


def main():
    env = Environment(5, 5)
    env.generate_goal()
    # env.show_environment()
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
