from typing import Callable
from intent.intents import get_intent
from intent.intent_functions import get_intent_function
from utils.response_metadata import (
    RESPONSE_CODES,
    RESPONSE_COMMANDS,
    EXCLUDE_RESPONSE_KEYS,
)
from utils.text_processing import format_response


# Intent Function Runner
def run_intent_function(intent_function: Callable, properties: dict) -> list:
    """Run an intent function with the given entities."""
    try:
        intent_function_response: list[dict] = intent_function(properties)
    except Exception as e:
        return [
            {
                "response_code": RESPONSE_CODES.get("SPEAK"),
                "command": RESPONSE_COMMANDS.get("SPEAK"),
                "text": "Sorry sir, An Error Occurred during the execution of your Command",
                "error": str(e),
            }
        ]

    return_response: list[dict] = []

    for response in intent_function_response:
        if response.get("perform") == "text_processing":
            response["text"] = format_response(response.get("text"))

        return_response.append(
            {
                "response_code": RESPONSE_CODES.get(response.get("key")),
                "command": RESPONSE_COMMANDS.get(response.get("key")),
                **{k: v for k, v in response.items() if k not in EXCLUDE_RESPONSE_KEYS},
            }
        )

    return return_response


while True:
    text = input("\n:> ")
    if text == "exit":
        break
    elif text.strip() == "":
        continue

    intentInfo = get_intent(text)
    if not intentInfo.get("success"):
        print("\nError:", intentInfo.get("message"))

    intent_function = get_intent_function(intent=intentInfo.get("intent"))
    if not intent_function:
        print(f"\nError: {intentInfo.get("intent")} Intent Function not Found!")

    intent_function_response: list[dict] = run_intent_function(
        intent_function, intentInfo
    )

    for response in intent_function_response:
        print("\nIntent Response:", response)
