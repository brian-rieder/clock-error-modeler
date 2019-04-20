#!/usr/bin/env python3

import json
import random
from read_config import read_configuration_file
from State import State, print_process, print_state
import sys

clock = 0
global_variables = {}
current_states = []

def transition(atomic=True, state_idx=None, invert_selection=False):
    if atomic or invert_selection:
        for idx, state in enumerate(current_states):
            if not atomic and idx == state_idx:
                continue
            for transition in state.transitions:
                # check the condition to see if it's true
                if transition["condition"]():
                    # if condition is true, current state becomes transition state
                    current_states[idx] = transition["state"]
                    break # we only want to transition on the first match
    else: # we're only iterating one process
        for transition in current_states[state_idx].transitions:
            # check the condition to see if it's true
            if transition["condition"]():
                # if condition is true, current state becomes transition state
                current_states[state_idx] = transition["state"]
                break # we only want to transition on the first match


def action(atomic=True, state_idx=None, invert_selection=False):
    if atomic or invert_selection:
        shuffled_states = list(current_states)
        if invert_selection:
            shuffled_states = [state for idx,state 
                in enumerate(shuffled_states) if idx != state_idx]
        random.shuffle(shuffled_states)
        for state in shuffled_states:
            for state_action in state.actions:
                exec(state_action, global_variables)
                global_variables.pop("__builtins__", None)
    else: # we're only doing the action of the selected process
        [state_action() for state_action in current_states[state_idx].actions]


def iterate():
    print("-" * 30)
    action()
    print(json.dumps(global_variables, indent=1) + "\n")
    for state in current_states:
        print_state(state)
    while True:
        input()
        print("-" * 30)
        transition()
        action()
        print(json.dumps(global_variables, indent=1) + "\n")
        for state in current_states:
            print_state(state)


def iterate_with_delay(process_to_delay, delay_amt, time_of_delay, is_slower=True):
    global clock
    print("TIME: " + str(clock) + " " + "-" * 30)
    action()
    print(json.dumps(global_variables, indent=1) + "\n")
    for state in current_states:
        print_state(state)
    while True:
        input()
        if time_of_delay <= clock < delay_amt + time_of_delay:
            # it's time to have the delay
            transition(atomic=False, state_idx=process_to_delay, invert_selection=is_slower)
            action(atomic=False, state_idx=process_to_delay, invert_selection=is_slower)
        else: # move atomically
            transition()
            action()
        clock += 1
        print("TIME: " + str(clock) + " " + "-" * 30)
        print(json.dumps(global_variables, indent=1) + "\n")
        for state in current_states:
            print_state(state)


if __name__ == "__main__":
    global_variables, current_states = read_configuration_file(sys.argv[1])
    #print(json.dumps(global_variables))
    iterate()
    #iterate_with_delay(0, 10, 1, is_slower=False)
