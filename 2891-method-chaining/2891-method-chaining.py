import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # 1. Filter for weight > 100
    heavy_animals = animals[animals['weight'] > 100]
    
    # 2. Sort by weight in descending order
    sorted_animals = heavy_animals.sort_values(by='weight', ascending=False)
    
    # 3. Return only the 'name' column as a DataFrame
    return sorted_animals[['name']]