"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

Input:
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]

Output:
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation:
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


constraints
1 <= size <= 1000
-105 <= val <= 105

"""

from collections import deque


# Approach 1
class MovingAverage:
    """
    Docstring for MovingAverage
    1. window using deque for O(1) insertion and removal
    2. if dqueue increase k (window size), remove elemenent from head and sum, add new ele at tail
    """

    def __init__(self, window_size: int) -> None:
        self.window = deque()
        self.k = window_size
        self.sum = 0

    def next(self, item: int):
        self.window.append(item)
        self.sum += item

        if len(self.window) > self.k:
            self.sum -= self.window.popleft()
            self.sum += item
            self.window.append(item)
        return float(self.sum / len(self.window))


# Approach 2


class MovingAverage2:
    """
    Docstring for MovingAverage2
    1.
    """

    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    movingAvg = MovingAverage(3)
    print(movingAvg.next(1))
    print(movingAvg.next(10))
    print(movingAvg.next(3))
    print(movingAvg.next(5))
