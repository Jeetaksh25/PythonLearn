class Maths:
    def __init__(self, n):
        self.n = n
        self.is_perfect_square, self.square_root = self.check_perfect_square()

    def check_perfect_square(self):
        for i in range(1, self.n+1):
            if i * i == self.n:
                return True, i
        return False, None

num = int(input("Enter a number: "))
func = Maths(num)

if func.is_perfect_square:
    print(f"{num} is a perfect square of {func.square_root}")
else:
    print(f"{num} is not a perfect square")
