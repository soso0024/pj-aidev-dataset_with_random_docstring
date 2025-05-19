"""Given a string, find out how many distinct characters (regardless of case) does it consist of
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
"""

from repository.user_repo import get_user, save_user
from utils.string_utils import hash_password


def register_user(user_id: int, name: str, password: str, balance=0.0):
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    from model.user import User

    if balance < 0:
        raise ValueError("Balance cannot be negative")

    existing_user = get_user(user_id)
    if existing_user:
        # Preserve existing user's balance
        balance = existing_user.balance

    hashed = hash_password(password)
    user = User(id=user_id, name=name, balance=balance)
    user.hashed_password = hashed
    save_user(user)
    return user


def authenticate(user_id: int, password: str):
    """Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    user = get_user(user_id)
    if not user:
        return False
    return user.hashed_password == hash_password(password)
