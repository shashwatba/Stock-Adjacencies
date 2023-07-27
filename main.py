#from AdjacencyList import *
import numpy as np
import pandas as pd
import yfinance as yahooFinance

'''
Option 1:
Correlation Graph: You can model correlations between different stocks. 
In this graph, an edge between two stocks might indicate a strong correlation (either positive or negative) 
between their price movements. If the correlation exceeds a certain threshold, you could add an edge in the graph. 
This graph would enable you to visualize clusters of highly correlated stocks.



Option 2:
Sector/Industry Graph: You could model a graph where edges represent stocks being in the same sector or industry. 
This can help you visualize how different sectors/industries are interconnected based on shared companies.
'''

GetFacebookInformation = yahooFinance.Ticker("META")

# whole python dictionary is printed here
print(GetFacebookInformation.info)