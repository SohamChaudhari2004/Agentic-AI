from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import DiGraphBuilder, GraphFlow
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Create an OpenAI model client
client = OpenAIChatCompletionClient(
    api_key=gemini_api_key,
    model= 'gemini-2.5-flash',
    model_info={
        'family': 'gemini-2.5-flash', 
        'vision' : False,
        'function_calling': True,
        'json_output' : True,
        'multiple_system_messages': True,
        'structured_output': True
    }
)

# Create the writer agent
writer = AssistantAgent("writer", model_client=client, system_message="Draft a short paragraph on climate change.")

# Create the reviewer agent
reviewer = AssistantAgent("reviewer", model_client=client, system_message="Review the draft and suggest improvements.")

# Build the graph
builder = DiGraphBuilder()
builder.add_node(writer).add_node(reviewer)
builder.add_edge(writer, reviewer)

# Build and validate the graph
graph = builder.build()

# Create the flow
flow = GraphFlow([writer, reviewer], graph=graph)

task = 'write a short blog on impact of reinforcement learning and AI on Finance applications'

    
print(asyncio.run(flow.run(task=task)))

