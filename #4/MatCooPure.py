import random

class MatCooPure():

    def __init__(self, n, m, n_non_null):

        self.n = n
        self.m = m
        self.non_n = n_non_null

        # Tous les coordonees possibles
        p = [(i,j) for i in range(n) for j in range(m)]

        # On prend n_non_null coordonees aleatoires
        coords = random.sample(p, n_non_null)

        self.matrice = []
        
        # Le résultat sont de triples (i, j, valeur) avec les coordonees tirees au hasard + valeur rand 
        for k in range(n_non_null):
            self.matrice.append((coords[k][0], coords[k][1], random.random()))

    @classmethod
    def identity(cls, n, m):
        cls.matrice = []

        for k in range(n):
            cls.matrice.append((k+1, k+1, 1))

        return cls



mat = MatCooPure(1,1,1).identity(10, 10).matrice
print(mat)