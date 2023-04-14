import random

class Agent:
    qtable = []
    for i in range(1, 7):
        qtable.append([0,0])

    move = [0, 1]
    alfa = 0.1
    gamma = 0.9
    eps = 0.1

    def get_action(self, state):
        if random.uniform() < eps:
            action = random.choice(move)
        else:
            action = get_best_actions(state)
        return action

    def get_best_actions(self, state):
        if qtable[state][0] == qtable[state][1]:
            action = random.choice(move)
        else:
            action = max(qtable[state])
        return action

    def update(self, state, action, next_state, reward, done):
        if done == 1:
            qtable[state][action] = qtable[state][action] + alfa * (reward - qtable[state][action])
        else:
            qtable[state][action] = qtable[state][action] + alfa * (reward + gamma * max(qtable[next_state]) - qtable[state][action])

    def show_qtable(self):
        for row in qtable:
            print(row)


class Environment():
    def __init__(self):
        self.model = ['S', ' ', ' ',' ',' ', 'G']
        self.state = 0

    def step(self, action):
        reward = 0
        done = 0

        if action == 0:
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
        state = 0

    def get_possible_actions(self):
        actions = [0, 1]
        return actions

# Mozemy miec ograniczone ruchy ze wzgledu na pozycje w modelu
    def get_possible_actions(self, state):
        actions = [0, 1]
        return actions


def main():
    env = Environment()
