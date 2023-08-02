from AdjacencyList import *



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
