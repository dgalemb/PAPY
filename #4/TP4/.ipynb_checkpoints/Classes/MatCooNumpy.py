import random
import time
from sys import getsizeof
import numpy as np

class MatCooNp:

    def __init__(self, n, m, n_non_null):
        
        self.n = n
        self.m = m
        self.non_n = n_non_null

        # Tous les coordonees possibles
        p = [np.array((i,j)) for i in np.arange(n) for j in np.arange(m)]

        # On prend n_non_null coordonees aleatoires
        coords = random.sample(p, n_non_null)

        self.matrice = np.array([])
        
        # Le résultat sont de triples (i, j, valeur) avec les coordonees tirees au hasard + valeur rand 
        for k in np.arange(n_non_null):
            self.matrice = np.append(self.matrice, (coords[k][0], coords[k][1], round(random.random(), 2)))
