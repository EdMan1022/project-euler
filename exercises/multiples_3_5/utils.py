

def divisible_by(value, divisors):
    """
    Raises a value error if the value isn't divisible by the divisors
    """
    for divisor in divisors:
            if value % divisor == 0:
                    return
    raise ValueError

def sum_of_values_divisible(max, divisors):
        """
        Returns the sum of all values under max divisible by divisors

        As long as the value is divisible by at least one divisor,
        it is counted
        """

        divisible_sum = 0

        for i in range(max):
                try:
                    divisible_by(i, divisors)
                    divisible_sum += i
                except ValueError:
                    continue
        return divisible_sum
