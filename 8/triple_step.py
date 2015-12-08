'''

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

'''
import datetime as dt

def triple_step(steps):
    memo = {}
    print dt.datetime.now()
    print count_ways(steps, memo)
    print dt.datetime.now()


def count_ways(steps, memo):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    elif steps in memo.keys():
        return memo[steps]
    else:
        memo[steps] = count_ways(steps - 1, memo) + count_ways(steps - 2, memo) + count_ways(steps - 3, memo)

        return memo[steps]


triple_step(30)

# steps = 30
# Without memoization
# 22:07:23.636153
# 53798080
# 22:08:13.765158

# With memoization
# 22:22:26.618838
# 53798080
# 22:22:26.619386
