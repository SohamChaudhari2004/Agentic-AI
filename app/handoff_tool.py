from typing import Annotated
from langchain_core.tools import tool , InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from langgraph.graph import MessagesState
from langgraph.types import Send

def create_tast_description_handoff_tool(*, agent_name: str, description: str | None = None):
    name = f"transfer_to_{agent_name}"
    description = description or f"Ask {agent_name} for help"

    @tool(name , description=description)
    def handoff_tool(
        task_description : Annotated[
            str,
            "This is the description of what the next agent should do , including all the relevant context"
        ],
        state: Annotated[MessagesState , InjectedState]
    ) -> Command:
        task_description_message = {"role": "user" , "content" : task_description}
        agent_input = {**state , "messages" : [task_description_message]}
        return Command(
            goto= [ Send(agent_name, agent_input)],
            graph = Command.PARENT
        )

    return handoff_tool


