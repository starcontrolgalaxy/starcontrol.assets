# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from .api import endpoints  # For import side-effects of setting up routes.
from .webui import endpoints  # For import side-effects of setting up routes.
