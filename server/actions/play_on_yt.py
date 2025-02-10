import requests


# Get Video URL from Video Topic
def get_video_url_from_topic(video_topic: str) -> str:
    """Will play video on following topic, takes a
    bout 10 to 15 seconds to load"""
    url = "https://www.youtube.com/results?q=" + video_topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            break
    if lst[count - 5] == "/results":
        return None

    return "https://www.youtube.com" + lst[count - 5]


# Function parses YouTube video URL from Video Topic and returns it to play on YouTube
def get_play_on_yt(properties: dict = {}) -> list[dict]:
    video_topic = None

    for entity in properties.get("entities", []):
        if entity["name"] == "video_topic":
            video_topic: str = entity["value"]
            break

    if not video_topic:
        sliced_text: str = (
            properties.get("text", "")
            .replace("play", "")
            .replace("on youtube", "")
            .replace("show on youtube")
            .strip()
        )

        if len(sliced_text) < 5:
            return [{"key": "SPEAK", "text": "Sir, Video Topic isn't Detected"}]
        else:
            video_topic: str = sliced_text

    video_url: str = get_video_url_from_topic(video_topic)

    if video_url is None:
        return [{"key": "SPEAK", "text": "Sir, Video URL not found"}]

    return_response = [
        {"key": "SPEAK", "text": "Opening YouTube"},
        {
            "key": "EXEC",
            "exec": f"""import webbrowser\nwebbrowser.open("{video_url}")""",
        },
    ]

    return return_response
