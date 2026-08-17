# Service Command Dispatcher

A simple Python function that simulates dispatching basic service commands and prints the corresponding action.

## How it works
- **start**: Starting the service...
- **stop**: Stopping the service...
- **restart**: Restarting the service...
- Any other command prints "Unknown command" as a fallback

## How to run
```bash
python command_dispatcher.py
```

## What I learned
- Using `if / elif / else` to handle a fixed set of known commands with a fallback
- Simulating command dispatch logic, a pattern used in CLIs and service management tools
