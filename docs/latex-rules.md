# LaTeX Rules

## Critical LaTeX Guidelines (MUST FOLLOW)

### LESSON LEARNED: Multi-line Set Definitions in Align Environment
**CORRECT FORMAT (MUST USE THIS):**
```latex
\begin{align}
\bar{\cal M}:=& \left\{z \in \mathbb P\,\middle|\,\lambda\geq 0, v_i\geq 0, \forall i, \right. \nonumber\\
&{\cal L}(x^\star,\lambda,u,v^\star)-{\cal L}(x^\star,\lambda^\star,u^\star,v^\star)=0, \nonumber\\
&\left. {\cal L}(x^\star,\lambda^\star,u^\star,v^\star)-{\cal L}(x,\lambda^\star,u^\star,v)=0 \right\}\;.\label{sad}
\end{align}
```
**KEY POINTS:**
- Use `\left\{` with `\right.` to balance delimiters across lines
- Use `\middle|` for the vertical bar in set notation
- Use `\left.` with `\right\}` to close the set
- Alignment `&` goes AFTER `:=` on first line, at START of continuation lines
- NEVER use `\Big\{`, `\bigg\{`, or plain `\{...\}` with alignment tabs - causes "Argument of \math@egroup has an extra }" errors

### LESSON LEARNED: LaTeX Math Notation Consistency
- **CRITICAL**: Check document's existing convention - some papers use `{\cal X}` (older style) instead of `\mathcal{X}` (modern style)
- **Subscript notation**: ALWAYS use `i\in[N]` NOT `i_{[N]}`; Use `i\in[N]^+` NOT `i^+_{[N]}`
- These incorrect notations cause compilation errors!

### LESSON LEARNED: Multi-line \rev{} Commands
**WRONG (causes paragraph/math mode errors):**
```latex
\rev{
\begin{enumerate}
\item First item
\item Second item
\end{enumerate}
}
```
**CORRECT:**
```latex
\begin{enumerate}
\item \rev{First item}
\item \rev{Second item}
\end{enumerate}
```
- NEVER wrap enumerate/itemize environments inside `\rev{}`
- Apply `\rev{}` to individual items instead

### LESSON LEARNED: Common LaTeX Error Patterns
1. **"Argument of \math@egroup has an extra }"**
   - Root cause: Trying to use alignment `&` inside set notation `\{...\}`
   - Solution: Use proper `\left\{`, `\middle|`, `\right.` format

2. **"Missing \cr inserted"**
   - Root cause: Incompatible alignment in math environments
   - Solution: Don't mix set notation with align environment tabs

3. **"Paragraph ended before \@textcolor was complete"**
   - Root cause: Multi-line `\rev{}` commands with environments inside
   - Solution: Apply `\rev{}` to content, not structural elements

## Critical LaTeX Guidelines — Revision Formatting

1. **Revnotes (Red Text)**:
   - Must ONLY describe the immediate blue text that follows
   - Format: "Reviewer X said [issue]. Changes: [specific change to following text]"
   - Do NOT describe changes elsewhere in the document

2. **Table Width in Two-Column Format**:
   - Tables must fit within column width (~7.5cm total)
   - Use `\small` and reduce column widths when needed
   - Typical safe widths: `p{2.3cm}` or less per column
   - Remove verbose captions to save space

3. **Abstract Content**:
   - Must match actual paper content - do NOT add examples that don't exist
   - Current valid examples: QP with ellipsoids, nonlinear optimization without RC, distributed sensor placement
   - NO portfolio optimization (this was incorrectly added and removed)

4. **Performance Claims**:
   - Avoid unsubstantiated speedup claims (e.g., "100-200x")
   - Use "significant computational efficiency improvements" instead
   - Only include metrics that can be technically proven

## PDF Building Lessons (IMPORTANT)

### Critical Requirements
1. **Bibliography file MUST be in working directory**: Copy `2.References.bib` from archive if missing
2. **Run full compilation sequence**: First pass -> bibtex -> second pass -> third pass
3. **Remove problematic citations**: Delete any 2024 preprint citations (maxminmax2024, drago2024, etc.)

### Common Issues and Solutions
- **All citations showing as [?]**: Missing .bib file - copy from archive/
- **Undefined references persist**: Run `bibtex` between first and second pdflatex passes
- **Corrupted references**: Clean build with `rm -f *.aux *.bbl *.blg` then recompile

## Debugging Commands
```bash
# Check if bibliography exists
ls *.bib

# Verify citation exists in bibliography
grep "citationkey" *.bib

# Run bibtex manually to see errors
bibtex Main_Cleaned_Revised

# Clean build when references are corrupted
rm -f *.aux *.bbl *.blg
./create_pdf.sh Main_Cleaned_Revised.tex
```
