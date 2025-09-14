#!/usr/bin/env python3

import re

# Read the original file
with open('Main_Revised.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the color package with xcolor
content = content.replace('\\usepackage{color}', '\\usepackage{xcolor}')

# Add color definition and revision command after the package declarations
# Find the position after all usepackage commands
packages_end = content.rfind('\\usetikzlibrary{shapes,arrows}')
if packages_end != -1:
    insert_pos = content.find('\n', packages_end) + 1
    color_definitions = """
% Define revision color for IEEE class compatibility
\\definecolor{revisionblue}{rgb}{0,0,0.8}
% Command for marking revisions
\\newcommand{\\rev}[1]{\\textcolor{revisionblue}{#1}}
"""
    content = content[:insert_pos] + color_definitions + content[insert_pos:]

# Replace all instances of {\color{blue} ... } with \rev{ ... }
# This needs careful handling due to nested braces

# First, replace simple cases where {\color{blue} starts a color block
content = re.sub(r'\{\\color\{blue\}\s*', r'\\rev{', content)

# Also handle cases where there might be extra spaces
content = re.sub(r'\{\\color\s*\{blue\}\s*', r'\\rev{', content)

# Write the fixed content
with open('Main_Revised_Fixed.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("File fixed and saved as Main_Revised_Fixed.tex")
print("Key changes made:")
print("1. Replaced \\usepackage{color} with \\usepackage{xcolor}")
print("2. Added proper color definition for IEEE class")
print("3. Replaced all {\\color{blue} with \\rev{ command")
print("\nNow compile with: pdflatex Main_Revised_Fixed.tex")