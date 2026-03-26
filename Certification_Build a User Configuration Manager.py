def add_setting(dictionary, tup):
    key_lower, value_lower = tup
    key_lower = key_lower.lower()
    value_lower = value_lower.lower()
    key = tup[0].lower()
    value = tup[1].lower()
    if key in dictionary.keys(): 
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else: 
        dictionary[key_lower] = value_lower
        return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(dictionary, tup): 
    key, val = tup
    key = key.lower()
    val = val.lower()
    if key in dictionary.keys(): 
        dictionary[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key): 
    key = key.lower()
    if key in dictionary.keys(): 
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else: 
        return f"Setting not found!"

def view_settings(dictionary): 
    if len(dictionary) == 0: 
        return "No settings available."
    else: 
        array = [f"{key.capitalize()}: {value}" for key, value in dictionary.items()]
        string = "\n".join(array)
        return f"Current User Settings:\n{string}\n"

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(update_setting({'theme': 'light'}, ('theme', 'dark')))

test_settings = {"nama": "martin", 
"umur" : "29"}
test = ''
print(view_settings(test_settings))
