import re

import numpy as np
import pandas as pd


# ============================================================
# LIMPEZA
# ============================================================

def clean_column_name(value):

    value = str(value)

    value = value.replace("\n", " ")

    value = re.sub(
        r"\s+",
        " ",
        value
    )

    return value.strip().rstrip("*").strip()


# ============================================================
# NÚMEROS
# ============================================================

def extract_numbers(value):

    if pd.isna(value):

        return []

    text = str(value)

    text = (
        text
        .replace("R$", "")
        .replace("kg", "")
        .replace("ha", "")
        .replace(",", ".")
    )

    found = re.findall(
        r"\d+(?:\.\d+)?",
        text
    )

    return [
        float(number)
        for number in found
    ]


# ============================================================
# PONTO MÉDIO
# ============================================================

def midpoint(value):

    numbers = extract_numbers(value)

    if not numbers:

        return np.nan

    text = str(value).lower()

    if len(numbers) >= 2:

        return (
            numbers[0] +
            numbers[1]
        ) / 2

    number = numbers[0]

    if (
        "até" in text
        or "abaixo" in text
    ):

        return number / 2

    return number


# ============================================================
# CONVERSÃO NUMÉRICA
# ============================================================

def numeric_series(series):

    return (
        series
        .dropna()
        .astype(str)
        .map(midpoint)
        .dropna()
    )


# ============================================================
# FREQUÊNCIA
# ============================================================

def frequency_table(series):

    values = (
        series
        .dropna()
        .astype(str)
        .str.strip()
    )

    counts = values.value_counts()

    total = counts.sum()

    if total == 0:

        return pd.DataFrame(
            columns=[
                "Categoria",
                "Frequência",
                "Percentual"
            ]
        )

    return pd.DataFrame({

        "Categoria": counts.index,

        "Frequência": counts.values,

        "Percentual": (
            counts.values /
            total *
            100
        ).round(2)

    })


# ============================================================
# ESTATÍSTICA
# ============================================================

def statistics(series):

    values = numeric_series(series)

    if len(values) == 0:

        return {}

    mode = values.mode()

    return {

        "n": int(values.count()),

        "mean": float(values.mean()),

        "median": float(values.median()),

        "mode": (
            float(mode.iloc[0])
            if len(mode)
            else None
        ),

        "q1": float(
            values.quantile(.25)
        ),

        "q3": float(
            values.quantile(.75)
        ),

        "min": float(
            values.min()
        ),

        "max": float(
            values.max()
        ),

        "std": float(
            values.std()
        )
    }


# ============================================================
# DADOS AGRUPADOS
# ============================================================

def grouped_table(series):

    frequencies = (
        series
        .dropna()
        .astype(str)
        .value_counts()
    )

    rows = []

    for label, frequency in frequencies.items():

        middle = midpoint(label)

        rows.append({

            "Classe":
                label,

            "Ponto médio":
                middle,

            "Frequência":
                int(frequency),

            "fx":
                (
                    middle *
                    frequency
                    if pd.notna(middle)
                    else np.nan
                )
        })

    table = pd.DataFrame(rows)

    if len(table):

        table[
            "Frequência acumulada"
        ] = table[
            "Frequência"
        ].cumsum()

    return table
