# loopFinder
if given a list of edges in a directed graph like : 
a = [(1,5),(3,2),(2,7),(7,3),(6,3)]
which means there is an edge from 1 -> 5 and 3 -> 2 and so on.

given this list the thereIsLoop will return True if it could find a loop in the list that is given. For example (3->2),(2->7),(7->3) is a loop.

if thereIsLoop(a):
    print("there is a loop!")
else:
    print("no loop!")
