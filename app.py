#Importação das bibliotecas
import streamlit as st 
import pandas as pd
import joblib
from joblib import load
from nbconvert import HTMLExporter
import nbformat




# Configuração inicial do Streamlit
st.set_page_config(page_title="Projeto Passos Mágicos", layout="wide")

# Definir as páginas
pages = {
    "Apresentação: Projeto e Passos Mágicos": "main",
    "Dashboard Interativo": "page_2",
    "Etapas do Desenvolvimento: Análise de Dados": "page_3",
    "Etapas do Desenvolvimento: Modelo Preditivo": "page_4",
    "Formulário: Modelo Preditivo": "page_5"
    }

# Barra de navegação
selected_page = st.sidebar.radio("Selecione a Página", list(pages.keys()))

if selected_page == "Apresentação: Projeto e Passos Mágicos":
    
    st.title("Datathon: Introdução da Atividade")
     
    st.markdown('''
O Datathon tem como objetivo criar propostas baseadas em dados para evidenciar o impacto da ONG Passos Mágicos na transformação social de crianças e jovens em situação de vulnerabilidade.

A ONG promove a educação como ferramenta de mudança, atendendo alunos do município de Embu-Guaçu. A competição oferece duas possibilidades de entrega:

### Proposta Analítica:

Criar um dashboard interativo e storytelling que demonstre os impactos da ONG.
Analisar o desempenho dos estudantes e criar indicadores úteis para a tomada de decisão.
Entregar insights sobre o perfil socioeconômico e educacional dos alunos.

### Proposta Preditiva:

Desenvolver um modelo preditivo para analisar o comportamento dos estudantes.
Utilizar técnicas como machine learning ou deep learning para propor soluções inovadoras.
Realizar o deploy do modelo preditivo em uma plataforma como Streamlit.
Os participantes podem optar por entregar apenas uma proposta ou ambas. A entrega deve conter o relatório e/ou modelo preditivo implementado com links no GitHub.
''')
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  
    
    

    col1, col2 = st.columns([1, 3])  # Define duas colunas, a primeira menor para o logo e a segunda maior para o texto

    with col1:
        st.image("logo.png", width=300)  # Insere o logotipo na primeira coluna

    with col2:
        st.title("Conhecendo o Projeto Passos Mágicos") 
     
    st.markdown('''
## Baseado no Objetivo e Princípios Comuns

A Associação Passos Mágicos é uma organização sem fins lucrativos que atua desde 1992 com o objetivo de transformar a vida de crianças e jovens em situação de vulnerabilidade social no município de Embu-Guaçu. Fundada por Michelle Flues Ivanoff, Dimitri Ivanoff e colaboradores, a ONG surgiu do desejo de oferecer oportunidades educativas e culturais que promovam autonomia e impacto positivo na comunidade. O projeto cresceu de ações voluntárias em orfanatos para uma associação formal em 2016, permitindo a ampliação de suas atividades.

### **Missão, Visão e Princípios**

* Missão: Transformar vidas por meio da educação, oferecendo ferramentas para criar oportunidades de um futuro digno.
* Visão: Construir um Brasil em que todas as crianças e jovens tenham as mesmas condições para realizar seus sonhos e se tornem agentes transformadores.
* Princípios: Amor ao próximo, empatia, gratidão, pertencimento, busca pelo saber, e educação que transforma.

### **Metodologia e Etapas**

A metodologia da Passos Mágicos é baseada em quatro pilares principais:

1. Educação de Qualidade: Aulas de português, matemática, inglês e alfabetização, com turmas organizadas de acordo com o nível de conhecimento, e não por idade. Isso é complementado por aulas interativas e dinâmicas que incentivam o aprendizado e a curiosidade.
2. Assistência Psicológica: Oferece suporte emocional para alunos e familiares, com acompanhamento individual e em grupo, além de oficinas para melhorar relacionamentos interpessoais.
3. Ampliação da Visão de Mundo: Realização de atividades extracurriculares como visitas a museus, parques e eventos culturais, que expandem o horizonte das crianças.
4. Protagonismo: Alunos são incentivados a desenvolver autonomia e liderar iniciativas dentro da ONG, incluindo a possibilidade de bolsas em escolas particulares e universidades para aqueles com bom desempenho.

### **A ONG implementa programas inovadores como:**

* Programa de Aceleração do Conhecimento (PAC): Uma jornada educacional com 7 fases e foco no desenvolvimento integral, oferecendo aulas complementares, suporte psicológico e bolsas de estudos.
* Parcerias Estratégicas: Colaborações com instituições como USP (Programa Paidéia), SENAI, FIAP e empresas privadas como Itaú, Santander, e Estácio de Sá. Essas parcerias possibilitam bolsas, treinamentos e acesso a tecnologias para potencializar o impacto educacional.

''')

if selected_page == "Dashboard Interativo":
    
    st.title("Dashboard Interativo")   
    
     
    
if selected_page == "Etapas do Desenvolvimento: Análise de Dados":
    
    st.title("Etapas do Desenvolvimento: Análise de Dados")
    
    # Carregar os dados do CSV
    url_dados = "https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/df_clean_datathon.csv"
    dados_clean = pd.read_csv(url_dados, sep=',')
    
    # Visualizar os dados
    st.write("### Visualização dos Dados:")
    st.dataframe(dados_clean.head(20))
    
        # Link para o notebook no GitHub
    st.write("### Acesse o Notebook Completo:")
    notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/Datathon-Passos_Magicos.ipynb"
    st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")

    
    
if selected_page == "Etapas do Desenvolvimento: Modelo Preditivo":
    
    st.title("Etapas do Desenvolvimento: Modelo Preditivo")
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")
