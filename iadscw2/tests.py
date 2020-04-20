import math
import graph
import numpy
import random

def euclid(p,q):
    x = p[0] - q[0]
    y = p[1] - q[1]
    return math.sqrt(x*x+y*y)

n = input("n(-1 or metrics): ")
n = (int) (n)

if(n == -1):
    weight = input("weight: ")
    size1 = input("size: ")
    weight = (int) (weight)
    size1 = (int) (size1)

    a = numpy.random.randint(0, weight , size=[size1, 2])

    f = open("testcity","x")
    for i in range(len(a)):
        node = [int(i) for i in a[i]]
        print(node[0],end='',file=f)
        print(' ',end ='',file=f)
        print(node[1],file=f)
    f.close()

    g = graph.Graph(-1,"testcity")
    print("g.tourValue():",g.tourValue())

    g = graph.Graph(-1,"testcity")
    g.swapHeuristic()
    print("g.swapHeuristic() && g.tourValue:",g.tourValue())

    g= graph.Graph(-1,"testcity")
    g.swapHeuristic()
    g.TwoOptHeuristic()
    print("g.swapHeuristic() && g.TwoOptHeuristic() && g.tourValue:",g.tourValue())

    g = graph.Graph(-1,"testcity")
    g.Greedy()
    print("g.Greedy() && g.tourValue():",g.tourValue())

    g = graph.Graph(-1,"testcity")
    g.Astar()
    print("g.Astar() && g.tourValue():",g.tourValue())

else:
    weight = input("weight: ")
    weight = (int)(weight)

    nodes = []
    b = []
    for i in range(n-1):
        i += 1
        for j in range(n-i):
            nodes.append(j)
            nodes.append(j+i)
            nodes.append(random.randint(0,weight))
    for z in range(0,len(nodes),3):
        b.append(nodes[z:z+3])

    f = open("testmetric","x")
    length = len(b)
    for i in range(length):
        node = [int(i) for i in b[i]]
        print(node[0],end='',file=f)
        print(' ',end='',file=f)
        print(node[1],end='',file=f)
        print(' ',end='',file=f)
        print(node[2],file=f)
    f.close()

    g = graph.Graph(n,"testmetric")
    print("g.tourValue():",g.tourValue())

    g = graph.Graph(n,"testmetric")
    g.swapHeuristic()
    print("g.swapHeuristic() && g.tourValue:",g.tourValue())

    g= graph.Graph(n,"testmetric")
    g.swapHeuristic()
    g.TwoOptHeuristic()
    print("g.swapHeuristic() && g.TwoOptHeuristic() && g.tourValue:",g.tourValue())

    g = graph.Graph(n,"testmetric")
    g.Greedy()
    print("g.Greedy() && g.tourValue():",g.tourValue())

    g = graph.Graph(n,"testmetric")
    g.Astar()
    print("g.Astar() && g.tourValue():",g.tourValue())
