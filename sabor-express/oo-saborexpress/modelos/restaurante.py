class Restaurante: 
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False #o underline indica que o "ativo" é privado, então as pessoas terão que usar a propriedade (property)
        Restaurante.restaurantes.append(self)
    
    def __str__(self): #em formato de string
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}")
        
    @property #modificar como o atributo será lido
    def ativo(self):
        return "✔️" if self._ativo else "❌"

    def alternar_estado(self):
        self._ativo = not self._ativo
        

restaurante_snake = Restaurante("snake", "Japonesa")
restaurante_snake.alternar_estado()
restaurante_renato = Restaurante("renato", "Lanches")


Restaurante.listar_restaurantes()