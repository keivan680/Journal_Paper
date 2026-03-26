---
title: Apply AI Review Required Fixes to Manuscript
type: fix
status: active
date: 2026-03-24
deepened: 2026-03-24
---

# Apply AI Review Required Fixes to Manuscript

Apply the 5 required fixes identified in the AI review section to make the paper publishable.

## Enhancement Summary

**Deepened on:** 2026-03-24
**Research agents used:** saddle-point framing (web + literature), model-free terminology (web + RO literature)

### Key Research Findings
1. Saddle-point property (Lemma 1) is standard bilevel duality — novelty should shift to dynamics design
2. "Reformulation-free" is the best replacement for "model-free" — no conflicting precedent, immediately clear
3. Cherukuri et al. (2018 TAC) should be cited to explain precisely what fails for the RO Lagrangian
4. Ho-Nguyen & Kilinc-Karzan (2021) explicitly treat the same "not jointly concave" structure — paper should cite

---

## Fixes (in order of complexity, simplest first)

### Fix 1: Typos in Lemma 3 proof (lines 584, 586)

**File:** `1.Main_Cleaned_Revised.tex`
**No user decision needed.**

**Line 584 current:**
```latex
&+ \sum_{i=1}^N(c_i+\lambda_i)-(c+\lambda_i^\star))(f_i(x,u_i)-v_i^\top h_i(u_i))\nonumber\\
```

**Line 584 replacement:**
```latex
&+ \sum_{i=1}^N((c_i+\lambda_i)-(c_i+\lambda_i^\star))(f_i(x,u_i)-v_i^\top h_i(u_i))\nonumber\\
```
Changes: `c` → `c_i`, add opening paren before `(c_i+\lambda_i)`

**Line 586 current:**
```latex
&+ \sum_{i=1}^N (c+\lambda_i^\star) (f_i(x,u_i)-f_i(x,u_i^\star)+v_i^\top (h_i(u_i^\star)-h_i(u_i))\nonumber\\
```

**Line 586 replacement:**
```latex
&+ \sum_{i=1}^N (c_i+\lambda_i^\star) (f_i(x,u_i)-f_i(x,u_i^\star)+v_i^\top (h_i(u_i^\star)-h_i(u_i)))\nonumber\\
```
Changes: `c` → `c_i`, add closing paren after `h_i(u_i)`

**Verification:** Lines 591-597 (simplified expression) use `c_i` correctly. Line 587 uses `c_i` correctly. These are isolated typos.

---

### Fix 2: Remove unjustified O(n^2) complexity claim (line 930)

**File:** `1.Main_Cleaned_Revised.tex`, line 930
**No user decision needed.** (Recommendation is clear: delete.)

**Current sentence:**
```
The dynamics handle nonlinear uncertainty constraints through gradient terms $\nabla_{u_j} h_j(u_j)$, achieving exact convergence where reformulation methods fail. Scenario-based methods have complexity $O(N^3n^3)$ for $N$ scenarios, compared to $O(n^2)$ scaling for the dynamics.
```

**Replace with (delete the complexity claim, keep the first sentence):**
```
The dynamics handle nonlinear uncertainty constraints through gradient terms $\nabla_{u_j} h_j(u_j)$, achieving exact convergence where reformulation methods fail.
```

**Why delete entirely:** The $O(N^3n^3)$ claim for scenario methods is wrong (interior-point methods scale as $O(Nn^2)$ per iteration). The $O(n^2)$ claim has no derivation anywhere in the paper. The timing comparison (0.8s vs 31.2s) on the previous lines already demonstrates the advantage concretely.

---

### Fix 3: Reframe Lemma 1 (saddle point) novelty claim

**File:** `1.Main_Cleaned_Revised.tex`
**USER DECISION NEEDED** — this changes the paper's positioning.

#### Research Insight

The saddle-point property (Lemma 1) is **standard bilevel duality**:
- Lower-level strong duality (Slater) yields inner saddle property for each $(u_i, v_i)$ independently
- Upper-level Lagrangian saddle point follows from standard convexity
- The "composition" of two levels of strong duality is standard (Vicente-Calamai 1994, Dempe 2002)
- Ho-Nguyen & Kilinc-Karzan (2021, INFORMS J. Computing) explicitly treat the same "not jointly concave" RO Lagrangian and treat saddle-point existence as known

**What IS genuinely novel:** The dynamics design (non-Lagrangian vector field) and the Lyapunov function (optimal dual weights). Cherukuri et al. (2018 TAC) framework assumes convex-concave structure and does NOT apply to the RO Lagrangian — this is the real gap the paper fills.

#### Location A: Remark (lines 402-404)

**Current:**
```latex
\begin{remark}[\rev{Non-standard Saddle Point Property}]
Classical results such as Sion's minimax theorem \cite{sion1958} or Rockafellar's saddle point theorem \cite{rockafellar1970} require joint concavity in the maximization variables. The Lagrangian $\mathcal{L}(x,\lambda,u,v)$ is jointly convex in $(x,v)$ for fixed $(\lambda,u)$, but not jointly concave in $(\lambda,u)$ for fixed $(x,v)$ due to product terms $(c_i+\lambda_i) \cdot f_i(x,u_i)$ that create bilinear coupling. This violation of joint concavity renders existing primal-dual methods \cite{arrow1958,feijer2010} inapplicable and requires a proof that exploits the min-max-max-min structure of robust optimization.
\end{remark}
```

**Proposed replacement:**
```latex
\begin{remark}[\rev{Saddle Point via Bilevel Duality}]
\rev{The Lagrangian $\mathcal{L}(x,\lambda,u,v)$ is not jointly concave
in $(\lambda,u)$ due to the bilinear terms
$(c_i+\lambda_i)\cdot f_i(x,u_i)$, so classical minimax theorems
(Sion \cite{sion1958}, Rockafellar \cite{rockafellar1970}) that
require joint concavity do not apply directly.  Nevertheless, the
saddle property (Lemma~\ref{saddle.lem}) follows from the separable
bilevel structure of $\mathcal{RO}$: strong duality at each lower
level (Assumption~\ref{assume_feasible} via Slater's condition
\cite[Section~5.2.3]{boyd2004}) yields the inner saddle property for
each $(u_i, v_i)$ pair independently, and strong duality at the upper
level then provides the outer saddle property in
$(x,\lambda)$.  Lemma~\ref{saddle.lem} makes this compositional
argument explicit for the $\mathcal{RO}$ Lagrangian.  The key
consequence for dynamics design is that, despite the saddle property
holding, the lack of joint concavity prevents the direct application
of standard primal--dual gradient dynamics
\cite{arrow1958,feijer2010,cherukuri2016} to solve
$\mathcal{RO}$---motivating the non-Lagrangian dynamics proposed in
Section~\ref{section_pddynamics}.}
\end{remark}
```

**Key changes:**
- Title: "Non-standard Saddle Point Property" → "Saddle Point via Bilevel Duality" (less provocative)
- Acknowledges saddle property follows from standard bilevel duality
- Shifts novelty to dynamics design (where it belongs)
- Cites Cherukuri et al. to explain what framework fails
- Uses "makes this compositional argument explicit" instead of claiming novelty

#### Location B: Introduction (line 154)

**Current sentence within \rev{} block:**
```
We establish the saddle-point property of the equilibrium even in the absence of joint concavity in $(\lambda,u)$. The non-classical structure of the dynamics necessitates the construction of a novel Lyapunov function to analyze stability.
```

**Proposed replacement:**
```
While the saddle-point property of the equilibrium can be established through the separable bilevel duality structure of $\mathcal{RO}$, the lack of joint concavity in $(\lambda,u)$ means the dynamics cannot be derived as the gradient flow of a Lagrangian function. This necessitates the construction of a novel Lyapunov function to analyze the stability of the proposed non-Lagrangian dynamics.
```

**Rationale:** Does NOT claim saddle point is a novel result. Immediately pivots to what IS novel (non-Lagrangian dynamics + Lyapunov). Keeps the "joint concavity" observation (factually correct and important for motivation).

---

### Fix 4: Replace "model-free" with "reformulation-free"

**File:** `1.Main_Cleaned_Revised.tex`
**USER DECISION NEEDED** — affects paper messaging.

#### Research Insight

- "Model-free" in RL/control = no model of environment dynamics, learning from samples. Paper's dynamics require exact gradients — opposite of model-free.
- "Derivative-free" / "zeroth-order" = no gradients. Paper uses gradients — wrong direction.
- "Oracle-based" = Ben-Tal et al. 2015 specific method (iterative oracle calls). Different structure.
- **"Reformulation-free"** = no robust counterpart reformulation needed. No conflicting precedent. Immediately clear to RO and broader optimization audiences. Best option.
- "Counterpart-free" = valid but less self-explanatory outside RO community.

#### Location: Line 158 (Introduction paragraph)

**Current:**
```latex
\rev{A distinctive feature of our dynamical system is its amenability to model-free implementation when deployed in physical systems where agents can sense local gradients but do not possess global knowledge of objective or constraint functions. Each agent requires only the ability to measure local gradient information $\nabla_x f_i(x,u_i)$ and $\nabla_{u_i} f_i(x,u_i)$ through sensing or finite-difference approximations at their current state, along with information from neighboring agents through local communication. This enables implementation in distributed settings where the global problem formulation may not be explicitly known to individual agents, yet the collective dynamics converge to the robust optimal solution. This model-free characteristic distinguishes our approach from robust counterpart methods that require complete a priori knowledge of problem structure.}
```

**Proposed replacement:**
```latex
\rev{A distinctive feature of our dynamical system is that it is \emph{reformulation-free}: it solves the robust optimization problem directly through gradient-based dynamics without requiring derivation of a tractable robust counterpart. Each agent requires only the ability to evaluate local gradient information $\nabla_x f_i(x,u_i)$ and $\nabla_{u_i} f_i(x,u_i)$ at its current state, along with information from neighboring agents through local communication. This enables implementation in distributed settings where the global problem formulation may not be explicitly known to individual agents, yet the collective dynamics converge to the robust optimal solution. This reformulation-free characteristic distinguishes our approach from robust counterpart methods that require complete a priori knowledge of problem structure and closed-form reformulations.}
```

**Changes:**
- "model-free" → "reformulation-free" (2 occurrences)
- "amenability to model-free implementation when deployed in physical systems where agents can sense local gradients but do not possess global knowledge..." → clearer definition: "reformulation-free: solves RO directly without requiring derivation of a tractable robust counterpart"
- "measure ... through sensing or finite-difference approximations" → "evaluate" (removes implication of zeroth-order operation which would need separate convergence proof)

#### Other locations needing update:

| Line | Section | Action |
|------|---------|--------|
| 1204 | Response to Reviewer 4 | Update quoted blue text to match new Introduction |
| 1330 | Response to Reviewer 5 | Update quoted blue excerpt to match |
| 1708 | AI Review, Resolved items | Change "Model-free" → "Reformulation-free" |
| 1859 | AI Review, Checklist | Update description |
| 1863 | AI Review, Checklist | Mark as resolved |
| 1881 | AI Review, Final Verdict | Mark as done |
| 166 | Commented-out contribution list | Skip (inactive) |

---

### Fix 5: Add convergence rate as explicit limitation in Conclusions

**File:** `1.Main_Cleaned_Revised.tex`, line 994
**No user decision needed.**

**Current (single sentence):**
```latex
This paper introduced a continuous-time dynamical system for solving robust optimization problems convex in the decision variable and concave in the uncertainty. The method provides solutions for problems where existing methods are intractable or computationally expensive. Future work includes applications to non-convex problems, large-scale distributed optimization and deriving convergence rates.
```

**Proposed replacement:**
```latex
This paper introduced a continuous-time dynamical system for solving robust optimization problems convex in the decision variable and concave in the uncertainty. The method provides solutions for problems where existing methods are intractable or computationally expensive. \rev{A limitation of the present work is the absence of explicit convergence rate bounds; while global asymptotic stability is established, the analysis does not characterize the rate of convergence (e.g., exponential convergence under strong convexity). Deriving such bounds and analyzing discretization error for practical ODE solver implementations are important directions for future research.} Future work also includes applications to non-convex problems and large-scale distributed optimization.
```

**Changes:**
- Adds explicit limitation statement (wrapped in `\rev{}` for visibility)
- Separates "convergence rates" from the future work list into its own limitation sentence
- Keeps other future work items

---

### Fix 6 (Bonus): Add missing bibliography entries for citations in Fix 3

**File:** `2.References.bib`
**No user decision needed.** Required if Fix 3 is applied (new `\cite{}` commands).

**Already in bib:** `cherukuri2016` (Systems & Control Letters), `cherukuri2016_2` (Allerton), `cherukuri2017` (SIAM J. Control & Opt.), `nguyen2018` (Operations Research)

**Need to add** (only if cited in the rewritten Remark or Introduction):

```bibtex
@article{honguyen2021,
  author = {Ho-Nguyen, N. and Kilin\c{c}-Karzan, F.},
  title = {First-Order Algorithms for Robust Optimization Problems via Convex-Concave Saddle-Point {L}agrangian Reformulation},
  journal = {INFORMS Journal on Computing},
  volume = {34},
  number = {3},
  pages = {1711--1728},
  year = {2022}
}

@article{qu2019exponential,
  author = {Qu, G. and Li, N.},
  title = {On the Exponential Stability of Primal-Dual Gradient Dynamics},
  journal = {IEEE Control Systems Letters},
  volume = {3},
  number = {1},
  pages = {43--48},
  year = {2019}
}
```

**Note:** The current proposed Remark replacement in Fix 3 cites `cherukuri2016` which is already in the bib. The Ho-Nguyen 2021/2022 paper and Qu-Li 2019 are recommended additions for the AI review section's "missing citations" list but are NOT cited in the main text edits — so they're optional unless the user wants to add them to the Introduction or Related Work.

---

## Execution Order

1. **Fix 1** (typos) — no decision, apply immediately
2. **Fix 2** (O(n²) claim) — no decision, delete sentence
3. **Fix 5** (conclusions) — no decision, expand
4. **Fix 3** (saddle point) — **ask user** before applying
5. **Fix 4** (model-free) — **ask user** before applying
6. **Update AI review section** — mark resolved items after Fixes 3-4 are applied
7. **Compile PDF** — verify clean build

## Acceptance Criteria

- [ ] Lines 584, 586: `c` → `c_i`, parentheses balanced
- [ ] Line 930: complexity sentence deleted
- [ ] Remark at lines 402-404: title + body reframed per user's choice
- [ ] Line 154: Introduction saddle point language softened
- [ ] Line 158: "model-free" → "reformulation-free" (or user's choice)
- [ ] Line 994: Conclusions expanded with convergence rate limitation
- [ ] Reviewer response quotes (lines 1204, 1330) updated to match new text
- [ ] AI review checklist items updated to reflect completed fixes
- [ ] PDF compiles cleanly with `./create_pdf.sh`
- [ ] No new LaTeX warnings introduced

## Sources

- [Cherukuri, Mallada, Low, Cortes — The Role of Convexity in Saddle-Point Dynamics (IEEE TAC 2018)](https://arxiv.org/abs/1608.08586)
- [Cherukuri, Gharesifard, Cortes — Saddle-Point Dynamics: Conditions for Asymptotic Stability (SIAM J. Control 2017)](https://epubs.siam.org/doi/10.1137/15M1026924)
- [Ho-Nguyen, Kilinc-Karzan — First-Order Algorithms for RO via Saddle-Point Lagrangian (INFORMS J. Computing 2022)](https://pubsonline.informs.org/doi/10.1287/ijoc.2022.0200)
- [Lin, Jin, Jordan — On Gradient Descent Ascent for Nonconvex-Concave Minimax (ICML 2020)](https://arxiv.org/abs/1906.00331)
- [Qu, Li — On the Exponential Stability of Primal-Dual Gradient Dynamics (IEEE CSL 2019)](https://arxiv.org/abs/1803.01825)
