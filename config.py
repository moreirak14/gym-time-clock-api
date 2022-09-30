from pathlib import Path

from dynaconf import Dynaconf

PATH_ROOT = Path(__file__).parent

settings = Dynaconf(
    environments=True,
    envvar_prefix="Forum API",
    settings_files=["settings.toml", ".secrets.toml"],
    includes=[f"{PATH_ROOT}/settings.toml", f"{PATH_ROOT}/.secrets.toml"],
)


def database_uri():
    _database_uri = (
        f"{settings.DATABASE_DIALECT_DRIVER}://"
        f"{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@"
        f"{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/"
        f"{settings.DATABASE_NAME}"
    )

    return _database_uri


settings.database_uri = database_uri()
