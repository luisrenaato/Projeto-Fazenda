import pandas as pd
import plotly.express as px

from config import COLORS


def theme(fig):

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(255,253,246,.55)",

        font={
            "family": "DM Sans",
            "color": COLORS["ink"]
        },

        margin={
            "l": 20,
            "r": 20,
            "t": 65,
            "b": 35
        },

        title={
            "font": {
                "family": "Georgia",
                "size": 19,
                "color": COLORS["coffee"]
            }
        },

        hoverlabel={
            "bgcolor": COLORS["paper_light"],
            "font_color": COLORS["ink"]
        }
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor=COLORS["moss"],
        linewidth=1
    )

    fig.update_yaxes(
        gridcolor="#DCCFB8",
        linecolor=COLORS["moss"],
        linewidth=1
    )

    return fig


def bar(series, title):

    data = (
        series
        .dropna()
        .astype(str)
        .value_counts()
        .reset_index()
    )

    data.columns = [
        "Categoria",
        "Frequência"
    ]

    fig = px.bar(

        data,

        x="Categoria",

        y="Frequência",

        title=title,

        text_auto=True,

        color_discrete_sequence=[
            COLORS["moss"]
        ]
    )

    fig.update_traces(
        marker_line_color=COLORS["moss_dark"],
        marker_line_width=1
    )

    return theme(fig)


def donut(series, title):

    data = (
        series
        .dropna()
        .astype(str)
        .value_counts()
        .reset_index()
    )

    data.columns = [
        "Categoria",
        "Frequência"
    ]

    fig = px.pie(

        data,

        names="Categoria",

        values="Frequência",

        hole=.62,

        title=title,

        color_discrete_sequence=[
            COLORS["moss"],
            COLORS["moss_light"],
            COLORS["coffee"],
            COLORS["coffee_light"],
            "#B6A47D",
            "#8D8068"
        ]
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent"
    )

    return theme(fig)


def histogram(values, title):

    data = pd.DataFrame({
        "Valor": values
    })

    fig = px.histogram(

        data,

        x="Valor",

        nbins=10,

        title=title,

        color_discrete_sequence=[
            COLORS["moss"]
        ]
    )

    return theme(fig)


def boxplot(values, title):

    data = pd.DataFrame({
        "Valor": values
    })

    fig = px.box(

        data,

        y="Valor",

        title=title,

        points="all",

        color_discrete_sequence=[
            COLORS["moss"]
        ]
    )

    return theme(fig)


def scatter(data, title, x_title, y_title):

    fig = px.scatter(

        data,

        x="X",

        y="Y",

        title=title,

        color_discrete_sequence=[
            COLORS["moss"]
        ]
    )

    fig.update_traces(
        marker={
            "size": 10,
            "line": {
                "width": 1,
                "color": COLORS["moss_dark"]
            }
        }
    )

    fig.update_xaxes(
        title=x_title
    )

    fig.update_yaxes(
        title=y_title
    )

    return theme(fig)
