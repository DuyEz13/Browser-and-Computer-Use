**# THE UNREASONABLE EFFECTIVENESS OF SCALING AGENTS FOR COMPUTER USE**



**## What is the research/project about?**

The paper introduce Behavior Best-of-N (bBoN), a method that scales over agents by generating multiple rollouts and selecting among them using behavior narratives that describe the agents' rollouts.



It also present new version Agent S3 with Agent Coding and new Flat Policy.



**## Main contributions**

Introduce the wide scaling paradigm for CUAs, showing that generating multiple trajectories in parallel and selecting among them substantially improves robustness and coverage.



Propose Behavior Best-of-N (bBoN), a framework that converts dense trajectories into compact behavior narratives and uses them for principled trajectory selection.



**## What is its methodology?**

**### Behavior Narrative Generation**

The Behavior Narrative Generator (instantiated using a VLM) extracts key facts from each transition (using pairs of screenshots before and after an action) to describe only the task-relevant changes caused by the agent. By overlaying visual markers and zoomed regions around the pointer, it verifies that actions such as clicks or drags achieved the intended effects while filtering out irrelevant visual details. The resulting behavior narrative is a compact sequence summarizing what the agent did and what outcomes occurred.



**### Behavior Best-of-N Judge**

The Behavior Best-of-N Judge then compares these generated narratives across multiple rollouts from different base policies. A VLM judge performs comparative evaluation in a multiple-choice format, identifying the trajectory that best fulfills task requirements. This approach simplifies evaluation, improves token efficiency, and scales effectively to large numbers of agents by focusing judgment on summarized behavior rather than raw, step-by-step data.



**### An improved agentic framework baseline**

**Coding Agent** allows the system to decide dynamically whether to perform GUI-based actions or programmatic edits within a sandboxed environment. This design enables flexible problem-solving through iterative code generation and execution, with each session summarized and fed back to assist future planning.



**Flat Policy** replaces traditional hierarchical (manager–worker) planning with a single unified policy capable of continuous replanning based on context. This structure leverages the strong reasoning abilities of modern foundation models, improving responsiveness and avoiding issues caused by outdated subgoals. The authors record only the operational constraint: the policy does not commit to a subgoal list; instead, it updates plans online based on current observation and compact history, enabling immediate course corrections while minimizing orchestration overhead. Together, these design choices make Agent S3 faster, more adaptable, and better suited as a high-performing base framework for large-scale agentic evaluation.





**## What are the results?**

The paper achieves a new SOTA of 69.9% on OSWorld, surpassing prior work by a large margin (10% absolute improvement compared to CoAct-1 59.9%) and approaching human performance at 72%.



The authors provide extensive ablations validating their design choices, like the correlation between the success rate and the number of rollouts, what is the best mixture-of-model ensemble, comparasion between behavior narratives and other trajectory representations, bBoN and other independent ranking method. 



Agent S3 also shows strong zeroshot generalizability on WindowsAgentArena and AndroidWorld.



**## What are the current challenges or limitations?**

The Behavior Best-of-N framework assumes that an agent can generate multiple independent rollouts from the same initial state, a condition met in controlled benchmarks or virtualized environments. In practice, this is achieved by running agents inside virtual machines (VMs) with snapshot and duplication support, enabling reproducible runs and efficient parallelization without increasing total latency. However, executing rollouts directly on a real desktop breaks this independence due to potential cross-run interference and uncontrollable side effects. Even with VMs, shared online resources like shopping carts or cloud accounts can cause interference between runs.



**## What are the future directions?**

Future research aims to extend parallel rollouts to real desktops and manage shared online resources so Behavior Best-of-N can operate over all CUA tasks.

