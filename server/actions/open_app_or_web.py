from .data.app_launchers import PC_LAUNCHERS, MOBILE_LAUNCHERS


# Function to Return Commands to Open App / Website
def get_open_app_or_web(entities: list, platform="pc") -> dict:
    app_or_web = None

    for entity in entities:
        if entity.get("name") == "app_or_web":
            app_or_web = entity.get("value")

    if (not app_or_web) or (app_or_web.lower() not in PC_LAUNCHERS.keys()):
        return {"command": None}

    if platform == "pc":
        launch_code = PC_LAUNCHERS[app_or_web.lower()]
        exec_code = (
            f"""import subprocess\nsubprocess.Popen(["{launch_code}"], shell=True)"""
        )
    elif platform == "android":
        launch_code = MOBILE_LAUNCHERS[app_or_web.lower()]
        exec_code = f"""import os\nos.system("am start -n {launch_code}")"""

    return_response = [
        {
            "key": "SPEAK",
            "text": "Opening " + app_or_web + " ...",
        },
        {"key": "EXEC", "exec": exec_code},
    ]

    return return_response
