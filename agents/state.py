from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

class Agentstate(TypedDict):
    message: Annotated[list,add_messages]