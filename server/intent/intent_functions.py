# Dictionary Containing Intent and Action Functions
from typing import Callable

# Functions to handle intent and action
from actions.weather import get_weather


INTENT_FUNCTIONS = {
    "get_weather": get_weather,
    "open_app_or_web": None,
    "chat_response": None,
}


# Function that Returns the Action Function to run based on the intent
def get_intent_function(intent: str) -> Callable:
    return INTENT_FUNCTIONS.get(intent)
