from django.test import TestCase
import numpy as np
from analise import analyse as ana
from analise import analysisCaller as ac

class AnaliseTest(TestCase):

    def setUp(self):
        self.data = np.array([
            [9,2,5,8],
            [6,1,3,2],
            [8,4,6,8],
            [7,1,2,6],
            [10,5,6,9],
            [6,2,4,7]
        ])
        self.data2 = np.array([
            [1,9,2,5,8,7],
            [2,6,1,3,2,8],
            [3,8,4,6,8,3],
            [4,7,1,2,6,2],
            [5,10,5,6,9,1],
            [6,6,2,4,7,0]
        ])
        self.data3 = np.array([
            [
                [1,9,2,5,8,7],
                [2,6,1,3,2,8],
                [3,8,4,6,8,3],
                [4,7,1,2,6,2],
                [5,10,5,6,9,5],
                [6,6,2,4,7,4]
            ],
            [
                [7,3,2,9,8,2],
                [8,4,1,3,4,3],
                [9,5,4,7,5,6],
                [10,2,2,3,6,0]
            ]
	    ])
        self.ci = np.array([[0,1,"c1"],[2,4,"c2"]])

    def test_icc(self):
        resultado_esperado = 0.289763779528 #para o icc2_1
        self.assertAlmostEqual(resultado_esperado, ana.icc2_1(self.data))
        resultado_esperado = 0.607528065155 #para o icc2_k
        self.assertAlmostEqual(resultado_esperado, ana.icc2_k(self.data))
        resultado_esperado = 0.714840714841  #para o icc3_1
        self.assertAlmostEqual(resultado_esperado, ana.icc3_1(self.data))
        resultado_esperado = 0.909315542377  #para o icc3_k
        self.assertAlmostEqual(resultado_esperado, ana.icc3_k(self.data))

    def test_pearson(self):
        resultado_esperado = [
            [1, 0.74535599, 0.725, 0.75017728],
            [0.74535599, 1, 0.89442719, 0.72932496],
            [0.725, 0.89442719, 1, 0.71756088],
            [0.75017728, 0.72932496, 0.71756088, 1, ]
        ]
        resultado_obtido = ana.pearson(self.data)
        self.assertEqual(len(resultado_esperado), len(resultado_obtido))

        for i in range(0, len(resultado_esperado)):
            self.assertEqual(len(resultado_esperado[i]), len(resultado_obtido[i]))
            for j in range(0, len(resultado_esperado[i])):
                self.assertAlmostEqual(resultado_esperado[i][j], resultado_obtido[i][j])

    def test_spearman(self):
        resultado_esperado = [
            [1, 0.71649772, 0.70588235, 0.88235294],
            [0.71649772, 1, 0.95533029, 0.94040326],
            [0.70588235, 0.95533029, 1, 0.89705882],
            [0.88235294, 0.94040326, 0.89705882, 1]
        ]
        resultado_obtido = ana.spearman(self.data)
        self.assertEqual(len(resultado_esperado), len(resultado_obtido))

        for i in range(0, len(resultado_esperado)):
            self.assertEqual(len(resultado_esperado[i]), len(resultado_obtido[i]))
            for j in range(0, len(resultado_esperado[i])):
                self.assertAlmostEqual(resultado_esperado[i][j], resultado_obtido[i][j])

    def test_shapiro_wilk(self):
        w_esperado = 0.9439817070960999
        p_value_esperado = 0.19998089969158173

        w_obtido, p_value_obtido = ana.shapiro_wilk(self.data)
        self.assertAlmostEqual(w_esperado, w_obtido)
        self.assertAlmostEqual(p_value_esperado, p_value_obtido)

    def test_analysisCaller(self):
        #flag 0
        resultado_esperado = np.array([np.array([5.08333333,  0.99146722]), np.array([4.83333333,  0.5443299])])
        resultado_obtido = ac.createReport(0, self.data2, self.ci)
        self.assertEqual(len(resultado_esperado), len(resultado_obtido))
        for i in range(0, len(resultado_esperado)):
            self.assertEqual(len(resultado_esperado[i]), len(resultado_obtido[i]))
            for j in range(0, len(resultado_esperado[i])):
                self.assertAlmostEqual(resultado_esperado[i][j], resultado_obtido[i][j])                

        #flag 1 
        #Lista total
        resultado_esperado = [
                    #Lista 1
                    [
                        #media do construct1, alpha do construct1
                        np.array([4.2, 0.9585048]),
                        #media do construct2, alpha do construct2
                        np.array([5.03333333, 0.65199674]),
                        #np.array de correlacao dos Constructs para a empresa
                        np.array([
                                [1, 0.68711656],
                                [0.68711656,  1]
                            ]),
                        #Icc para a empresa
                        0.64731653888280405
                    ],
                    #Lista 2
                    [
                        #time 1
                        [
                            #media do construct1 pro time 1, alpha do construct1  pro time 1
                            np.array([5.08333333, 0.99146722]),
                            #media do construct2 pro time 1, alpha do construct2  pro time 1
                            np.array([5.27777778, 0.5006135 ])
                        ],
                        [
                            #media do construct1 pro time 2, alpha do construct1  pro time 2
                            np.array([2.875, 0.74666667]),
                            #media do construct2 pro time 2, alpha do construct2  pro time 2
                            np.array([4.66666667, 0.5914787 ])
                        ]
                    ]
                ]
        resultado_obtido = ac.createReport(1, self.data3, self.ci) 
        self.assertEqual(len(resultado_esperado), len(resultado_obtido))
        lista1_esperada = resultado_esperado[0] 
        lista1_obtida = resultado_obtido[0]
        lista2_esperada = resultado_esperado[1]
        lista2_obtida = resultado_obtido[1]
        self.assertEqual(len(lista1_esperada), len(lista1_obtida))
        self.assertEqual(len(lista2_esperada), len(lista2_obtida))
        
        for i in range(0, len(lista1_esperada)):
            if type(lista1_esperada[i]) == float:
                self.assertEqual(lista1_esperada[i], lista1_obtida[i])
            else:
                self.assertEqual(len(lista1_esperada[i]), len(lista1_obtida[i]))
                for j in range(0, len(lista1_esperada[i])):
                    if type(lista1_esperada[i][j]) != np.ndarray:
                        self.assertAlmostEqual(lista1_esperada[i][j], lista1_obtida[i][j])
                    else:
                        self.assertEqual(len(lista1_esperada[i][j]), len(lista1_obtida[i][j]))
                        for n in range(0, len(lista1_esperada[i][j])):
                            self.assertAlmostEqual(lista1_esperada[i][j][n], lista1_obtida[i][j][n])

        for k in range(0, len(lista2_esperada)):
            for i in range(0, len(lista2_esperada[k])):
                self.assertEqual(len(lista2_esperada[k][i]), len(lista2_obtida[k][i]))
                for j in range(0, len(lista2_esperada[k][i])):
                    self.assertAlmostEqual(lista2_esperada[k][i][j], lista2_obtida[k][i][j])
            
