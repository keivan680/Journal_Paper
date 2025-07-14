# TASKS.md - Reviewer Comments Implementation Plan

## Overview
This document organizes all reviewer comments by individual reviewer, with each milestone dedicated to addressing one reviewer's feedback. Each milestone includes tasks derived from the reviewer's main comments (txt files) and detailed annotations (md/pdf/png files).

---

## Milestone 1: Reviewer 4 Comments
*Source: Review359593(Reviewer4).txt*

### 1.1 Clarify Paper Contributions
- [ ] Create a clear section explicitly stating improvements over existing results
- [ ] Add comparison table with existing methods
- [ ] Highlight what is novel in the proposed approach
- [ ] Make evaluation criteria more explicit

### 1.2 Language and Grammar Improvements
- [ ] Conduct comprehensive grammar review throughout the paper
- [ ] Fix all language issues identified
- [ ] Improve clarity of technical descriptions
- [ ] Ensure consistent terminology usage

### 1.3 Formatting Issues
- [ ] Remove definite articles from all figure captions
- [ ] Remove definite articles from section titles
- [ ] Fix non-standard italics in formulas
- [ ] Ensure consistency in mathematical notation formatting
- [ ] Replace all incorrect quotation marks throughout the manuscript

---

## Milestone 2: Reviewer 5 Comments
*Sources: Review359595(Reviewer5).txt, AttachmentToReview359595.md/pdf/png*

### 2.1 Structural and Organizational Issues
- [ ] Reorganize introduction to clearly articulate contributions
- [ ] Shorten introduction while maintaining key information
- [ ] Fix equation referencing order (equations 5 and 6 referenced before introduction)
- [ ] Move Appendix B conclusions to main text (Section V-D)
- [ ] Ensure logical flow throughout the paper

### 2.2 Algorithm and Technical Presentation
- [ ] Add detailed explanation and context for Algorithm (23)
- [ ] Provide step-by-step discussion after Algorithm (23)
- [ ] Include detailed theoretical analysis of convergence performance
- [ ] Add Z parameter introduction right after equation (23)

### 2.3 Specific Technical Issues
- [ ] Remove duplicate "RC" abbreviation explanation (before equation 9)
- [ ] Add explanation for "RHS" abbreviation after inequality (51)
- [ ] Clarify superscript "ε+" in equation (43)
- [ ] Fix expression error: change "lim_{k→∞}=y" to "lim_{k→∞} y_k=y" in Proposition 6
- [ ] Clarify meaning of h_{ij} and K_i in equation (3)
- [ ] Add missing proof of Lemma 4 (from Ref. [41])
- [ ] Fix reversed quotation marks (page 5, first column, last paragraph)

### 2.4 Assumptions and Analysis
- [ ] Provide justification for Assumption 1 and discuss possible extensions
- [ ] Address restrictiveness of Assumption 2 - can it be relaxed?
- [ ] Explain why Lagrangian function (15) analysis is necessary
- [ ] Provide clearer justification for Proposition 6

### 2.5 Numerical Evaluation
- [ ] Replace outdated results from Ref. [22] with state-of-the-art algorithms
- [ ] Include more comprehensive evaluation with modern benchmarks
- [ ] Justify why proposed algorithm is more effective despite showing larger values

---

## Milestone 3: Reviewer 6 Comments
*Sources: Review359597(Reviewer6).txt, AttachmentToReview359597.md/pdf/png*

### 3.1 Problem Formulation Clarification
- [ ] Clarify motivation for problem formulation (4) vs. (3)
- [ ] Provide detailed comparison between new formulation (3) and classical (2)
- [ ] Explain the specific role of c_i terms
- [ ] Address suggestion of using γ_i := c_i + λ_i instead
- [ ] Discuss non-smoothness introduced by taking maximum in formulation (2)

### 3.2 Technical Clarifications
- [ ] Clarify whether Lemma 1 is well-known or novel (appears to be standard saddle point property)
- [ ] Address whether Definition 1 KKT conditions differ from standard KKT
- [ ] Explain if set U_i remains compact under convex assumptions
- [ ] Add discussion on what happens when constraints are nonlinear in u_i

### 3.3 Assumption 3 Issues
- [ ] Address how Assumption 3 (c_i > 0) prevents recovery of formulation (2)
- [ ] Discuss implications of this restriction
- [ ] Consider relaxing or modifying this assumption

### 3.4 Numerical Examples
- [ ] Expand examples beyond linear constraints in u_i
- [ ] Add examples with nonlinear constraints
- [ ] Include more diverse test cases

---

## Milestone 4: Reviewer 10 Comments
*Sources: Review359605(Reviewer10).txt, AttachmentToReview359605.md/pdf/png*

### 4.1 Publication Format Decision
- [ ] Evaluate resubmission as technical note vs. full article
- [ ] If keeping as article, add substantial technical depth
- [ ] If converting to technical note, condense content appropriately

### 4.2 Writing Style and Clarity
- [ ] Shorten abstract to appropriate length
- [ ] Break up long sentences throughout the paper
- [ ] Replace "the paper" with "this paper" consistently
- [ ] Improve overall writing clarity and conciseness

### 4.3 Specific Technical Issues
- [ ] Add continuity assumption to Footnote 2
- [ ] Fix notation inconsistency: u_i should be u_1 in relevant examples
- [ ] Add missing parentheses in equation (36) in Lemma 3 proof
- [ ] Clarify novelty of Lemma 1 (seems like standard saddle point property)
- [ ] Make Remark 4 formulation clearer
- [ ] Make conclusion in Theorem 4 proof more self-evident

### 4.4 Assumption and Method Limitations
- [ ] Address why Assumption 3 (C > 0) is too rigid for practical modeling
- [ ] Add discussion on empirical strategies for selecting C parameters
- [ ] Consider adding proximal/regularization terms (Corollary 1 requirement too strong)

### 4.5 Missing Technical Content
- [ ] Add actual robust optimization examples with scenario-based uncertain constraints
- [ ] Include convergence analysis results
- [ ] Add stability analysis of the proposed approach
- [ ] Provide more comprehensive technical depth throughout

---

## Milestone 5: Common Themes and Integration

### 5.1 Cross-Reviewer Issues
- [ ] Ensure all formatting issues are consistently addressed
- [ ] Verify that technical clarifications satisfy all reviewers
- [ ] Create unified response showing how contributions are clarified
- [ ] Ensure examples address concerns from multiple reviewers

### 5.2 Final Review and Response
- [ ] Create detailed response letter for each reviewer
- [ ] Document how each specific comment was addressed
- [ ] Ensure all changes are tracked in the manuscript
- [ ] Conduct final proofreading for consistency

---

## Priority Implementation Order

### Phase 1: Immediate Fixes (Address basic issues across all reviewers)
1. **Formatting**: Fix articles, italics, quotation marks (from Reviewers 4, 5)
2. **Notation**: Fix mathematical errors and inconsistencies (from Reviewers 5, 10)
3. **Language**: Fix grammar and clarity issues (from Reviewers 4, 10)

### Phase 2: Technical Clarifications (Address understanding issues)
1. **Contributions**: Clarify what's new (Reviewers 4, 5, 6, 10)
2. **Formulations**: Explain problem formulations clearly (Reviewer 6)
3. **Assumptions**: Justify and possibly relax assumptions (Reviewers 5, 6, 10)

### Phase 3: Content Enhancement (Add missing content)
1. **Algorithm**: Add detailed Algorithm (23) discussion (Reviewer 5)
2. **Analysis**: Add convergence and stability analysis (Reviewers 5, 10)
3. **Examples**: Expand with practical examples (Reviewers 6, 10)

### Phase 4: Structural Changes (Reorganize content)
1. **Introduction**: Reorganize and shorten (Reviewers 5, 10)
2. **Appendix**: Move content to main text (Reviewer 5)
3. **Format**: Decide on article vs. technical note (Reviewer 10)

---

## Response Strategy
- Address each reviewer's comments systematically
- Create a point-by-point response document
- Show specific changes made for each comment
- Highlight major improvements in cover letter