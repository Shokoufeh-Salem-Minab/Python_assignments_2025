import pandas as pd # also needs "pip install openpyxl" for excel
import os   # for directory manipulations
from datetime import datetime   # to get current time

# Make the correct path to a project folder
def path_to_folder(folder,filename):
    base_dir = os.path.dirname(__file__)    # current directory path
    super_dir = os.path.dirname(base_dir)   # path to the the parent of "base_dir"
    return f"{super_dir}/{folder}/{filename}"

# Log the output of the function
def log(filename):
    # Create decorator that makes the wrapper (have to use for additional arguments)
    def decorator(func):
        # Wrap the function to return modified wrapper
        def wrapper(*args, **kwargs):
            # Append the output of the function to the file
            with open(path_to_folder("log",f"{filename}.txt"), "a")as file:
                result = func(*args, **kwargs)
                file.write(f"{str(result)} - {datetime.now()}\n")
            return result
        return wrapper
    return decorator

# Save df to a device
def save_df(df, filename):
    # Format specified by the user (case insensitive)
    format = input("Would you like to save it to your device? [N (don't save) / CSV / EXCEL / JSON] - ") # instead of "N" can be anything else 
    
    # Save based on file type
    save_path = path_to_folder("save",filename)
    if format == "csv":
        df.to_csv(f"{save_path}.csv", index=False)
        print("Playlist saved as csv!")
    elif format in ("excel", "xlsx"):
        df.to_excel(f"{save_path}.xlsx", index=False)
        print("Playlist saved as excel!")
    elif format == "json":
        df.to_json(f"{save_path}.json", orient="records", indent=4)
        print("Playlist saved as json!")
    else:
        print("Playlist not saved!")