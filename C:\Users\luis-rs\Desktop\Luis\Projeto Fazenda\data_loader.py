import io
import re

import pandas as pd
import requests
import streamlit as st

from analytics import clean_column_name
from demo_data import make_demo_data


# ============================================================
# TRANSFORMA LINK DO SHEETS EM CSV
# ============================================================

def sheet_to_csv_url(url):

    match = re.search(
        r"/spreadsheets/d/([a-zA-Z0-9_-]+)",
        url
    )

    if not match:

        raise ValueError(
            "Link do Google Sheets inválido."
        )

    sheet_id = match.group(1)

    gid_match = re.search(
        r"[?&#]gid=([0-9]+)",
        url
    )

    gid = (
        gid_match.group(1)
        if gid_match
        else "0"
    )

    return (
        f"https://docs.google.com/spreadsheets/d/"
        f"{sheet_id}/export?format=csv&gid={gid}"
    )


# ============================================================
# LEITURA
# ============================================================

@st.cache_data(ttl=60)
def read_sheet(url):

    csv_url = sheet_to_csv_url(url)

    response = requests.get(
        csv_url,
        timeout=20
    )

    response.raise_for_status()

    if (
        "<html" in
        response.text[:500].lower()
    ):

        raise ValueError(
            "A planilha não está pública."
        )

    dataframe = pd.read_csv(
        io.StringIO(
            response.text
        )
    )

    return dataframe


# ============================================================
# NORMALIZAÇÃO
# ============================================================

def normalize(dataframe):

    dataframe = dataframe.copy()

    dataframe.columns = [

        clean_column_name(column)

        for column in dataframe.columns
    ]

    # Não precisamos exibir timestamp.
    remove = []

    for column in dataframe.columns:

        lower = column.lower()

        if (
            "carimbo de data" in lower
            or lower == "timestamp"
        ):

            remove.append(column)

        if lower in {
            "e-mail",
            "email"
        }:

            remove.append(column)

    if remove:

        dataframe = dataframe.drop(
            columns=remove,
            errors="ignore"
        )

    return dataframe


# ============================================================
# CARREGAMENTO PRINCIPAL
# ============================================================

def load_data(sheet_url):

    try:

        dataframe = read_sheet(
            sheet_url
        )

        dataframe = normalize(
            dataframe
        )

        if dataframe.empty:

            raise ValueError(
                "A planilha ainda não possui respostas."
            )

        return dataframe, True

    except Exception as error:

        demo = make_demo_data()

        return demo, False


# ============================================================
# ERRO
# ============================================================

def get_sheet_error(sheet_url):

    try:

        dataframe = read_sheet(
            sheet_url
        )

        dataframe = normalize(
            dataframe
        )

        return None

    except Exception as error:

        return str(error)
