from AdjacencyList import *

import numpy as np
import pandas as pd

'''
Note: All the data you need should be in columns A-G, anything after can be disregarded but don't delete it because we need it in the file to satisfy the 18,000 data points

Similarity Score =(Sector Similarity Score * 0.2) + (Market Cap Similarity Score * 0.2) + (Employee Similarity Score * 0.2) + (Revenue Similarity Score * 0.2) + (Profit Similarity Score * 0.2)

Each individual score ranges from 0 to 1. Here's how you calculate each one:

1. Sector Similarity Score: If the two stocks are in the same "Sector", the score is 1. If not, the score is 0.

2. Market Cap Similarity Score: For instance, you might say that two stocks are similar if their market caps are within 10% of each other. To calculate the score:
    - If the market caps are within 10% of each other, the score is 1.
    - If one stock's market cap is more than double the other's, the score is 0.
    - For anything in between, calculate the score as `1 - (Absolute Difference in Market Cap / Larger Market Cap)`.

3. Employee Similarity Score: You might define two stocks as similar if their number of employees is within 10% of each other:
    - If the numbers of employees are within 10% of each other, the score is 1.
    - If one company's number of employees is more than double the other's, the score is 0.
    - For anything in between, calculate the score as `1 - (Absolute Difference in Number of Employees / Company with More Employees)`.

4. Revenue Similarity Score: Define two stocks as similar if their revenues are within 10% of each other:
    - If the revenues are within 10% of each other, the score is 1.
    - If one company's revenue is more than double the other's, the score is 0.
    - For anything in between, calculate the score as `1 - (Absolute Difference in Revenue / Company with Higher Revenue)`.

5. Profit Similarity Score: Define two stocks as similar if their profits are within 10% of each other:
    - If the profits are within 10% of each other, the score is 1.
    - If one company's profit is more than double the other's, the score is 0.
    - For anything in between, calculate the score as `1 - (Absolute Difference in Profit / Company with Higher Profit)`.

Then, you can add up the scores for each criterion, weighted according to their importance in your analysis, to get the total Similarity Score.
If the Similarity Score >= 0.5, you might consider the stocks to be "similar". (We can make this number smaller or larger later on but for now I feel like this is good)

'''