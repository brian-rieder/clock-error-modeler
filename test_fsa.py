#!/usr/bin/env python3

from State import State, print_process

global_variables = {}

def create_test_fsa():
    always_take = lambda : True
    p0 = State("A")
    b = State("B")
    p0.addTransition(b, always_take)
    c = State("C")
    b.addTransition(c, always_take)

    p1 = State("V")
    w = State("W")
    p1.addTransition(w, always_take)
    x = State("X")
    w.addTransition(x, always_take)
    y = State("Y")
    x.addTransition(y, always_take)
    z = State("Z")
    x.addTransition(z, always_take)

    return p0, p1



if __name__ == "__main__": 
    print("This is not an executable class. Exiting...")
    create_test_fsa()
    exit(0)