# Review Attachment: AttachmentToReview359597.pdf

*Converted from PDF - 2 page(s)*

---

# Robust Optimization via Continuous-Time Dynamics

Keivan Ebrahimi, Nicola Elia, and Umesh Vaidya

## 1 Summary of the paper

The paper proposes a novel dynamical system-based approach, called RO dynamics, for solving robust optimization problems in a general convex-concave framework. Unlike traditional primal-dual gradient dynamics, this approach does not rely on the gradient of the Lagrangian function. Instead, it treats the uncertain variable as a dynamical state and shows that the globally asymptotically stable equilibrium point of RO dynamics can recover robust optimal solutions for a broad class of convex-concave robust optimization problems. The method does not require prior knowledge of the problem formulation and is suitable for decentralized implementation, making it ideal for real-time applications in dynamic environments. The paper provides a simulation example to demonstrate the effectiveness of the approach, highlighting its advantages over existing methods that require complete prior knowledge of the problem.

## 2 Major comments

The papers present interesting approaches to the addressed problems. However, some aspects require clarification to better understand the contribution of the work.

• My concern lies in the motivation behind the problem formulation (4). Does it offer any advantages compared to formulation (3)? The authors should emphasize the main reason for introducing (4), beyond merely presenting it as a more general version of (3).

• The paper also considers a slight variation of problem formulation (2), presented in (3). The authors should provide more details on this new formulation and explain how it differs from the classical one. For instance, is the motivation behind presenting the sets $U_i$ as nonlinear inequalities? Some explanation would help the reader better understand the contribution of the paper.

• This question is related to the first one. In equation (10), to derive the Lagrangian function, the authors introduce λᵢ as multipliers. However,

---

one could instead consider multipliers of the form γᵢ := cᵢ + λᵢ, which would reduce to the Lagrangian function of formulation (3). Therefore, I still do not see the novelty or specific role of the cᵢ terms.

• In formulation (2), the authors take the maximum over the constraint functions, which significantly increases the problem's complexity compared to the classical robust optimization problem (1). Specifically, if the constraint functions are smooth, taking the maximum introduces non-smoothness, making the problem harder to solve than formulation (1). It would be helpful for the authors to justify whether this complexity is justified, whether this step is essential or whether smoother alternatives could be considered would improve the reader's understanding of the trade-offs involved.

• Lemma 1 is a well-known result, or am I missing something? since, Definition 1 KKT conditions seems to be identical to the KKT conditions, which are then referred to as a saddle point condition, when certain constraint qualifications hold (e.g., Slater's condition). Please clarify this definition, since Section 5.9.1 in Convex Optimization by Boyd refers to the Lagrangian function using generalized inequalities.

## 3 Minor comments

• Note that even if U₀ is a singleton, formulation (2) is defined over general sets Uᵢ, whereas in formulation (3), the variables uᵢ are specifically defined over the convex functions hᵢ,ⱼ. My point is that, in this case, formulation (2) remains more general than formulation (3).

• Is the set Uᵢ in formulation (3) still compact under the assumption that the functions hᵢ,ⱼ are convex? I believe some continuity assumptions are also needed.

• Assumption 3 states that cᵢ > 0, which implies that the problem formulation presented in (2) is not recovered. Since this assumption is introduced for technical reasons, it may need to be relaxed to ensure consistency with formulation (2).

• In the numerical experiments, the constraints fᵢ(x, uᵢ) are linear in uᵢ. Did the authors observe similar results when dealing with problem such that the constraints are not necessarily linear in uᵢ?