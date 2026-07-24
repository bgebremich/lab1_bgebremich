#!/bin/bash

# 1. Create archive directory if it doesn't exist
mkdir -p archive

# 2. Move existing grades.csv to archive/ with a timestamp (if present)
if [ -f "grades.csv" ]; then
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    mv grades.csv "archive/grades_backup_${TIMESTAMP}.csv"
    echo "Backed up existing grades.csv to archive/"
fi

# 3. Create a fresh, empty grades.csv with standard headers
echo "assignment,score,weight,group" > grades.csv
echo "Fresh grades.csv created."

# 4. Log execution
echo "$(date): Organizer script executed successfully." >> organizer.log
