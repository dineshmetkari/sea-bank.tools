# W oparciu o skrypt Edgardo z physicsforums.com
# Based on Edgardo script from physicsforums.com

import time

class Matrix:
        def __init__(self, n):
                self.matrix = []
                self.n = n
                for i in range(0,n):
                        self.matrix.append([])

                
                for i in range(0,n):
                        for j in range(0,n):
                                self.matrix[i].append(0)

                counter = 0
                for j in range(0,n):
                        for i in range(0,n):
                                self.matrix[j][i] = counter
                                counter+=1

        def getMatrix(self):
                return self.matrix

        def getEntry(self,x,y):
                return self.matrix[x][y]

        def printMatrix(self):
                for i in range(0,n):
                        print(self.matrix[i])

        def getNeighborhood(self,i,j):
                entry = self.getEntry(i,j)
                neighList = []

                x = i-1
                y = j-1
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i
                y = j-1
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i+1
                y = j-1
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i-1
                y = j
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i+1
                y = j
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i-1
                y = j+1
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i
                y = j+1
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))

                x = i+1
                y = j+1
                if(x in range(0,self.n) and y in range(0,self.n)):
                        neighList.append(self.getEntry(x,y))
                
                    
                return (neighList)
                

class GraphFromMatrix:
        def __init__(self,n):
                self.n = n
                m = Matrix(n)
                self.adjList = []
                for i in range(0,n*n):
                        self.adjList.append([])

                for i in range(0,n):
                        for j in range(0,n):
                                matrixEntry = m.getEntry(i,j)
                                self.adjList[matrixEntry] = m.getNeighborhood(i,j)
                                
                                
        def printAdjList(self):
                for i in range(0,self.n*self.n):
                        print("node ", i, ": ", self.adjList[i])

        def getAdjList(self):
                return self.adjList

def visit(v,l,path, mark, adj, counter,dotsInPath):
    if(l<dotsInPath):
        for i in adj[v]:
            if(mark[i]==0):
                markCopy = mark[:]
                markCopy[i] = 1
                pathCopy = path[:]
                pathCopy.append(i)
                visit(i,l+1,pathCopy,mark, adj, counter, dotsInPath)
    else:
        counter[0]+=1
        
def numberOfPathsFromVertex(startVertex,n, dotsInPath):
    path=[startVertex]

    mark = []
    for i in range(0,n*n):
        mark.append(0)
    
    mark[startVertex]=1
    counter = [0]

    g = GraphFromMatrix(n)
    adj = g.getAdjList()

    visit(startVertex,1,path, mark, adj, counter, dotsInPath)
    return counter[0]

def numberOfPaths(dotsInPath,n):
    total = 0
    for i in range(0,n*n):
        total+=numberOfPathsFromVertex(i,n,dotsInPath)

    if dotsInPath > 1:
        return total/2
    else:
        return total

for n in range(4,6):
    print ""
    print "Dla macierzy %i na %i"%(n,n)
    print ""
    for i in range(1,11):
        ts = time.time()
        number = numberOfPaths(i,n)
        te = time.time()
        print "Liczba scierzek o dlugosci %i wynosi: %i (%2.2f sek)"%(i,number, (te-ts))
