#A system that uses a genetic algorithm to maximize a function of many variables

import random
import sys


#No global max, actually just overflows. need a simpler "hard problem"
def equation(a, b, c, d):
    return (4 * (a**2)) - (150 * a) + (12 * b * c) - (120 * (b**3)) + (2 * (c * d)) - (d**2) - (d + a)


# simpler equation, solved using WolfRamAlpha, maximum at (x=1, y=2)
def simple_equation(x, y):
    return - (x**2) + (2 * x) - (y ** 2) + (4 * y)


#takes a function and list of arguements, applies function to arguments
def calculate(args):
    scores = []
    avg = 0
    for arg in args:
        if len(arg) == 2:
            r = simple_equation(arg[0], arg[1])
            scores.append(r)
            avg += r
        elif len(arg) == 4:
            r = equation(arg[0], arg[1], arg[2], arg[3])
            scores.append(r)
            avg += r
        else:
            print("error: Wrong number of arguements received")
    avg = avg / len(scores)
    return scores, avg


#Create child from parent
def mutate(args):
    new = []
    for a in args:
        new.append(a + random.normalvariate(0, a + .1)) #random factor of normal distribution
    return new


#create a population of 100 lists, all elements 0, of any length
def start(n, p):
    pop = [[0] * n]
    for i in range(p):
        pop.append(mutate(pop[0]))
    return pop


def find_best(args):
    best = 0
    val = None
    for arg in args:
        if len(arg) == 2:
            r = simple_equation(arg[0], arg[1])
            try:
                if r > val:
                    best = arg
                    val = r
            except:
                best = arg
                val = r
        elif len(arg) == 4:
            r = equation(arg[0], arg[1], arg[2], arg[3])
            try:
                if r > val:
                    best = arg
                    val = r
            except:
                best = arg
                val = r
        else:
            print("error: Wrong number of arguements received")
    return best, val


if __name__ == "__main__":
    if len(sys.argv) != 4: #Old School CS 161 checks
        print("Usage: python geneticmax.py len pop iter")
        exit()
    population = start(int(sys.argv[1]), int(sys.argv[2]))
    iterations = 0
    while (iterations < int(sys.argv[3])):
        scores, avg = calculate(population)
        deleted = 0
        new_population = []
        for i in range(len(population)):
            if scores[i] < avg:
                deleted += 1
            else:
                new_population.append(population[i])
        for i in range(deleted):
            new_population.append(mutate(new_population[i % len(new_population)])) #iterate over population with overflow protection
        population = new_population
        iterations += 1
    best, val = find_best(population)
    print("After", sys.argv[3], "iterations, the best out of a population of", sys.argv[2], "the optimal input is", best, "with a value of", val)
