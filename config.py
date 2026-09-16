# ============================================================
# PROJETO FAZENDA
# CONFIGURAÇÕES
# ============================================================

SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1IH9S__uyU11xFJYprjBrnsidPENbqzpfXx-cZ51QjhI/"
    "edit?gid=1297145970#gid=1297145970"
)

FORM_URL = (
    "https://docs.google.com/forms/d/"
    "1fQs4M3DzqVW0x3IgkyLTNW_Fl9gDZPPVAsC7bxSOSBw/viewform"
)


APP_NAME = "Projeto Fazenda"

APP_SUBTITLE = (
    "Leitura estatística do rebanho, "
    "do manejo e do ambiente de criação."
)


# ============================================================
# IDENTIDADE VISUAL
# ============================================================

COLORS = {

    # papel
    "paper": "#EDE2CC",
    "paper_light": "#F6EEDC",
    "paper_dark": "#DCCAA9",

    # café
    "coffee": "#5A402C",
    "coffee_dark": "#39291E",
    "coffee_light": "#9A7652",

    # verde musgo
    "moss": "#536B45",
    "moss_dark": "#354932",
    "moss_light": "#788A67",

    # texto
    "ink": "#2E2B25",
    "muted": "#746B5E",

    # branco de papel
    "white": "#FFFDF6",
}


# ============================================================
# CAMPOS
# ============================================================

NUMERIC_FIELDS = [

    "Qual a quantidade de gado que você possui?",

    "Qual o peso médio dos animais?",

    "Qual o gasto mensal com a alimentação dos animais?",

    "Qual é o tamanho aproximado da área utilizada para criação?",

    "Qual é a temperatura média da região onde os animais são criados?",

    "Qual a média de ganho de peso dos animais por mês?",
]


# Perguntas usadas nos filtros.
FILTER_FIELDS = [

    "Qual a raça do animal",

    "Qual o sistema de criação predominante?",

    "Qual é a principal finalidade da criação?",
]
