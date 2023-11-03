class Vagao:
    def __init__(self, numero_vagao):
        self.numero_vagao = numero_vagao
        self.proximo = None
        self.acoplado = None  # Indica se algo está acoplado ao vagão (pode ser uma máquina ou outro vagão)

class ComposicaoTremMetro:
    def __init__(self):
        self.cauda = None
        self.contagem = 0

    def adicionar_vagao(self, numero_vagao):
        novo_vagao = Vagao(numero_vagao)

        if not self.cauda:
            novo_vagao.proximo = novo_vagao  # Se a composição estiver vazia, o próximo é ele mesmo
            self.cauda = novo_vagao
        else:
            novo_vagao.proximo = self.cauda.proximo
            self.cauda.proximo = novo_vagao
            self.cauda = novo_vagao

        self.contagem += 1

    def acoplar_maquina(self, numero_maquina):
        if not self.cauda:
            return False  # Lista vazia

        self.cauda.acoplado = "Máquina " + str(numero_maquina)
        return True

    def acoplar_vagao(self, numero_vagao):
        if not self.cauda:
            return False  # Lista vazia

        self.cauda.acoplado = "Vagão " + str(numero_vagao)
        return True

    def remover_vagao(self, numero_vagao):
        if not self.cauda:
            return  # Lista vazia

        atual = self.cauda.proximo
        anterior = None

        while True:
            if atual.numero_vagao == numero_vagao:
                if atual == self.cauda:
                    if self.contagem == 1:
                        self.cauda = None
                    else:
                        self.cauda = anterior
                        self.cauda.proximo = atual.proximo
                    self.contagem -= 1
                    return
                else:
                    if atual == self.cauda.proximo:
                        self.cauda.proximo = self.cauda.proximo.proximo
                    anterior.proximo = atual.proximo
                    self.contagem -= 1
                    return

            anterior = atual
            atual = atual.proximo

            if atual == self.cauda.proximo:
                return  # O vagão não foi encontrado

    def encontrar_vagao(self, numero_vagao):
        if not self.cauda:
            return False  # Lista vazia

        atual = self.cauda.proximo

        while True:
            if atual.numero_vagao == numero_vagao:
                return True
            atual = atual.proximo
            if atual == self.cauda.proximo:
                return False  # O vagão não foi encontrado

    def obter_contagem_vagoes(self):
        return self.contagem

    def __str__(self):
        if not self.cauda:
            return "Composição vazia"

        info_vagoes = [f"Vagão {self.cauda.numero_vagao} ({self.cauda.acoplado})"]
        atual = self.cauda.proximo
        while atual != self.cauda:
            info_vagoes.append(f"Vagão {atual.numero_vagao} ({atual.acoplado})")
            atual = atual.proximo

        return "Composição do trem: " + " -> ".join(info_vagoes)

# Exemplo de uso
trem = ComposicaoTremMetro()

trem.adicionar_vagao(1)
trem.adicionar_vagao(2)
trem.adicionar_vagao(3)

print(trem)
print("Quantidade de vagões na composição:", trem.obter_contagem_vagoes())

trem.remover_vagao(2)
print("Vagão 2 removido")

print(trem)
print("Quantidade de vagões na composição após remoção:", trem.obter_contagem_vagoes())

trem.acoplar_maquina(101)
trem.acoplar_vagao(4)
print("Máquina 101 e Vagão 4 acoplados ao último vagão")

print(trem)
