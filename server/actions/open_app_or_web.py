from .data.launchers import PC_APP_LAUNCHERS, MOBILE_APP_LAUNCHERS, WEBSITE_URLS


# Function to Return Commands to Open App / Website
def get_open_app_or_web(properties: dict = {}) -> list[dict]:
    app_or_web: list = []

    for entity in properties.get("entities", []):
        if entity.get("name") == "app_or_web":
            app_or_web.append(entity.get("value"))

    if (not app_or_web) or (
        not any([x.lower() not in PC_APP_LAUNCHERS.keys() for x in app_or_web])
        and not any([x.lower() not in WEBSITE_URLS.keys() for x in app_or_web])
        and not any([x.lower() not in MOBILE_APP_LAUNCHERS.keys() for x in app_or_web])
    ):
        return [
            {
                "key": "SPEAK",
                "text": "Sorry Sir, Asked Software or Website is not in my Database",
            }
        ]

    if properties.get("platform", "pc") == "pc":
        app_launch_codes = [PC_APP_LAUNCHERS.get(x.lower()) for x in app_or_web]
        web_launch_codes = [WEBSITE_URLS.get(x.lower()) for x in app_or_web]

        exec_code: str = ""
        if any(app_launch_codes):
            exec_code += f"""import subprocess\n{"\n".join([f"subprocess.Popen(['{x}'], shell=True)" for x in app_launch_codes if x])}\n"""

        if any(web_launch_codes):
            exec_code += f"""import webbrowser\n{"\n".join([f"webbrowser.open('{x}')" for x in web_launch_codes if x])}"""

    elif properties.get("platform", "pc") == "android":
        launch_code = MOBILE_APP_LAUNCHERS.get(app_or_web[0].lower())
        exec_code = f"""import os\nos.system("am start -n {launch_code}")"""

    return_response = [
        {
            "key": "SPEAK",
            "text": "Launching...",
        },
        {"key": "EXEC", "exec": exec_code},
    ]

    return return_response
