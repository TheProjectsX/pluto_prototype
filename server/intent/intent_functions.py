# Dictionary Containing Intent and Action Functions
from typing import Callable
import importlib.util

# Intent Action Functions root folder
ACTION_ROOT = "actions"


# Function that Returns the Action Function to run based on the intent
def get_intent_function(intent: str) -> Callable:
    if not importlib.util.find_spec(f"{ACTION_ROOT}.{intent}"):
        return None

    module = importlib.import_module(f"{ACTION_ROOT}.{intent}")
    return getattr(module, f"get_{intent}")
