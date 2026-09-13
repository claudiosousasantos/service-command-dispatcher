def dispatch(command):
    """
    Simulate dispatching a service command and print the resulting action.
 
    This function only handles a fixed set of known commands.
    Anything else falls back to a generic "Unknown command" message.
    """
    # Convert to lowercase so "Start", "START", and "start" all work the same
    command = command.lower()
 
    if command == 'start':
        print("Starting the service...")
    elif command == 'stop':
        print("Stopping the service...")
    elif command == 'restart':
        print("Restarting the service...")
    elif command == 'status':
        print("Checking service status...")
    elif command == 'reload':
        print("Reloading service configuration...")
    else:
        print(f"Unknown command: '{command}'")
 
 
# A few examples to show how the function behaves
dispatch('start')
dispatch('stop')
dispatch('restart')
dispatch('status')
dispatch('reload')
dispatch('destroy')
