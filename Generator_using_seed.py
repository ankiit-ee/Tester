import sys
import random

n = int(sys.argv[1])
myseed = int(sys.argv[2])
random.seed(myseed)
print(n)

print('\n'.join([str(random.randint(1,1000)) for i in range(n)]))