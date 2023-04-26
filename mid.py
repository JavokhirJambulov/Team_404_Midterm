import tkinter as tk
import urllib.parse
import requests
import openai

openai.api_key = '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'
messages = [ {"role": "system", "content": 
              "You are an intelligent assistant."} ]

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "LiK0g4cAuVKdQX7nkNGbVCFd4XIjKzNT"

def get_directions():
    orig = orig_entry.get()
    dest = dest_entry.get()
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        directions_text.config(state="normal")
        directions_text.delete("1.0", tk.END)
        directions_text.insert(tk.END, f"Directions from {orig} to {dest}\n\n")
        directions_text.insert(tk.END, f"Trip Duration: {json_data['route']['formattedTime']}\n")
        directions_text.insert(tk.END, f"Kilometers: {str('{:.2f}'.format((json_data['route']['distance'])*1.61))}\n\n")
        for each in json_data['route']['legs'][0]['maneuvers']:
            directions_text.insert(tk.END, f"{each['narrative']} ({str('{:.2f}'.format((each['distance'])*1.61))} km)\n")
        directions_text.insert(tk.END, "\n\n")
        messages.append({"role": "system", "content": "You are an intelligent assistant."})
        messages.append({"role": "user", "content": f"Give me 5 best hotels in {dest}. Do not display 'Sure, here are the 5 best hotels in {dest}:'"})
        chat = openai.Completion.create(model="davinci", prompt=messages, max_tokens=1024)
        reply = chat.choices[0].text
        directions_text.insert(tk.END, f"{reply}\n")
        messages.append({"role": "assistant", "content": reply})
        messages.append({"role": "user", "content": f"Give me gas station locations in the route from {orig} to {dest}. Do not display the initial message of the chatgpt response."})
        chat = openai.Completion.create(model="davinci", prompt=messages, max_tokens=1024)
        reply = chat.choices[0].text
        directions_text.insert(tk.END, f"{reply}\n")
        messages.append({"role": "assistant", "content": reply})
        directions_text.config(state="disabled")
    elif json_status == 402:
        tk.messagebox.showerror("Error", f"Status Code: {json_status}; Invalid user inputs for one or both locations.")
    elif json_status == 611:
        tk.messagebox.showerror("Error", f"Status Code: {json_status}; Missing an entry for one or both locations.")
    else:
        tk.messagebox.showerror("Error", f"For Status Code: {json_status}; Refer to https://developer.mapquest.com/documentation/directions-api/status-codes")

# GUI setup
root = tk.Tk()
root.title("Directions App")

orig_label = tk.Label(root
