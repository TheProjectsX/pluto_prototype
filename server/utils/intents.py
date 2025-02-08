from wit import Wit
from dotenv import load_dotenv
from typing import TypedDict
import os

# Load the .env file
load_dotenv()

# Create Wit Client
client = Wit(os.getenv("WIT_ACCESS_TOKEN"))


# Types for IDE
class EntityInfo(TypedDict):
    name: str
    value: str


class IntentInfo(TypedDict):
    success: bool
    error: str
    intent: str
    entities: EntityInfo


# Get intent from text
def get_intent(text: str) -> IntentInfo:
    try:
        response = client.message(text)
    except Exception as e:
        return {"success": False, "error": str(e), "intent": "", "entities": []}

    if len(response.get("intents", [])) == 0:
        return {"success": True, "intent": "chat_response", "entities": []}

    intent = response.get("intents", [{}])[0].get("name")
    entities = []

    for key in response.get("entities", {}).keys():
        obj = response.get("entities").get(key)
        for entity in obj:
            name = entity.get("role")
            value = entity.get("body")

            entities.append({"name": name, "value": value})

    return {"success": True, "intent": intent, "entities": entities}
