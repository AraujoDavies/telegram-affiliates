import enum
import logging
import os
from datetime import datetime

import dotenv
from fake_data import fake_data_signais, fake_data_users
from sqlalchemy import (
    Column,
    DateTime,
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
    active = 1
    disabled = 2


user_table = Table(
    'tbl_users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('status', Enum(StatusDb), default='active', nullable=False),
    Column('email', String(80), nullable=False),
    Column('password', String(30), nullable=False),
    Column(
        'create_datetime', DateTime, default=datetime.now(), nullable=False
    ),
)

signais_table = Table(
    'tbl_signals',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', Integer, nullable=False),
    Column('chat_id', String(30), default='me', nullable=False),
    Column('status', Enum(StatusDb), default='active', nullable=False),
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
            populate_signais = signais_table.insert().values(fake_data_signais)
            populate_users = user_table.insert().values(fake_data_users)
            conn.execute(populate_signais)
            conn.execute(populate_users)
            conn.commit()
            logging.warning('Tabela populada com sucesso.')
        except Exception as error:
            conn.rollback()
            logging.warning(
                'Erro ao popular tabela.\nMensagem de erro: %s', error
            )
