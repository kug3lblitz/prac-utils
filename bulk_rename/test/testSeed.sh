# original version

# for i in {i...100}
# do
#   touch "file$i.txt"
# done
# for i in {1..1000}; do touch "file${i}.txt"; done

#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "No arguments provided. Please provide the number of files to create."
    exit 1
fi

# Create the files
for i in $(seq 1 $1); do
    touch "file${i}.txt"
done