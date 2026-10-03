"Diccionario de prueba"
test_settings = {
    "theme": "light",
    "language": "english",
    "notificacions": "enabled"
}

def add_setting(settings: dict, pair: tuple) -> str:
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, pair: tuple) -> str:
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str) -> str:
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."
    result = "Current User Settings:\n"
    for k, v in settings.items():
        result += f"{k.capitalize()}: {v}\n"
    return result  

print(add_setting(test_settings, ("THEME", "dark")))
print(add_setting(test_settings, ("volume", "high")))
print(update_setting(test_settings, ("theme", "dark")))
print(update_setting(test_settings, ("volume", "low")))
print(delete_setting(test_settings, "language"))
print(delete_setting(test_settings, "sound"))
print(view_settings(test_settings))
