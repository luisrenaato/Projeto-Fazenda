import random

import pandas as pd


OPTIONS = {

    "Qual a raça do animal": [
        "Nelore",
        "Angus",
        "Brahman",
        "Gir Leiteiro",
        "Holandês",
        "Outro"
    ],

    "Com que frequência o animal é pesado?": [
        "Semanalmente",
        "Quinzenalmente",
        "Mensalmente",
        "A cada 3 meses ou mais"
    ],

    "Qual o peso médio dos animais?": [
        "Até 180 kg",
        "181 kg - 240 kg",
        "241 kg - 400 kg",
        "401 kg - 500 kg",
        "Acima de 501 kg"
    ],

    "Qual é o principal tipo de alimento fornecido ao animal?": [
        "Pastagem",
        "Ração",
        "Silagem",
        "Feno"
    ],

    "Quantas vezes por dia o animal recebe alimentação fornecida pelo produtor?": [
        "1 vez",
        "2 vezes",
        "3 vezes",
        "4 vezes ou mais"
    ],

    "Como é a disponibilidade de água para os animais?": [
        "Natural",
        "Bebedouros",
        "Ambos",
        "Não há disponibilidade adequada"
    ],

    "Qual o gasto mensal com a alimentação dos animais?": [
        "Até R$50 por cabeça",
        "R$51 - R$100 por cabeça",
        "R$101 - R$200 por cabeça",
        "R$201 - R$300 por cabeça",
        "Acima de R$301 por cabeça"
    ],

    "Qual o sistema de criação predominante?": [
        "Extensivo",
        "Semi intensivo",
        "Intensivo",
        "Confinamento"
    ],

    "Qual é a principal finalidade da criação?": [
        "Corte",
        "Leite",
        "Reprodução",
        "Mista"
    ],

    "Qual é o tipo predominante de pastagem?": [
        "Pastagem natural",
        "Pastagem cultivada",
        "Pastagem consorciada",
        "Não utiliza pastagem"
    ],

    "Qual é a temperatura média da região onde os animais são criados?": [
        "Abaixo de 18°C",
        "18°C - 22°C",
        "23°C - 27°C",
        "28°C - 32°C",
        "Acima de 32°C"
    ],

    "Como você classifica a frequência de períodos de calor intenso na região?": [
        "Raramente",
        "Algumas vezes ao ano",
        "Frequentemente",
        "Quase sempre"
    ],

    "Como é a disponibilidade de água durante períodos de seca?": [
        "Não é afetada",
        "Diminui pouco",
        "Diminui bastante",
        "Falta água"
    ],

    "Com que frequência os animais apresentam problemas de saúde?": [
        "Nunca ou raramente",
        "Algumas vezes ao ano",
        "Mensalmente",
        "Frequentemente"
    ],

    "Existe mortalidade de animais no rebanho?": [
        "Não",
        "Sim, baixa",
        "Sim, moderada",
        "Sim, alta"
    ],

    "Como é feita a identificação dos animais?": [
        "Brinco",
        "Marca",
        "Identificação eletrônica",
        "Não são identificados",
        "Outro"
    ],

    "Qual a média de ganho de peso dos animais por mês?": [
        "Até 5 kg",
        "6 kg - 10 kg",
        "11 kg - 20 kg",
        "21 kg - 30 kg",
        "Acima de 31 kg",
        "Não acompanha"
    ],

    "Como você avalia o desempenho geral do rebanho?": [
        "Muito baixo",
        "Baixo",
        "Regular",
        "Bom",
        "Muito bom"
    ],

    "Os animais possuem acesso a sombra durante o dia?": [
        "Sim, em toda a área",
        "Sim, em parte da área",
        "Pouca disponibilidade",
        "Não"
    ],

    "Qual tipo de suplementação o animal recebe?": [
        "Não recebe suplementação",
        "Mineral",
        "Proteica",
        "Energética"
    ]
}


def make_demo_data(n=45):

    random.seed(21)

    data = {}

    for question, choices in OPTIONS.items():

        data[question] = random.choices(
            choices,
            k=n
        )

    return pd.DataFrame(data)
