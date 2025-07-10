#!/bin/bash
# Initialize Git repository for MegaParse Optimized

# Make script executable
chmod +x init_git.sh

# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: MegaParse Optimized structure"

# Instructions for remote repository
echo ""
echo "Git repository initialized with initial commit."
echo ""
echo "To connect to a remote repository, run:"
echo "  git remote add origin https://github.com/yourusername/megaparse-optimized.git"
echo "  git push -u origin main"
echo ""
echo "Remember to update the remote URL with your actual GitHub repository."
