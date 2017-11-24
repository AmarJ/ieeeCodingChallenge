class Fibonacci:
    def __init__(self):
        self.num_memoized = 2
        self.memo = [0, 1]

    def get_nth_fibonacci(self, n):
        while n > self.num_memoized:
            self.memo.append(self.memo[-1] + self.memo[-2])
            self.num_memoized += 1
        return self.memo[n - 1]
