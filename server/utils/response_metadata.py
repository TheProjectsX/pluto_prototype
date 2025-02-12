# This file Contains the Response Codes and Commands need to Send to the Client

RESPONSE_CODES = {"SPEAK": 0, "EXEC": 1, "FUNC": 2}

RESPONSE_COMMANDS = {
    "SPEAK": "assistant_speak",
    "EXEC": "assistant_execute",
    "FUNC": "assistant_run_func",
}


EXCLUDE_RESPONSE_KEYS = ["key", "perform"]
