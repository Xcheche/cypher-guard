#!/usr/bin/env python
import os
import sys
from decouple import config


def main():
    debug = config("DEBUG", default=False, cast=bool)
    print("DEBUG value from .env or environment:", debug)
    # Propagate DEBUG to the env so Django settings modules that read
    # os.environ["DEBUG"] (or decouple) see the same value.
    os.environ["DEBUG"] = str(debug)
    if debug:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
        print("Using settings module:", os.environ.get("DJANGO_SETTINGS_MODULE"))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


# To see settings module being used
# echo $DJANGO_SETTINGS_MODULE
# To unset the variable
# unset DJANGO_SETTINGS_MODULE
