from random import random
from math import exp
from math import sqrt

class firefly_algo:

    def __init__(self,data, population, max_iter, low_bound=0, up_bound=1, gamma=1, alpha=0.1, beta=0.2, damping_ratio=0.98, m=2):
        self.data = data #store pos
        self.population = population
        self.iter = max_iter;
        self.low_bound = low_bound
        self.up_bound = up_bound
        self.gamma = gamma
        self.alpha = alpha
        self.beta = beta
        self.delta = 0.05*(self.up_bound - self.low_bound)
        self.damping_rat = damping_ratio;
        self.m = m
        self.fitness_value = self.fitness_function() 
        self.movement = [] # store the history of pos
        self.movement_fitness = [] # store the history of cost
    
    def fitness_function(self): # count the cost
        mod_data = []
        for i in self.data:
            mod_data.append(i**2)
        return mod_data;

    def update_data(self):
        self.movement.append(self.data)
        self.movement_fitness.append(self.fitness_value)

    def run(self):
        self.update_data()
        for i in range(self.population):
            for j in range(self.population):
                if(self.fitness_value[i] < self.fitness_value[j]):
                    self.data[j] = self.move_to(i, j)
                else:
                    self.data[j] = self.move_random(i)
            self.fitness_value = self.fitness_function()
            self.update_data()
        print(self.movement)
    

    def move_random(self, x):
        e = random() * (self.low_bound, self.up_bound) - 0.5
        # equation - xi = xi + alpha*ei
        new_pos = self.data[x] + (self.alpha * e)
        return new_pos

    def move_to(self, x, y):
        e = random() * (self.low_bound, self.up_bound) - 0.5
        beta = self.beta * exp((self.gamma*-1) * (self.distance(self.data[x], self.data[y])**2))

        new_pos = self.data[x] + beta + e
        return new_pos

    def distance(self, xi, xj):
        return sqrt((xi - xj)**2)


    