#!/usr/bin/env python3

import json
import random
from read_config import read_test_configuration
from State import State, print_process, print_state

global_variables = {}
current_states = []

def atomic_transition():
    for idx, state in enumerate(current_states):
        for transition in state.transitions:
            # check the condition to see if it's true
            if transition["condition"]():
                # if condition is true, current state becomes transition state
                current_states[idx] = transition["state"]
                break # we only want to transition on the first match

def atomic_action():
    shuffled_states = list(current_states)
    random.shuffle(shuffled_states)
    for state in shuffled_states:
        for action in state.actions:
            action()


def iterate_with_input():
    print("-" * 30)
    atomic_action()
    print(json.dumps(global_variables, indent=1) + "\n")
    for state in current_states:
        print_state(state)
    while True:
        input()
        print("-" * 30)
        atomic_transition()
        atomic_action()
        print(json.dumps(global_variables, indent=1) + "\n")
        for state in current_states:
            print_state(state)

if __name__ == "__main__":
    global_variables, current_states = read_test_configuration()
    iterate_with_input()
