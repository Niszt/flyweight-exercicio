import sys
import random

class EspecieArvore:
    def __init__(self, id_raca_arvore, nome_raca_arvore, textura):
        self.id = id_raca_arvore
        self.raca_arvore = nome_raca_arvore
        self.textura = textura 
        self.instancias_dados = [] 

    def adicionar_arvore(self, altura, pos_x, pos_y):
        self.instancias_dados.append((altura, pos_x, pos_y))

    def DRAW(self):
        for altura, pos_x, pos_y in self.instancias_dados:
            pass


class ArvoreFactory:
    def __init__(self):
        self.instancias = {} 
        
    def get_instancia(self, id_raca_arvore):
        if id_raca_arvore in self.instancias:
            return self.instancias[id_raca_arvore]
        else:
            nova_especie = EspecieArvore(id_raca_arvore, f"raca_arvore_{id_raca_arvore}", "Textura_Base64_")
            self.instancias[id_raca_arvore] = nova_especie
            return nova_especie

factory = ArvoreFactory()


def main():
    QTD_ARVORES_SIMULACAO = 1000000
    QTD_raca_arvoreS = 5
    
    for _ in range(QTD_ARVORES_SIMULACAO):
        id_esp = random.randint(1, QTD_raca_arvoreS)
        altura = random.uniform(2.0, 30.0)
        pos_x = random.randint(0, 10000)
        pos_y = random.randint(0, 10000)
        
        especie = factory.get_instancia(id_esp)
        especie.adicionar_arvore(altura, pos_x, pos_y)
        
    for id_esp, especie in factory.instancias.items():
        especie.DRAW()


    primeira_especie = factory.get_instancia(1)
    tamanho_tupla = sys.getsizeof(primeira_especie.instancias_dados[0])
    for item in primeira_especie.instancias_dados[0]:
        tamanho_tupla += sys.getsizeof(item)

    print("\n" + "-"*20)
    print("memoria usada")
    print("-"*20)
    print(f"Custo de 1 Árvore em Tupla: {tamanho_tupla} bytes")
    
    memoria_total_megas = (tamanho_tupla * QTD_ARVORES_SIMULACAO) / (1024*1024)
    print(f"RAM tot para 1 Mi de arvores: {memoria_total_megas:.2f} MB")
    
    print("-" * 20)
    print("tot para 39 trilhoes de arvores:")
    gigas_total = (tamanho_tupla * 39000000000) / (1024**3)
    
    print(f"ram Exigida: {gigas_total:,.2f} GB")
    print("-"*20)

if __name__ == "__main__":
    main()
