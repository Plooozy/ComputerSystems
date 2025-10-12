#!/usr/bin/env bash

# Getting status
output=$(git status --porcelain)
# Checking for changes
if [ "$output" = "" ]; then
    echo "No changes"
else
    echo "There are changes"
    git add .
    git commit -m "Auto-commit on $(date)"
    output=$(git status --porcelain)
    if [ "$output" = "" ]; then
        echo "Successful commit"
    else
        echo "Error: commit failed"
    fi
    # Runs git push and checks if it succeeded
    if git push origin master; then # If push command exits with status 0 - means success, code runs "then"
        echo "Successful push"
    else                            # If push command exits with non-zero status - means failure, code runs "else"
        echo "Error: push failed"
    fi
fi
