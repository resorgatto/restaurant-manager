class restaurante: 
    nome = ""
    categoria = ""
    ativo = False

restaurante_snake = restaurante()
restaurante_snake.nome = "Snake"
restaurante_snake.categoria = "Japonesa"
restaurante_renato = restaurante()

restaurantes = [restaurante_snake, restaurante_renato]

print (restaurantes)