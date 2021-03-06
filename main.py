import sys
import random
import os

tests = int(sys.argv[1])  # Number of testcases
n = int(sys.argv[2])  # Parameter for test

for i in range(tests):
    print("Test #" + str(i))
    # run the generator gen.py with parameter n and the seed i
    os.system("python gen.py "+ str(n) + " " + str(i) + " > input.txt")
    # run the model solution.py
    # Notice that it is not necessary that solution is implemented in
    # python, we can as well run ./model < input.txt > model.txt for a c++ solution

    os.system("python model.py < input.txt > model.txt")
    # runt the main solution
    os.system("python main.py < input.txt > main.txt")

    # read the output of the model solution:
    with open('model.txt') as f: model = f.read()
    print("Model: ", model)
    # read the output of the main solution:
    with open('main.txt') as f: main = f.read()
    print("Main: ", main)
    if model != main:
        break


