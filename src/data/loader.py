import os
import pandas as pd

def load_csv(file_path: str)-> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset not found !!")

    file_size_in_mb = os.stat(file_path).st_size / (1024 *1024)
    print(f"Loading {file_path} ({file_size_in_mb:.1f} MB)...")
 # suppose files are very large and cant be fitted in ram then something we have to do like chunking and iterating
    return pd.read_csv (file_path)
