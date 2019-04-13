#!/usr/bin/env python3

class State:
    def addAction(self, action):
        if not callable(action):
            print("Attempted to add non-function action. Exiting...")
            exit(1)
        self.actions += action

    def addTransition(self, transition):
        if type(transition) != tuple:
            print("Attempted to add non-tuple transition. Exiting...")
            exit(1)
        if type(transition[0]) != State:
            print("Attempted to add non-State-type transition state. Exiting...")
            exit(1)
        if not callable(transition[1]):
            print("Attempted to add non-function condition to transition. Exiting...")
            exit(1)
        self.transitions += transition

    def addTransition(self, state, condition):
        if type(state) != State:
            print("Attempted to add non-State-type transition state. Exiting...")
            exit(1)
        if not callable(condition):
            print("Attempted to add non-function condition to transition. Exiting...")
            exit(1)
        self.transitions.append(tuple([state, condition]))

    def __init__(self, name):
        self.name = name
        self.transitions = []
        self.actions = []

    def __str__(self):
        return "State: " + self.name


def print_process(state, depth=0):
    print('\t' * depth + str(state))
    for transition in state.transitions:
        print_process(transition[0], depth+1)


if __name__ == "__main__":
    print("This class is not executable. Exiting...")
    exit(0)