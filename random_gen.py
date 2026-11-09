# A004 9/10/26 23/1426 Grp A
class SimpleRandom:
    def __init__(self, seed):
        self.seed = seed

    def next(self):
        # LCG constants
        a = 1103515245
        c = 12345
        m = 2**31

        # Generate the next pseudo-random number
        self.seed = (a * self.seed + c) % m

        # Normalize the result between 0 and 1
        return self.seed / m


random_generator = SimpleRandom(3)

print(random_generator.next())
print(random_generator.next())
print(random_generator.next())


# ChatGPT used for the code
