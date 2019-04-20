#!/usr/bin/env python3

from graphviz import Digraph
import json
import sys

def generate_dotfile(fsa, filename):
    dot = Digraph(comment="clock-error-modeler output")
    for process in fsa["processes"]:
        # generate the nodes themselves
        for state in process["states"]:
            name = state["name"]
            actions = json.dumps(state["actions"], indent=1)
            dot.node(name, name + "\n" + str(actions))
        # draw the edges between the vertices
        for transition in process["transitions"]:
            dot.edge(transition["from"], transition["to"], label=transition["condition"])
    dot.render("viz-output/" + filename + ".dot")

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("Usage: visualize_fsa.py filename")
        print("Please provide (only) a filename argument.")
        exit(1)
    filename = sys.argv[1]
    try:
        fh = open(filename, 'r')
        fsa = json.load(fh)
        fh.close()
    except FileNotFoundError:
        print("Error: File " + filename + " not found. Exiting...")
        exit(2)
    # made it past all the hurdles, time to execute visualization
    generate_dotfile(fsa, filename)

    exit(0)