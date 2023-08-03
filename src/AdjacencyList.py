import csv
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter.font import Font
import time

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
            self.adjacency_list[vertex.ticker_name] = vertex
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
        mc_percentdiff=abs((v1.market_cap - v2.market_cap) / ((v1.market_cap + v2.market_cap)/2))
        mc_form = abs(v1.market_cap - v2.market_cap) / max(v1.market_cap, v2.market_cap)
        mc_score = 0 if mc_percentdiff > 1 else 1 if mc_percentdiff <= 0.1 else 1 - mc_form

        # Employee Similarity Score
        emp_percentdiff=abs((v1.employee_count - v2.employee_count) / ((v1.employee_count + v2.employee_count)/2))
        emp_form = abs(v1.employee_count - v2.employee_count) / max(v1.employee_count, v2.employee_count)
        emp_score = 0 if emp_percentdiff > 1 else 1 if emp_percentdiff <= 0.1 else 1 - emp_form

        # Revenue Similarity Score
        rev_percentdiff=abs((v1.revenue - v2.revenue) / ((v1.revenue + v2.revenue)/2))
        rev_form = abs(v1.revenue - v2.revenue) / max(v1.revenue, v2.revenue)
        rev_score = 0 if rev_percentdiff > 1 else 1 if rev_percentdiff <= 0.1 else 1 - rev_form

        # Profit Similarity Score
        if v1.profit + v2.profit == 0: #in case when add profits of two companies so don't divide by 0
            profit_percentdiff = 0
        else:
            profit_percentdiff = abs((v1.profit - v2.profit) / ((v1.profit + v2.profit) / 2))
        profit_form = abs(v1.profit - v2.profit) / max(v1.profit, v2.profit)
        profit_score = 0 if profit_percentdiff > 1 else 1 if profit_percentdiff <= 0.1 else 1 - profit_form

        # Total Similarity Score
        total_score = 0.2 * (sector_score + mc_score + emp_score + rev_score + profit_score)

        return total_score

    def create_edges(self):
        for v1 in self.adjacency_list.values():
            for v2 in self.adjacency_list.values():
                if v1 != v2 and self.similarity_score(v1, v2)>0.50:
                    self.add_edge(v1.ticker_name, v2.ticker_name)