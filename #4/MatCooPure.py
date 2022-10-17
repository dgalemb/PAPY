import random
from sys import getsizeof
import numpy as np

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
            self.matrice.append((coords[k][0], coords[k][1], round(random.random(),2)))

    @classmethod
    def identity(cls, n, m):
        cls.n = n
        cls.m = m
        cls.non_n = n
        
        cls.matrice = []

        for k in range(n):
            cls.matrice.append((k, k, 1))

        return cls

    def affichage(self, limit_n, limit_m, printt = True):

        aux = [[0 for p in range(limit_m)] for l in range(limit_n)]

        for k in range(self.non_n):
            if self.matrice[k][0] < limit_n and self.matrice[k][1] < limit_m:
                aux[self.matrice[k][0]][self.matrice[k][1]] = self.matrice[k][2]
        if printt:
            print('\n'.join([''.join(['{:.3f}  '.format(item) for item in row]) 
            for row in aux]), '\n')

            print(f'On montre un morceau {limit_n} x {limit_m} ( à partir de (1,1) ) d une matrice {self.n} x {self.m}')
            print(f'La matrice prend {getsizeof(aux)} octets')

        return aux

    @staticmethod
    def mat_vec(mat, vec):
        mat = mat.affichage(mat.n, mat.m, False)
        
        result = [[0 for k in range(1)] for o in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result[i][0] += mat[i][j] * vec[j]

        return result

    @staticmethod
    def mat_vec_rap(mat, vec):
        if mat.m != len(vec):
            return 'Produit nest pas possible'
        else:
            vec = [(k, []) for k in vec]
            for k in range(mat.non_n):
                vec[mat.matrice[k][1]][1].append({mat.matrice[k][0]: mat.matrice[k][2] * vec[mat.matrice[k][1]][0]})

        return vec




mat = MatCooPure(3, 3, 9)
mat.affichage(3, 3)

print(mat.mat_vec(mat, vec = [2, 1, 1]))
#print(mat.matrice)

matr = np.matrix(MatCooPure(3, 3, 9).affichage(3, 3, printt = False))
vecc = np.array([2,1,1])
print(np.dot(matr, vecc))