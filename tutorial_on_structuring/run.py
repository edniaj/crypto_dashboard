import constants as c
from helpers import *
from email.email import Email
def run():
    primes = calculate_primes(start = c.START, finish = c.FINISH)
    prettier = primes.prettify()
    new_email = Email()
    new_email.to = 'JohnDoe@email.com'
    new_email.subject = f'Prime Numbers execution between {c.START} to {c.FINISH}'
    new_email.body = prettier
    new_email.send()

if __name__ == '__main__':
    run()