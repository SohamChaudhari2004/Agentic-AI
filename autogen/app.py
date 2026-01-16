import os
import asyncio
import logging  # Add logging module
import time  # Add time module for retry mechanism
from typing import List, Dict, Any
from xml.parsers.expat import model
from langchain_mistralai import ChatMistralAI
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat, Swarm
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from functools import lru_cache
import traceback  # new import for richer logging
from groq import Groq
from datetime import datetime  # Add datetime for timestamping files

# asyncio.Semaphore(3)

# change to selectorGroupchat or Groupchat and Groupchatmanager
load_dotenv()
# Initialize the language model client
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise EnvironmentError("❌ MISTRAL_API_KEY environment variable is not set.")
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise EnvironmentError("❌ GEMINI_API_KEY environment variable is not set.")  # <-- added validation

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )
# completion = client.chat.completions.create(
    
#     model="openai/gpt-oss-120b",
#     messages=[
#       {
#         "role": "user",
#         "content": ""
#       }
#     ],
#     temperature=1,
#     max_completion_tokens=9361,
#     top_p=1,
#     reasoning_effort="medium",
#     stream=True,
#     stop=None,
#     tools=[{"type":"browser_search"}]
# )


Gemini_client = OpenAIChatCompletionClient(
    api_key=gemini_api_key,
    model='gemini-2.5-flash'
)



# Mistral_client = OpenAIChatCompletionClient(
#     api_key=mistral_api_key,
#     model= 'mistral-large-latest'

# )

# llm = ChatMistralAI(
#     api_key= mistral_api_key,
#     model_name ="mistral-large-latest",
#     temperature=0.7
# )

# Mock the model_info attribute to ensure compatibility
# llm.model_info = {"vision": False}  # Add this line

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")



async def create_travel_agent_system():
    """Creates a travel agent system with multiple specialized agents."""
    logging.info("Initializing travel agent system...")
    gemini_client = Gemini_client
    # mistral_client = Mistral_client

    # Define agents with their respective roles
    logging.info("\n=============================================")
    logging.info("Creating DestinationExpert agent...")
    logging.info("=============================================\n")
    destination_agent = AssistantAgent(
        name="DestinationExpert",
        model_client=gemini_client,
        tools=[],
        system_message="""You are a destination expert specializing in travel recommendations. 
        Analyze user preferences (budget, interests, travel dates, group size) and suggest 
        3-5 ideal destinations with detailed reasoning. Consider factors like:
        - Weather and seasonality
        - Cultural attractions and activities
        - Budget compatibility
        - Safety and accessibility
        Provide specific destination recommendations with brief descriptions."""
    )
    logging.info("\n=============================================\n")
    logging.info("Creating ItineraryPlanner agent...")
    logging.info("\n=============================================\n")

    itinerary_agent = AssistantAgent(
        name="ItineraryPlanner",
        model_client=gemini_client,
        system_message="""You are an expert itinerary planner. Based on the chosen destination,
        create a detailed day-by-day itinerary including:
        - Must-see attractions and landmarks
        - Recommended restaurants and local cuisine
        - Transportation between locations
        - Estimated time for each activity
        - Alternative options for different weather conditions
        Format your response as a structured daily schedule."""
    )
    logging.info("=============================================")
    logging.info("Creating BudgetAnalyst agent...")
    logging.info("=============================================")
    budget_agent = AssistantAgent(
        name="BudgetAnalyst",
        model_client=gemini_client,
        system_message="""You are a travel budget specialist. Calculate comprehensive trip costs including:
        - Flight estimates (provide ranges for economy/business class)
        - Accommodation options (budget/mid-range/luxury)
        - Daily food and dining expenses
        - Transportation costs (local transport, car rentals, etc.)
        - Activity and attraction fees
        - Emergency fund recommendations
        Provide detailed budget breakdowns with money-saving tips."""
    )
    logging.info("\n=============================================")   
    logging.info("Creating TravelLogistics agent...")
    logging.info("=============================================\n")
    logistics_agent = AssistantAgent(
        name="TravelLogistics",
        model_client=gemini_client,
        system_message="""You are a travel logistics coordinator. Handle practical travel arrangements:
        - Visa requirements and documentation
        - Vaccination and health recommendations
        - Travel insurance suggestions
        - Packing recommendations based on destination and season
        - Time zone and currency information
        - Emergency contacts and local customs
        Provide actionable logistics checklist."""
    )
    logging.info("\n=============================================")   
    logging.info("Creating ReportCompiler agent...")
    logging.info("=============================================\n")
    report_agent = AssistantAgent(
        name="ReportCompiler",
        model_client=gemini_client,
        system_message="""You are a travel report compiler. Synthesize all agent inputs into 
        a comprehensive, well-formatted travel plan including:
        - Executive summary of the recommended trip
        - Complete itinerary with all details
        - Comprehensive budget breakdown
        - Logistics checklist and important notes
        - Contact information and emergency procedures
        Format as a professional travel document ready for the traveler."""
    )

    # Create a group chat with round-robin coordination
    logging.info("\n=============================================")
    logging.info("Creating RoundRobinGroupChat with all agents...")
    logging.info("==============================================\n")

    
    # travel_team = SelectorGroupChat(
    #     name="TravelPlanningTeam",
    #     max_selector_attempts=5,
    #     model_client=gemini_client,
    #     description="Group chat for travel planning agents. Choose only the necessary agents based on the user query and keep the response limited to the user query." \
    #     " Once there is no need to involve additional agents, the conversation should be ended with the one of the flags [final answer, task_complete, satisfied]." \
    #     " NO JARGON." \
    #     "NO PREAMBLE",
    #     participants=[
    #         destination_agent,
    #         itinerary_agent,
    #         budget_agent,
    #         logistics_agent,
    #         report_agent
    #     ]

    # )

    travel_team = RoundRobinGroupChat(
        name="TravelPlanningTeam",
        participants=[
            destination_agent,
            itinerary_agent,
            budget_agent,
            logistics_agent,
            report_agent
        ],
        max_turns=5  # One turn per agent (5 agents)
    )
    #     " Once there is no need to involve additional agents, the conversation should be ended with the one of the flags [final answer, task_complete, satisfied]." \
    #     " NO JARGON." \
    #     "NO PREAMBLE",
    #     participants=[
    #         destination_agent,
    #         itinerary_agent,
    #         budget_agent,
    #         logistics_agent,
    #         report_agent
    #     ]

    # )

    logging.info("=============================================")
    logging.info("Travel agent system initialized successfully.")
    logging.info("=============================================")
    return travel_team

async def call_with_retries(func, *args, retries=5, backoff_factor=2, **kwargs):
    """Retries a coroutine function with exponential backoff using asyncio.sleep."""
    attempt = 0
    while attempt < retries:
        try:
            return await func(*args, **kwargs)
        except asyncio.CancelledError:
            # Re-raise cancellation immediately - don't retry
            logging.warning("Operation was cancelled by user (Ctrl+C)")
            raise
        except Exception as e:
            # log full traceback for diagnostics
            logging.warning(f"Attempt {attempt + 1}/{retries} failed with: {e}")
            logging.debug(traceback.format_exc())
            err_str = str(e).lower()
            # retry on rate limits, transient network issues, 503 service unavailable
            if any(keyword in err_str for keyword in ["ratelimit", "rate limit", "timeout", "temporar", "503", "service unavailable", "overloaded"]):
                wait_time = backoff_factor ** attempt
                logging.warning(f"Transient error detected. Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
                attempt += 1
                continue
            # for other errors, re-raise to avoid silent swallowing
            raise
    logging.error("Max retries reached. Unable to complete the request.")
    raise RuntimeError("Max retries reached. Please check your API usage and limits.")

async def plan_travel(travel_request: str):
    """Main function to handle travel planning requests."""
    try:
        logging.info("Starting travel planning process...")
        # Create the travel agent system
        travel_system = await create_travel_agent_system()

        # Enhanced travel planning prompt
        logging.info("Sending travel request to the agent system...")
        enhanced_prompt = f"""
        TRAVEL PLANNING REQUEST: {travel_request}

        Please work together as a travel planning team to create a comprehensive travel plan.

        WORKFLOW:
        1. DestinationExpert: Analyze the request and recommend suitable destinations
        2. ItineraryPlanner: Create detailed day-by-day itinerary for the top recommendation
        3. BudgetAnalyst: Provide comprehensive cost analysis and budget breakdown
        4. TravelLogistics: Handle all practical arrangements and requirements
        5. ReportCompiler: Synthesize everything into a final comprehensive travel report

        Each agent should build upon the previous agent's work and reference specific details.
        """

        # Execute the travel planning workflow with retries
        logging.info("Calling travel_system.run with retries...")
        result = await call_with_retries(travel_system.run, task=enhanced_prompt, retries=3)

        # Defensive validation of result
        if result is None:
            logging.error("Received None result from travel system.")
            raise RuntimeError("Travel system returned no result. Check API keys and network.")
        # common shape: object with .messages list or direct string
        if hasattr(result, "messages"):
            msgs = getattr(result, "messages")
            if not msgs:
                logging.error("Result contains empty messages.")
                raise RuntimeError("Travel system returned empty messages.")
        logging.info("Travel planning process completed successfully.")
        return result

    except Exception as e:
        logging.error(f"Error during travel planning: {str(e)}")
        logging.debug(traceback.format_exc())
        raise RuntimeError(f"❌ Error during travel planning: {str(e)}")

def save_output_to_file(content: str, output_dir: str = "d:\\AIML\\Research\\autogen\\outputs") -> str:
    """Save the travel plan output to a text file with timestamp."""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"travel_plan_{timestamp}.txt"
        filepath = os.path.join(output_dir, filename)
        
        # Write content to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logging.info(f"✅ Travel plan saved to: {filepath}")
        return filepath
    except Exception as e:
        logging.error(f"❌ Error saving output to file: {str(e)}")
        logging.debug(traceback.format_exc())
        raise

# Example usage
async def main():
    travel_request = """
    I want to plan a 10-day itinerary for travel and stay in Udupi, India under Rs. 10000
    """

    try:
        travel_plan = await plan_travel(travel_request)
        
        # Extract content from travel_plan
        content_to_save = None
        
        # Safely print the final assistant message content if available
        if travel_plan is None:
            print("No travel plan was returned.")
        elif hasattr(travel_plan, "messages"):
            msgs = travel_plan.messages
            # handle Pydantic-like wrappers where messages might be a list or other container
            if isinstance(msgs, (list, tuple)) and len(msgs) > 0:
                last = msgs[-1]
                # some frameworks wrap content differently; attempt multiple access patterns
                content = getattr(last, "content", None) or (last.get("content") if isinstance(last, dict) else None)
                content_to_save = content if content is not None else repr(last)
                print(content_to_save)
            else:
                content_to_save = repr(travel_plan)
                print(content_to_save)
        else:
            # fallback: pretty-print whatever the run returned
            content_to_save = repr(travel_plan)
            print(content_to_save)
        
        # Save to file if we have content
        if content_to_save:
            saved_file = save_output_to_file(content_to_save)
            print(f"\n📄 Output saved to: {saved_file}")
        else:
            logging.warning("No content available to save to file.")
            
    except KeyboardInterrupt:
        logging.warning("\n⚠️  Process interrupted by user (Ctrl+C)")
        print("\n⚠️  Travel planning was interrupted. Please try again.")
    except Exception as e:
        logging.error(f"❌ Error occurred: {str(e)}")
        logging.debug(traceback.format_exc())
        print(f"\n❌ Error: {str(e)}")
        print("Please check:")
        print("  1. Your GEMINI_API_KEY is valid and has available quota")
        print("  2. Your internet connection is stable")
        print("  3. Google's Gemini API service is available (not experiencing outages)")

# Run the travel planning system
if __name__ == "__main__":
    asyncio.run(main())

