from django.apps import AppConfig
from .predictor import NTSNetPredictor

class ModelapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ModelApi'

    # Load Model here
    ML_MODEL = NTSNetPredictor