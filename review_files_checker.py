#!/usr/bin/env python3
"""
Script to review and verify all review files in the Reviews folder
"""
import os
import PyPDF2
from PIL import Image

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def analyze_png_files(png_path):
    """Analyze PNG files to extract any text"""
    try:
        # For now, just get image info since OCR is not installed
        img = Image.open(png_path)
        return f"Image size: {img.size}, Mode: {img.mode}"
    except Exception as e:
        return f"Error reading PNG: {str(e)}"

def read_file_content(file_path):
    """Read content of text/markdown files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def main():
    reviews_dir = "/mnt/c/Users/tensu/OneDrive/Desktop/Journal_Paper/Reviews"
    
    # Get all files
    files = os.listdir(reviews_dir)
    
    print("=== REVIEW FILES ANALYSIS ===\n")
    
    # Group files by review number
    reviews = {
        '359593': {'type': 'Reviewer4'},
        '359595': {'type': 'Reviewer5'},
        '359597': {'type': 'Reviewer6'},
        '359605': {'type': 'Reviewer10'}
    }
    
    # Categorize files
    for file in sorted(files):
        for review_num in reviews:
            if review_num in file:
                if file.endswith('.pdf'):
                    reviews[review_num]['pdf'] = file
                elif file.endswith('.png'):
                    if 'pngs' not in reviews[review_num]:
                        reviews[review_num]['pngs'] = []
                    reviews[review_num]['pngs'].append(file)
                elif file.endswith('.md'):
                    if 'mds' not in reviews[review_num]:
                        reviews[review_num]['mds'] = []
                    reviews[review_num]['mds'].append(file)
                elif file.endswith('.txt'):
                    reviews[review_num]['txt'] = file
                break
    
    # Analyze each review
    for review_num, data in reviews.items():
        print(f"\n{'='*50}")
        print(f"REVIEW {review_num} ({data['type']})")
        print(f"{'='*50}")
        
        # Text review file
        if 'txt' in data:
            print(f"\nText Review File: {data['txt']}")
            content = read_file_content(os.path.join(reviews_dir, data['txt']))
            print(f"First 200 chars: {content[:200]}...")
        
        # PDF attachment
        if 'pdf' in data:
            print(f"\nPDF Attachment: {data['pdf']}")
            pdf_text = extract_pdf_text(os.path.join(reviews_dir, data['pdf']))
            print(f"PDF text preview (first 200 chars): {pdf_text[:200]}...")
        
        # PNG files
        if 'pngs' in data:
            print(f"\nPNG Screenshots: {len(data['pngs'])} files")
            for png in sorted(data['pngs']):
                info = analyze_png_files(os.path.join(reviews_dir, png))
                print(f"  - {png}: {info}")
        
        # Markdown files
        if 'mds' in data:
            print(f"\nMarkdown Files: {data['mds']}")
            for md in data['mds']:
                content = read_file_content(os.path.join(reviews_dir, md))
                print(f"\n  {md} preview (first 200 chars):")
                print(f"  {content[:200]}...")
    
    # Check for duplicate/extra markdown files
    print(f"\n\n{'='*50}")
    print("ISSUES TO FIX:")
    print(f"{'='*50}")
    
    # Find 'Of25' files that need merging
    of25_files = [f for f in files if 'Of25' in f and f.endswith('.md')]
    if of25_files:
        print(f"\nFiles with 'Of25' that need merging:")
        for f in of25_files:
            target = f.replace('Of25', '')
            print(f"  - {f} -> {target}")

if __name__ == "__main__":
    main()