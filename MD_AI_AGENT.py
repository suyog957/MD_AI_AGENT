# Import the necessary libraries. These libraries help us build and run the AI-based medical agent.
from phi.agent import Agent  # Used to create AI agents that can interact and perform tasks.
from phi.model.groq import Groq  # This is the model we use to perform AI tasks, like understanding medical symptoms.
from phi.tools.duckduckgo import DuckDuckGo  # We use DuckDuckGo to search for additional information on the internet if needed.
from dotenv import load_dotenv  # This helps us securely load sensitive information like API keys from a .env file.

# Load environment variables (like keys or tokens stored securely) from a file called .env.
load_dotenv()

# This function creates a "Medical Agent" that can diagnose based on symptoms.
def create_medical_agent(model: str = "llama-3.3-70b-versatile"):
    """
    This function creates an AI agent designed to help diagnose based on symptoms.
    The agent uses a machine learning model and can also search for extra information online.
    """
    return Agent(
        name="Medical Agent",  # This is the name of the agent.
        
        # Here we specify which AI model the agent should use for reasoning and diagnosis.
        # The Groq model is set with a specific version of the model (you can change the model if needed).
        model=Groq(id=model),  
        
        # The tools the agent can use. Here, DuckDuckGo is the tool we use to search the internet for extra information.
        tools=[DuckDuckGo()],
        
        # Instructions tell the agent how to behave when helping with medical diagnosis.
        instructions=[
            "Ask clarifying questions if needed to understand symptoms",  # The agent should ask for more details if it is unsure.
            "Provide possible medical causes for given symptoms",  # The agent should give a list of potential medical issues.
            "Always mention if a professional medical consultation is recommended",  # Always recommend seeing a doctor.
            "Ensure accuracy and responsibility in responses"  # The agent should be careful and reliable.
        ],
        
        # Set this to True so we can see when the agent is using its tools (like searching online).
        show_tool_calls=True,
        
        # Set this to True so the agent can provide responses in markdown format, which is a readable style.
        markdown=True
    )

# This function creates a "team" of agents, which includes the medical agent and other tools.
def create_medical_agent_team(medical_agent, model: str = "llama-3.3-70b-versatile"):
    """
    This function sets up a team of agents. The team includes the Medical Agent and possibly additional AI models or tools.
    """
    return Agent(
        # We again specify the AI model the whole team will use. This ensures the team uses the same model for tasks.
        model=Groq(id=model),  
        
        # This is where we specify that the team includes the medical agent we just created.
        team=[medical_agent],
        
        # Instructions for the team on what they should do when working together.
        instructions=[
            "Provide possible causes for symptoms",  # The team should provide possible reasons for the symptoms.
            "If needed, fetch related medical news or research papers",  # The team can search for relevant research or news articles.
            "Ensure information is based on credible sources and is up-to-date",  # Ensure the information is trustworthy and current.
            "Suggest seeing a healthcare provider for an accurate diagnosis"  # Always recommend seeing a doctor.
        ],
        
        # Set this to True to see when the team is using tools (like searching for research papers).
        show_tool_calls=True,
        
        # Set this to True so the team's response is in markdown format (for readability).
        markdown=True
    )

# This function asks the medical agent team to analyze the symptoms and provide potential medical causes.
def get_medical_causes(agent_team, symptoms: str):
    """
    This function takes a set of symptoms and asks the AI agent team to provide possible medical causes for those symptoms.
    The agent can also search the internet for additional information if needed.
    """
    prompt = f"Based on the following symptoms, provide possible medical causes: {symptoms}"
    # Here we call the agent team to process the symptoms and give a response.
    # The `stream=True` option ensures we get updates in real-time as the agent works.
    agent_team.print_response(prompt, stream=True)

# Main entry point of the program. This is where the code starts running.
if __name__ == "__main__":
    """
    This part of the code is the starting point of the program. It will create the agents and make them work together
    to diagnose symptoms based on the input provided.
    """
    
    # Create the individual medical agent by calling the function `create_medical_agent`.
    medical_agent = create_medical_agent()

    # Create the team of agents by calling the `create_medical_agent_team` function.
    # This includes the medical agent we just created.
    agent_team = create_medical_agent_team(medical_agent)

    # Example task: Let's test the agent by providing it with a set of symptoms.
    symptoms = "itchy skin, nausea, abdomen pain"  # These are the symptoms we want the agent to analyze.

    # Ask the agent team to provide possible medical causes for the given symptoms.
    get_medical_causes(agent_team, symptoms)

    # You can change the symptoms to test different cases, e.g.:
    # symptoms = "headache, fever, running nose, cough"  # Another set of symptoms.
    # get_medical_causes(agent_team, symptoms)
