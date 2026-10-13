# título - Sistema de Vendas
# Seção de cadastro de vendas
    # campo de data
    # campo de vendedor - Alexandre, João, Maria....
    # campo de produto - Notebook, Celular, Fone
    # campo de quantidade
    # campo de valor
    # botão de cadastrar venda
        # quando clicar no botão, salvar a venda na base de dados (tabela) (arquivo CSV)

# Seção de vendas cadastradas
    # tabela com as vendas

# Seção de dashboard com gráficos
    # Card/Metrica -> Faturamento total
    # Gráfico de barras -> Vendas por vendedor
    # Gráfico de pizza -> Vendas por produto 


# Ferramentas utilizadas:
    # Streamlit - para criar a interface do sistema
    # Pandas - para manipulação e análise de dados
    # Plotly - para criar os gráficos interativos

# comando para instalar as bibliotecas necessárias:
# pip install streamlit pandas plotly
# streamlit run codigo.py

#-----------------------CODIGO--------------------

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base dados -vendas
tabela_vendas = pd.read_csv("vendas.csv")

# título - Sistema de Vendas
st.write("# Sistema de Vendas")

# Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")

#st.write("## Cadastrar Vendas")
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data da Venda", value=pd.to_datetime("today"))
vendedor = st.sidebar.selectbox("Vendedor", ["Alexandre", "João", "Maria"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", min_value=1, step=1)
valor = st.sidebar.number_input("Valor", min_value=0.0, step=0.01, format="%.2f")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# logica de cadastro de vendas
if botao_cadastrar:


    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada!")
    #tabela_vendas = pd.concat([tabela_vendas, nova_venda], ignore_index=True)
    
    

# Seção de vendas cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Seção de dashboard
st.write("## Dashboard de Vendas")

    # Card/Metrica -> Faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento:.2f}")

    # Gráfico de barras -> Vendas por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", title="Vendas por Vendedor", color="produto")
st.plotly_chart(grafico1)


    # Gráfico de pizza -> Vendas por produto 
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", title="Vendas por Produto", hole=0.3)
st.plotly_chart(grafico2)