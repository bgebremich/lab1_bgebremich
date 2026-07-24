#!/bin/bash
# organizer.sh
# Archives the current grades.csv with a timestamp,
# creates a fresh grades.csv, and logs actions to organizer.log.

LOG_FILE="organizer.log"
CSV_FILE="grades.csv"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="grades_backup_${TIMESTAMP}.csv"

echo "=============================================="
echo "         Grade Organizer Script"
echo "=============================================="

# 1. Archive existing grades.csv
if [ -f "$CSV_FILE" ]; then
    cp "$CSV_FILE" "$ARCHIVE_NAME"
    echo "Archived '$CSV_FILE' as '$ARCHIVE_NAME'"
    echo "[$TIMESTAMP] Archived '$CSV_FILE' as '$ARCHIVE_NAME'" >> "$LOG_FILE"
else
    echo "No existing '$CSV_FILE' found to archive."
    echo "[$TIMESTAMP] No existing '$CSV_FILE' found to archive." >> "$LOG_FILE"
fi

# 2. Create a fresh grades.csv
cat > "$CSV_FILE" << 'EOF'
assignment,group,score,weight
Quiz,Formative,0,20
Group Exercise,Formative,0,20
Functions and Debugging Lab,Formative,0,20
Midterm Project - Simple Calculator,Summative,0,20
Final Project - Text-Based Game,Summative,0,20
EOF

echo "Created fresh '$CSV_FILE' with default structure."
echo "[$TIMESTAMP] Created fresh '$CSV_FILE' with default structure." >> "$LOG_FILE"

# 3. Run the grade evaluator
echo ""
echo "Running grade-evaluator.py..."
echo "[$TIMESTAMP] Running grade-evaluator.py" >> "$LOG_FILE"

python grade-evaluator.py
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "[$TIMESTAMP] grade-evaluator.py completed successfully." >> "$LOG_FILE"
else
    echo "[$TIMESTAMP] grade-evaluator.py exited with code $EXIT_CODE." >> "$LOG_FILE"
fi

echo ""
echo "All done. Check '$LOG_FILE' for the full log."
echo "=============================================="
