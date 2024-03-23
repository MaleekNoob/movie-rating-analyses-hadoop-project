#!/usr/bin/env python3

import sys

# Initialize variables to keep track of movie ratings
movie_ratings = {}

# Process the input line by line
for line in sys.stdin:
    # Split the line into fields
    fields = line.strip().split('\t')
    
    # Check if the line has the expected number of fields
    if len(fields) != 5:
        # Skip this line if it does not match the expected format
        continue
    
    # Extract movie title and rating from the fields
    movie_title = fields[1]
    rating = float(fields[4])
    
    # Update the movie ratings dictionary
    if movie_title in movie_ratings:
        movie_ratings[movie_title].append(rating)
    else:
        movie_ratings[movie_title] = [rating]

# Emit the aggregated ratings for each movie title
for movie_title, ratings in movie_ratings.items():
    # Calculate the total rating and count of ratings
    total_rating = sum(ratings)
    rating_count = len(ratings)
    
    # Emit the movie title and aggregated rating
    print('%s\t%s\t%s' % (movie_title, total_rating, rating_count))
