**# UI-TARS: Pioneering Automated GUI Interaction with Native Agents**



**## What is the research/project about?**

This paper introduces UI-TARS, a native GUI agent model that solely perceives the screenshots as input and performs human-like interactions. Unlike conventional agent frameworks that rely on wrapped commercial models (e.g., GPT-4o) and expert-crafted prompts, UI-TARS is an end-to-end model.



**## The main contributions**

**### Enhanced Perception for GUI Screenshots**

Enhanced Perception is achieved by curating a large-scale dataset of GUI screenshots and rich metadata using specialized parsing tools. The dataset targets the following tasks: element description, dense captioning, state transition captioning, question answering and set-of-mark prompting. This ensures UI-TARS recognizes and understands GUI elements with exceptional precision, providing a robust foundation for subsequent reasoning and action.



**### Unified Action Modeling for Multi-step Execution**

The authors establish a unified action space to standardize semantically equivalent actions across platforms, supported by a large-scale dataset of multi-step action traces combining original annotated trajectories and standardized open-source data. The agent's critical grounding ability — accurately locating and interacting with specific GUI elements — is improved by curating a vast dataset that pairs element descriptions directly with their spatial coordinates, thus ensuring precise and reliable interactions.



**### System-2 Reasoning for Deliberate Decision-making**

Decision-making is enhanced by crawling and refining 6M GUI tutorials, then injecting reasoning patterns like task decomposition, consistency, and reflection into action traces. UI-TARS integrates these capabilities by generating explicit “thoughts” before each action, enabling robust and deliberate reasoning in dynamic environments.



**### Iterative Refinement by Learning from Prior Experience**

UI-TARS addresses the lack of large-scale, high-quality action traces by continuously collecting and refining new interaction data through hundreds of virtual machines. Multi-stage filtering, VLM scoring, and human review are retained for training. In addition, reflection tuning with annotated error-correction and post-reflection data, combined with Direct Preference Optimization, ensure that the agent not only learns to avoid errors but also adapts dynamically when they occur. Together, these strategies enable UI-TARS to achieve robust, scalable learning with minimal human oversight.



**## What is its methodology?**

**### Architechture Overview**

UI-TARS is an iterative native GUI agent model that receives the task instruction, current screenshot, and interaction history to generate subsequent actions. To foster deliberate decision-making, a reasoning component called "thoughts" is generated prior to each action, reflecting System 2 thinking, which guides the agent to reconsider previous actions and observations. The model retains the full history of previous thoughts and actions as short-term memory but limits the visual input to the last N observations to optimize memory usage and maintain efficiency within constrained token budgets.



**### Enhancing GUI Perception**

**Screen Collection**: To address data scarcity and ensure diverse coverage, the authors built a large-scale dataset comprising screenshots and metadata from websites, apps, and operating systems.

**Element Description**: Focus on creating detailed and structured descriptions for each element. Such descriptions are based on metadata extracted using parsing tools and further synthesized by a VLM, covering four aspects: Element Type, Visual Description, Position Information and Element Function.

**Dense Captioning**: Train UI-TARS to understand the entire interface while maintaining accuracy and minimizing hallucinations. For each recorded element in the screenshot, they first obtain their element descriptions. For embedded images, which often lack detailed metadata, they also generate their descriptive captions. After that, integrating all the image and element descriptions into a cohesive, highly detailed caption that preserves the structure of the GUI layout using a VLM. During training, UI-TARS is given only the image and tasked with outputting the corresponding dense caption.

**State Transition Captioning**: Train the model to identify and describe the differences between two consecutive screenshots and determine whether an action, such as a mouse click or keyboard input, has occurred. During training, UI-TARS is presented with a pair of images and tasked with predicting the specific visual changes (and possible reasons) of the two images.

**Question Answering (QA)**: Synthesize a diverse set of QA data that spans a broad range of tasks, including interface comprehension, image interpretation, element identification, and relational reasoning.

**Set-of-Mark (SoM)**: Draw visually distinct markers for parsed elements on the GUI screenshot based on their spatial coordinates. These markers vary in attributes such as form, color, and size, providing clear, intuitive visual cues for the model to locate and identify specific elements. They integrate SoM annotations with tasks like dense captioning and QA. For example, the model might be trained to describe an element highlighted by a marker.



**### Unified Action Modeling and Grounding**

**Unified Action Space**: Design a common action space that standardizes semantically equivalent actions across devices. Also define two terminal actions: Finished(), indicating task completion, and CallUser(), invoked in cases requiring user intervention, such as login or authentication.

**Action Trace Collection**: Rely on two primary data sources, their annotated dataset and open-source data standardizing into a unified action space format.

**Improving Grounding Ability**: Train UI-TARS to directly predict the coordinates of the elements it needs to interact with. Screenshots and metadata such as type, depth, bounding boxes, and text are collected and used to generate training samples, with normalized coordinates ensuring consistency across devices. Each element description is mapped to its corresponding coordinates, enhancing the model’s grounding ability. To further expand the dataset, multiple open-source resources were standardized into a unified action space, enabling high-precision grounding for tasks like clicking and dragging.





**### Infusing System-2 Reasoning**

**Reasoning Enrichment** with GUI Tutorials by filtering approximately 6 million GUI tutorials to provide foundational GUI knowledge and logical execution patterns.

**Reasoning Stimulation with Thought Augmentation** is applied to action traces by injecting explicit "thoughts" generated via VLM prompting (ActRe).

**Thought Bootstrapping** refines this process by sampling thought-action pairs to ensure the generated reasoning causally aligns with the chosen correct action, producing higher-quality annotations.



**### Learning from Prior Experience in Long-term Memory**

**Online Trace Bootstrapping**: The agent executes instructions on virtual PCs, generating raw interaction traces which are rigorously filtered using multi-level steps, including rule-based heuristics, VLM scoring, and human review, before being used for fine-tuning the model iteratively.

**Reflection Tuning**: Address error correction by creating trace paired samples for both the immediate mistake fix and a subsequent post-reflection step, simulating how the agent should realign task progress after an error.

**Agent DPO (Direct Preference Optimization)**: Leverage both the generated erroneous steps (negative examples) and the corrected steps (positive examples) to explicitly guide the model's policy, reinforcing optimal actions and penalizing suboptimal ones





**### Training**

Use the same VLM backbone, Qwen-2-VL, and adopt a **three-phase training process**. This process refines the model’s capabilities across diverse GUI tasks, utilizing a total data size of approximately 50B tokens.

**Continual Pre-training Phase**: Utilize the full set of data described above, excluding the reflection tuning data, for continual pre-training with a constant learning rate. This foundational phase allows the model to learn all the necessary knowledge for automated GUI interaction.

**Annealing Phase**: Select high-quality subsets of perception, grounding, action trace, reflection tuning data for annealing. Denote the model trained after this phase as UI-TARS-SFT.

**DPO Phase**: Finally, employ annotated reflective pairs from online bootstrapping data for DPO training. During this process, the model refines its decision-making, reinforcing optimal actions while penalizing suboptimal ones. This process improves the model’s ability to make precise, context-aware decisions in real-world GUI interactions. The final model is denoted as UI-TARS-DPO.



**## What are the results?**

**### Overall and Perception SOTA**

UI-TARS achieves SOTA performance across over 10 GUI Agent benchmarks covering perception, grounding, and agent task execution. In perception evaluation, UI-TARS-72B scores 82.8 on Visual-WebBench, outperforming GPT-4o (78.5) and Claude 3.5 Sonnet (78.2).



**### Grounding and Offline Agent SOTA**

UI-TARS achieves high-precision grounding, scoring 38.1 (SOTA) on the challenging ScreenSpot Pro benchmark. In offline agent capability evaluation, UI-TARS-72B achieves SOTA performance on Multimodal Mind2Web and shows notable superiority in mobile tasks like Android Control and GUI Odyssey compared to previous methods.



**### Online Agent SOTA and Scaling Benefit**

In online benchmarks, UI-TARS-72B-DPO sets new SOTA results on OSWorld, achieving 24.6 (50 steps) and 22.7 (15 steps), surpassing Claude’s 22.0 and 14.9, respectively. On AndroidWorld, UI-TARS-72B-SFT achieves 46.6, outshining GPT-4o’s 34.5. Scaling the model size from 7B to 72B significantly improves System-2 reasoning, resulting in a larger performance gap in online tasks compared to offline tasks.



**## What are the current challenges or limitations?**



**## What are the future directions?**

The future path for GUI agents is the integration of active and lifelong learning, where agents autonomously drive their own learning through continuous, real-world interactions.



