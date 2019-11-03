import random


class Agent:
    location = 0

    def __init__(self, location):
        self.location = location


i = 1
perf = 0
perfSum = 0


class Environment:
    A = ''
    B = ''

    def __init__(self, A, B):
        self.A = A
        self.B = B


def vacumm_cleaner(location, A, B):
    global i
    global perf

    if A == 'clean' and B == 'clean':
        perf += 2
    elif A == 'dirty' and B == 'clean':
        perf += 1
    elif A == 'clean' and B == 'dirty':
        perf += 1

    if A == 'clean' and B == 'clean':
        print('End')
        return i
    elif location == 0:
        if A == 'dirty':
            print('[A, Dirty] : Suck')
            i = i + 1
            vacumm_cleaner(0, 'clean', B)
        elif A == 'clean':
            print('[A, Clean] : Right')
            i = i + 1
            vacumm_cleaner(1, A, B)
    elif location == 1:
        if B == 'dirty':
            print('[B, Dirty] : Suck')
            i = i + 1
            vacumm_cleaner(1, A, 'clean')
        elif B == 'clean':
            print('[B, Clean] : Left')
            i = i + 1
            vacumm_cleaner(0, A, B)


perf = 0
print('Start at A, A: Clean, B: Clean\n')
agent1 = Agent(0)
env1 = Environment('clean', 'clean')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at A, A: Clean, B: Dirty\n')
agent1 = Agent(0)
env1 = Environment('clean', 'dirty')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at A, A: Dirty, B: Clean\n')
agent1 = Agent(0)
env1 = Environment('dirty', 'clean')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at A, A: Dirty, B: Dirty\n')
agent1 = Agent(0)
env1 = Environment('dirty', 'dirty')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at B, A: Clean, B: Clean\n')
agent1 = Agent(1)
env1 = Environment('clean', 'clean')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at B, A: Clean, B: Dirty\n')
agent1 = Agent(1)
env1 = Environment('clean', 'dirty')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at B, A: Dirty, B: Clean\n')
agent1 = Agent(1)
env1 = Environment('dirty', 'clean')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

perf = 0
print('Start at B, A: Dirty, B: Dirty\n')
agent1 = Agent(1)
env1 = Environment('dirty', 'dirty')
vacumm_cleaner(agent1.location, env1.A, env1.B)
print('Performance Score: ' + str(perf))
perfSum += perf
print('\n\n')

print('Average Performance Score: ' + str(perfSum))

perf = 0

while i <= 1000:
    loc = random.randint(0, 1)
    if loc == 0:
        agent1 = Agent(0)
    else:
        agent1 = Agent(1)

    clean = random.randint(0, 3)
    if clean == 0:
        env1 = Environment('clean', 'clean')
    elif clean == 1:
        env1 = Environment('clean', 'dirty')
    elif clean == 2:
        env1 = Environment('dirty', 'clean')
    elif clean == 3:
        env1 = Environment('dirty', 'dirty')

    print('\n')
    print('\n')
    if agent1.location == 0:
        print('Agent1: A ' + 'A: ' + env1.A + ' B: ' + env1.B)
    else:
        print('Agent1: B ' + 'A: ' + env1.A + ' B: ' + env1.B)

    vacumm_cleaner(agent1.location, env1.A, env1.B)

print('Average Performance Score over 1000 time steps: ' + str(perf / 1000))