import tkinter as tk
from tkinter import messagebox
import requests
from pprint import pprint

def search_bing(query, response_filter):
    subscription_key = "confidential"  # Podmień na swój klucz subskrypcji
    endpoint = "https://api.bing.microsoft.com/v7.0/search"
    mkt = 'en-US'
    params = {'q': query, 'mkt': mkt, 'responseFilter': response_filter}
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if response_filter in data:
            result_text = ""
            for item in data[response_filter]['value']:
                if response_filter == 'webPages':
                    result_text += f"Title: {item['name']}\nURL: {item['url']}\n\n"
                elif response_filter == 'images':
                    result_text += f"Image URL: {item['contentUrl']}\n\n"
                elif response_filter == 'news':
                    result_text += f"Headline: {item['name']}\nDate: {item['datePublished']}\nDescription: {item['description']}\nURL: {item['url']}\n\n"
            return result_text
        else:
            return f"No {response_filter} found."

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as ex:
        return f"Error occurred: {ex}"

def on_search():
    query = query_entry.get()
    choice = search_type_var.get()

    if query and choice:
        if choice == 'WebPages':
            response_filter = 'webPages'
        elif choice == 'Images':
            response_filter = 'images'
        elif choice == 'News':
            response_filter = 'news'

        search_results = search_bing(query, response_filter)
        messagebox.showinfo("Search Results", search_results)
    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

root = tk.Tk()
root.title("Bing Search")

# Query Entry
query_label = tk.Label(root, text="Query:")
query_label.pack()
query_entry = tk.Entry(root)
query_entry.pack()

# Search Type Radio Buttons
search_type_var = tk.StringVar()
search_type_label = tk.Label(root, text="Search Type:")
search_type_label.pack()

search_types = ['WebPages', 'Images', 'News']
for search_type in search_types:
    search_type_radio = tk.Radiobutton(root, text=search_type, variable=search_type_var, value=search_type)
    search_type_radio.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack()

root.mainloop()
