from pathlib import Path

_base_dir = Path("/tmp")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': _base_dir / 'db.sqlite3',
    }
}
