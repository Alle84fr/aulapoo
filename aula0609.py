class pessoas:
    def __init__ (self, nome:str, cpf:int):
        self.nome = nome
        self.__cpf = cpf    # 2 _ undersocre é o dica de atributo privado

dicio = pessoas ( "Victor", 12345654)
