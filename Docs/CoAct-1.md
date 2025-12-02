**# CoAct-1: Computer-using Agents with Coding as Actions**



**## What is the research/project about?**

This paper introduces CoAct-1, a novel multi-agent system designed for autonomous agents that operate computers. This system presents a robust and flexible paradigm by enabling agents to use coding as an enhanced action, synergistically combining conventional GUI-based control with direct programmatic execution.



**## What problem does it solve? (or what does it introduce?, or what is the main contribution?)**

Existing computer-using agents, which rely primarily on Graphical User Interfaces (GUIs), often struggle with efficiency and reliability when facing complex, long-horizon tasks. Workflows like complex data processing or file management that require intricate sequences of precise GUI manipulations are susceptible to failure due to visual grounding ambiguity and the high probability of error accumulation over a long action horizon.



This paper propose a hybrid approach that combines the intuitive, human-like strengths of GUI manipulation with the precision, reliability, and efficiency of direct system interaction through code. They introduce CoAct-1 (Computer-using Agent with Coding as Actions), a novel multi-agent system that is architected around three specialized agents: Orchestrator, Programmer, and GUI Operator. A high-level Orchestrator serves as the central planner, decomposing the user’s goal and assessing the nature of each subtask. Based on this analysis, it assigns the task to one of two distinct execution agents: a Programmer agent, which writes and executes Python or Bash scripts for backend operations like file management, data processing, or environment configuration; or a GUI Operator, a VLM-based agent that performs frontend actions like clicking buttons and navigating visual interfaces. This dynamic delegation allows CoAct-1 to strategically bypass inefficient GUI sequences in favor of robust, single-shot code execution where appropriate, while still leveraging visual interaction for tasks where it is indispensable.



**## What is its methodology?**

**### Multi-agent System Design for Computer Use**

**Orchestrator**: This part is central to the system, tasked with task decomposition and dynamic planning based on all previous observations. The Orchestrator cannot interact directly with the OS. Instead, it assigns a subtask to either the Programmer or the GUI Operator. Upon the completion of a subtask, the Orchestrator receives a summarization of the task-solving process and a screenshot reflecting the current system state, and it returns a termination signal when the overall task is complete.



**Programmer**: When the Orchestrator assigns a subtask to the Programmer, a new conversation is established between this coding agent and a code interpreter. The Programmer is required to solve the assigned subtask by generating Python or Bash scripts. This setup enables the Programmer to reflect on its generated code based on environmental feedback across multiple rounds. Once the code interpreter successfully retrieves the code, it sends it to the operating system (which might be a remote virtual machine) and subsequently returns the execution result, along with a screenshot, back to the conversation. Given that the coding agent is a language model with limited sequential image understanding, the Orchestrator is mandated to provide sufficient environmental context, such as currently opened windows, browser tabs, or inferred file paths, to the Programmer.



**GUI operator**: The GUI Operator functions as a vision-language action model capable of receiving a sequence of images and text instructions to generate GUI actions. When receiving a subtask, it establishes a conversation with a GUI action interpreter. The GUI action space includes fundamental computer operations such as mouse movement, mouse clicks, keyboard hotkeys, and keyboard typing. The GUI interpreter is a non-language model proxy agent that interprets the language model’s instructions as actual system operations and returns the resulting screenshot to the GUI agent. When the GUI agent successfully completes its task, it outputs a message, including any information the Orchestrator required it to collectz`, along with a termination signal to end its conversation.



**### Workflow and Memory Design**

CoAct-1 utilizes the instance conversation history as the memory for each of its agents. When the Programmer completes its assigned subtask, a language model summarizes the conversation between the coding agent and the code interpreter. This summary and a screenshot are then returned to the Orchestrator, where they are stored as part of the Orchestrator’s memory. Similarly, the GUI Operator returns a message containing the required information from the Orchestrator, along with a screenshot, which is also stored as part of the Orchestrator’s memory.



The Programmer, Orchestrator, and GUI Operator do not share their conversation history. Once the subtask is completed, the system will clean the instance conversation history of the Programmer and the GUI Operator, allowing them to focus solely on the current assigned subtask.



**### Model Settings**

They implement CoAct-1 using AG2. They tried different backbones for the Programmer and Orchestrator, including OpenAI o3 and o4-mini. For the GUI Operator, they use computer-use-preview, a vision-language action model finetuned by OpenAI for computer use, as the backbone model. They use the o4-mini as the summarizer for summarizing the conversation history between the Programmer and the Orchestrator.



**## What are the results?**

**### State-of-the-Art Success on OSWorld Benchmark**

CoAct-1 achieved a new state-of-the-art success rate of 60.76% on the challenging OSWorld benchmark (100+ steps), significantly surpassing leading prior methods like GTA-1 (53.10%). The system demonstrated robust performance across different maximum step allowances. 



The advantages of their hybrid approach are most evident in task categories that benefit from programmatic control. Similarly, major performance gains are observed in application-specific and OS-level tasks.



**### Enhanced Operational Efficiency via Reduced Action Steps**

The hybrid approach dramatically improved operational efficiency, solving successful tasks with an average of just 10.15 steps. This contrasts sharply with the average of 15.22 steps required by GTA-1 - a high-performing agents. By reducing the total number of steps, the hybrid approach not only accelerates task completion but also minimizes the opportunities for error. Coding actions were shown to be most frequently applied and beneficial in complex domains like LibreOffice Calc, Multi-Apps, and direct OS interactions.



**## What are the current challenges or limitations?**

**### High-level query**

These queries require the agent to infer the user's underlying intent and conceptual context that is not explicitly stated in the instructions. For instance, a Programmer agent failed a VSCode task because it could not make the conceptual link between a debugging console focus request and the required setting name, "focusEditorOnBrake," highlighting a limitation in the agent’s ability to reason about concepts that are not explicitly mentioned in the query.



**### Ambiguous query**

The system also faces challenges with ambiguous queries that omit critical information. In a case involving modifying VSCode settings to hide the "pycache" folder, the Programmer successfully identified the required action but incorrectly modified the workspace-specific settings instead of the global user settings. This failure illustrates the difficulty in correctly disambiguating the intended scope when the user request is vague.



**## What are the future directions?**

The success of CoAct-1 confirms that integrating coding as a core action offers a more powerful, efficient, and scalable approach toward generalized computer automation. The results endorse further development of systems that combine the strengths of precise, programmatic control with the versatility of GUI manipulation.



Future research should focus on optimizing the backbone models used for the specialized agents.

