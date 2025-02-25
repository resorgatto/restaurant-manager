import os

restaurantes = [{"Nome" : "snake", "Categoria" : "Italiano", "Ativo" : True },
                {"Nome" : "Renato", "Categoria" : "Lanches", "Ativo" : False}                
                
]

def exibir_nome_do_programa():
    print ("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
    print ("1. Cadastrar Restaurante")
    print ("2. Listar Restaurante")
    print ("3. Alternar estado do Restaurante")
    print ("4. Sair\n")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def finalizar_app():
    exibir_subtitulo("Finalizando o APP\n")

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto) + 4 ) 
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurante = {"Nome": nome_do_restaurante, "Categoria": categoria, "Ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo("Listando os Restaurantes\n")
    
    print (f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()
    
def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante ["Ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print (mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado!")   
    voltar_ao_menu_principal()
    

    
def escolher_opcoes():
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida
    except:
        opcao_invalida()
        
        
def main():
    os.system("cls")
    exibir_nome_do_programa()   
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()