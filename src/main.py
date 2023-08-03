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

def merge_sort(arr, vertex):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half,vertex), merge_sort(right_half,vertex),vertex)

def merge(left, right, vertex):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if graph.similarity_score(left[left_index],vertex) > graph.similarity_score(right[right_index],vertex):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either half, append them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def quick_sort(arr, vertex):
    """Implementing QuickSort Algorithm to sort the array in descending order"""
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if graph.similarity_score(vertex, x) < graph.similarity_score(vertex, pivot):
                less.append(x)
            elif graph.similarity_score(vertex, x) == graph.similarity_score(vertex, pivot):
                equal.append(x)
            elif graph.similarity_score(vertex, x) > graph.similarity_score(vertex, pivot):
                greater.append(x)
        return quick_sort(greater, vertex)+equal+quick_sort(less, vertex)
    else:
        return arr


def search_stock(event=None):
    start_time = time.time()
    query = search_entry.get().upper()

    if query in graph.adjacency_list:
        vertex = graph.adjacency_list[query]
        stock_info_label.config(text=f"Company Name: {vertex.name}\n"
                                     f"Sector: {vertex.sector}\n"
                                     f"Market Cap: {vertex.market_cap}\n"
                                     f"Employee Count: {vertex.employee_count}\n"
                                     f"Revenue: {vertex.revenue}\n"
                                     f"Profit: {vertex.profit}")

        # Apply sort on similar stocks by similarity score in descending order
        if quick_button.cget('image') == str(blue_img):
            sorted_similar_stocks = quick_sort(vertex.similar_stocks,vertex) # Worst Case: O(n^2)
        elif merge_button.cget('image') == str(blue_img):
            sorted_similar_stocks = merge_sort(vertex.similar_stocks,vertex) # Worst Case: O(nlog(n))
        else:
            error_label.config(text="Error: Please select a sorting method", fg="red")
            return

        similar_stocks_string = "\n".join([f"{v.name} ({v.ticker_name}), Similarity Score: {graph.similarity_score(vertex, v)* 100:.2f}%"
                                    for v in sorted_similar_stocks])
        similar_stocks_label.config(text=similar_stocks_string)
    else:
        stock_info_label.config(text="Stock not found!")
        similar_stocks_label.config(text="")

    end_time = time.time()
    time_taken_label.config(text=f"Time taken: {end_time - start_time:.10f} seconds")

app = tk.Tk()
app.title("Stock Info")
app.geometry("400x400")

search_entry = tk.Entry(app, width=30)
search_entry.pack(pady=10)

search_button = tk.Button(app, text="Search", command=search_stock)
search_button.pack()

def quick_button_clicked():
    quick_button.config(image=blue_img)
    merge_button.config(image=gray_img)
    error_label.config(text="")  # reset the error message

def merge_button_clicked():
    merge_button.config(image=blue_img)
    quick_button.config(image=gray_img)
    error_label.config(text="")  # reset the error message

# load images
blue_img = tk.PhotoImage(file="blue_circle.png")
gray_img = tk.PhotoImage(file="gray_circle.png")

# resize images
blue_img = blue_img.subsample(140, 140)
gray_img = gray_img.subsample(100, 100)

# create buttons with images and text
quick_button = tk.Button(app, image=gray_img, text="Quick", compound="left", anchor="w", command=quick_button_clicked)
quick_button.pack()

merge_button = tk.Button(app, image=gray_img, text="Merge", compound="left", anchor="w", command=merge_button_clicked)
merge_button.pack()

stock_info_label = tk.Label(app, text="")
stock_info_label.pack(pady=10)

similar_stocks_label = tk.Label(app, text="")
similar_stocks_label.pack(pady=10)

error_label = tk.Label(app, text="", fg="red")
error_label.pack(pady=10)

time_taken_label = tk.Label(app, text="")
time_taken_label.pack(pady=10)

search_entry.bind("<Return>", search_stock)

app.mainloop()