#!/bin/bash

base_directory = ".."

for((i = 1; i <= 25; i++)); do
    folder_name="$base_directory/$i"
    #Check if the folder already exists

    if [ ! -d "$folder_name" ]; then
       #Create the folder
       mkdir -p "$folder_name"
       echo "Created folder $folder_name"
    else
        echo "Folder $folder_name already exists"
    fi
done
