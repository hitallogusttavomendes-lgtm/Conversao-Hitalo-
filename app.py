import streamlit as st

st.title("🧮 Comparador de Combustível")

n1 = st.number_input('Valor do Etanol', value=4.59, format="%.2f")
n2 = st.number_input('Valor da Gasolina', value=6.29, format="%.2f")

if n2 > 0:
    p = (n1 / n2) * 100
    st.write(f'O preço do etanol corresponde a **{p:.2f}%** do da gasolina.')
    
    if p <= 70:
        st.success('👉 Compensa abastecer com **Etanol**!')
    else:
        st.error('👉 Compensa abastecer com **Gasolina**!')
