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
            print("Attempted to add non-function action to transition. Exiting...")
            exit(1)
        self.transitions += transition

    def addTransition(self, state, action):
        if type(state) != State:
            print("Attempted to add non-State-type transition state. Exiting...")
            exit(1)
        if not callable(action):
            print("Attempted to add non-function action to transition. Exiting...")
            exit(1)
        self.transitions += (state, action)

    def __init__(self, name):
        self.name = name
        self.transitions = []
        self.actions = []


if __name__ == "__main__":
    print("This class is not executable. Exiting...")
    exit(0)