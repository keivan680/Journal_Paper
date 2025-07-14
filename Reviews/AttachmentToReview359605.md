# Review Attachment: AttachmentToReview359605.pdf

*Converted from PDF - 3 page(s)*

---

## Page 1

The reviewer acknowledges the authors' efforts in addressing a relevant and timely problem. The core idea presented is original and points toward a promising research direction with potential impact. However, the current manuscript has several important limitations in terms of technical depth and presentation, which make it unsuitable for publication as a full research article.

Given the value of the contribution, the reviewer encourages the authors to consider re-submitting the work in the form of a technical note. This would allow the main idea to be shared with the community while leaving room for future refinement and development.

The reviewer has provided specific comments below and hopes they will help improve the quality of the current submission.

• The abstract is overly long, and the writing style—both in the abstract and throughout the paper—could benefit from greater clarity and conciseness. In several places, long sentences obscure the intended message, making the content harder to follow. The reviewer recommends a thorough revision of the text to improve readability and precision. An example of such issues can be found in the abstract and introduction.
    ○ This is while the existing solutions such as the robust counterpart and scenario-based random sampling assume that the problem formulation is completely known a priori.
    ○ The reformulation approach to solving the RO problem, which is often a challenging, albeit usually convex, optimization problem, has the deficiency of suffering from case-by-case scenarios depending on the specific form of the uncertainty constraint and the specific form of the uncertainty set. In other words, depending on how simple the uncertainty set looks and based on the optimization problem type (whether it is linear programming, quadratic programming, second-order cone programming, semidefinite programming, etc.), an RC is being calculated and provided at hand.
    ○ Also throughout this paper, the author used "the paper ... or the main contribution of the paper .. ". It is confusing from the reviewer point of view. It is suggested to use "this paper" to highlight that it refers to this paper under review.

• Footnote 2, related to Optimization Problem 2, should include the assumption that the constraint functions are continuous with respect to the uncertain variable. This continuity is essential to ensure that the maximum is achieved and the problem is well-posed.

• The novelty of Lemma 1 and its proof is unclear. From the reviewer's point of view, it appears to reflect a standard saddle point property within the context of Lagrangian duality. To strengthen the contribution, it would be helpful to clearly explain what is new in this result and how it differs from classical formulations. Under the usual convex–concave assumptions, similar inequality chains follow from well-known results such as Sion's or Rockafellar's saddle point theorems. As it stands, the lemma seems to extend a classical property to a broader set of variables, as commonly done in robust optimization. Clarifying this point and situating the lemma more clearly within existing literature would improve the presentation.

• Regarding Assumption 3, the strict positivity of the C parameter is mathematically convenient—particularly for establishing exact-penalty properties and strong duality

---

## Page 2

results—but may be overly rigid for practical modeling purposes. The reviewer acknowledges the theoretical benefits of this assumption, including eliminating undesirable solutions, supporting exact-penalty formulations, ensuring dual consistency, and preserving convexity or monotonicity properties. However, this comes with practical implications: determining appropriate values for C, accounting for the fact that some constraints may be soft, and recognizing that different scenarios may require different weightings. Moreover, the manuscript does not discuss empirical strategies for selecting these parameters, which would be valuable for practical implementation.

• There is a notation inconsistency in item 1 of the one-uncertain-constraint example: the variable ui should be written as u1 for clarity and consistency.

• To improve readability, the reviewer suggests introducing the Z parameter directly after the compact notation for the robust optimization formulation (23). This would help streamline the presentation and make the structure of the argument clearer to the reader.

• In Equation (36) within the proof of Lemma 3, there appear to be two missing parentheses, which make the expression difficult to follow. Specifically, line 3 is missing an opening parenthesis, and line 5 lacks a closing one as well as in the second line of next equations after (36). The reviewer suggests correcting these to improve clarity and ensure the logical flow of the proof is maintained.

• Remark 4 raises an important technical point but would benefit from clearer formulation and improved writing. From the reviewer's perspective, the content of the remark could be more effectively communicated if it were split into two separate parts, each addressing a distinct aspect of the discussion. This would enhance clarity and better highlight the significance of the observation.

• From the reviewer's perspective, the conclusion presented in the final paragraph of the proof of Theorem 4 is neither straightforward nor self-evident. To improve clarity and support the argument, further elaboration and justification are recommended.

• The requirement imposed in Corollary 1 is quite strong and may pose challenges in both theoretical analysis and practical implementation. The reviewer acknowledges that the assumption—particularly the strict complementarity condition—is introduced to avoid degeneracy and to ensure the existence of a Lyapunov function with a guaranteed negative rate of change. While this is a mathematically sound approach, it relies on a structural regularity that may not hold in many realistic settings.

In fact, such assumptions can fail even in simple convex examples, especially when some robust constraints are inactive—an entirely common occurrence in robust optimization. As a result, the general applicability of the corollary is limited under its current form.

From the reviewer's point of view, a promising direction to relax this requirement would be to introduce proximal (or regularization) terms on the primal side. This modification can help recover strong monotonicity at the saddle point, which in turn can support similar convergence guarantees without relying on strict complementarity. Incorporating this perspective would broaden the relevance of the result and make it more robust to practical modeling scenarios.

---

## Page 3

• In the presented examples, the actual robust optimization setting—particularly with scenario-based uncertain constraints—is not fully addressed. Incorporating such scenarios would strengthen the practical relevance of the examples. In addition, the reviewer was expecting to see results related to convergence analysis, including the stability of the proposed approach and its convergence to optimal points. Providing these insights would offer a more complete picture of the method's performance and theoretical soundness.