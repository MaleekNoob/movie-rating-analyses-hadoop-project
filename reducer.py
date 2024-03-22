#!/usr/bin/env python3

import sys
from collections import defaultdict

# Minimum number of votes required for a movie to be considered
min_votes = 10

# Initialize a dictionary to store the ratings for each film
film_ratings = defaultdict(list)

# Process the input line by line
for line in sys.stdin:
    try:
        # Parse the input line
        key, value = line.strip().split('\t')
        year, genre = key.split('_')
        rating = float(value)
    except ValueError:
        # Skip lines with invalid format
        continue
    
    # Add the rating to the list of ratings for the current film
    film_ratings[key].append(rating)

# Calculate and output the average rating for each film
for key, ratings in film_ratings.items():
    total_votes = len(ratings)
    if total_votes >= min_votes:
        avg_rating = sum(ratings) / total_votes
        print('%s\t%s\t%s' % (key, avg_rating, total_votes))