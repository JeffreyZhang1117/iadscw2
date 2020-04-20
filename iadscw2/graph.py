import math

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)

class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
            self.text = open(filename,'r')
            self.lines = self.text.readlines()


            if n  == -1:
              self.n = len(self.lines)
              self.nodes = []

              for i in range(self.n):
                self.lines[i] = self.lines[i].strip('\n')
                x = [int(x) for x in self.lines[i].split()]
                self.nodes.append(x)

              self.dists = [[0 for i in range(self.n)] for i in range(self.n)]
              for i in range(self.n):
                  for j in range(self.n):
                     self.dists[i][j] = euclid(self.nodes[i],self.nodes[j])


              self.perm = [i for i in range(self.n)]
            else:
              self.n = n
              self.nodes = [i for i in range(self.n)]
              self.dists = [[0 for i in range(self.n)] for i in range(self.n)]
              for i in range(len(self.lines)):
                self.lines [i] = self.lines[i].strip('\n')
                x = [int(z) for z in self.lines[i].split()]
                self.dists[x[0]][x[1]] = x[2]

              self.perm = [i for i in range(self.n)]


        # Complete as described in the spec, to calculate the cost of the
        # current tour (as represented by self.perm).
    def tourValue(self):
            sum = 0
            for i in range(self.n-1):
              start = self.perm[i]
              end = self.perm[i+1]
              sum += self.dists[start][end]
            sum += self.dists[self.perm[-1]][self.perm[0]]

            return sum
    #def tourValue(self):
    #        sum = 0
    #        for i in range(self.n):
    #            sum += self.dist[self.perm[i]][self.perm[(i+1)]]
    #        return sum


    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
              currenttour = [self.perm[i] for i in range(self.n)]
              perms = [self.perm[i] for i in range(self.n)]
              temp = perms[i] #current value at i
              perms[i] = perms[(i+1) % self.n]
              perms[(i+1) % self.n] = temp

              before = self.tourValue()
              self.perm = perms #swap the two values
              after = self.tourValue()

              if before <= after:
                self.perm = currenttour   #swap back
                return False
              else:
                return True



    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.137  263

    # Return True/False depending on success.
    def tryReverse(self,i,j):

        original = [self.perm[i] for i in range(self.n)]
        mid = original[i:j+1]
        mid.reverse()
        tem = self.perm[:i] + mid + self.perm[j+1:]


        before = self.tourValue()

        self.perm = tem

        after = self.tourValue()

        if before <= after:
          self.perm = original
          return False
        else:
          return True




    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True


    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        start = self.perm.pop(0)
        self.perm.append(start)
        for i in range(1,self.n):
            minimum = float("inf")
            for node in self.perm[:(self.n-i)]:
                if self.dists[node][self.perm[-1]] < minimum:
                    minimum = self.dists[node][self.perm[-1]]
                    minNode = node
            self.perm.remove(minNode)
            self.perm.append(minNode)


   # my own algorithm
    def Astar(self):
        start = self.perm[0]
        self.perm.remove(start)
        self.perm.append(start)
        for i in range (1,self.n):
            minimum = float("inf")
            for node in self.perm[:(self.n-i)]:
               g = self.dists[node][self.perm[-1]]
               h = self.dists[node][start]
               f = g + h
               if f < minimum:
                   minimum = f
                   minNode = node
            self.perm.remove(minNode)
            self.perm.append(minNode)
