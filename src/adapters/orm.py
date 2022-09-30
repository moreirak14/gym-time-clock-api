from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Table
from sqlalchemy.orm import clear_mappers, registry

from src.adapters.databases import Base
from src.domain.work.entity.work import Work

metadata = Base.metadata
mapper_registry = registry()


table_work = Table(
    "work",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("work_status", String(10), nullable=True, default=None),
    Column("description", String(100), nullable=True, default=None),
    Column("registered_at", DateTime, nullable=False,
           default=datetime.now(timezone.utc))
)


def start_mappers():
    clear_mappers()

    mapper_registry.map_imperatively(Work, table_work)
