from .apps import AuthenticationConfig

app_name = AuthenticationConfig.name

def apply_configurations(globals_dict):
    installed_apps = globals_dict["INSTALLED_APPS"]
    installed_apps.append(app_name)
    globals_dict["REST_FRAMEWORK"] = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        )
    }
