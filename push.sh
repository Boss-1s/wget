#!/bin/bash

git pull origin main

# Capture the output of git status --porcelain
GIT_STATUS_OUTPUT=$(git status --porcelain)

# Check if the output is empty
if [ -z "$GIT_STATUS_OUTPUT" ]; then
  echo "Git working tree is clean (no uncommitted changes)."
  exit 0
else
  echo "Git working tree has uncommitted changes:"
  echo "$GIT_STATUS_OUTPUT"
  echo "These changes will be pushed to the main branch."
fi

git add .

# Find staged files larger than 100MB (102400 KB)
large_files=$(find . -type f -size +100M -not -path '*/.*')

if [ -n "$large_files" ]; then
    echo "Found files exceeding 100MB. Moving to Git LFS..."
    echo "$large_files" | xargs git lfs track
    git add .gitattributes
    # Re-stage files to ensure they are tracked as LFS pointers
    echo "$large_files" | xargs git add
    echo "Files are now tracked by LFS. You can proceed with your commit."
else
    echo "No files exceed 100MB."
fi

git commit -m "[WORKFLOW] Push Changes"
git push origin main
