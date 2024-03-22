#!/usr/bin/env python3

import sys

# Read included years from years.txt
with open('years.txt', 'r') as f:
    included_years = f.read().split()

# Process the input line by line
for line in sys.stdin:
    # Parse the input line
    uid, title, genres, year, rating = line.strip().split('\t')
    
    # Check if the year is included in the list of years
    if included_years and year not in included_years:
        continue
    
    # Split genres and emit key-value pairs for each genre
    for genre in genres.split('|'):
        # Emit key-value pairs with composite key (year_title) and rating as value
        print('%s_%s\t%s' % (year, genre, rating))
