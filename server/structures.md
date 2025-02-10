## Program Files Structure

-   `main.py`: This is the entry point of the program.
-   `action`: This directory contains the action functions of the Intents and required data
    -   `data`: Contains data to use for executing action functions
    -   `functions`: Contains the action functions themselves
-   `intent`: This directory contains functions relative to Intent detection and Intent function detections
    -   `intent.py`: Contains the Intent detection function
    -   `intent_functions.py`: Contains the Intent function detection functions
-   `utils`: This directory contains utility functions used throughout the program
-   `.env`: This file contains environment variables used throughout the program
-   `.env.example`: This file contains an example of environment variables used throughout the program

## Entity List:

-   `name`: Contains the Entity Name
-   `value`: Contains the Entity Value

## Intents List

-   weather
-   open_app_or_web
-   chat_response [!]

## Action Functions

-   Intent's Action Function's file has the same name as intent (ex: Intent `weather` > `weather.py`)
-   The main Function of that Intent's Action contains almost same name as the Intent but contains a `get_` suffix (ex: Intent `weather` > `weather.py` > `get_weather` function)
-   Every Intent Functions takes one parameter called `properties`, which is a `dict`. This parameter contains the properties of the Intent, which are the values of the Entities detected in the Intent as well as some additional Information

## Response Structure from a Intent Function

Intent Functions will return an Array of Response. As we don't want to use the Message send feature in every intent function, intent Functions will return Array / List of response. That way, more than one command (ex: speak + execute) will be sent to the client separately.

## [{}] ->

-   ### `key` (str)
    > This contains the name Command that the Client is required to perform. Caller function will get the required codes and commands of this Command Name
-   ### `perform` (str) [!]
    > This declarers a Pre Execution of the returned Answer / Reply to the Caller function.
-   ### `text` (str) [!]
    > This contains the Response after running the function
