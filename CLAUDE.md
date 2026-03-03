# CLAUDE.md — Journal Paper

Robust Optimization via Continuous-Time Dynamics — IEEE journal format, currently under review.

## Commands

```bash
./create_pdf.sh Main_Cleaned_Revised.tex   # Build PDF (preferred)
```

## Key Files

- **Main_Cleaned_Revised.tex** — Primary revised manuscript
- **2.References.bib** — Bibliography (MUST be in working directory for compilation)
- **Reviews/** — Reviewer comments and attachments

## Context-Based Rules

| When you're... | Read |
|----------------|------|
| Compiling LaTeX / fixing build errors | [docs/latex-rules.md](docs/latex-rules.md) |
| Addressing reviewer comments / revisions | [docs/revision-guide.md](docs/revision-guide.md) |

## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for concision.
- List unresolved questions at the end of each plan.

## Critical Reminders

- Always use `./create_pdf.sh` to compile — never run pdflatex manually
- Bibliography file MUST exist in working directory or all citations show as [?]
- Use `{\cal X}` not `\mathcal{X}` — match existing document convention
