# Update the paths for mapper, combiner, reducer scripts, and years.txt
hadoop jar /home/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-D mapred.reduce.tasks=5 \
-files C:/movie-rating-analyses-hadoop-project/mapper.py,C:/movie-rating-analyses-hadoop-project/combiner.py,C:/movie-rating-analyses-hadoop-project/reducer.py,C:/movie-rating-analyses-hadoop-project/years.txt \
-mapper C:/movie-rating-analyses-hadoop-project/mapper.py \
-combiner C:/movie-rating-analyses-hadoop-project/combiner.py \
-reducer C:/movie-rating-analyses-hadoop-project/reducer.py \
-input C:/movie-rating-analyses-hadoop-project/ratings.txt \
-output /user/xyz123/assignment/results
