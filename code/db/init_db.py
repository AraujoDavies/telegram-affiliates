import enum
import logging
import os

import dotenv
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Integer,
    MetaData,
    Table,
    Text,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import CreateSchema

dotenv.load_dotenv()

# first engine
schema_name = os.getenv('SCHEMA_NAME')
engine = create_engine(os.getenv('DATABASE_URI'))

# create schema
if not engine.dialect.has_schema(engine.connect(), schema_name):
    logging.warning('Criando schema...')
    engine.connect().execute(CreateSchema(schema_name))
    logging.warning('Schema criado com sucesso!')
else:
    logging.warning('Schema já existe no DB.')

# update engine
engine = create_engine(os.getenv('DATABASE_URI') + schema_name)

# create tables
class Base(DeclarativeBase):
    pass


metadata = MetaData()


class StatusDb(enum.Enum):
    Ativo = 1
    Desativo = 2


sinais_table = Table(
    'tbl_sinais',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', Integer),
    Column('status', Enum(StatusDb)),
    Column('message_per_minute', Integer),
    Column('message1', Text),
    Column('wait_message2', Integer),
    Column('message2', Text),
    Column('wait_message3', Integer),
    Column('message3', Text),
    Column('chat_id', Integer),
    Column('last_message_datetime', DateTime),
    Column('last_message', Text),
)

# metadata.drop_all(engine) # deixa comentado pra não ficar dropando
metadata.create_all(engine)
