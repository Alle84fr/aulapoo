# definior classe, em arquivo separado

class Triangulo:
    def __init__(self, a:int, b:int, c:int):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
    
    def calcularPerimetro(self): # não precisa passar parâmetro, só fazer a conta
        """
        calcula o perímetro de um triângulo
        """
        return self.ladoA+self.ladoB+self.ladoC