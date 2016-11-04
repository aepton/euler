#!/usr/bin/python

from decimal import Decimal, getcontext
from itertools import count, islice


class EulerPrimeFinder(object):
    def __init__(self, num_places=1000):
        """
        num_places is the number of places to expand Euler's number to.
        """
        self.num_places = num_places
        self.euler_number = self.expand_euler()

    def is_prime(self, n):
        """
        Method from http://stackoverflow.com/a/27946768/7027687

        Returns True if n is a prime number, False otherwise.
        """
        # Smallest prime is 2
        if n < 2:
            return False
        
        # Only need to check up to sqrt(n), which == n^0.5, to determine primality
        # This is slow for large primes, but we're guaranteed to see at worst
        # 1,000,000 (i.e. sqrt(999999999999), the largest 12-digit number)
        # Using n^0.5 insted of sqrt(n) is just convenience to avoid importing another
        # library
        for num in islice(count(2), int(pow(n, 0.5) - 1)):
            if not n % num:
                return False
        return True

    def expand_euler(self):
        """
        Method from http://stackoverflow.com/a/23442813/7027687

        Expands Euler's number to self.num_places and returns it as a string.
        """
        # Set precision to number of places we're computing
        # (+1 to account for leading "2.")
        getcontext().prec = self.num_places + 1

        e = Decimal(0)
        f = Decimal(1)
        n = Decimal(1)

        while True:
            prev_e = e
            e += Decimal(1) / f

            # If there's no change, we've reached maximal precision; stop.
            if e == prev_e:
                break

            f *= n
            n += Decimal(1)
        return str(e)

    def find_xth_prime_of_y_digits(self, x, y, count_the_two):
        """
        Finds the Xth prime of Y digits in Euler's number. If count_the_two is True, considers
        the leading 2 as part of Euler's number; if False, just uses all numbers after the
        decimal place.

        Returns a dict containing two items:
        * "euler": Euler's number with 1,000 decimal places (for use in visualization on the frontend).
        * "x": value for x
        * "y": value for y
        * "count_the_two": True if we're counting the 2, False otherwise
        * "primes": list of dicts (for use in visualization on the frontend). Each item in the list is a
          dict containing two items:
          * "prime": the prime number found
          * "position": the offset of the first digit in the prime number
        """
        # Turns out, 1000 places is enough to find 23 12-digit primes, so that should be enough
        # Computing the first 1000 is fast enough that we can just do it. Obvious optimization
        # would be to base the size of the search space on the number of digits in the prime we're
        # looking for.
        num_places = 1000

        if not count_the_two:
            digits = self.euler_number[2:] # Just want to search after decimal
        else:
            digits = self.euler_number.replace('.', '')

        matches = {
            'euler': self.euler_number,
            'x': x,
            'y': y,
            'count_the_two': count_the_two,
            'primes': []
        }
        begin = 0
        end = y
        comparisons = 0

        while y < len(digits) + 1:
            # Pick the candidate number
            window = digits[begin:end]
            
            # If length < y, we didn't pick enough digits in our search space.
            # This would be where we expand search space if we needed to, but
            # as above, for this specific problem that seems unnecessary.
            if len(window) < y:
                print 'Could only find %d matches' % len(matches['primes'])
                return matches

            if window.startswith('0'):
                begin += 1
                end += 1
                continue
            comparisons += 1
            if self.is_prime(int(window)):
                # Yay, we found a match. Create a results object for future display.
                matches['primes'].append({
                    'prime': window,
                    'position': begin
                })
            if len(matches['primes']) == x:
                return matches
            begin += 1
            end += 1