"""For a given list of input numbers, calculate Mean Absolute Deviation
around the mean of this dataset.
Mean Absolute Deviation is the average absolute difference between each
element and a centerpoint (mean in this case):
MAD = average | x - x_mean |
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
"""

from datetime import datetime


class Order:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    def __init__(self, user_id: int, amount: float):
        """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
        For each of the group, output the deepest level of nesting of parentheses.
        E.g. (()()) has maximum two levels of nesting while ((())) has three.

        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
        """
        self.user_id = user_id
        self.amount = amount
        self.timestamp = datetime.utcnow()

    def summary(self):
        """Filter an input list of strings only for ones that contain given substring
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
        """
        return f"Order for user {self.user_id}: ${self.amount:.2f} at {self.timestamp.isoformat()}"
