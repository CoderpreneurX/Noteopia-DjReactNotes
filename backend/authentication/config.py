from .apps import AuthenticationConfig
from datetime import timedelta

app_name = AuthenticationConfig.name

def apply_configurations(globals_dict):
    installed_apps = globals_dict["INSTALLED_APPS"]
    installed_apps.append(app_name)
    installed_apps.append('rest_framework')
    installed_apps.append('corsheaders')
    globals_dict["REST_FRAMEWORK"] = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        )
    }
    globals_dict["SIMPLE_JWT"] = {
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1)
    }
    globals_dict["CORS_ALLOW_ALL_ORIGINS"] = True
    globals_dict["CORS_ALLOW_CREDENTIALS"] = True
    globals_dict["MIDDLEWARE"].append("corsheaders.middleware.CorsMiddleware")
