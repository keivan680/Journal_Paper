#!/bin/bash

# PDF Creation Script with EPS to PDF Conversion
# Usage: ./create_pdf.sh <tex_file>
#        ./create_pdf.sh all  (to process all .tex files)

# Function to process a single tex file
process_tex_file() {
    local TEX_FILE="$1"
    local BASE_NAME="${TEX_FILE%.tex}"
    
    echo "========================================="
    echo "Starting PDF creation for: $TEX_FILE"
    echo "========================================="
    
    # Step 1: Convert all EPS files to PDF if they don't exist
    echo ""
    echo "Step 1: Converting EPS files to PDF..."
    echo "-----------------------------------------"
    
    EPS_COUNT=0
    CONVERTED_COUNT=0
    
    for eps_file in *.eps; do
        if [ -f "$eps_file" ]; then
            ((EPS_COUNT++))
            pdf_file="${eps_file%.eps}.pdf"
            
            # Check if PDF already exists and is newer than EPS
            if [ ! -f "$pdf_file" ] || [ "$eps_file" -nt "$pdf_file" ]; then
                echo "Converting: $eps_file -> $pdf_file"
                
                # Try to use epstopdf first
                if command -v epstopdf &> /dev/null; then
                    epstopdf "$eps_file"
                elif [ -f /Library/TeX/texbin/epstopdf ]; then
                    /Library/TeX/texbin/epstopdf "$eps_file"
                else
                    echo "Warning: epstopdf not found, skipping $eps_file"
                    continue
                fi
                
                ((CONVERTED_COUNT++))
            else
                echo "Skipping: $pdf_file (already up to date)"
            fi
            
            # Create the -eps-converted-to.pdf version for compatibility
            eps_converted_name="${eps_file%.eps}-eps-converted-to.pdf"
            if [ -f "$pdf_file" ] && [ ! -f "$eps_converted_name" ]; then
                cp "$pdf_file" "$eps_converted_name"
            fi
        fi
    done
    
    if [ $EPS_COUNT -eq 0 ]; then
        echo "No EPS files found to convert."
    else
        echo "Processed $EPS_COUNT EPS files, converted $CONVERTED_COUNT"
    fi
    
    # Step 2: Run LaTeX compilation sequence
    echo ""
    echo "Step 2: Running LaTeX compilation..."
    echo "-----------------------------------------"
    
    # Determine the pdflatex command
    if [ -f /Library/TeX/texbin/pdflatex ]; then
        PDFLATEX="/Library/TeX/texbin/pdflatex"
    elif command -v pdflatex &> /dev/null; then
        PDFLATEX="pdflatex"
    else
        echo "Error: pdflatex not found!"
        return 1
    fi
    
    # Determine the bibtex command
    if [ -f /Library/TeX/texbin/bibtex ]; then
        BIBTEX="/Library/TeX/texbin/bibtex"
    elif command -v bibtex &> /dev/null; then
        BIBTEX="bibtex"
    else
        echo "Warning: bibtex not found, skipping bibliography processing"
        BIBTEX=""
    fi
    
    # First pdflatex pass
    echo "Running first pdflatex pass..."
    "$PDFLATEX" -interaction=nonstopmode "$TEX_FILE" > /tmp/pdflatex_output.txt 2>&1
    LATEX_EXIT_CODE=$?
    
    # Check if PDF was created despite warnings/errors
    if [ -f "$BASE_NAME.pdf" ]; then
        echo "First pass completed (PDF created, though there may be warnings)"
    elif [ $LATEX_EXIT_CODE -ne 0 ]; then
        echo "Error during first pdflatex pass. Showing output:"
        cat /tmp/pdflatex_output.txt
        return 1
    fi
    
    # Run bibtex if available and .aux file exists
    if [ -n "$BIBTEX" ] && [ -f "$BASE_NAME.aux" ]; then
        echo "Running bibtex..."
        "$BIBTEX" "$BASE_NAME" > /tmp/bibtex_output.txt 2>&1
        BIBTEX_EXIT_CODE=$?
        
        # Check if bibtex succeeded or if there are just warnings
        if [ $BIBTEX_EXIT_CODE -ne 0 ]; then
            # Check if the error is just about missing citations
            if grep -q "I found no" /tmp/bibtex_output.txt; then
                echo "Note: Some citations may be undefined. Checking for .bbl file..."
                if [ ! -f "$BASE_NAME.bbl" ]; then
                    echo "Warning: No .bbl file created. Bibliography may be missing."
                fi
            else
                echo "Warning: bibtex encountered issues:"
                head -10 /tmp/bibtex_output.txt
            fi
        else
            echo "Bibtex completed successfully"
        fi
    fi
    
    # Second pdflatex pass
    echo "Running second pdflatex pass..."
    "$PDFLATEX" -interaction=nonstopmode "$TEX_FILE" > /tmp/pdflatex_output.txt 2>&1
    LATEX_EXIT_CODE=$?
    
    # Check if PDF still exists after second pass
    if [ -f "$BASE_NAME.pdf" ]; then
        echo "Second pass completed (PDF updated)"
    elif [ $LATEX_EXIT_CODE -ne 0 ]; then
        echo "Error during second pdflatex pass. Showing output:"
        cat /tmp/pdflatex_output.txt
        return 1
    fi
    
    # Third pdflatex pass (to resolve all references)
    echo "Running third pdflatex pass..."
    "$PDFLATEX" -interaction=nonstopmode "$TEX_FILE" > /tmp/pdflatex_output.txt 2>&1
    LATEX_EXIT_CODE=$?
    
    # Check if PDF still exists after third pass
    if [ -f "$BASE_NAME.pdf" ]; then
        echo "Third pass completed (all references resolved)"
    elif [ $LATEX_EXIT_CODE -ne 0 ]; then
        echo "Error during third pdflatex pass. Showing output:"
        cat /tmp/pdflatex_output.txt
        return 1
    fi
    
    # Step 3: Check results
    echo ""
    echo "========================================="
    if [ -f "$BASE_NAME.pdf" ]; then
        # Get file size in human-readable format
        if command -v stat &> /dev/null; then
            FILE_SIZE=$(stat -f%z "$BASE_NAME.pdf" 2>/dev/null || stat -c%s "$BASE_NAME.pdf" 2>/dev/null)
            FILE_SIZE_MB=$(echo "scale=2; $FILE_SIZE / 1048576" | bc 2>/dev/null || echo "unknown")
            echo "SUCCESS: $BASE_NAME.pdf created (${FILE_SIZE_MB} MB)"
        else
            echo "SUCCESS: $BASE_NAME.pdf created"
        fi
        
        # Count pages if pdfinfo is available
        if command -v pdfinfo &> /dev/null; then
            PAGE_COUNT=$(pdfinfo "$BASE_NAME.pdf" 2>/dev/null | grep "Pages:" | awk '{print $2}')
            if [ -n "$PAGE_COUNT" ]; then
                echo "PDF contains $PAGE_COUNT pages"
            fi
        fi
    else
        echo "ERROR: PDF creation failed!"
        return 1
    fi
    
    echo "========================================="
    echo ""
    
    # Clean up auxiliary files (keeping only the PDF)
    echo "Cleaning up auxiliary files..."
    rm -f "$BASE_NAME.aux" "$BASE_NAME.log" "$BASE_NAME.out" "$BASE_NAME.toc" \
          "$BASE_NAME.lof" "$BASE_NAME.lot" "$BASE_NAME.bbl" "$BASE_NAME.blg" \
          "$BASE_NAME.nav" "$BASE_NAME.snm" "$BASE_NAME.vrb" \
          *-eps-converted-to.pdf
    echo "Cleanup complete."
    
    return 0
}

# Main script logic
if [ $# -eq 0 ]; then
    echo "Usage: $0 <tex_file>"
    echo "       $0 all  (to process all .tex files)"
    echo "Example: $0 Main.tex"
    exit 1
fi

if [ "$1" = "all" ]; then
    # Process all .tex files
    echo "Processing all .tex files in the current directory..."
    echo ""
    
    # Count tex files
    TEX_FILES=(*.tex)
    if [ ! -f "${TEX_FILES[0]}" ]; then
        echo "No .tex files found in the current directory!"
        exit 1
    fi
    
    TOTAL_FILES=${#TEX_FILES[@]}
    PROCESSED=0
    FAILED=0
    FAILED_FILES=()
    
    echo "Found $TOTAL_FILES .tex file(s) to process"
    echo ""
    
    # Process each tex file
    for tex_file in "${TEX_FILES[@]}"; do
        if [ -f "$tex_file" ]; then
            echo "[$((PROCESSED + 1))/$TOTAL_FILES] Processing: $tex_file"
            echo ""
            
            if process_tex_file "$tex_file"; then
                ((PROCESSED++))
                echo "✓ Successfully processed: $tex_file"
            else
                ((FAILED++))
                FAILED_FILES+=("$tex_file")
                echo "✗ Failed to process: $tex_file"
            fi
            
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""
        fi
    done
    
    # Summary
    echo "========================================="
    echo "BATCH PROCESSING COMPLETE"
    echo "========================================="
    echo "Successfully processed: $PROCESSED file(s)"
    if [ $FAILED -gt 0 ]; then
        echo "Failed: $FAILED file(s)"
        echo "Failed files:"
        for failed_file in "${FAILED_FILES[@]}"; do
            echo "  - $failed_file"
        done
    fi
    echo "========================================="
    
else
    # Process single file
    TEX_FILE="$1"
    
    # Check if the tex file exists
    if [ ! -f "$TEX_FILE" ]; then
        echo "Error: File '$TEX_FILE' not found!"
        exit 1
    fi
    
    if process_tex_file "$TEX_FILE"; then
        echo "Done!"
    else
        exit 1
    fi
fi