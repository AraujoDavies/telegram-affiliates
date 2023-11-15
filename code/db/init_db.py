import enum
import logging
import os

import dotenv
from fake_data import fake_data
from sqlalchemy import (
    Column,
    Enum,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import CreateSchema

dotenv.load_dotenv()

# first engine and metadata
schema_name = 'affiliatesdev'
engine = create_engine(os.getenv('DATABASE_URI'))
metadata = MetaData()

# create schema
if not engine.dialect.has_schema(engine.connect(), schema_name):
    logging.warning('Criando schema...')
    engine.connect().execute(CreateSchema(schema_name))
    logging.warning('Schema criado com sucesso!')
else:
    logging.warning('Schema já existe no DB.')

# update engine with schema
engine = create_engine(os.getenv('DATABASE_URI') + schema_name)

# create tables
class Base(DeclarativeBase):
    pass


class StatusDb(enum.Enum):
    Ativo = 1
    Desativo = 2


sinais_table = Table(
    'tbl_sinais',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', Integer, nullable=False),
    Column('chat_id', String(30), default='me', nullable=False),
    Column('status', Enum(StatusDb), default='Ativo', nullable=False),
    Column('message_per_minute', Integer, default=1, nullable=False),
    Column('message1', Text),
    Column('wait_sec_message2', Integer, default=1, nullable=False),
    Column('message2', Text),
    Column('wait_sec_message3', Integer, default=1, nullable=False),
    Column('message3', Text),
    Column('last_message_info', Text),
)

# Populate table
if __name__ == '__main__':
    logging.warning('Removendo tabela(drop).')
    metadata.drop_all(engine)
    logging.warning('Criando tabela')
    metadata.create_all(engine)

    with engine.connect() as conn:
        conn.begin()
        try:
            stmt = sinais_table.insert().values(fake_data)
            conn.execute(stmt)
            conn.commit()
            logging.warning('Tabela populada com sucesso.')
        except:
            conn.rollback()
            logging.warning('Erro ao popular tabela.')
