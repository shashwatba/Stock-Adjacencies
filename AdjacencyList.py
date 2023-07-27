class Vertex:
    def __init__(self, name):
        self.name = name
        self.outDegree = 0
        #self.oldRank = 0.0
        #self.newRank = 0.0
        self.pointingToVertex = [] # list of Vertices that point to the Vertex

class AdjacencyList:
    def __init__(self, linesToRead):
        self.vertices = {} # dictionary of Vertex objects

        for i in range(linesToRead):
            givingVertex=input()
            receivingVertex = input()

            # Get or create the vertices by their names
            if givingVertex not in self.vertices: # if this is a new vertex
                self.vertices[givingVertex] = Vertex(givingVertex)
            if receivingVertex not in self.vertices: # if this is a new vertex
                self.vertices[receivingVertex] = Vertex(receivingVertex)

            # Increment outDegree of givingVertex
            self.vertices[givingVertex].outDegree += 1

            # Add givingVertex to the list of vertices pointing to receivingVertex
            self.vertices[receivingVertex].pointingToVertex.append(self.vertices[givingVertex])

        # Now that we have all vertices, calculate initial rank (1/numOfTotalVertices)
        for vertex in self.vertices.values():
            vertex.oldRank = 1.0 / len(self.vertices)
'''
    def PageRank(self, numOfPowerIterations):
        for i in range(1, numOfPowerIterations): # starts at one because 1 is the least amount of power iterations we can have (ranks are all 1/numOfTotalVertices)
            for vertex in self.vertices.values():
                for j in vertex.pointingToVertex: # iterates through list of Vertices that point to Vertex that we are at.
                    vertex.newRank += (1.0 / j.outDegree) * j.oldRank

         if i+1 != numOfPowerIterations: # if there will be another powerIteration coming, we have to reset newRank to 0 and make newRank's prev value now be oldRank.
            for vertex in self.vertices.values():
                vertex.oldRank = vertex.newRank
                vertex.newRank = 0
                '''

def print(self, numOfPowerIterations):
        for vertex in self.vertices.values():
            if numOfPowerIterations > 1: # means we can use "newRank" because has been upgraded from 0
                print(f"{vertex.name} {vertex.newRank:.2f}")
            elif numOfPowerIterations <= 1: # means we cannot use "newRank" because it's still zero but should be 1/numOfTotalVertices
                print(f"{vertex.name} {vertex.oldRank:.2f}")