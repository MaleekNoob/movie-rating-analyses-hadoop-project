#!/usr/bin/env bash

# Update the paths for mapper, combiner, and reducer scripts
cat C:/movie-rating-analyses-hadoop-project/r5.txt | ./C:/movie-rating-analyses-hadoop-project/mapper.py > mapout.txt
sort mapout.txt | ./C:/movie-rating-analyses-hadoop-project/combiner.py > comout.txt 
sort comout.txt | ./C:/movie-rating-analyses-hadoop-project/reducer.py > results.txt
