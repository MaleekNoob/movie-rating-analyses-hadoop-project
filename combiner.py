#!/usr/bin/env python3

import sys

# Initialize variables to store aggregated ratings
current_key = None
total_rating = 0
count = 0

# Process input from standard input
for line in sys.stdin:
    key, rating = line.strip().split('\t')
    rating = float(rating)

    # Check if the key (year and genre combination) has changed
    if key != current_key:
        # If it's a new key, output the aggregated rating for the previous key
        if current_key:
            print(f"{current_key}\t{total_rating / count}")
        
        # Update current_key and reset total_rating and count for the new key
        current_key = key
        total_rating = rating
        count = 1
    else:
        # If it's the same key, accumulate the rating and increment the count
        total_rating += rating
        count += 1

# Output the aggregated rating for the last key
if current_key:
    print(f"{current_key}\t{total_rating / count}")
