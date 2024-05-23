import comfy.options
comfy.options.enable_args_parsing()

import os
import importlib.util
import folder_paths
import time

def execute_prestartup_script():
    def execute_s
    
            import webbrowser
            if os.name == 'nt' and address == '0.0.0.0':
                address = '127.0.0.1'
            webbrowser.open(f"http://{address}:{port}")
        call_on_start = startup_server

    try:
        loop.run_until_complete(run(server, address=args.listen, port=args.port, verbose=not args.dont_print_server, call_on_start=call_on_start))
    except KeyboardInterrupt:
        logging.info("\nStopped server")

    cleanup_temp()
