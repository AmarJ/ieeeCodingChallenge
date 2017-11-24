class Fibonacci:
    def get_nth_fibonacci(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.get_nth_fibonacci(n-1) + self.get_nth_fibonacci(n-2)
