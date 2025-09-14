#!/usr/bin/env python3

import os
import re

# List of tex files to process
tex_files = [
    'Main.tex',
    'Main_Revised.tex', 
    'Main_Revised_Fixed.tex',
    'Main_Revised_Clean.tex',
    'Main_Backup.tex',
    'Main_Revised_backup.tex'
]

for filename in tex_files:
    filepath = f'/Users/kebrahimi/Documents/Journal_Paper/{filename}'
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
        
    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find where the reviewers' comments section starts
    review_start = -1
    for i, line in enumerate(lines):
        if re.search(r'\\section\{[Rr]eviewer.*[Cc]omment', line):
            # Check if there's a \newpage or \onecolumn before it
            if i > 0 and ('\\newpage' in lines[i-1] or '\\onecolumn' in lines[i-1]):
                review_start = i - 1
            elif i > 1 and ('\\newpage' in lines[i-2] and '\\onecolumn' in lines[i-1]):
                review_start = i - 2
            else:
                review_start = i
            break
    
    if review_start == -1:
        print(f"No reviewers' comments section found in {filename}")
        continue
    
    # Find where \end{document} is
    doc_end = -1
    for i, line in enumerate(lines):
        if '\\end{document}' in line:
            doc_end = i
            break
    
    if doc_end == -1:
        print(f"Warning: No \\end{{document}} found in {filename}")
        continue
    
    # Remove everything from review_start to just before \end{document}
    new_lines = lines[:review_start] + ['\n'] + lines[doc_end:]
    
    # Create backup
    backup_name = filepath.replace('.tex', '_original.tex')
    if not os.path.exists(backup_name):
        with open(backup_name, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Created backup: {backup_name}")
    
    # Write the modified content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Removed reviewers' comments section from {filename}")
    print(f"  - Section started at line {review_start + 1}")
    print(f"  - Removed {doc_end - review_start} lines")

print("\nAll files processed successfully!")