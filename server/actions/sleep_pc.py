# Function returns Response for sleep_pc intent
def get_sleep_pc(properties: dict = {}):
    return_response = [
        {"key": "SPEAK", "text": "Putting PC to sleep!"},
        {
            "key": "EXEC",
            "exec": f"""import os\nos.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")""",
        },
    ]

    return return_response
