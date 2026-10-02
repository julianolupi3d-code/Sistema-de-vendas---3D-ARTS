# título - Sistema de vendas
# Seção - Cadstrar vendas 
    # campo data
    # campo vendedor - Juliano  
    # Campo produto - objetos 3d
    # Campo quantidade 
    #campo valor
    #

import streamlit as st
import pandas as pd
import plotly.express as px


#carregar a base de dados
tabela_vendas= pd.read_csv("vendas.csv")

st.write("#Sistema de vendas - 3D ARTS")

# seção de cadastro de vendas
st.sidebar.write("##Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Juliano", "Caroline"])
produto = st.sidebar.selectbox("Produto", ["Objetos 3D", "Modelagem 3D", "Animação 3D"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botão_cadastrar = st.sidebar.button("Cadastrar Venda")  

# lógica de cadastro
if botão_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada!")


# seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

#seção de dashboard
st.write("##Dashboard")

#Card/métrica
faturamento = tabela_vendas["Valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

#Grafico de barras
grafico1 = px.bar(tabela_vendas, x="vendedor", y="Valor", color="Produto", text_auto=True)
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="Produto", values="Valor", hole=0.3)
st.plotly_chart(grafico2)


