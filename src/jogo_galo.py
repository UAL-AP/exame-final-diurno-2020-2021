# Regras
# 1. O número de estudante determina que funcionalidades deve implementar.
#    Verifique no comentário de cada método.
# 2. A variável jogo é um dicionário com a seguinte estrutura mínima:
#
#    jogo = {'jogadores': lista, 'tabuleiro': lista de listas}
#
# 3. Pode aumentar o dicionário jogo, desde que mantenha a estrutura mínima.
# 4. Não pode alterar a assinatura de qualquer método.
# 5. Não pode acrescentar métodos.
# 6. Não pode recorrer a bibliotecas externas à distribuição padrão Python 3.8.5


# IMPORTANTE: Indique o seu número de estudante em string, na variável de módulo
# `number`
number = "INDICAR NÚMERO DE ESTUDANTE"

# IMPORTANTE: A variável de módulo last_digit guarda o último dígito do número de aluno, e
# soma o valor 1. Vai ser utilizada para determinar que funcionalidades deve implementar.
last_digit = int(number[len(number)-1])+1

# Assumir que last_digit par.

def registar_jogador(jogo, nome):
    # Um jogador é representado com um dicionário com a seguinte estrutura
    # mínima:
    #
    # jogador = {'nome': string, 'vitorias': int}
    #
    # Se last_digit par: o nome deve ser guardado em maiúsculas, com espaços em branco removidos.
    #
    # Se last_digit ímpar: o nome deve guardado com os espaços em branco
    # convertidos em underscore.

    # Estratégia 1
    nome_jogador = "".join([x for x in nome if x != " "])

    # Estratégia 2
    nome_jogador = []
    for letra in nome:
        if letra != " ":
            nome_jogador.append(letra.upper())
    nome_jogador = "".join(nome_jogador)

    jogador = {

        "nome": nome_jogador,
        "vitorias": 0,
        "jogos": 0
    }
    jogo["jogadores"].append(jogador)


def existe_jogador(jogo, nome):
    # Retorna True se o jogador com o nome indicado estiver registado.
    for jogador in jogo["jogadores"]:
        if jogador["nome"] == nome:
            return True
    return False


def obter_jogadores(jogo):
    # Retorna uma lista de dicionários com a informação dos jogadores.
    return jogo["jogadores"]


def iniciar_jogo(jogo, nome_primeiro_jogador, marca_primeiro_jogador, nome_segundo_jogador, marca_segundo_jogador):
    # Deve criar o tabuleiro no dicionário jogo.
    jogo["tabuleiro"] = [[None for _ in range(3)] for _ in range(3)]
    for jogador in jogo["jogadores"]:
        if jogador["nome"] == nome_primeiro_jogador:
            primeiro_jogador = jogador
        if jogador["nome"] == nome_segundo_jogador:
            segundo_jogador = jogador
    jogo["em_curso"] = {
        "primeiro_jogador": primeiro_jogador,
        "marca_primeiro_jogador": marca_primeiro_jogador,
        "segundo_jogador": segundo_jogador,
        "marca_segundo_jogador": marca_segundo_jogador,
    }


def existe_jogo_em_curso(jogo):
    # Retorna True se estiver um jogo em curso.
    return jogo["em_curso"] is not None


def localizacao_valida(linha, coluna):
    # Retorna True se as localização indicada for válida, i.e., dentro de uma
    # grelha de 3x3.
    return linha > 0 and linha <=3 and coluna > 0 and coluna <= 3


def colocar_peca(jogo, nome_jogador, linha, coluna):
    # Retorna True se o jogo terminou (com vitória ou empate) depois de colocar
    # a peça. Retorna False caso contrário.
    #
    # Não é necessário verificar se já existe alguma peça na localização
    # indicada.
    #
    # Depois de colocar a peça, utiliza a função verificar_vitoria para
    # determinar se algum jogador ganhou.
    #
    # Se todas as posições do tabuleiro estiverem ocupadas, e nenhum jogador
    # ganhou, o jogo termina num empate.
    #
    # Se last_digit par: o empate soma uma vitória a cada jogador.
    #
    # Se last_digit ímpar: o empate não altera o número de vitorias dos
    # jogadores.
    pass


def verificar_vitoria(jogo):
    # Retorna True se o jogo em curso terminou em vitória.
    #
    # Se last_digit par: vitória apenas diagonal
    #
    # Se last_digit ímpar: vitória apenas horizontal e vertical
    pass
