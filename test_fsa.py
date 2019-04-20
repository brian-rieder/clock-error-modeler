#!/usr/bin/env python3

from State import State, print_process

global_variables = {"cnt":0}

def create_test_fsa():
    always_take = lambda : True
    cnt_eq_5 = lambda : global_variables["cnt"] == 5
    cnt_eq_10 = lambda : global_variables["cnt"] == 10

    p0 = State("A")
    b = State("B")
    p0.add_transition(b, always_take)
    c = State("C")
    b.add_transition(c, always_take)
    c.add_transition(p0, cnt_eq_5)
    c.add_transition(c, always_take)

    p1 = State("V")
    w = State("W")
    p1.add_transition(w, always_take)
    x = State("X")
    w.add_transition(x, always_take)
    y = State("Y")
    x.add_transition(y, always_take)
    z = State("Z")
    y.add_transition(z, always_take)
    z.add_transition(p1, cnt_eq_10)

    def inc_count():
        global_variables["cnt"] += 1
    z.add_action(inc_count)

    p2 = State("U")
    g = State("G")
    p2.add_transition(g, always_take)
    h = State("H")
    g.add_transition(h, always_take)
    h.add_transition(p2, always_take)

    return [p0, p1, p2]



if __name__ == "__main__": 
    print("This is not an executable class. Exiting...")
    create_test_fsa()
    exit(0)