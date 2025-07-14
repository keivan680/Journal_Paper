# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview
This is a journal paper submission titled "Robust Optimization via Continuous-Time Dynamics" that uses IEEE journal format. The paper proposes a dynamical system-based approach for solving robust optimization problems and is currently under review.

## Build Commands
To compile the LaTeX document:
```bash
pdflatex Main.tex
bibtex Main
pdflatex Main.tex
pdflatex Main.tex
```

## Key Files and Structure
- **Main.tex**: Primary manuscript file using IEEE journal format (ieeecolor.cls)
- **2.References.bib**: Bibliography with robust optimization literature
- **generic.sty**: Custom style definitions
- **Reviews/**: Contains reviewer comments and attachments that need to be addressed
- **LLM.txt**: Research notes on robust optimization concepts and methods

## Reviewer Comments to Address
The paper has received feedback from 4 reviewers with key concerns:
1. Unclear improvements over existing results
2. Language and grammar issues throughout
3. Formatting problems (article usage in captions/titles, formula italics, quotation marks)
4. Suggestion to submit as technical note rather than full article (Reviewer 10)
5. Need for deeper technical content and better presentation

## Figure Files
The repository contains multiple trajectory and visualization figures in EPS/PDF/PNG formats. When updating figures, maintain consistent naming conventions:
- trajectories_*.eps for trajectory plots
- Use descriptive suffixes (e.g., _geometric, _intersection, _nonlinear_exp_no_RC)

## Development Workflow
1. Read reviewer comments in Reviews/ folder before making changes
2. Address formatting issues first (articles, italics, quotation marks)
3. Focus on clarifying technical contributions and improvements over existing work
4. Update figures as needed to better illustrate concepts
5. Check grammar and language throughout the manuscript

## Important Notes
- The paper uses custom theorem environments extensively (theorem, lemma, corollary, etc.)
- Mathematical notation is defined in the preamble with custom commands
- Git status shows several modified trajectory figures - ensure consistency when updating
- Reviews folder is currently untracked - consider adding to git after addressing comments