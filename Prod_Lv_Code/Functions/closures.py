'''A function that "remembers" variables from its enclosing scope.
Production use: configuration-bound callbacks, decorators (below), building small stateful functions without a full class.
'''

def make_multiplier(factor):
    def multiply(x):
        return x * factor          # factor is captured, not passed
    return multiply

double = make_multiplier(2)
double(5)   # 10