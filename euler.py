from decimal import Decimal, getcontext
from itertools import count, islice

def is_prime(n):
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

def expand_euler(num_places):
    """
    Method from http://stackoverflow.com/a/23442813/7027687

    Expands Euler's number to num_places and returns it as a string.
    """
    # Set precision to number of places we're computing
    # (+1 to account for leading "2.")
    getcontext().prec = num_places + 1

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

def find_xth_prime_of_y_digits(x, y, count_the_two):
    """
    Finds the Xth prime of Y digits in Euler's number. If count_the_two is True, considers
    the leading 2 as part of Euler's number; if False, just uses all numbers after the
    decimal place.

    Returns a dict containing two items:
    * "euler": Euler's number with 1,000 decimal places (for use in visualization on the frontend).
    * list of dicts (for use in visualization on the frontend). Each item in the list is a
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
        digits = expand_euler(num_places)[2:] # Just want to search after decimal
    else:
        digits = expand_euler(num_places).replace('.', '')

    matches = []
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
            print 'Could only find %d matches' % len(matches)
            return matches

        if window.startswith('0'):
            begin += 1
            end += 1
            continue
        comparisons += 1
        if is_prime(int(window)):
            # Yay, we found a match. Create a results object for future display.
            matches.append({
                'prime': window,
                'position': begin
            })
        if len(matches) == x:
            return matches
        begin += 1
        end += 1

if __name__ == '__main__':
    tests = [
        (3, 3, 353, 523),
        (4, 5, 24709, 24977),
        # 24977 is the 3rd, not 4th, 5-digit prime
        (3, 2, 23, 23),
        (1, 4, 4523, 4523),
        #(3, 20, -1, -1),
        (5, 6, 995957, 995957),
        (9, 6, 594571, 594571),
        (6, 10, 1573834187, 1063686487),
        # 1063686487 doesn't appear in first 1000 digits
        (4, 1, 5, 2),
        (3, 5, 24977, 62497),
        # 62497 is the 2nd, not 3rd, 5-digit prime
        (2, 7, 2497757, 6028747),
        (8, 3, 277, 967),
        (5, 11, 33829880753, 36864870169),
        # 36864870169 doesn't appear in first 1000 digits
        (5, 13, 3232862794349, 7099983170353),
        # 7099983170353 doesn't appear in first 1000 digits
        (6, 12, 157383418793, 82449550453),
        # 82449550453 doesn't appear in first 1000 digits
        (7, 6, 630353, 630353)
    ]

    for test in tests:
        for case in [(test[0], test[1], test[2], False), (test[0], test[1], test[3], True)]:
            result = find_xth_prime_of_y_digits(case[0], case[1], case[3])
            if int(result[-1]['prime']) != case[2]:
                print 'Error with x: %d, y: %d, result: %d, count_the_two: %s' % (case[0], case[1], case[2], case[3])
                print 'Found %d' % int(result[-1]['prime'])
                candidates = find_xth_prime_of_y_digits(case[0] + 25, case[1], case[3])
                
                for idx, candidate in enumerate(candidates):
                    if int(candidate['prime']) == case[2]:
                        found = True
                        print 'Found true answer - %sth prime: %s\n' % (idx, candidate)
                print '\n'