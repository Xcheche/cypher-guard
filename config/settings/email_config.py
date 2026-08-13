"""
Email configuration.

Two profiles, chosen by the DEBUG flag:
- DEBUG=True   -> Mailpit (local SMTP capture, default localhost:1025)
- DEBUG=False  -> Zoho (real SMTP for production)

Both profiles use the SMTP backend; nothing falls back to the console backend.
"""
from decouple import config

# ======== Email Configuration from Environment Variables =======
debug = config("DEBUG", default=False, cast=bool)

# Mailpit defaults (used when DEBUG=True)
MAILPIT_HOST = config("MAILPIT_HOST", default="localhost")
MAILPIT_PORT = config("MAILPIT_PORT", default=1025, cast=int)

# Zoho defaults (used when DEBUG=False)
ZOHO_HOST = config("ZOHO_HOST", default="smtp.zoho.com")
ZOHO_PORT = config("ZOHO_PORT", default=465, cast=int)
ZOHO_HOST_USER = config("ZOHO_HOST_USER", default="williams@fortitech9ja.com")
ZOHO_HOST_PASSWORD = config("ZOHO_HOST_PASSWORD", default="")
ZOHO_FROM_EMAIL = config("ZOHO_FROM_EMAIL", default="williams@fortitech9ja.com")

# Shared
DEFAULT_FROM_EMAIL = config(
    "DEFAULT_FROM_EMAIL",
    default="williams@fortitech9ja.com" if not debug else "webmaster@localhost",
)

# ======== Profile selection =======
if debug:
    # Local development -> Mailpit
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = MAILPIT_HOST
    EMAIL_PORT = MAILPIT_PORT
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = False
else:
    # Production -> Zoho (real SMTP)
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = ZOHO_HOST
    EMAIL_PORT = ZOHO_PORT
    EMAIL_HOST_USER = ZOHO_HOST_USER
    EMAIL_HOST_PASSWORD = ZOHO_HOST_PASSWORD
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = True
    DEFAULT_FROM_EMAIL = ZOHO_FROM_EMAIL


# Debugging output to verify email settings are loaded correctly
print(
    "Email configuration loaded: ",
    {
        "profile": "mailpit" if debug else "zoho",
        "EMAIL_BACKEND": EMAIL_BACKEND,
        "EMAIL_HOST": EMAIL_HOST,
        "EMAIL_PORT": EMAIL_PORT,
        "EMAIL_USE_TLS": EMAIL_USE_TLS,
        "EMAIL_USE_SSL": EMAIL_USE_SSL,
    },
)
