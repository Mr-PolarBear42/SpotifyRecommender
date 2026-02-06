import pandas as pd
from sklearn.preprocessing import LabelEncoder
def import_data(data_dir="./Data"): # Returns numerical data, artist data, and genre data, requires the path to the data directory as an argument
    print("Importing data...")
    data_path = f"{data_dir}/dataset.csv"
    data=pd.read_csv(data_path)
    print("Data imported successfully.")
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns # Select only numerical columns
    numerical_data = data[numerical_cols]
    Artist_encoder = LabelEncoder()
    artist_data= Artist_encoder.fit_transform(data['artists']) # Encode the 'artists' column using LabelEncoder
    Genre_encoder = LabelEncoder()
    genre_data= Genre_encoder.fit_transform(data['track_genre']) # Encode the 'track_genre' column using LabelEncoder
    print("Data preprocessing (step 1) completed.")
    return numerical_data, artist_data, genre_data
    
if __name__ == "__main__":
    import_data()