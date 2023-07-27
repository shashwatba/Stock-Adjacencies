#from AdjacencyList import *
import numpy as np
import pandas as pd
import yfinance as yahooFinance

'''
Let's start by defining a similarity score that ranges from 0 to 1, with 1 being the most similar:

Similarity Score = Industry Similarity Score * 0.5 + Market Cap Similarity Score * 0.3 + Dividend Similarity Score * 0.2

Each individual score also ranges from 0 to 1. Here's how you might calculate each one:

Industry Similarity Score: This one's simple. If the two stocks are in the same industry, the score is 1. If not, the score is 0.

Market Cap Similarity Score: First, you might define what counts as a "similar" market cap. For instance, you might say 
that two stocks are similar if their market caps are within 10% of each other. To calculate the score:

If the market caps are within 20% of each other, the score is 1.
If one stock's market cap is more than double the other's, the score is 0.
For anything in between, you could calculate the score as 1 - (Absolute Difference in Market Cap / Larger Market Cap).
Dividend Similarity Score: Again, you'll need to define what counts as a "similar" dividend yield. For instance, you might say 
that two stocks are similar if their dividend yields are within 1% of each other. To calculate the score:

If the dividend yields are within 20% of each other, the score is 1.
If one stock's dividend yield is more than double the other's, the score is 0.
For anything in between, you could calculate the score as 1 - (Absolute Difference in Dividend Yield / Larger Dividend Yield).
Then, you can add up the scores for each criterion, weighted according to their importance in your analysis, to get the total 
Similarity Score. If the Similarity Score is above a certain threshold, you might consider the stocks to be "similar".
'''

GetFacebookInformation = yahooFinance.Ticker("META")

# whole python dictionary is printed here
print(GetFacebookInformation.info)