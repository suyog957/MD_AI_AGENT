Medical Diagnosis AI Agent System
This project creates an AI-based system designed to help provide insights into potential medical causes based on symptoms provided by users. It leverages an AI model for reasoning and a web search tool (DuckDuckGo) to fetch additional information from the internet. The system also encourages users to seek a professional medical consultation for an accurate diagnosis.

Table of Contents
Overview
Features
Installation
Usage
Code Explanation
Dependencies
Environment Variables
Contributing
License
Overview
The Medical Diagnosis AI Agent System consists of an AI agent that analyzes symptoms and provides potential medical causes. It uses a combination of:

A large language model (Groq or other AI models) for reasoning and diagnosing symptoms.
A web search tool (DuckDuckGo) to fetch additional medical information if necessary.
A team-based approach, where the primary medical agent can collaborate with other agents for additional insights.
This system is designed to assist in understanding possible causes for medical symptoms, but it is not a replacement for professional medical advice. Always consult with a healthcare provider for an accurate diagnosis.

Features
Symptom Analysis: Given a set of symptoms, the AI agent will provide possible medical causes.
Web Search for Additional Information: The agent can search the web for related medical news and research papers to offer more context.
Recommendation for Professional Consultation: The agent always recommends consulting a healthcare professional for a final diagnosis.
Customizable Models: The system allows you to change the AI model used for diagnosis (e.g., Groq, Llama).
Real-Time Responses: You can get real-time updates as the system processes the symptoms.
Installation
1. Clone the repository
Start by cloning the repository to your local machine. You can do this by running the command: git clone https://github.com/yourusername/medical-diagnosis-ai-agent.git Afterward, navigate into the project directory: cd medical-diagnosis-ai-agent

2. Install the dependencies
The project requires several Python libraries. To install them, use the following command: pip install -r requirements.txt

3. Set up environment variables
Create a .env file in the root of the project directory and add any necessary API keys or tokens for external services (such as AI models or web search tools). For example, the .env file might contain:

makefile
Copy code
DUCKDUCKGO_API_KEY=your_duckduckgo_api_key
GROQ_API_KEY=your_groq_api_key
If you do not have any external services requiring keys, you can skip this step.

4. Install any additional tools
If you're using a specific AI model or web search tool that requires installation, make sure those are set up as well.

Usage
1. Running the Medical Diagnosis Agent
Once the dependencies are installed and environment variables are configured, you can run the system by executing the following:

python main.py

This will start the system, which will create the medical agent and the agent team, then prompt it to analyze a sample set of symptoms.

2. Modify Symptoms
In the main.py file, you can modify the symptoms variable to test the agent with different sets of symptoms. For example, you can diagnose different symptoms such as:

symptoms = "headache, fever, running nose, cough"

Simply replace the symptoms with any others that you would like the agent to analyze.

3. View the Results
The agent will output possible medical causes for the symptoms you provided. It will also indicate when it is using DuckDuckGo for further web-based research. All responses are provided in a readable markdown format.

Note: The system always recommends consulting with a healthcare professional for an accurate diagnosis.

Code Explanation
1. create_medical_agent()
This function sets up a single medical agent. The agent is configured to:

Use a specific AI model (e.g., Groq).
Have the ability to search the web (using DuckDuckGo).
Follow specific instructions, such as asking clarifying questions and recommending professional consultation.
2. create_medical_agent_team()
This function creates a team of agents, which includes the individual medical agent. The team can work together to provide more accurate and detailed information, including searching for relevant news articles or research papers.

3. get_medical_causes()
This function takes a set of symptoms and asks the agent team to analyze and provide possible medical causes. The system processes the symptoms and uses the AI model to generate a list of possible conditions or causes for the symptoms.

4. main.py
This is the entry point of the program. It:

Creates the medical agent.
Forms the team of agents.
Executes the analysis of the provided symptoms.
Important Notes:
This system is not a substitute for professional medical advice.
The agent provides suggestions based on AI analysis and available information from the internet but cannot replace a diagnosis from a healthcare provider.
Dependencies
The following Python libraries are required:

phi: The framework for creating agents and using models like Groq.
dotenv: Used to securely load environment variables from a .env file.
requests (or another HTTP client): If you're making web requests for additional research.
duckduckgo-search: A simple Python interface to DuckDuckGo's search engine (for web searches).
markdown: To format the output responses in a human-readable markdown format.
These dependencies can be installed with the command: pip install -r requirements.txt

Environment Variables
Some services (like Groq or DuckDuckGo) may require API keys or other configuration. You can store these in a .env file, which should not be committed to source control (it should be included in .gitignore).

Here’s an example .env file:

makefile
Copy code
DUCKDUCKGO_API_KEY=your_duckduckgo_api_key
GROQ_API_KEY=your_groq_api_key
Make sure to update this file with the appropriate API keys if you're using paid services.

