from AdjacencyList import *


import tkinter as tk
from tkinter.font import Font
import time

# Sample stock data for demonstration purposes
sample_stock_data = {
    "AAPL": {"Name": "Apple Inc.", "Price": "$148.90", "Change": "+1.24 (+0.84%)"},
    "GOOGL": {"Name": "Alphabet Inc.", "Price": "$2790.75", "Change": "+17.80 (+0.64%)"},
    "AMZN": {"Name": "Amazon.com Inc.", "Price": "$3342.88", "Change": "+26.68 (+0.80%)"},
    "MSFT": {"Name": "Microsoft Corp.", "Price": "$291.66", "Change": "+1.86 (+0.64%)"},
    "TSLA": {"Name": "Tesla Inc.", "Price": "$711.92", "Change": "+8.02 (+1.14%)"}
}

def search_stock(event=None):
    start_time = time.time()
    query = search_entry.get().upper()
    if query in sample_stock_data:
        stock_info_label.config(text=f"Stock: {sample_stock_data[query]['Name']}\n"
                                     f"Price: {sample_stock_data[query]['Price']}\n"
                                     f"Change: {sample_stock_data[query]['Change']}")
    else:
        stock_info_label.config(text="Stock not found!")
    end_time = time.time()
    time_taken_label.config(text=f"Time taken: {end_time - start_time:.5f} seconds")

# Create the main application window
app = tk.Tk()
app.title("Triumph Trading")
app.geometry("400x400")
app.configure(bg="black")

# Set the custom "Pacifico" font for the Triumph Trading title
title_font = Font(family="Pacifico", size=24, slant="italic")
title_label = tk.Label(app, text="Triumph Trading", font=title_font, fg="#FFD700", bg="black")
title_label.pack(pady=10)

# Create and place the widgets
search_entry = tk.Entry(app, width=30, fg="white", bg="black")
search_entry.pack(pady=10)

search_button = tk.Button(app, text="Search", command=search_stock, fg="black", bg="#FFD700")
search_button.pack()

stock_info_label = tk.Label(app, text="", fg="white", bg="black")
stock_info_label.pack(pady=10)

time_taken_label = tk.Label(app, text="", fg="white", bg="black")
time_taken_label.pack(pady=10)

# Bind the <Return> event to the search_stock function
search_entry.bind("<Return>", search_stock)

app.mainloop()


# Initialize the graph
graph = Graph()

# Load the CSV file into a DataFrame
df = pd.read_csv('Fortune1000_Stock_Info.csv')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    vertex = Vertex(row['Company'], row['Ticker'], row['Sector'], float(row['Market Cap']),
                    int(row['num. of employees']), float(row['revenue']), float(row['profit']))
    graph.add_vertex(vertex)

# Create edges based on similarity score
graph.create_edges()



ticker_name = input("Enter a ticker name: ")

# Find the vertex with that ticker name and display its similar stocks
graph.find_and_display_vertex(ticker_name)