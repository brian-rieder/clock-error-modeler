#!/usr/bin/env python3

from State import State, print_process

global_variables = {"cnt":0}

def create_test_fsa():
    always_take = lambda : True
    cnt_eq_5 = lambda : global_variables["cnt"] == 5
    cnt_eq_10 = lambda : global_variables["cnt"] == 10

    p0 = State("A")
    b = State("B")
    p0.addTransition(b, always_take)
    c = State("C")
    b.addTransition(c, cnt_eq_5)

    p1 = State("V")
    w = State("W")
    p1.addTransition(w, always_take)
    x = State("X")
    w.addTransition(x, always_take)
    y = State("Y")
    x.addTransition(y, always_take)
    z = State("Z")
    y.addTransition(z, always_take)
    z.addTransition(p1, cnt_eq_10)

    def inc_count():
        global_variables["cnt"] += 1
    z.addAction(inc_count)

    return [p0, p1]



if __name__ == "__main__": 
    print("This is not an executable class. Exiting...")
    create_test_fsa()
    exit(0)