# Review Attachment: AttachmentToReview359595.pdf

*Converted from PDF - 2 page(s)*

---

## Page 1

This paper proposes a novel continuous-time dynamical system, termed RO dynamics, for solving robust optimization (RO) problems in a convex-concave framework. While the approach is innovative and has potential, the manuscript requires significant revisions to improve clarity, technical rigor, and presentation. Below are specific comments and suggestions for improvement.

1. The paper discusses contributions and motivation in multiple sections, but these points are not clearly articulated or cohesively presented. To improve readability and impact, I recommend reorganizing the introduction to explicitly highlight the key contributions.

2. Algorithm (23) is presented in isolation without sufficient explanation or context. The authors should provide a detailed discussion immediately after introducing the algorithm, including the intuition behind its design, a clear comparison with existing methods to highlight key differences, and specific improvements or advantages over traditional approaches.

3. The paper lacks a detailed theoretical analysis of the proposed algorithm's convergence performance compared to existing methods.

4. The structure of the manuscript needs improvement for better readability, as equations (5) and (6) are referenced in Assumption 2 before they are formally introduced in the text.

5. The conditions in Assumption 2 seem restrictive. Can they be relaxed, as in Ref. [34]? If not, please provide a detailed explanation.

6. The need for Assumption 1 should be justified. Can the framework be extended to more general cases?

7. The meaning of $h_{ij}\$ and $K_i$ in equation (3) should be clearly understood, and the purpose of introducing them here should be explicitly justified.

8. The Lagrangian function (15) for the RO problem (4) appears to be straightforward, raising questions about the necessity of the lengthy and intricate analysis preceding it. The authors should assess whether the detailed derivation in the earlier part of Section IV is essential. If the complexity is indeed necessary, the authors should provide a clearer justification for its inclusion, highlighting how it enhances the

---

## Page 2

understanding of the problem or the robustness of the solution.

9. The abbreviation "RC" in the line before equation (9) has been explained earlier and could be deleted here. The meaning of the abbreviation "RHS" after inequality (51) needs to be explained. The authors should carefully review the entire manuscript for similar issues.

10. In Section V-D, since the Appendix B only contains conclusions without detailed proofs, it is recommended to incorporate these conclusions directly into the main text for better readability and logical flow.

11. We note that the proof of Lemma 4 is not provided in Ref. [41], and this issue needs to be addressed.

12. What is the meaning of the superscript $\epsilon$ +$ in the second line of equation (43)? Please explain.

13. The results obtained from Ref. [22] in the simulation are much smaller, so why are the results of the proposed algorithm in this paper considered to be more effective?

14. The justification for Proposition 6 in Appendix B requires further clarification to enhance understanding.

15. The expression $\lim_{k \to \infty}=y$ in Proposition 6 seems incorrect. It should likely be $\lim_{k \to \infty} y_k=y$.

16. There are several language issues, such as the reversed quotation marks in the last paragraph of the first column on page 5. Please carefully proofread the manuscript.

17. The introduction is lengthy and lacks a coherent structure. Please revise it to emphasize the advantages of the proposed method, particularly its ability to operate without prior problem modeling.

18. The techniques from Ref. [22] used in the simulation appear outdated and may not reflect the current advancements in the field. To strengthen the comparative analysis, it is recommended to include state-of-the-art algorithms in the evaluation.