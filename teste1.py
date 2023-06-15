class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome=nome
        self.idade=idade
        self.cpf= cpf
        
        
    def apresentar(self):
        print('Ola meu nome é: ',self.nome)   
        
    def envelhecer(self,anos):
        self.idade += anos
    
            
pessoa1 = Pessoa('Lucas',28)
pessoa2 = Pessoa('Laysa',70)
pessoa3 = Pessoa('Neymar',56)

pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()