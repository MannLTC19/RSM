#!/usr/bin/env python
"""Django's command-line utility for administrative tasks with PyMISP logging."""
import os
import sys
import logging
from pymisp import PyMISP

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("django_pymisp.log"),
        logging.StreamHandler()
    ]
)

MISP_URL = "https://your-misp-instance.com"  
MISP_API_KEY = "your_api_key_here"  
MISP_VERIFY_SSL = False  

try:
    misp = PyMISP(MISP_URL, MISP_API_KEY, MISP_VERIFY_SSL)
    logging.info("Connected to MISP successfully.")
except Exception as e:
    logging.error(f"Failed to connect to MISP: {e}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logging.critical("Django import failed. Check if Django is installed and virtualenv is activated.", exc_info=True)
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    logging.info("Executing Django command: %s", " ".join(sys.argv))
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
