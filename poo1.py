class Personagem:

    def __init__(self, nome, classe, raca):
        self.nome = nome
        self.classe = classe
        self.raca = raca
        # self.altura = altura
        # self.cor_cabelo = cor_cabelo
        # self.cor_olhos = cor_olhos
        # self.peso = peso
    def get_nome(self):
        return f"O personagem se chama {self.nome}"
    def get_classe(self):
        return f"O personagem tem a classe {self.classe}."
    def get_raca(self):
        return f"O personagem é da raca {self.raca}."
    # def get_altura(self):
    #     return f"O personagem se chama {self.altura}"
    # def get_cor_cabelo(self):
    #     return f"O personagem se chama {self.cor_cabelo}"
    # def get_cor_olhos(self):
    #     return f"O personagem se chama {self.cor_olhos}"
    # def get_peso(self):
    #     return f"O personagem se chama {self.peso}"
    
jogador1 = Personagem('Oona', 'Druida', 'Elfo')
jogador2 = Personagem ('Doppo', 'Pequenes', 'Ladino')
print("Primeiro Jogador")
print(jogador1.get_nome())
print(jogador1.get_classe())
print(jogador1.get_raca())
print("Segundo Jogador")
print(jogador2.get_nome())
print(jogador2.get_classe())
print(jogador2.get_raca())


        # segundo_jogador = Personagem ('Ladino', 'Pequenes', 'Doppo')
    
        # return f"{jogador1.nome} é da classe {jogador1.classe} e tem a raca{jogador1.raca}."
        # print(f'{segundo_jogador.nome} é da classe {segundo_jogador.classe} e tem a raca{segundo_jogador.raca}.')
    
    # def lore(self, lore):
    #     if self.nome == 'Oona':
    #         print(f'Lorem ipsum')
    #     if self.nome == 'Doppo':
    #         print(f'dolor sit amet')    
  
       
        
    
# class HogwartsHouse:
#     def __init__(self, name, color, founder):
#         self.name = name
#         self.color = color
#         self.founder = founder

#     def get_points_house(self):
#         return f"A casa {self.name} possui a pontuação total \
#                 de 50 pontos"

#     def play_quidditch(self):
#         return f"A pontuação do quadribol foi de 10 pontos"


# hufflepuff = HogwartsHouse('Lufa-Lufa',
#                            'Amarelo e Preto',
#                            'Helga Lufa-Lufa')

# points_house = hufflepuff.get_points_house()
# print('Pontuação =>', points_house)