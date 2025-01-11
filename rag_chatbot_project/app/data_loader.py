import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully with {len(data)} entries.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
