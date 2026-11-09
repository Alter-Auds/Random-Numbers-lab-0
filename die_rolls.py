# A004 9/10/26 23/1426 Grp A
class SimpleRandom:
    def __init__(self, seed):
        self.seed = seed

    def next(self):
        a = 1664525
        c = 1013904223
        m = 2**32

        self.seed = (a * self.seed + c) % m

        return self.seed / m


# Create global random generator with seed 123
generator = SimpleRandom(123)


# Simulate die rolls and calculate the average
def simulate_die_rolls(n):
    total = 0

    for i in range(n):
        random = generator.next()

        roll = int(random * 6) + 1

        total += roll

    return total / n


# Demonstrate the Law of Large Numbers
for n in [10, 100, 1000, 10000]:
    average = simulate_die_rolls(n)

    print(f"Average of {n:5d} rolls: {average:.4f}")
