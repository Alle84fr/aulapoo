# print("Modifique a classe de finconario para atributos privados e crie métodos \n")
class Funcionario:
    def __init__(self, nome:str, cargo:str, salario:float):
        self.__nome = nome
        self.__cargo = cargo 
        self.__salario = round(salario,2) #aqui deico apenas 2 casas depois da vírgula

#get recebe, sem parameto e com retorno

    def get_nome(self):     #self vincula o valor ao nome
        return self.__nome
    
#set modifica o valor da chave, tem parametro e sem retorno

    def set_nome(self, nome):     #set muda o valor do atributo
        self.__nome = nome
    
    def get_cargo(self):     
        return self.__cargo

    def set_cargo(self, cargo):     
        self.__cargo = cargo
    
    def get_salario(self):     
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")


# Programa principal

funcionario1 = Funcionario("João", "Desenvolvedor", 5000)

print("Nome:", funcionario1.get_nome())

print("Cargo:", funcionario1.cargo)

print("Salário:", funcionario1.salario)

funcionario2 = Funcionario("Maria", "Gerente de Projetos", 7000)

print("Nome:", funcionario2.nome)

print("Cargo:", funcionario2.cargo)

print("Salário:", funcionario2.salario)