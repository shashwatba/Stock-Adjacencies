import csv
import numpy as np
import pandas as pd

class Vertex:
    def __init__(self, name, ticker_name, sector, market_cap, employee_count, revenue, profit):
        self.name = name
        self.ticker_name = ticker_name
        self.sector = sector
        self.market_cap = market_cap
        self.employee_count = employee_count
        self.revenue = revenue
        self.profit = profit
        self.similar_stocks = []

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.adjacency_list:
            self.adjacency_list[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex_from, vertex_to):
        if vertex_from in self.adjacency_list and vertex_to in self.adjacency_list:
            self.adjacency_list[vertex_from].similar_stocks.append(self.adjacency_list[vertex_to])
            return True
        else:
            return False

    def similarity_score(self, v1, v2):
        # Sector Similarity Score
        sector_score = 1 if v1.sector == v2.sector else 0

        # Market Cap Similarity Score
        mc_diff = abs(v1.market_cap - v2.market_cap) / max(v1.market_cap, v2.market_cap)
        mc_score = 0 if mc_diff > 1 else 1 - mc_diff

        # Employee Similarity Score
        emp_diff = abs(v1.employee_count - v2.employee_count) / max(v1.employee_count, v2.employee_count)
        emp_score = 0 if emp_diff > 1 else 1 - emp_diff

        # Revenue Similarity Score
        rev_diff = abs(v1.revenue - v2.revenue) / max(v1.revenue, v2.revenue)
        rev_score = 0 if rev_diff > 1 else 1 - rev_diff

        # Profit Similarity Score
        profit_diff = abs(v1.profit - v2.profit) / max(v1.profit, v2.profit)
        profit_score = 0 if profit_diff > 1 else 1 - profit_diff

        # Total Similarity Score
        total_score = 0.2 * (sector_score + mc_score + emp_score + rev_score + profit_score)

        return total_score >= 0.5  # true if similar, false otherwise

    def create_edges(self):
        for v1 in self.adjacency_list.values():
            for v2 in self.adjacency_list.values():
                if v1 != v2 and self.similarity_score(v1, v2):
                    self.add_edge(v1.name, v2.name)



# Initialize the graph
graph = Graph()

# Load the CSV file into a DataFrame
df = pd.read_csv('Fortune1000_Stock_Info.csv')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    vertex = Vertex(row['Company'], row['Ticker'], row['Sector'], row['Market Cap'],
                    row['num. of employees'], row['revenue'], row['profit'])
    graph.add_vertex(vertex)

# Create edges based on similarity score
graph.create_edges()


