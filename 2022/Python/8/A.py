import numpy as np

def solve:

    with open('input.txt','r') as file:
        lines = file.readlines()
        lines = [entry.strip() for entry in lines]

    trees = np.zeros((len(lines), len(lines[0])), dtype=int)
    for i,line in enumerate(lines):
        trees[i,:] = np.array(list(line))


    visible_trees = 2*len(lines[0]) + 2*(len(lines)-2)

    for i in range(1,trees.shape[0]-1):
        for j in range(1,trees.shape[1]-1):
