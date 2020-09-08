import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# add an argument filename='myProgramLog.txt' to logging.basicConfig to save debug logs to a file
logging.disable(logging.CRITICAL) # this line disables debug logging

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
