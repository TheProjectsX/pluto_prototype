from .data.launchers import PC_APP_LAUNCHERS, MOBILE_LAUNCHERS, WEBSITE_URLS


# Function to Return Commands to Open App / Website
def get_open_app_or_web(properties: dict = {}) -> list[dict]:
    app_or_web = None

    for entity in properties.get("entities", []):
        if entity.get("name") == "app_or_web":
            app_or_web: str = entity.get("value")

    if (not app_or_web) or (app_or_web.lower() not in PC_APP_LAUNCHERS.keys()):
        return {"command": None}

    if properties.get("platform", "pc") == "pc":
        launch_code = PC_APP_LAUNCHERS.get(app_or_web.lower())
        if launch_code:
            exec_code = f"""import subprocess\nsubprocess.Popen(["{launch_code}"], shell=True)"""
        else:
            launch_code = WEBSITE_URLS.get(app_or_web.lower().replace(" ", ""))
            exec_code = f"""import webbrowser\nwebbrowser.open({launch_code})"""

    elif properties.get("platform", "pc") == "android":
        launch_code = MOBILE_LAUNCHERS.get(app_or_web.lower())
        exec_code = f"""import os\nos.system("am start -n {launch_code}")"""

    return_response = [
        {
            "key": "SPEAK",
            "text": "Opening " + app_or_web + " ...",
        },
        {"key": "EXEC", "exec": exec_code},
    ]

    return return_response
