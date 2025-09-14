#!/usr/bin/env python3

import re

# Read the original file
with open('Main_Revised.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all color-related commands
# Pattern to match {\color{blue} ... } and replace with just the content
pattern = r'\{\\color\{blue\}\s*([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}'

def remove_color_commands(text):
    """Remove all {\color{blue} ... } keeping only the content inside"""
    while True:
        # Keep replacing until no more matches
        new_text = re.sub(r'\{\\color\{blue\}([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', r'\1', text, count=1)
        if new_text == text:
            break
        text = new_text
    return text

# Apply the removal
content = remove_color_commands(content)

# Also handle simpler pattern
content = re.sub(r'\{\\color\{blue\}\s*', '', content)

# Write the cleaned content  
with open('Main_Revised_Clean.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("File cleaned and saved as Main_Revised_Clean.tex")
print("All color commands have been removed.")
print("\nTo compile: pdflatex Main_Revised_Clean.tex")