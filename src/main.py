from AdjacencyList import *

# Initialize the graph
graph = Graph()

# Load the CSV file into a DataFrame
df = pd.read_csv('Fortune1000_Stock_Info.csv')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    vertex = Vertex(row['Company'], row['Ticker'], row['Sector'], float(row['Market Cap']),
                    float(row['num. of employees']), float(row['revenue']), float(row['profit']))
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
    #Implementing QuickSort Algorithm to sort the array in descending order
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

allow_scroll = False  # global flag variable

def search_stock(event=None):
    start_time = time.time()

    global allow_scroll

    query = search_entry.get().upper()

    if query in graph.adjacency_list:
        vertex = graph.adjacency_list[query]
        stock_info_label.config(text=f"Company Name: {vertex.name}\n" #added commas to separate number values, also some numbers were shortened in the csv file so printing full values (converted to int so no ".0" at the end)
                                     f"Sector: {vertex.sector}\n"
                                     f"Market Cap: ${int(vertex.market_cap*1000000):,}\n"
                                     f"Yearly Revenue: ${int(vertex.revenue*1000000):,}\n"
                                     f"Yearly Profit: ${int(vertex.profit*1000000):,}\n"
                                     f"Employee Count: {int(vertex.employee_count):,}\n")

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

    allow_scroll = True
    end_time = time.time()
    time_taken_label.config(text=f"Time taken: {end_time - start_time:.10f} seconds")

app = tk.Tk()
app.title("Triumph Trading")
app.geometry("400x600")

# Set up the scrolling frame
canvas = tk.Canvas(app, borderwidth=0, background="gray")  # changing the canvas background to gray
frame = tk.Frame(canvas, background="gray")  # changing the frame background to gray
vsb = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)
canvas.create_window((200,300), window=frame, anchor="center")

def onFrameConfigure(canvas):
    # Reset the scroll region to encompass the inner frame
    canvas.after_idle(lambda: canvas.configure(scrollregion=canvas.bbox("all")))

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# Create a container frame that will expand and fill its parent
container_outer = tk.Frame(frame, background="gray")  # changing the outer container background to gray
container_outer.pack(side="top", fill="both", expand=True)

# Create another frame that will hold your widgets
container = tk.Frame(container_outer, background="gray")  # changing the inner container background to gray

# Pack the container in its parent (it will center automatically)
container.pack()

# Add a label for the company name "Triumph Trading"
company_name_label = tk.Label(container, text="Triumph Trading", font=("Helvetica", 16, "bold"), fg="yellow", bg="gray")
company_name_label.pack(pady=10)

# Modify the scroll handlers to check the flag
def _on_mousewheel(event):
    global allow_scroll
    if allow_scroll:
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def _on_unix_scroll(event):
    global allow_scroll
    if allow_scroll:
        if event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")


app.bind_all("<MouseWheel>", _on_mousewheel)
app.bind_all("<Button-4>", _on_unix_scroll)
app.bind_all("<Button-5>", _on_unix_scroll)


# We use padx and pady to give some space around the widgets
search_entry = tk.Entry(container, width=30)
search_entry.pack(pady=10)
search_entry.bind('<Return>', search_stock)


search_button = tk.Button(container, text="Search", command=search_stock)
search_button.pack(pady=10)

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

# Quick Button
quick_button = tk.Button(container, image=gray_img, text="Quick", compound="left", anchor="w", command=quick_button_clicked)
quick_button.pack(pady=10)

# Merge Button
merge_button = tk.Button(container, image=gray_img, text="Merge", compound="left", anchor="w", command=merge_button_clicked)
merge_button.pack(pady=10)

# Stock Info Label
stock_info_label = tk.Label(container, bg="gray")
stock_info_label.pack(pady=10)

# Similar Stocks Label
similar_stocks_label = tk.Label(container, bg="gray")
similar_stocks_label.pack(pady=10)

# Error Label
error_label = tk.Label(container, bg="gray")
error_label.pack(pady=10)

# Time Taken Label
time_taken_label = tk.Label(container, bg="gray")
time_taken_label.pack(pady=10)

app.mainloop()