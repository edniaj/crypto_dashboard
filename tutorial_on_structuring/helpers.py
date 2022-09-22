def is_prime(num):
    if num > 1 :
        for n in range(2,num) :
            if num % n != 0:
                continue
            else:
                return False
    return True

def calculate_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n):
            primes.append(n)
    print('primes : ',primes)
    return primes
def prettify(self):
    body = ''
    for result in self.calculate_primes():
        body += f"This is a prime number: {result} \n"

    return body