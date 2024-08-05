from .apps import NoteopiaConfig

app_name = NoteopiaConfig.name

def apply_configurations(globals_dict: dict):
    installed_apps = globals_dict.get('INSTALLED_APPS')
    installed_apps.append(app_name)
