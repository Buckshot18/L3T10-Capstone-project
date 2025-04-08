from django.apps import AppConfig

class BandAppConfig(AppConfig):
    """
    Configuration class for the 'band_app' application.

    This class defines the configuration for the 'band_app' Django application
    including the default settings for database fields and the app's name. It
    inherits from `AppConfig`, which allows Django to manage
    application-specific settings.

    Attributes:
        default_auto_field (str): Specifies the type of auto-generated field to
        use for primary keys in models. By default, this is set to
        'django.db.models.BigAutoField', which provides a 64-bit integer field.
        name (str): The full Python path to the application, in this case,
        'band_app'. This helps Django locate the app in the project.
    """
    # Specifies the type of auto field to use for primary keys in models
    # Django will automatically create primary keys for models using this
    # field type unless otherwise specified.
    default_auto_field = 'django.db.models.BigAutoField'

    # Specifies the name of the application. This is used by Django to uniquely
    # identify the app.
    name = 'band_app'
