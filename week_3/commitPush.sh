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
        echo "Succesfull commit"
    else
        echo "Error: commit failed"
    fi
    git push origin master
