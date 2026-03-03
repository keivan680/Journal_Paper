# Revision Guide

## Reviewer Comments to Address
The paper has received feedback from 4 reviewers with key concerns:
1. Unclear improvements over existing results
2. Language and grammar issues throughout
3. Formatting problems (article usage in captions/titles, formula italics, quotation marks)
4. Suggestion to submit as technical note rather than full article (Reviewer 10)
5. Need for deeper technical content and better presentation

## Development Workflow
1. Read reviewer comments in Reviews/ folder before making changes
2. Address formatting issues first (articles, italics, quotation marks)
3. Focus on clarifying technical contributions and improvements over existing work
4. Update figures as needed to better illustrate concepts
5. Check grammar and language throughout the manuscript

## Current Manuscript Status
- **Main_Cleaned_Revised.tex**: Primary revised manuscript (17 pages)
- **Report.tex**: 3-page revision summary for internal use
- **Response.tex**: 3-page point-by-point reviewer responses
- **Diffs.tex/pdf**: DELETED - key content integrated into revnotes

## Revision Tracking
- Blue text (`\rev{}`) marks all revisions
- Red text (`\revnote{}`) explains reviewer comments being addressed
- ~40% of manuscript has been revised (marked in blue)
- All 42 reviewer comments have been addressed

## Figure Files
The repository contains multiple trajectory and visualization figures in EPS/PDF/PNG formats. When updating figures, maintain consistent naming conventions:
- trajectories_*.eps for trajectory plots
- Use descriptive suffixes (e.g., _geometric, _intersection, _nonlinear_exp_no_RC)

## Important Notes
- The paper uses custom theorem environments extensively (theorem, lemma, corollary, etc.)
- Mathematical notation is defined in the preamble with custom commands
- Git status shows several modified trajectory figures - ensure consistency when updating
- Reviews folder is currently untracked - consider adding to git after addressing comments
- Whenever you want to compile a tex file, use ./create_pdf.sh
