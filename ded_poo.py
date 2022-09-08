class Raca:
    def __init__(self, tamanho, deslocamento, idioma, bonus, penalidade):
        self.tamanho = tamanho
        self.deslocamento = deslocamento
        self.idioma = idioma
        self.bonus = bonus
        self.penalidade = penalidade
        
class Dwarf(Raca):
        def __init__(self, tamanho, deslocamento, idioma, bonus, penalidade, proeficiencia = "Lapidacao"):
            self.proeficiencia = proeficiencia
            super().__init__(tamanho, deslocamento, idioma, bonus, penalidade)

        def get_personagem(self):   
            return f"Atributos do personagem, respectivamente, são: {self.tamanho}, {self.deslocamento}, {self.idioma}, {self.bonus}, {self.penalidade} e {self.proeficiencia}."

Oona = Dwarf('Medio',6,'Comum','Constituição','Carisma', 'Navegacao')      

personagem1 = Oona.get_personagem()
print(personagem1)






        
        
        
        
        
 