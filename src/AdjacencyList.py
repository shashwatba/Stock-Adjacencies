class Vertex: #Each stock will be a vertex
    def __init__(self, name):
        self.name = name
        self.ticker_name=""
        self.sector=""
        self.market_cap=0
        self.employee_count=0
        self.revenue=0
        self.profit=0
        self.similar_stocks = [] #list of Stock Vertices that are similar to this Vertex (Stock)

class AdjacencyList: #ToDO: This is a constructor I used for Proj 2 but we will need to fix it to parse through the CSV file, not read from user input
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
    def Similarity Score():


        Gonna have to code this one
                '''