# Representa um unico commit no historico de versoes.
class Commit:
    # O construtor inicializa os dados do commit.
    # O pai e opcional porque o primeiro commit do projeto nao tem pai.
    def __init__(self, identificador, mensagem, autor, pai=None):
        self.id = identificador
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Imprime os dados deste commit e chama recursivamente o commit pai.
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")

        # Caso base: se nao tiver pai, encerramos a recursao sem usar else
        if self.pai is None:
            return

        self.pai.historico()


# Gerencia o conjunto de commits e o ponteiro para o commit mais recente.
class Repositorio:
    # Inicializa o repositorio com nome, autor, sem commits e contador zerado.
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0

    # Cria um novo commit com id unico e atualiza o head para apontar para ele.
    def commitar(self, mensagem):
        self.contador += 1
        novo_commit = Commit(self.contador, mensagem, self.autor, self.head)
        self.head = novo_commit

    # Exibe o historico completo a partir do commit mais recente (head).
    def log(self):
        # Se nao houver nenhum commit registrado, avisa e retorna antecipadamente
        if self.head is None:
            print("Nenhum commit ainda")
            return

        self.head.historico()

    # Conta o numero total de commits percorrendo a corrente de pais ate o inicio.
    def total_de_commits(self):
        total = 0
        atual = self.head
        while atual is not None:
            total += 1
            atual = atual.pai
        return total


# Teste do repositorio com dados reais
repositorio = Repositorio("meu-projeto", "Matheus Ramos - SEU_RA_AQUI")
repositorio.log()
repositorio.commitar("Cria a estrutura inicial do projeto")
repositorio.commitar("Adiciona a documentacao de instalacao")
repositorio.commitar("Atualiza instrucoes no README")
repositorio.log()
print(repositorio.total_de_commits())
