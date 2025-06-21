import pandas as pd

def recommend_food(mood_category, preference="Veg"):
    # Load food data
    df = pd.read_csv("data/food_data.csv")
    
    # Filter by mood and preference
    recommended = df[
        (df["Mood Category"] == mood_category) & 
        (df["Type"] == preference)
    ]
    
    # Return list of food items
    return recommended["Food"].tolist()
