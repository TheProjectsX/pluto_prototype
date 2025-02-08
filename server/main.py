from utils.intents import get_intent


# Test Intent
while True:
    text = input("\n:> ")
    intentInfo = get_intent(text)

    if intentInfo["success"]:
        print("\nIntent:", intentInfo["intent"])
        print(
            "Entities:",
            ", ".join([x["name"] + " - " + x["value"] for x in intentInfo["entities"]]),
        )
    else:
        print("\nError:", intentInfo["error"])
