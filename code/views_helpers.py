import os

from view import sessions


def session_is_ok(session_file: str) -> bool:
    """verify if session exists in session path.

    Args:
        session_file (str): name of session

    Returns:
        bool: True is exists or False if not exists
    """
    found_sessions = os.listdir(sessions)   # sessoes encontradas
    # print(found_sessions)
    session_is_ok = (
        session_file + '.session' in found_sessions
    )   # sessao existe na pasta ?
    # print(session_is_ok)
    return session_is_ok
