import json
import random
from models import Carta, Jogador

def carregar_cartas():
    with open("data/cards.json", "r", encoding="utf-8") as f:
        cartas_json = json.load(f)
    return [Carta(c["nome"], {k: v for k, v in c.items() if k != "nome"}) for c in cartas_json]

def dividir_baralho(cartas):
    random.shuffle(cartas)
    meio = len(cartas) // 2
    return cartas[:meio], cartas[meio:]

def escolher_atributo(carta):
    print(f"\nSua carta: {carta.nome}")
    for i, (atrib, valor) in enumerate(carta.atributos.items(), 1):
        print(f"{i} - {atrib}: {valor}")
    while True:
        escolha = input("Escolha um atributo (número): ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(carta.atributos):
            return list(carta.atributos.keys())[int(escolha)-1]
        print("Escolha inválida.")

def iniciar_jogo():
    print("=== SUPER TRUNFO ===")

    cartas = carregar_cartas()
    baralho_jogador, baralho_computador = dividir_baralho(cartas)

    jogador = Jogador("Você")
    computador = Jogador("Computador")
    jogador.baralho = baralho_jogador
    computador.baralho = baralho_computador

    rodada = 1
    while jogador.tem_cartas() and computador.tem_cartas():
        print(f"\n--- Rodada {rodada} ---")
        carta_jogador = jogador.puxar_carta()
        carta_pc = computador.puxar_carta()

        atributo = escolher_atributo(carta_jogador)

        valor_jogador = carta_jogador.atributos[atributo]
        valor_pc = carta_pc.atributos[atributo]

        print(f"Você: {valor_jogador} vs Computador: {valor_pc}")

        if valor_jogador > valor_pc:
            print("Você venceu a rodada!")
            jogador.ganhar_cartas([carta_jogador, carta_pc])
        elif valor_pc > valor_jogador:
            print("Computador venceu a rodada!")
            computador.ganhar_cartas([carta_jogador, carta_pc])
        else:
            print("Empate! Cada um mantém sua carta.")
            jogador.ganhar_cartas([carta_jogador])
            computador.ganhar_cartas([carta_pc])

        rodada += 1

    if jogador.tem_cartas():
        print("\nParabéns! Você venceu o jogo!")
    else:
        print("\nFim de jogo. O computador venceu!")
