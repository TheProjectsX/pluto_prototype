# Function returns Response for shutdown_pc intent
def get_shutdown_pc(properties: dict = {}):
    return_response = [
        {"key": "SPEAK", "text": "Closing the PC, sir"},
        {"key": "EXEC", "exec": f"""import os\nos.system("shutdown /s /t 0")"""},
    ]

    return return_response
