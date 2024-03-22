#!/usr/bin/env python3

import sys

# Minimum number of votes required for a movie to be considered
min_votes = 10

current_key = None
film_ratings = []

# Process the input line by line
for line in sys.stdin:
    # Parse the input line
    key, value = line.strip().split('\t')
    year, genre = key.split('_')
    rating = float(value)
    
    # If the key changes, it means we're moving to a new film or year
    if key != current_key:
        # Output the average rating for the previous film if it meets the minimum votes criteria
        if current_key:
            total_votes = len(film_ratings)
            if total_votes >= min_votes:
                avg_rating = sum(film_ratings) / total_votes
                print('%s\t%s\t%s' % (current_key, avg_rating, total_votes))
        
        # Reset variables for the new film or year
        current_key = key
        film_ratings = []
    
    # Add the rating to the list of ratings for the current film
    film_ratings.append(rating)

# Output for the last film
if current_key:
    total_votes = len(film_ratings)
    if total_votes >= min_votes:
        avg_rating = sum(film_ratings) / total_votes
        print('%s\t%s\t%s' % (current_key, avg_rating, total_votes))
