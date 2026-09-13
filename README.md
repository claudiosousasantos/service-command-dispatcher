# Service Command Dispatcher
 
A simple Python function that simulates dispatching basic service commands and prints the corresponding action.
 
## How it works
The `dispatch()` function takes a command (a string) and prints back the matching action:
 
| Command   | Action |
|-----------|--------|
| start     | Starting the service... |
| stop      | Stopping the service... |
| restart   | Restarting the service... |
| status    | Checking service status... |
| reload    | Reloading service configuration... |
 
Any command not listed above prints **"Unknown command"**, along with the command itself so you can see what was passed in.
 
The function also converts the command to lowercase before checking it, so `"Start"`, `"START"`, and `"start"` are all treated the same way.
 
## How to run
```bash
python command_dispatcher.py
```
 
You should see output like:
```
Starting the service...
Stopping the service...
Restarting the service...
Checking service status...
Reloading service configuration...
Unknown command: 'destroy'
```
 
## Try it yourself
Call the function with your own command at the bottom of the file:
```python
dispatch('pause')
```
 
## What I learned
- Using `if / elif / else` to handle a fixed set of known commands with a fallback
- Simulating command dispatch logic, a pattern used in CLIs and service management tools
- Using `.lower()` to make text comparisons case-insensitive
- Using an f-string (`f"..."`) to include a variable's value inside a printed message
