# This file Contains the Response Codes and Commands need to Send to the Client

RESPONSE_CODES = {"SPEAK": 0, "EXEC": 1, "EXECNSPEAK": 10}

RESPONSE_COMMANDS = {
    "SPEAK": "assistant_speak",
    "EXEC": "assistant_execute",
    "EXECNSPEAK": "assistant_execute_n_speak",
}


EXCLUDE_RESPONSE_KEYS = ["key", "perform"]
