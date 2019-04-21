#!/usr/bin/env python3

import json
from State import State
import test_fsa

def read_configuration_file(filename):
    process_list = []

    with open(filename) as json_file:
        fsa = json.load(json_file)
        
    for process in fsa["processes"]:
        state_list = []
        index = 0
    
        # create list of states
        for s in process["states"]:
        
            # create new state object
            state_list.append(State(s["name"], process["name"]))

            # assign the actions to the state
            for a in s["actions"]:
                state_list[index].add_action(a)

            # assign index to state
            s["index"] = index
            index += 1

        for t in process["transitions"]:
            
            # get from state
            for s in process["states"]:
                if s["name"] == t["from"]:
                    fromState = state_list[s["index"]]
                    break
                    #print("From state =", s["name"], s["index"])
            
            # get to state
            for s in process["states"]:
                if s["name"] == t["to"]:
                    toState = state_list[s["index"]]
                    break
            
            # add the transitions
            func = eval("lambda : " + t["condition"], fsa["global_variables"])
            fsa["global_variables"].pop("__builtins__", None)
            fromState.add_transition(toState, func, t["condition"])
            
        # add process to the list
        process_list.append(state_list[0])

    return fsa, process_list

def read_test_configuration():
    return test_fsa.global_variables, test_fsa.create_test_fsa()

if __name__ == "__main__":
    print("This is not an executable class. Exiting...")
    exit(0)