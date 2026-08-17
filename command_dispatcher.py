def dispatch(command):
    if command == 'start':
        print("Starting the service...")
    elif command == 'stop':
        print("Stopping the service...")
    elif command == 'restart':
        print("Restarting the service...")
    else:
        print("Unknown command")

dispatch('start')
dispatch('stop')
dispatch('restart')
dispatch('status')