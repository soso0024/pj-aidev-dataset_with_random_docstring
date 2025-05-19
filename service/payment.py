"""Input is a space-delimited string of numberals from 'zero' to 'nine'.
Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five')
'one three five'
"""

from repository.user_repo import get_user, save_user
from repository.order_repo import save_order
from model.order import Order


def make_payment(user_id: int, amount: float):
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if amount <= 0:
        raise ValueError("Payment amount must be positive")

    user = get_user(user_id)
    if not user:
        raise ValueError("User not found")
    new_balance = user.debit(amount)
    order = Order(user_id=user_id, amount=amount)
    save_order(order)
    save_user(user)
    return new_balance
