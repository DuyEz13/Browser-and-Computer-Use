**# ScreenAgent : A Vision Language Model-driven Computer Control Agent**



**## What is the research/project about?**

The paper introduces ScreenAgent, a novel Vision Language Model (VLM) designed as a computer control agent capable of interacting with a real computer screen.



**## The main contributions**

Present a Reinforcement Learning (RL) environment that enables the VLM agent to directly interact with a real computer screen via VNC protocol. By observing the screenshot, their agent can interact with the GUI through basic mouse and keyboard operations.



Develop an automated pipeline that encompasses the planning phase, acting phase, and reflecting phase. This integrated pipeline facilitates the agent’s continuous interaction with the environment, distinguishing their agent from others.



Propose the ScreenAgent dataset, which includes action sequences for completing generic tasks on Linux and Windows desktops. They also provide a finegrained scoring metric to comprehensively evaluate the various capabilities that are necessary for a VLM agent in computer-controlling tasks.



They test GPT-4V and two state-of-the-art open-source VLMs on their test set. The results demonstrate that GPT-4V is capable of controlling computers, but it lacks precise positioning capabilities. They thus trained a ScreenAgent to enable precise positioning and achieved comparable results to GPT-4V in all aspects. Their work can facilitate further research on building a generalist agent.



**## What is its methodology?**

**### Framework**

They construct Reinforcement Learning (RL) environment that uses function calls to execute defined mouse and keyboard actions on a desktop operating system via VNC.



To guide the agent to continually interact with the environment and complete multi-step complex tasks, they design a control pipeline including the Planning, Acting, and Reflecting phases. The pipeline will ask the agent to disassemble the complex task, execute subtasks, and evaluate execution results. The agent will have the opportunity to retry some subtasks or adjust previously established plans to accommodate the current occurrences. Starting with the Planning Phase where the agent decomposes the overall complex task into subtasks based on the current screen state, and then in the Acting Phase the agent generates low-level mouse or keyboard operations in JSON-style function calls. And the Reflecting Phase enables the agent to autonomously assess the execution status of the current action based on the after-action screen, deciding whether to retry the current subtask, proceed, or reformulate the plan.



**### ScreenAgent Dataset \& CC-Score**

The dataset was created using an interactive annotation process on Linux and Windows operating systems to provide action sequences for completing generic tasks, filling a gap left by datasets typically focused on web browsing or Android. The dataset covers a wide range of daily computer usage scenarios, encompassing 39 sub-task categories across 6 themes, utilizing 273 complete task sessions (with 203 for training). Statistical analysis indicates that Mouse actions comprise the majority of recorded control actions.



The CC-Score is a fine-grained evaluation metric designed to comprehensively assess the agent's computer-controlling capability by measuring the similarity of control action sequences. This score considers both the sequential order and the attribution of actions, employing specific metrics for every action type and utilizing an alignment algorithm to find the maximal matching pairs while maintaining sequence integrity.





**## What are the results?**

ScreenAgent achieved computer control capabilities comparable to GPT-4V in overall performance metrics (CC-Score), with GPT-4V achieving 0.63 and ScreenAgent achieving 0.61 on the test set. Fine-tuning the ScreenAgent model also allowed it to reach the same level as GPT-4V in following instructions and making successful function calls.



ScreenAgent notably surpassed existing state-of-the-art models, including GPT-4V, in the precision of mouse clicking (Mouse Position Accuracy). The vision fine-tuning effectively enhanced ScreenAgent's precise positioning capabilities, a crucial skill where GPT-4V often refused to give precise coordinate results or failed to output them correctly.



**## What are the current challenges or limitations?**

A significant challenge is the insufficient accuracy of all tested models in the reflection phase. For instance, GPT-4V achieved only a 0.60 F1 score in determining whether a subtask has been completed or if adjustments are necessary, implying that human intervention is still required during continuous task execution.



Due to the input restrictions of VLM, their model can only process single-frame images, not videos or multi-frame images. The VLM’s language capability is limited by the abilities of its foundation language model. They also found that even GPT-4V has limited support for non English text on the screen.



**## What are the future directions?**

The work aims to inspire further research in building more powerful and generalized VLM agents capable of seamlessly assisting humans with digital tasks.



Future research should focus on improving areas where the current model lags, such as enhancing task planning abilities (where GPT-4V demonstrated superiority over ScreenAgent), and boosting the robustness of the reflection phase to facilitate truly autonomous and continuous interactive processes.

