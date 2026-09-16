import streamlit as st
import pandas as pd

from config import (
    SHEET_URL,
    FORM_URL,
    APP_NAME,
    APP_SUBTITLE,
    COLORS,
    NUMERIC_FIELDS,
    FILTER_FIELDS
)

from data_loader import (
    load_data
)

from analytics import (
    clean_column_name,
    numeric_series,
    frequency_table,
    statistics,
    grouped_table,
    midpoint
)

from charts import (
    bar,
    donut,
    histogram,
    boxplot,
    scatter
)


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(

    page_title=APP_NAME,

    page_icon="🐄",

    layout="wide",

    initial_sidebar_state="expanded"
)


# ============================================================
# IDENTIDADE VISUAL
# ============================================================

st.html(f"""

<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap'
);


/* ==========================================================
   BASE
   ========================================================== */

html,
body,
[data-testid="stAppViewContainer"] {{

    background:
        {COLORS["paper"]};

}}


.stApp {{

    color:
        {COLORS["ink"]};

    font-family:
        'DM Sans',
        sans-serif;

}}


.block-container {{

    max-width:
        1420px;

    padding:
        2rem 2.5rem 4rem;

}}


/* ==========================================================
   PAPEL MANCHADO DE CAFÉ
   ========================================================== */

[data-testid="stAppViewContainer"] {{

    background-color:
        {COLORS["paper"]};

    background-image:

        radial-gradient(
            ellipse at 12% 18%,
            rgba(94, 63, 35, .13) 0%,
            rgba(94, 63, 35, .07) 7%,
            transparent 18%
        ),

        radial-gradient(
            ellipse at 84% 72%,
            rgba(94, 63, 35, .10) 0%,
            rgba(94, 63, 35, .05) 8%,
            transparent 20%
        ),

        radial-gradient(
            ellipse at 65% 12%,
            rgba(82, 60, 38, .07) 0%,
            transparent 16%
        ),

        repeating-linear-gradient(
            0deg,
            rgba(82,60,38,.018) 0px,
            rgba(82,60,38,.018) 1px,
            transparent 1px,
            transparent 5px
        );

}}


/* ==========================================================
   SIDEBAR
   ========================================================== */

[data-testid="stSidebar"] {{

    background:
        {COLORS["coffee_dark"]};

    border-right:
        5px solid {COLORS["moss"]};

}}


[data-testid="stSidebar"] * {{
    color:
    #F7F0DF !important;
}}


/* ==========================================================
   TÍTULOS
   ========================================================== */

h1,
h2,
h3 {{

    font-family:
        Georgia,
        serif !important;

    color:
        {COLORS["coffee"]} !important;

}}


/* ==========================================================
   BORDA GERAL
   ========================================================== */

.paper-card {{

    background:
        rgba(255,253,246,.78);

    border:
        2px solid {COLORS["moss"]};

    border-radius:
        18px;

    box-shadow:
        5px 5px 0
        rgba(53,73,50,.13);

    padding:
        1.25rem;

}}


/* ==========================================================
   HERO
   ========================================================== */

.hero {{

    background:
        rgba(246,238,220,.86);

    border:
        3px solid {COLORS["moss"]};

    border-radius:
        26px;

    padding:
        2.2rem 2.5rem;

    box-shadow:
        8px 8px 0
        rgba(53,73,50,.16);

    position:
        relative;

    overflow:
        hidden;

}}


.hero::before {{

    content:
        "";

    position:
        absolute;

    inset:
        10px;

    border:
        1px dashed
        rgba(83,107,69,.45);

    border-radius:
        19px;

    pointer-events:
        none;

}}


.eyebrow {{

    color:
        {COLORS["moss"]};

    text-transform:
        uppercase;

    letter-spacing:
        .18em;

    font-size:
        .72rem;

    font-weight:
        700;

}}


.hero h1 {{

    font-size:
        3rem;

    margin:
        .35rem 0;

    position:
        relative;

}}


.hero p {{

    color:
        {COLORS["muted"]};

    max-width:
        700px;

    font-size:
        1rem;

    position:
        relative;

}}


/* ==========================================================
   VACA DESENHADA
   ========================================================== */

.cow-mark {{

    position:
        absolute;

    right:
        35px;

    bottom:
        8px;

    width:
        190px;

    height:
        150px;

    opacity:
        .92;

}}


/* ==========================================================
   MÉTRICAS
   ========================================================== */

.metric {{

    background:
        rgba(255,253,246,.82);

    border:
        2px solid {COLORS["moss"]};

    border-radius:
        16px;

    padding:
        1rem;

    box-shadow:
        4px 4px 0
        rgba(53,73,50,.11);

}}


.metric-label {{

    font-size:
        .74rem;

    color:
        {COLORS["muted"]};

    text-transform:
        uppercase;

    letter-spacing:
        .07em;

}}


.metric-value {{

    font-family:
        Georgia,
        serif;

    font-size:
        1.65rem;

    font-weight:
        700;

    color:
        {COLORS["coffee"]};

    margin-top:
        .2rem;

}}


.metric-detail {{

    color:
        {COLORS["moss"]};

    font-size:
        .72rem;

}}


/* ==========================================================
   SEÇÕES
   ========================================================== */

.section-title {{

    border-bottom:
        2px solid {COLORS["moss"]};

    margin:
        1.8rem 0 1rem;

    padding-bottom:
        .5rem;

}}


.section-title h2 {{

    margin:
        0;

    font-size:
        1.7rem;

}}


.section-title p {{

    color:
        {COLORS["muted"]};

    margin:
        .25rem 0 0;

}}


/* ==========================================================
   BOTÕES
   ========================================================== */

.stButton > button {{

    background:
        {COLORS["moss"]};

    color:
        white;

    border:
        2px solid
        {COLORS["moss_dark"]};

    border-radius:
        12px;

    font-weight:
        700;

}}


.stButton > button:hover {{

    background:
        {COLORS["moss_dark"]};

    color:
        white;

}}


/* ==========================================================
   SELECTS
   ========================================================== */

[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
    background-color: #FFFDF6 !important;
    border: 2px solid #536B45 !important;
    border-radius: 10px !important;
}}

[data-testid="stSidebar"] div[data-baseweb="select"] * {{
    color: #2E2B25 !important;
    -webkit-text-fill-color: #2E2B25 !important;
}}

[data-testid="stSidebar"] div[data-baseweb="select"] input {{
    color: #2E2B25 !important;
    -webkit-text-fill-color: #2E2B25 !important;
}}

[data-testid="stSidebar"] div[data-baseweb="select"] svg {{
    fill: #536B45 !important;
}}

/* MENU QUE ABRE AO CLICAR */

div[data-baseweb="popover"] {{
    background-color: #FFFDF6 !important;
}}

div[data-baseweb="popover"] [role="listbox"] {{
    background-color: #FFFDF6 !important;
}}

div[data-baseweb="popover"] [role="option"] {{
    background-color: #FFFDF6 !important;
    color: #2E2B25 !important;
}}

div[data-baseweb="popover"] [role="option"] * {{
    color: #2E2B25 !important;
    -webkit-text-fill-color: #2E2B25 !important;
}}

div[data-baseweb="popover"] [role="option"]:hover {{
    background-color: #EDE2CC !important;
}}

div[data-baseweb="popover"] [role="option"]:hover * {{
    color: #2E2B25 !important;
}}
/* ==========================================================
   TABELAS
   ========================================================== */

[data-testid="stDataFrame"] {{

    border:
        2px solid
        {COLORS["moss"]};

    border-radius:
        12px;

    overflow:
        hidden;

}}


/* ==========================================================
   LINKS
   ========================================================== */

a {{

    color:
        {COLORS["moss_light"]} !important;

}}

</style>
""")


# ============================================================
# VACA SVG
# ============================================================

COW_SVG = """

<svg
    class="cow-mark"
    viewBox="0 0 240 180"
    xmlns="http://www.w3.org/2000/svg"
>

<g
    fill="none"
    stroke="#536B45"
    stroke-width="4"
    stroke-linecap="round"
    stroke-linejoin="round"
>

    <!-- corpo -->

    <path
        d="
        M58 75
        C62 48 95 35 138 43
        C170 48 190 66 187 91
        C184 116 155 128 116 124
        C83 121 57 108 58 75
        "
    />

    <!-- cabeça -->

    <path
        d="
        M164 58
        C181 43 210 48 219 67
        C226 81 220 101 203 107
        C184 113 168 101 164 84
        "
    />

    <!-- focinho -->

    <path
        d="
        M201 88
        C218 85 229 92 226 104
        C222 117 200 118 190 108
        "
    />

    <!-- orelha -->

    <path
        d="
        M190 58
        C197 40 216 37 220 45
        C220 54 208 62 196 64
        "
    />

    <!-- chifre -->

    <path
        d="
        M183 54
        C178 39 183 30 192 26
        "
    />

    <!-- olho -->

    <circle
        cx="201"
        cy="75"
        r="3"
        fill="#536B45"
    />

    <!-- pernas -->

    <path
        d="M79 116 L77 153"
    />

    <path
        d="M105 121 L103 157"
    />

    <path
        d="M151 119 L153 154"
    />

    <path
        d="M173 111 L178 147"
    />

    <!-- cauda -->

    <path
        d="
        M61 68
        C42 59 34 68 39 81
        C43 91 32 97 25 91
        "
    />

    <!-- manchas -->

    <path
        d="
        M89 52
        C78 54 75 67 85 73
        C96 78 105 70 103 60
        C101 54 96 51 89 52
        "
    />

    <path
        d="
        M132 85
        C118 84 111 96 118 106
        C126 116 143 110 147 100
        C150 92 142 85 132 85
        "
    />

    <path
        d="
        M170 65
        C162 65 158 72 162 79
        "
    />

    <!-- sorriso -->

    <path
        d="
        M204 101
        C209 104 214 103 217 99
        "
    />

</g>

</svg>
"""


# ============================================================
# CARREGAMENTO
# ============================================================

df, connected = load_data(
    SHEET_URL
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## PROJETO FAZENDA"
    )

    st.caption(
        "Caderno estatístico do rebanho"
    )

    st.divider()

    if connected:

        st.success(
            "● Planilha conectada"
        )

    else:

        st.warning(
            "● Modo demonstração"
        )

    st.markdown(
        "### Navegação"
    )

    page = st.radio(

        "Abrir",

        [
            "Visão geral",
            "Rebanho",
            "Alimentação",
            "Saúde & manejo",
            "Ambiente",
            "Estatística"
        ],

        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(
        "### Filtros"
    )


    for field in FILTER_FIELDS:

        if field not in df.columns:

            continue

        values = sorted(

            df[field]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected = st.selectbox(

            clean_column_name(field),

            ["Todos"] + values,

            key=f"filter_{field}"
        )

        if selected != "Todos":

            df = df[
                df[field]
                .astype(str)
                == selected
            ]


    st.divider()

    st.link_button(
        "Abrir formulário",
        FORM_URL
    )

    if st.button(
        "↻ Atualizar dados",
        width="stretch"
    ):

        st.cache_data.clear()

        st.rerun()


# ============================================================
# HERO
# ============================================================

st.html(f"""

<div class="hero">

    {COW_SVG}

    <div class="eyebrow">
        {APP_NAME}
    </div>

    <h1>
        Inteligência do Rebanho
    </h1>

    <p>
        {APP_SUBTITLE}
        Um painel construído como um caderno
        de campo: papel, café, verde-musgo
        e dados.
    </p>

</div>

""")


# ============================================================
# FUNÇÕES
# ============================================================

def section(title, description=""):

    st.html(f"""

    <div class="section-title">

        <h2>
            {title}
        </h2>

        <p>
            {description}
        </p>

    </div>

    """)


def metric_card(
    label,
    value,
    detail=""
):

    st.html(f"""

    <div class="metric">

        <div class="metric-label">
            {label}
        </div>

        <div class="metric-value">
            {value}
        </div>

        <div class="metric-detail">
            {detail}
        </div>

    </div>

    """)


# ============================================================
# VISÃO GERAL
# ============================================================

if page == "Visão geral":

    section(
        "Panorama",
        "Uma leitura rápida das respostas coletadas."
    )

    total = len(df)


    # raça
    race = "—"

    if "Qual a raça do animal" in df.columns:

        modes = df[
            "Qual a raça do animal"
        ].mode()

        if len(modes):

            race = modes.iloc[0]


    # sistema
    system = "—"

    field = (
        "Qual o sistema de criação predominante?"
    )

    if field in df.columns:

        modes = df[field].mode()

        if len(modes):

            system = modes.iloc[0]


    # finalidade
    purpose = "—"

    field = (
        "Qual é a principal finalidade da criação?"
    )

    if field in df.columns:

        modes = df[field].mode()

        if len(modes):

            purpose = modes.iloc[0]


    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(
            "Respostas",
            str(total),
            "registros analisados"
        )

    with c2:

        metric_card(
            "Raça dominante",
            race,
            "maior frequência"
        )

    with c3:

        metric_card(
            "Sistema",
            system,
            "maior frequência"
        )

    with c4:

        metric_card(
            "Finalidade",
            purpose,
            "maior frequência"
        )


    section(
        "Retrato do rebanho",
        "As distribuições mais importantes da pesquisa."
    )


    c1, c2 = st.columns(2)

    with c1:

        field = "Qual a raça do animal"

        if field in df.columns:

            st.plotly_chart(
                donut(
                    df[field],
                    "Raças do rebanho"
                ),
                width="stretch"
            )


    with c2:

        field = (
            "Qual é a principal finalidade da criação?"
        )

        if field in df.columns:

            st.plotly_chart(
                donut(
                    df[field],
                    "Finalidade da criação"
                ),
                width="stretch"
            )


# ============================================================
# REBANHO
# ============================================================

elif page == "Rebanho":

    section(
        "Rebanho",
        "Quantidade, peso, raça, finalidade e identificação."
    )


    charts = [

        (
            "Qual a quantidade de gado que você possui?",
            "Quantidade de gado"
        ),

        (
            "Qual a raça do animal",
            "Raças"
        ),

        (
            "Qual o peso médio dos animais?",
            "Peso médio"
        ),

        (
            "Com que frequência o animal é pesado?",
            "Frequência de pesagem"
        ),

        (
            "Qual é a principal finalidade da criação?",
            "Finalidade"
        ),

        (
            "Como é feita a identificação dos animais?",
            "Identificação"
        )
    ]


    for i in range(
        0,
        len(charts),
        2
    ):

        c1, c2 = st.columns(2)

        for column, chart_title, target in [
            (c1, charts[i][1], charts[i][0]),
            (
                c2,
                charts[i + 1][1],
                charts[i + 1][0]
            )
            if i + 1 < len(charts)
            else (None, None, None)
        ]:

            if (
                column is None
                or target not in df.columns
            ):

                continue

            with column:

                st.plotly_chart(
                    bar(
                        df[target],
                        chart_title
                    ),
                    width="stretch"
                )


# ============================================================
# ALIMENTAÇÃO
# ============================================================

elif page == "Alimentação":

    section(
        "Alimentação",
        "Alimento, água, suplementação e investimento."
    )


    fields = [

        (
            "Qual é o principal tipo de alimento fornecido ao animal?",
            "Alimento principal"
        ),

        (
            "Quantas vezes por dia o animal recebe alimentação fornecida pelo produtor?",
            "Frequência de alimentação"
        ),

        (
            "Onde o alimento fornecido pelo produtor é disponibiliado ao animal",
            "Local de alimentação"
        ),

        (
            "Como é a disponibilidade de água para os animais?",
            "Disponibilidade de água"
        ),

        (
            "Qual o gasto mensal com a alimentação dos animais?",
            "Gasto com alimentação"
        ),

        (
            "Qual tipo de suplementação o animal recebe?",
            "Suplementação"
        )
    ]


    for i in range(0, len(fields), 2):

        c1, c2 = st.columns(2)

        if fields[i][0] in df.columns:

            with c1:

                st.plotly_chart(
                    bar(
                        df[fields[i][0]],
                        fields[i][1]
                    ),
                    width="stretch"
                )

        if i + 1 < len(fields):

            if fields[i + 1][0] in df.columns:

                with c2:

                    st.plotly_chart(
                        bar(
                            df[fields[i + 1][0]],
                            fields[i + 1][1]
                        ),
                        width="stretch"
                    )


# ============================================================
# SAÚDE
# ============================================================

elif page == "Saúde & manejo":

    section(
        "Saúde & manejo",
        "Sanidade, vacinação, parasitas e rotina de manejo."
    )


    fields = [

        (
            "Com que frequência o animal recebe acompanhamento veterinário?",
            "Acompanhamento veterinário"
        ),

        (
            "Com que frequência os animais recebem vacinação?",
            "Vacinação"
        ),

        (
            "Com que frequência os animais apresentam problemas de saúde?",
            "Problemas de saúde"
        ),

        (
            "Qual é a principal ocorrência de saúde observada no rebanho",
            "Ocorrências"
        ),

        (
            "Existe mortalidade de animais no rebanho?",
            "Mortalidade"
        ),

        (
            "Como é realizado o controle de parasitas no animal?",
            "Controle de parasitas"
        ),

        (
            "Com que frequência é realizada a limpeza/manutenção das instalações?",
            "Manutenção"
        )
    ]


    for i in range(0, len(fields), 2):

        c1, c2 = st.columns(2)

        if fields[i][0] in df.columns:

            with c1:

                st.plotly_chart(
                    bar(
                        df[fields[i][0]],
                        fields[i][1]
                    ),
                    width="stretch"
                )

        if i + 1 < len(fields):

            if fields[i + 1][0] in df.columns:

                with c2:

                    st.plotly_chart(
                        bar(
                            df[fields[i + 1][0]],
                            fields[i + 1][1]
                        ),
                        width="stretch"
                    )


# ============================================================
# AMBIENTE
# ============================================================

elif page == "Ambiente":

    section(
        "Ambiente & bem-estar",
        "Área, clima, água, pastagem e conforto térmico."
    )


    fields = [

        (
            "Qual é o tamanho aproximado da área utilizada para criação?",
            "Área utilizada"
        ),

        (
            "Qual é o tipo predominante de pastagem?",
            "Pastagem"
        ),

        (
            "Qual é a temperatura média da região onde os animais são criados?",
            "Temperatura"
        ),

        (
            "Como você classifica a frequência de períodos de calor intenso na região?",
            "Calor intenso"
        ),

        (
            "Como é a disponibilidade de água durante períodos de seca?",
            "Água na seca"
        ),

        (
            "Os animais possuem acesso a sombra durante o dia?",
            "Acesso à sombra"
        )
    ]


    for i in range(0, len(fields), 2):

        c1, c2 = st.columns(2)

        if fields[i][0] in df.columns:

            with c1:

                st.plotly_chart(
                    bar(
                        df[fields[i][0]],
                        fields[i][1]
                    ),
                    width="stretch"
                )

        if i + 1 < len(fields):

            if fields[i + 1][0] in df.columns:

                with c2:

                    st.plotly_chart(
                        bar(
                            df[fields[i + 1][0]],
                            fields[i + 1][1]
                        ),
                        width="stretch"
                    )


# ============================================================
# ESTATÍSTICA
# ============================================================

elif page == "Estatística":

    section(
        "Laboratório estatístico",
        "Medidas descritivas e distribuição das variáveis."
    )


    available = [

        field

        for field in NUMERIC_FIELDS

        if field in df.columns
    ]


    if not available:

        st.info(
            "Nenhuma variável quantitativa encontrada."
        )

    else:

        selected = st.selectbox(
            "Variável",
            available
        )


        values = numeric_series(
            df[selected]
        )


        if len(values):

            result = statistics(
                df[selected]
            )


            c1, c2, c3, c4, c5 = st.columns(5)


            with c1:

                metric_card(
                    "Média",
                    f"{result['mean']:.2f}",
                    "valor estimado"
                )


            with c2:

                metric_card(
                    "Mediana",
                    f"{result['median']:.2f}",
                    "Q2"
                )


            with c3:

                mode_value = result["mode"]

                metric_card(
                    "Moda",
                    (
                        f"{mode_value:.2f}"
                        if mode_value is not None
                        else "—"
                    ),
                    "mais frequente"
                )


            with c4:

                metric_card(
                    "Q1",
                    f"{result['q1']:.2f}",
                    "25%"
                )


            with c5:

                metric_card(
                    "Q3",
                    f"{result['q3']:.2f}",
                    "75%"
                )


            c1, c2 = st.columns(2)


            with c1:

                st.plotly_chart(
                    histogram(
                        values,
                        "Distribuição"
                    ),
                    width="stretch"
                )


            with c2:

                st.plotly_chart(
                    boxplot(
                        values,
                        "Boxplot"
                    ),
                    width="stretch"
                )


            section(
                "Tabela de frequência"
            )


            st.dataframe(
                frequency_table(
                    df[selected]
                ),
                width="stretch",
                hide_index=True
            )


            section(
                "Dados agrupados",
                "O ponto médio representa cada intervalo."
            )


            st.dataframe(
                grouped_table(
                    df[selected]
                ),
                width="stretch",
                hide_index=True
            )


            st.caption(
                "Quando uma resposta é dada em faixa, "
                "como 181–240 kg, utiliza-se o ponto "
                "médio da classe para as estimativas."
            )


# ============================================================
# RELAÇÃO ENTRE VARIÁVEIS
# ============================================================

if page == "Estatística" and len(available) >= 2:

    section(
        "Relação entre variáveis",
        "Explore possíveis associações entre medidas."
    )


    c1, c2 = st.columns(2)


    with c1:

        x_field = st.selectbox(
            "Variável X",
            available,
            key="variable_x"
        )


    with c2:

        y_field = st.selectbox(
            "Variável Y",
            available,
            index=1,
            key="variable_y"
        )


    relation = pd.DataFrame({

        "X":
            df[x_field]
            .astype(str)
            .map(midpoint),

        "Y":
            df[y_field]
            .astype(str)
            .map(midpoint)

    }).dropna()


    if len(relation):

        st.plotly_chart(

            scatter(
                relation,
                "Relação entre variáveis",
                clean_column_name(x_field),
                clean_column_name(y_field)
            ),

            width="stretch"
        )


# ============================================================
# ASSINATURA
# ============================================================

st.html(f"""

<div style="
    margin-top:50px;
    padding:18px;
    text-align:center;
    border-top:2px solid {COLORS["moss"]};
    color:{COLORS["muted"]};
    font-size:.78rem;
">

    PROJETO FAZENDA ·
    CADERNO ESTATÍSTICO DO REBANHO

</div>

""")
