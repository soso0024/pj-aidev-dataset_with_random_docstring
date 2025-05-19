"""Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the list of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
"""

import random
from model.user import User
from model.order import Order


def generate_users(n):
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if n < 0:
        raise ValueError("Number of users must be positive")

    users = []
    for i in range(1, n + 1):
        users.append(User(id=i, name=f"User{i}", balance=random.uniform(10, 100)))
    return users


def generate_orders(users, max_orders=3):
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    orders = []
    print("\nGenerating orders...")
    for user in users:
        available_balance = user.balance
        for _ in range(random.randint(1, max_orders)):
            if available_balance <= 1:  # Skip if below minimum order amount
                print("Skipping order generation due to insufficient balance.")
                break
            amount = random.uniform(1, min(available_balance, user.balance))
            order = Order(user_id=user.id, amount=amount)
            orders.append(order)
            available_balance -= amount
    return orders
