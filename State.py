#!/usr/bin/env python3

import inspect

class State:
    def add_action(self, action):
        if not callable(action):
            print("Attempted to add non-function action. Exiting...")
            exit(1)
        self.actions.append(action)

    def add_transition(self, transition):
        if type(transition) != dict:
            print("Attempted to add non-dictionary transition. Exiting...")
            exit(1)
        if type(transition["state"]) != State:
            print("Attempted to add non-State-type transition state. Exiting...")
            exit(1)
        if not callable(transition["condition"]):
            print("Attempted to add non-function condition to transition. Exiting...")
            exit(1)
        self.transitions += transition

    def add_transition(self, state, condition, string):
        if type(state) != State:
            print("Attempted to add non-State-type transition state. Exiting...")
            exit(1)
        if not callable(condition):
            print("Attempted to add non-function condition to transition. Exiting...")
            exit(1)
        self.transitions.append({"state":state, "condition":condition, "string":string})

    def __init__(self, name):
        self.name = name
        self.transitions = []
        self.actions = []

    def __str__(self):
        return "State: " + self.name


def print_state(state):
    print(state)
    for transition in state.transitions:
        #func = transition["condition"]
        #print(func)
        #funcString = str(inspect.getsourcelines(func)[0])
        #funcString = funcString.strip("['\\n']").split(" = ")[1]
        print("\t", transition["state"], ", " + transition["string"])


def print_process(state, depth=0):
    print('\t' * depth + str(state))
    for transition in state.transitions:
        print_process(transition["state"], depth+1)


if __name__ == "__main__":
    print("This class is not executable. Exiting...")
    exit(0)