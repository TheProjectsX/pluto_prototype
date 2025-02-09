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
def run_intent_function(intent_function: Callable, entities: list[dict]) -> dict:
    """Run an intent function with the given entities."""
    try:
        intent_function_response = intent_function(entities)
    except Exception as e:
        return {
            "response_code": RESPONSE_CODES.get("SPEAK"),
            "command": RESPONSE_COMMANDS.get("SPEAK"),
            "text": "Sorry sir, An Error Occurred during the execution of your Command",
            "error": str(e),
        }

    if intent_function_response.get("perform") == "text_processing":
        intent_function_response["text"] = format_response(
            intent_function_response.get("text")
        )

    return {
        "response_code": RESPONSE_CODES.get(intent_function_response.get("key")),
        "command": RESPONSE_COMMANDS.get(intent_function_response.get("key")),
        **{
            k: v
            for k, v in intent_function_response.items()
            if k not in EXCLUDE_RESPONSE_KEYS
        },
    }


while True:
    text = input("\n:> ")
    if text == "exit":
        break

    intentInfo = get_intent(text)
    if not intentInfo.get("success"):
        print("\nError:", intentInfo.get("message"))

    intent_function = get_intent_function(intent=intentInfo.get("intent"))
    if not intent_function:
        print(f"\nError: {intentInfo.get("intent")} Intent Function not Found!")

    intent_function_response = run_intent_function(
        intent_function, intentInfo.get("entities")
    )

    print("\nIntent Response:", intent_function_response)

# Test Intent
# while True:
#     text = input("\n:> ")
#     intentInfo = get_intent(text)

#     if intentInfo["success"]:
#         print("\nIntent:", intentInfo["intent"])
#         print(
#             "Entities:",
#             ", ".join([x["name"] + " - " + x["value"] for x in intentInfo["entities"]]),
#         )
#     else:
#         print("\nError:", intentInfo["error"])
