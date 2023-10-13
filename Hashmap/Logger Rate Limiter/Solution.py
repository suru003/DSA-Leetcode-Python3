'''
Link: https://leetcode.com/problems/logger-rate-limiter/
Link: https://www.lintcode.com/problem/3620/
For function: could_print_message
Time Complexity: O(1)
Space Complexity: O(1)
'''

class Logger:
    """
    @param timestamp: Timestamp
    @param message: Message
    @return: Whether the log can be printed
    """

    def __init__(self):
        self.last = {}

    def could_print_message(self, timestamp: int, message: str) -> bool:
        if timestamp - self.last.get(message, -11) >= 10:
            self.last[message] = timestamp
            return True

        return False
