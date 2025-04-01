// delete log file older than 7 days
#!/bin/bash

# Set the main folder path
MAIN_FOLDER_PATH="/path/to/your/main/folder"

# Set the number of days
DAYS=7

# Check if the main folder exists
if [ ! -d "$MAIN_FOLDER_PATH" ]; then
  echo "Error: Main folder '$MAIN_FOLDER_PATH' does not exist."
  exit 1
fi

# Delete files older than 7 days in all subfolders
find "$MAIN_FOLDER_PATH" -type f -mtime +$DAYS -delete