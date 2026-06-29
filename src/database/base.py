from typing import Optional

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
# this file was very hard to figure out first because i just didnt understand how the architecture works
# if you dont remember or get anything refer the architecture egingine -> factory merges forms single pipleine etc


class Base(DeclarativeBase):
    pass

_engine : Optional[Engine] = None # pipe for the data transferr
# call below this is a global func not local
_session_factory : Optional[sessionmaker] = None


def get_engine(database_url:str,echo:bool = False) -> Engine:

    global _engine  # the above var rather than local variable
    if _engine is None:
        _engine = create_engine(
            database_url,
            echo = echo,
            poop_pre_ping = True, # checks connection by sending ping to db if doesnt come back then establishes new
            pool_recycle = 1200,
        )
        return _engine

def get_session_factory(database_url:str,echo:bool = False) -> sessionmaker:

    global _session_factory
    if _session_factory is None:
        engine  = get_engine(database_url,echo = echo)
        _session_factory = sessionmaker(bind=engine, expire_on_commit=False) # create active database
        return _session_factory

def get_session(database_url:str,echo:bool = False) -> Session:
    factory = get_session_factory(database_url,echo = echo)
    return factory()


def reset_engine() -> None: # resets the cache things
    global _engine, _session_factory
    _engine = None
    _session_factory = None
