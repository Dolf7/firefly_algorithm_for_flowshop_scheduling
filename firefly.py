from random import random
from math import exp
from math import e 
from math import sqrt
import numpy as np


class firefly_algo:

    def __init__(self,data, population:int, max_iter:int, low_bound=0, up_bound=1, gamma=0.01, alpha=0.1, beta=0.2, delta=0.97):
        self.data = data #store pos
        self.population = population
        self.iter = max_iter;
        self.low_bound = low_bound
        self.up_bound = up_bound
        self.gamma = gamma
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.scale = abs(up_bound - low_bound)
        self.fitness_value = self.fitness_set_all() 
        self.movement = [] # store the history of pos
        self.movement_fitness = [] # store the history of cost
    
    def fitness_function(self, x):
        return x**2
    
    def fitness_set_all(self): # count the cost
        mod_data = []
        for i in self.data:
            mod_data.append(self.fitness_function(i))
        return mod_data;

    def run(self):
        # print(self.data)
        for x in range(self.iter):
            for i in range(self.population):
                for j in range(self.population):
                    if(self.fitness_value[j] < self.fitness_value[i]):
                        if i == j: 
                            continue
                        self.data[i], updated_stat = self.move_to(i, j)
                        if updated_stat:
                            self.fitness_value[i] = self.fitness_function(self.data[i])
            self.movement.append(self.data)
            self.movement_fitness.append(self.fitness_value)
    
    # def run(self):
    # # Pre-calculate distances for efficiency
    #     distances = np.zeros((self.population, self.population))
    #     for i in range(self.population):
    #         for j in range(i + 1, self.population):  # Avoid redundant calculations
    #             distances[i, j] = self.distance(self.data[i], self.data[j])
    #             distances[j, i] = distances[i, j]  # Mirror for efficiency

    #     for x in range(self.iter):
    #         for i in range(self.population):
    #             # Find the brightest firefly (excluding itself)
    #             brightest_index = np.argmin(self.fitness_value)
    #             if i != brightest_index:
    #                 # Update position based on the brightest firefly
    #                 self.data[i], updated_stat = self.move_to(i, brightest_index, distances)
    #                 if updated_stat:
    #                     self.fitness_value[i] = self.fitness_function(self.data[i])
    #         self.movement.append(self.data.copy())  # Copy data to avoid memory leaks
    #         self.movement_fitness.append(self.fitness_value.copy())




    def move_to(self, x, y):
        data_x = self.data[x]
        data_y = self.data[y]

        new_x = data_x + self.beta*(e**(self.gamma*-1 * (self.distance(data_x, data_y)**2)))*(data_x - data_y) + self.alpha * self.gamma * (self.generate_random() - 0.5) * self.scale

        if new_x < data_x:
            return new_x, True
        return data_x, False

    def distance(self, xi:float, xj:float):
        return sqrt((xi - xj)**2)
    
    def generate_random(self):
        return random()
    
    def print_result(self):
        for i in self.data:
            print(f'{i:.3f}')

    