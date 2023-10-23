
import gradio as gr

def hello_greet(name):
    """This function add 'Hello' in front of the str name 

    Args:
        name (str): The text that pass to the interface

    Returns:
        str: 
    """
    return "Hello " + name + "!"

def interface_greet(name, is_morning, temperature):
    """_summary_

    Args:
        name (str): _description_
        is_morning (bool): _description_
        temperature (int): _description_

    Returns:
        _type_: _description_
    """
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)