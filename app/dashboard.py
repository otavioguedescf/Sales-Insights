# 📦 Importando as bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# 🧹 Configurações da página
st.set_page_config(
    page_title="Sales Insights Dashboard",
    layout="wide"
)

# 📢 Título principal
st.title("📈 Sales Insights Dashboard")
st.markdown("Análise interativa de vendas, campanhas e canais.")

# 📥 Carregar os dados
# Ajuste o caminho se necessário
df = pd.read_csv("G:/Meu Drive/Data Science/Sales Insights/data/data.csv", sep=";", encoding="utf-8")

# 🧹 Pré-processamento (se necessário)
df["Data"] = pd.to_datetime(df["Data"])

# 🎛️ Filtros laterais
st.sidebar.header("Filtros")

campanhas = st.sidebar.multiselect("Campanha", options=df["Campanha_Marketing"].unique(), default=df["Campanha_Marketing"].unique())
canais = st.sidebar.multiselect("Canal de Venda", options=df["Canal_Venda"].unique(), default=df["Canal_Venda"].unique())
regioes = st.sidebar.multiselect("Região", options=df["Região"].unique(), default=df["Região"].unique())

# 🎯 Aplicar filtros
df_filtrado = df[
    (df["Campanha_Marketing"].isin(campanhas)) &
    (df["Canal_Venda"].isin(canais)) &
    (df["Região"].isin(regioes))
]

# 📈 KPIs principais
faturamento_total = df_filtrado["Valor_Final"].sum()
ticket_medio = (df_filtrado["Valor_Final"] / df_filtrado["Quantidade"]).mean()
quantidade_total = df_filtrado["Quantidade"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Faturamento Total", f"R$ {faturamento_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col2:
    st.metric("🎯 Ticket Médio", f"R$ {ticket_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col3:
    st.metric("📦 Quantidade Vendida", f"{quantidade_total:,}".replace(",", "."))

# 📊 Gráficos
st.markdown("---")

# Faturamento por Categoria
fat_categoria = df_filtrado.groupby("Categoria_Produto")["Valor_Final"].sum().reset_index()

fig_categoria = px.bar(
    data_frame=fat_categoria,
    x="Categoria_Produto",
    y="Valor_Final",
    color="Categoria_Produto",
    text_auto=".2s",
    title="Faturamento por Categoria de Produto"
)

st.plotly_chart(fig_categoria, use_container_width=True)

# Faturamento ao longo do tempo
vendas_mensais = df_filtrado.groupby(df_filtrado["Data"].dt.to_period("M"))["Valor_Final"].sum().reset_index()
vendas_mensais["Data"] = vendas_mensais["Data"].dt.to_timestamp()

fig_tempo = px.line(
    vendas_mensais,
    x="Data",
    y="Valor_Final",
    title="Evolução de Vendas Mensais"
)

st.plotly_chart(fig_tempo, use_container_width=True)

