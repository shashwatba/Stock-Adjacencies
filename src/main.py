from AdjacencyList import *


import tkinter as tk
from tkinter.font import Font
import time



# Initialize the graph
graph = Graph()

# Load the CSV file into a DataFrame
df = pd.read_csv('Fortune1000_Stock_Info.csv')

stock_data = {}
# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    vertex = Vertex(row['Company'], row['Ticker'], row['Sector'], float(row['Market Cap']),
                    int(row['num. of employees']), float(row['revenue']), float(row['profit']))
    graph.add_vertex(vertex)
    stock_data[row['Ticker'].upper()] = vertex

# Create edges based on similarity score
graph.create_edges()


def search_stock(event=None):
    start_time = time.time()
    query = search_entry.get().upper()

    if query in stock_data:
        vertex = stock_data[query]
        stock_info_label.config(text=f"Stock: {vertex.name}\n"
                                     f"Ticker: {vertex.ticker_name}\n"
                                     f"Sector: {vertex.sector}\n"
                                     f"Market Cap: {vertex.market_cap}\n"
                                     f"Employee Count: {vertex.employee_count}\n"
                                     f"Revenue: {vertex.revenue}\n"
                                     f"Profit: {vertex.profit}")
        similar_stocks = "\n".join([f"{v.name} ({v.ticker_name}), similarity score: {graph.similarity_score(vertex, v)* 100:.2f}%"
                                    for v in vertex.similar_stocks])
        similar_stocks_label.config(text=similar_stocks)
    else:
        stock_info_label.config(text="Stock not found!")
        similar_stocks_label.config(text="")

    end_time = time.time()
    time_taken_label.config(text=f"Time taken: {end_time - start_time:.5f} seconds")


app = tk.Tk()
app.title("Stock Info")
app.geometry("400x400")

search_entry = tk.Entry(app, width=30)
search_entry.pack(pady=10)

search_button = tk.Button(app, text="Search", command=search_stock)
search_button.pack()

stock_info_label = tk.Label(app, text="")
stock_info_label.pack(pady=10)

similar_stocks_label = tk.Label(app, text="")
similar_stocks_label.pack(pady=10)

time_taken_label = tk.Label(app, text="")
time_taken_label.pack(pady=10)

search_entry.bind("<Return>", search_stock)

app.mainloop()
