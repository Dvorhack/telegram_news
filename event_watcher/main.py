from os.path import dirname, basename, isfile, splitext
import glob, threading
import os, types
import importlib


def execute_function(script_path, function_name):
    """
        Check if @function_name is a function in @script_path and creates a thread which calls it
    """
    try:
        module_name = splitext(basename(script_path))[0]
        module = importlib.import_module(f'scripts.{module_name}')
        if hasattr(module, function_name) and callable(getattr(module, function_name)):
            print(f'Calling {function_name} in {module_name}')
            #getattr(module, function_name)()
            
            
            my_thread = threading.Thread(target=getattr(module, function_name))
            my_thread.start()
            return module_name, my_thread
        
        else:
            print(f"{module_name} doesn't have {function_name}")
    
    except (ImportError, AttributeError) as e:
        print(f'Error executing {function_name} in {script_path}: {e}')


def execute_function_in_all_scripts(folder_path, function_name):
    """
        call @function_name in every python scripts in @folder_path
    """
    threads = {}
    for file_name in os.listdir(folder_path) :
        if file_name.endswith('.py') and not file_name.endswith('__init__.py'):
            script_path = os.path.join(folder_path, file_name)
            if (result := execute_function(script_path, function_name)) is not None:
                threads[result[0]] = result[1] 
            
    return threads

print(execute_function_in_all_scripts('scripts', 'event_watcher'))

