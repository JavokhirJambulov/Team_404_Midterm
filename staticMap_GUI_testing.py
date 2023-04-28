import tkinter as tk
import requests
import io
from PIL import Image, ImageTk

# MapQuest Static Map API endpoint
url = "https://www.mapquestapi.com/staticmap/v5/map"

# MapQuest API key
key = "LiK0g4cAuVKdQX7nkNGbVCFd4XIjKzNT"

# Create tkinter window
root = tk.Tk()
root.geometry("1000x900")

# Create tkinter labels and entries for origin and destination
tk.Label(root, text="Origin").grid(row=0)
origin_entry = tk.Entry(root)
origin_entry.grid(row=0, column=1)

tk.Label(root, text="Destination").grid(row=1)
dest_entry = tk.Entry(root)
dest_entry.grid(row=1, column=1)

# Create tkinter button to show map and route
def show_map():
    origin = origin_entry.get()
    dest = dest_entry.get()
    # Parameters for the static map image
    params = {
        "key": key,
        "size": "600,400@2x",
        "zoom": 8,
        "start": origin,
        "end": dest,
    }

    # Send a GET request to the MapQuest Static Map API
    response = requests.get(url,params = params)

    img_data = Image.open(io.BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    map_label = tk.Label(root, image=img)
    map_label.image = img
    map_label.grid(row=3, columnspan=2)


    

# Create tkinter button to show map and route
tk.Button(root, text="Show Map", command=show_map).grid(row=2, columnspan=2)

# Run tkinter main loop
root.mainloop()
