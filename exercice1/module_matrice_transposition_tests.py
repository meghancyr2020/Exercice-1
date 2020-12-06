import unittest

from arreter_programme import MauvaiseEntreeException
from module_matrice import transposition
from utils import TestBasique


class ModuleMatriceTranspositionTest(TestBasique):

    def test_mauvaises_matrices(self):
        mauvaisesMatrices = [
            [[]],
            [[1, 2], [1, float('nan')]],
            [[1, 2], [1, float('inf')]],
            [[1, 10], [1, float('-inf')]],
            [[1, 2, 3], [-1, -2, -3], [0, 0, 0], [0]]
        ]
        for matrice in mauvaisesMatrices:
            def fonction():
                try:
                    transposition(matrice)
                    self.fail(
                        f'{matrice} n\'est pas une matrice valide. La fonction transposition() devrait appeler la fonction arreter_programme() quand un tel cas survient')
                except MauvaiseEntreeException:
                    pass
            self.executerTest(fonction, f'transposition({matrice})')

    def test_transposition(self):
        casDeTests = [
            ([[1]], [[1]]),
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]],
             [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            ([[1, 1], [2, 2], [3, 3]], [[1, 2, 3], [1, 2, 3]]),
            ([[1, 2, 3], [1, 2, 3]], [[1, 1], [2, 2], [3, 3]]),
        ]
        for matrice, matriceAttendue in casDeTests:
            def fonction():
                matriceObtenue = transposition(matrice)
                self.assertEqual(
                    matriceObtenue,
                    matriceAttendue,
                    f'La matrice retournée par l\'appel fonction transposition({matrice}) n\'est pas valide. La valeur attendue est {matriceAttendue}. La valeur obtenue est {matriceObtenue}.')
            self.executerTest(fonction, f'transposition({matrice})')


if __name__ == '__main__':
    unittest.main(verbosity=2)
