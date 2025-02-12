# Below Function is used to get the response of take_screenshot Intent. It does not support Android at this moment
def get_take_screenshot(properties: dict = {}):
    if properties.get("platform", "pc") == "pc":
        from datetime import datetime

        filename = f"C:/Users/User/Pictures/Screenshots/Screenshot {datetime.now().strftime('%Y-%m-%d %H%M%S')}.png"

        # Regular ScreenShot
        return_response = [
            {"key": "SPEAK", "text": "Taking ScreenShot"},
            {
                "key": "EXEC",
                "exec": f"""import pyautogui\nss=pyautogui.screenshot('{filename}')""",
            },
        ]
    elif properties.get("platform", "pc") == "android":
        return_response = [
            {
                "key": "SPEAK",
                "text": "Sorry Sir, Taking ScreenShot in Mobile device is not Implemented Yet!",
            }
        ]

    return return_response
