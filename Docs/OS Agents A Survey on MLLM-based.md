**# OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use**



**## What is the research/project about?**

The survey focuses on advanced agents, designated as OS Agents, which are (Multimodal) Large Language Model ((M)LLM)-based Agents. These agents use computers, mobile phones, and web browsers by operating within the environments and interfaces provided by operating systems (OS), such as Graphical User Interface (GUI) and Command Line Interface (CLI), to automate tasks.



**## What problem does it solve? (or what does it introduce?, or what is the main contribution?)**

Given the significant advancement and growing body of work in (M)LLM-based OS Agents in both academic research and commercial products, the survey addresses the need for a comprehensive resource that consolidates the current state of research in this area.



This paper provides a comprehensive survey on OS Agents. It elucidates the fundamentals of OS Agents, explores methodologies for their construction (focusing on domain-specific foundation models and agent frameworks), reviews evaluation metrics and benchmarks, and discusses current challenges and promising directions for future research.



**## Content of the survey**

**### Fundamental of OS Agents**

OS Agents are specialized AI agents that utilize the environment, input, and output interfaces provided by operating systems (OS) to operate computers, mobile phones, and web browsers in response to user-defined goals. These agents are designed to automate tasks executed within the OS by leveraging the exceptional understanding and generative capabilities of (M)LLMs.



OS Agents are based on **three key components**. **The Environment** refers to the platforms they operate within, such as computers, phones, and browsers. **The Observation** Space encompasses the information they can access about the system's state, including capturing information like screen images or textual data (such as screen descriptions and HTML code). **The Action Space** defines the set of interactions used to manipulate the environment, broadly categorized into input operations, navigation operations, and extended operations.



To achieve their objectives, OS Agents necessitate **core capabilities**. **Understanding** is fundamental for comprehending complex OS environments, which involve diverse data formats like HTML code and high-resolution Graphical User Interfaces (GUIs). **Planning** is a crucial capability, enabling agents to decompose complex tasks into manageable sub-tasks and formulate action sequences, often requiring dynamic adjustment of plans based on environmental feedback. Lastly, **Action Grounding** is essential for translating textual instructions or plans into executable actions by correctly identifying screen elements and providing necessary parameters.



**### Construction of OS Agents**

The survey disscuss effective strategies for constructing OS Agents, including training **domain specific foundation models** and designing **agent frameworks** for OS Agents.

1. **Foundation Models**
   Two key components: model architechture and training strategies.

   * **Model architechture**:  Four common model architectures are used: Existing LLMs (which can process user instructions and HTML code, but only textual input), Existing MLLMs (which incorporate vision processing for GUIs), Concatenated MLLMs (combining suitable LLMs and vision encoders via an adapter or cross-attention module), and Modified MLLMs (adjusting architectures, often to handle high-resolution GUI screenshots, e.g., CogAgent).
   * **Pre-training**: This enhances the model's understanding of GUI and visual-textual correlations. Data sources include publicly available data and synthetic data. Key tasks in pre-training include Screen Grounding (extracting 2D coordinates/bounding boxes based on descriptions), Screen Understanding (extracting semantic information and interpreting image content), and Optical Character Recognition (OCR) (handling textual content in GUIs).
   * **Supervised Finetuning**: Improves GUI referring, grounding abilities, and model suitability for navigation tasks. High-quality SFT data is collected through Rule-Based Data Synthesis (using tools and rules to explore and extend trajectory data), Model-Based Data Synthesis (using (M)LLMs to generate samples), and Model-Based Data Augmentation (using (M)LLMs to construct Chain-of-Action-Thought (CoAT) data)
   * **Reinforcement Learning**: RL is increasingly applied, treating (M)LLMs as policy models to align them with final objectives. Methods include fine-tuning with hierarchical planning and integrating with multimodal networks, leveraging human demonstrations through behavior cloning before further training with algorithms like PPO, or specialized methods like Q-ICRL.



1. **Agent Frameworks**

Four core components: Perception, Planning, Memory, and Action.

* **Perception**: This component collects and analyzes information from the environment, extracting relevant data for planning, action, and memory optimization. It is categorized by input modality
* **Planning**: Planning develops a sequence of actions to achieve a goal, breaking complex tasks into manageable sub-tasks. Global Planning: generates a plan once (often using Chain-of-Thought (CoT) prompts) and executes it without adjustments based on environmental changes. Iterative Planning: continuously iterate and adjust their plans based on historical actions or changes in the environment, utilizing methods like ReAct (integrating reasoning with action outcomes).
* **Memory**: The Memory module saves useful information for task performance, environment adaptation, and optimization. Memory Sources: Internal Memory (stores information during task completion, such as action history and screenshots) and External Memory (provides long-term knowledge support through knowledge bases, documents, and online tools). Memory Optimization: Key strategies include Management (processing and abstracting information, consolidating content), Growth Experience (revisiting steps to analyze successes/failures and optimize future performance, sometimes returning to a previous state), and Experience Retrieval (retrieving similar past experiences from long-term memory).
* **Action**: The Action space defines the interfaces for agents to interact with OS platforms (computers, phones, browsers). Actions are categorized as: Input Operations (Interactions via mouse/touch and keyboard), Navigation Operations (Actions enabling traversal across platforms), Extended Operations (Provides additional capabilities, primarily including code execution and API integration - accessing external tools and services).





**### Evaluation of OS Agents**

Evaluation metrics are categorized into Step-level Evaluation, which details the planning trajectory and action grounding accuracy, and Task-level Evaluation, which assesses the final outcome using metrics like the Overall Success Rate (SR) and Efficiency Metrics such as the Step Ratio.

Benchmarks cover various platforms, specifically Computer, Phone, and Browser environments, and target specialized tasks including GUI Grounding, Information Retrieval, and Agentic Tasks. These benchmarks utilize either Static Environments (offline, cached data) or more realistic Interactive Environments. Interactive settings, particularly real-world environments (like OSWorld and AndroidWorld) provide dynamic feedback and are crucial for testing an agent's strong generalization capabilities.



**### Product of OS Agents**

Commercial OS Agent products are rapidly evolving, driven by academic research, and show trends in platform diversification (covering browsers, computers, and phones) and functional stratification (into task execution-oriented and search-oriented types). Initial explorations around 2023 featured low-invasiveness solutions like browser plugins (e.g., AgentGPT, Taxy AI) for technological validation. Products released in 2024 and 2025, such as Apple Intelligence (for computer and phone) and Anthropic's Computer Use, demonstrate a shift towards deep OS integration, enhanced capabilities like multimodal interaction (e.g., Project Mariner), and optimized complex task decomposition. This progression signifies a movement from the tool layer to the system layer.



**## What are the results?**

Tables show that in Computer/OSWorld and Browser/WebArena, Commercial Product outperforms Research Work. But in Phone/AndroidWorld, Research Work gives better results.



**## What are the current challenges or limitations?**

* **Safety and Privacy Risks**: A significant challenge involves security and privacy risks, as OS Agents operate on personal devices with user data. Identified vulnerabilities include Web Indirect Prompt Injection (WIPI), where adversaries embed instructions in web pages to control agents, and environmental injection attacks that induce unintended actions or data theft.
* **Limited Personalization and Memory Management**: Many OS Agents today still perform insufficient in providing personalized experience to users and self-evolving over user interactions. The challenge of expanding memory to multi-modal forms and ensuring the efficient management and retrieval of this complex memory.



**## What are the future directions?**

* **Developing Robust Defense Mechanisms**: Future research should prioritize the development of robust defense mechanisms specifically tailored to the unique vulnerabilities of OS Agents, such as injection attacks and backdoor exploits. This is necessary because defenses developed for general LLM agents are still nascent or insufficient for OS Agents.
* **Enhancing Self-Evolution and Context-Awareness**: A key future direction is to overcome the hurdles related to memory expansion and management, allowing OS Agents to evolve sophisticated self-evolution mechanisms. Success in this area will enable agents to provide more personalized, dynamic, and context-aware assistance by learning and adapting continuously to the user’s needs and environment.
