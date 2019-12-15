import math
from random import uniform


def equiv(A):
    if (A[0][0] == A[1][0] == A[2][0] == A[3][0] and A[0][1] == A[1][1] == A[2][1] == A[3][1]):
        return 1
    else:
        return 0

def mutation(A):
    delta = 0.05;
    for i in range(0, len(A)):
        if (uniform(0, 1) <= 0.25):
            if (uniform(0, 1) <= 0.5):
                if (uniform(0, 1) <= 0.5):
                    A[i][0] += delta
                else:
                    A[i][0] -= delta
            else:
                if (uniform(0, 1) <= 0.5):
                    A[i][1] += delta
                else:
                    A[i][1] -= delta

def function(x, y):
    return math.sin(x) * math.exp(-(x ** 2) - (y ** 2))


def middle_res(A):
    return sum(A) / len(A)


def print_matr(A, F):
    # print('%.4f' % max(F),' ','%.4f' % middle_res(F))
    print("   X      Y     FIT    Max    Middle")
    for i in range(0, len(A)):
        if (i == 0):
            print('%.4f' % A[i][0], '%.4f' % A[i][1], '%.4f' % F[i], '%.4f' % max(F), ' ', '%.4f' % middle_res(F))
        else:
            print('%.4f' % A[i][0], '%.4f' % A[i][1], '%.4f' % F[i])


N = 10
#zero generation
generation = [[uniform(-2, 2), uniform(-2, 2)],
              [uniform(-2, 2), uniform(-2, 2)],
              [uniform(-2, 2), uniform(-2, 2)],
              [uniform(-2, 2), uniform(-2, 2)]]
fit = [0, 0, 0, 0]
for i in range(0, len(generation)):
    fit[i] = function(generation[i][0], generation[i][1])
P = [0, 0, 0, 0]

# genetic algorithm
iterator=0
print(iterator,')',sep="")
print_matr(generation,fit)
print()
##while equiv(generation)!=1:
for i in range (N):
    for j in range(0, len(fit)):
        P[j] = 1 - fit[j] / sum(fit)
    rand = uniform(0, sum(P))
    if rand <= P[0]:
        generation[0][0] = generation[0][1] = 0
        generation[0], generation[3] = generation[3], generation[0]
        fit[0], fit[3] = fit[3], fit[0]
    elif P[0] < rand <= P[0] + P[1]:
        generation[1][0] = generation[1][1] = 0
        generation[1], generation[3] = generation[3], generation[1]
        fit[1], fit[3] = fit[3], fit[1]
    elif P[0] + P[1] < rand <= P[0] + P[1] + P[2]:
        generation[2][0] = generation[2][1] = 0
        generation[2], generation[3] = generation[3], generation[2]
        fit[2], fit[3] = fit[3], fit[2]
    elif P[0] + P[1] + P[2] < rand <= P[0] + P[1] + P[2] + P[3]:
        generation[3][0] = generation[3][1] = 0

    # crossover
    maximum = 0
    maximum_i = 0
    for i in range(0, len(generation) - 1):
        if (fit[i] > maximum):
            maximum = fit[i]
            maximum_i = i
    generation[0], generation[maximum_i] = generation[maximum_i], generation[0]
    generation[0][1], generation[1][1] = generation[1][1], generation[0][1]
    generation[3][0] = generation[0][0]
    generation[3][1] = generation[2][1]
    generation[2][1] = generation[1][1]

    # mutation
    generation=mutation(generation)

    iterator += 1
    print(iterator,')',sep="")
    for i in range(0, len(generation)):
        fit[i] = function(generation[i][0], generation[i][1])
    print_matr(generation, fit)
    print()
for i in range(0, len(generation)):
    fit[i] = function(generation[i][0], generation[i][1])
