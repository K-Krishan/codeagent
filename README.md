# codeagent
An AI agent coding buddy that helps you complete tasks.

## Usage Instructions
- make a .env file in main directory
- visit [Google AI Studio](https://aistudio.google.com/) to make a project and get an API key
- store this key as GEMINI
- run `pip install -r requirements.txt` to install libraries used for project
- change `WORKING_DIRECTORY` variable to the directory for project where Agent is needed
- 

## Functionalities
Current tasks can be done by agent:
- list files under a directory
- read any file inside project directory
- write onto any file
- run any python script and get it's results

## Future Plans
Certain ideas that I plan to work on in future:
- A summary/compression alternative file that Agent can access to reduce tokens spent.
- Craft an alternative of full files in context/history.
- User approval of write/executes showing what was changed by agent.
- Search function for agent letting it to view context around the search terms, currently planning to include function in which word was along with context around the searched term.
- Git integration allowing agent access to git commands on the specific repository.