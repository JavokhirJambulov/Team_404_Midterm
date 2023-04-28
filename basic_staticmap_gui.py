import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

# MapQuest Static Map API endpoint
url = "https://www.mapquestapi.com/staticmap/v5/map"

# MapQuest API key
key = "LiK0g4cAuVKdQX7nkNGbVCFd4XIjKzNT"

# Parameters for the static map image
params = {
    "key": key,
    "size": "600,400@2x",
    "zoom": 10,
    "start": "Seoul",
    "end": "Incheon",
}


# Send a GET request to the MapQuest Static Map API
response = requests.get(url,params = params)

# Create a Tkinter window
root = tk.Tk()

# Convert the response content to a PIL Image object
image = Image.open(io.BytesIO(response.content))

# Convert the PIL Image to a Tkinter PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a label with the PhotoImage and pack it to the Tkinter window
label = tk.Label(root, image=photo)
label.pack()

# Run the Tkinter event loop
root.mainloop()