# View the layout of an API JSON response

import requests
import sys

def json_expand(x, indent = 0):                 # Defines the function and the indent of the output
    if isinstance(x, dict):                     # if x  is a dictionary or something alike
        for key, value in x.items(): 
            label = str(key)
            if isinstance(value, list):
                label += f" (list, {len(value)} items)"           # then  for every key, value pairs in the items of x
            print(' ' * indent + str(key))      # print spacebar times the indent value + the key as a string
            json_expand(value, indent + 2)       # recursive call to the function with the value and increased indent    
    elif isinstance(x,list):                    # if x is a list or something alike
        if len(x) > 0:                          # if the length of x is more than 0
            json_expand(x[0], indent + 0)       # recursive call to the function with the first element of the list and same indent
    else:
        pass

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://api.openalex.org/works"

    response = requests.get(url)
    data = response.json()

    # debug / info
    print(f"URL: {url}")
    print(f"Top-level type: {type(data)}")
    if isinstance(data, dict):
        print(f"Top-level keys: {list(data.keys())}")
    print("\nStructure:\n")
    json_expand(data)

if __name__ == "__main__":
    main()