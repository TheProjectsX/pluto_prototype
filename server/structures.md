## Intents List

-   weather
-   open_app_or_web
-   chat_response [!]

## Action Functions

-   Intent's Action Function's file has the same name as intent (ex: Intent `weather` > `weather.py`)
-   The main Function of that Intent's Action contains almost same name as the Intent but contains a `get_` suffix (ex: Intent `weather` > `weather.py` > `get_weather` function)

## Response Structure from a Intent Function

-   ### `key` (str)
    > This contains the name Command that the Client is required to perform. Caller function will get the required codes and commands of this Command Name
-   ### `perform` (str) [!]
    > This declarers a Pre Execution of the returned Answer / Reply to the Caller function.
-   ### `text` (str) [!]
    > This contains the Response after running the function
