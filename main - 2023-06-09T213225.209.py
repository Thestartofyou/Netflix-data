import pandas as pd

# Load the Netflix data (CSV file)
netflix_data = pd.read_csv('netflix_data.csv')

# Display the first few rows of the dataset
print("First 5 rows of the Netflix data:")
print(netflix_data.head())

# Get the total number of shows/movies in the dataset
total_entries = len(netflix_data)
print("Total number of shows/movies:", total_entries)

# Get the number of unique titles in the dataset
unique_titles = len(netflix_data['Title'].unique())
print("Number of unique titles:", unique_titles)

# Get the most watched genres
top_genres = netflix_data['Genre'].value_counts().head(5)
print("Top 5 most watched genres:")
print(top_genres)

# Convert the 'Date Watched' column to datetime format
netflix_data['Date Watched'] = pd.to_datetime(netflix_data['Date Watched'])

# Get the earliest and latest date of watching
earliest_date = netflix_data['Date Watched'].min()
latest_date = netflix_data['Date Watched'].max()
print("Earliest date watched:", earliest_date)
print("Latest date watched:", latest_date)

# Calculate the total duration watched
total_duration = netflix_data['Duration'].sum()
print("Total duration watched (in minutes):", total_duration)

# Calculate the average rating
average_rating = netflix_data['Rating'].mean()
print("Average rating:", average_rating)
