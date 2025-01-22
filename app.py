#Importação das bibliotecas
import streamlit as st 
import pandas as pd
import joblib
from joblib import load
from nbconvert import HTMLExporter
import nbformat
import seaborn as sns
import matplotlib.pyplot as plt




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
    
    st.title("📊 Análise de Dados")

    # 1. Importação do Dataset
    st.header("1️⃣ Carregando e Explorando os Dados")
    st.write("Carregando o dataset diretamente do GitHub.")
    data_url = 'https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/refs/heads/main/dados/PEDE_PASSOS_DATASET_FIAP.csv'
    df = pd.read_csv(data_url, sep=';')

    # Exibindo as primeiras linhas do dataset
    st.subheader("Primeiras linhas do dataset:")
    st.dataframe(df.head())

    # Exibindo o formato do dataset
    st.subheader("Dimensões do dataset:")
    st.write(f"O dataset possui {df.shape[0]} linhas e {df.shape[1]} colunas.")

    # Exibindo as colunas do dataset
    st.subheader("Colunas do dataset:")
    st.write(list(df.columns))

    # 2. Funções Utilizadas
    st.header("2️⃣ Funções para Manipulação de Dados")

    # Função para filtrar colunas
    def filter_columns(df, filters: list):
        """
        Filtra colunas do dataframe que não possuem determinados padrões definidos no array `filters`.
        """
        selected_columns = [True] * len(df.columns)  # Inicializa todas as colunas como True
        for index, column in enumerate(df.columns):
            if any(filter in column for filter in filters): 
                selected_columns[index] = False
        return df[df.columns[selected_columns]]

    st.code("""
    def filter_columns(df, filters: list):
        selected_columns = [True] * len(df.columns)
        for index, column in enumerate(df.columns):
            if any(filter in column for filter in filters): 
                selected_columns[index] = False
        return df[df.columns[selected_columns]]
    """, language="python")

    # Função para limpeza de dados
    def cleaning_dataset(df):
        """
        Limpa o dataset, removendo linhas que tenham todos os valores nulos, exceto na coluna 'NOME'.
        """
        _df = df.dropna(subset=df.columns.difference(['NOME']), how='all')
        _df = _df[~_df.isna().all(axis=1)]
        return _df

    st.code("""
    def cleaning_dataset(df):
        _df = df.dropna(subset=df.columns.difference(['NOME']), how='all')
        _df = _df[~_df.isna().all(axis=1)]
        return _df
    """, language="python")

    # Função para gerar gráfico de contagem
    def plot_exact_counter(size, x, y, df):
        """
        Plota um gráfico de contagem com os valores exatos em cada barra.
        """
        plt.figure(figsize=size)
        barplot = plt.bar(y.index, y.values)
        plt.xlabel(x)
        plt.ylabel('Count')

        for index, value in enumerate(y.values):
            plt.text(index, value, round(value, 2), color='black', ha="center")

    st.code("""
    def plot_exact_counter(size, x, y, df):
        plt.figure(figsize=size)
        barplot = plt.bar(y.index, y.values)
        plt.xlabel(x)
        plt.ylabel('Count')

        for index, value in enumerate(y.values):
            plt.text(index, value, round(value, 2), color='black', ha="center")
    """, language="python")

    # Função para analisar correlações
    def analyse_corr(df):
        """
        Gera um mapa de correlação entre as variáveis numéricas.
        """
        df = df.apply(pd.to_numeric, errors='coerce')
        corr_matrix = df.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.show()

    st.code("""
    def analyse_corr(df):
        df = df.apply(pd.to_numeric, errors='coerce')
        corr_matrix = df.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.show()
    """, language="python")

    # 3. Aplicando Funções
    st.header("3️⃣ Aplicando as Funções")

    # Exemplo: Filtrar colunas
    st.subheader("Filtrando colunas do dataset")
    filters = ['2020', '2021']
    filtered_df = filter_columns(df, filters)
    st.write(f"Colunas após o filtro (removendo colunas com {filters}):")
    st.dataframe(filtered_df)

    # Exemplo: Limpeza do dataset
    st.subheader("Limpando o dataset")
    cleaned_df = cleaning_dataset(filtered_df)
    st.write("Dataset após limpeza:")
    st.dataframe(cleaned_df)

    # Carregar os dados
    st.title('Explorando os Dados do Ano 2020')

    data_url = 'https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/refs/heads/main/dados/PEDE_PASSOS_DATASET_FIAP.csv'
    df = pd.read_csv(data_url, sep=';')
        # Limpeza e seleção dos dados

    def cleaning_dataset(df):
        return df.dropna().drop_duplicates()

    def analyse_corr(df):
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        st.pyplot(plt)

    st.dataframe(df.head())

    # Filtro inicial do dataset
    df_2020 = filter_columns(df, ['2021', '2022'])
    df_2020 = cleaning_dataset(df_2020)

    st.write("### Dataset 2020 - Após Filtro e Limpeza Inicial:")
    st.dataframe(df_2020.head())

    st.write(f"**Colunas no Dataset:** {df_2020.columns.tolist()}")
    st.write(f"**Tamanho do Dataset:** {df_2020.shape}")

    # Dados nulos e duplicados
    st.write("### Dados Nulos e Duplicados")
    st.write("**Dados Nulos:**")
    st.write(df_2020.isnull().sum())
    st.write("**Contagem de Valores em 'NOME':**")
    st.write(df_2020['NOME'].value_counts())


    # Tratamento dos Dados
    st.write("### Tratamento e Limpeza dos Dados")

    df_2020_clean = df_2020.copy()
    df_2020_clean = df_2020_clean[df_2020_clean['PEDRA_2020'] != 'D9891/2A']

    ano_map_2020 = {
        2020: '0',
        2019: '1',
        2018: '2',
        2017: '3',
        2016: '4',
        None: 'D971'
    }

    reverse_ano_map_2020 = {v: k for k, v in ano_map_2020.items()}
    
    df_2020_clean['ANOS_PM_2020'] = df_2020_clean['ANOS_PM_2020'].map(reverse_ano_map_2020)

    df_2020_clean.rename(columns={'ANOS_PM_2020': 'ANO_INGRESSO_2020'}, inplace=True)
    df_2020_clean['ANO_INGRESSO_2020'] = pd.to_datetime(df_2020_clean['ANO_INGRESSO_2020'], format='%Y', errors='coerce')
    df_2020_clean['ANO_INGRESSO_2020'] = df_2020_clean['ANO_INGRESSO_2020'].dt.year

    df_2020_clean['FASE_2020'] = df_2020_clean['FASE_TURMA_2020'].str.extract('(\\d+)')
    df_2020_clean['TURMA_2020'] = df_2020_clean['FASE_TURMA_2020'].str.extract('([A-Za-z]+)')

    df_2020_clean['PONTO_VIRADA_2020'] = df_2020_clean['PONTO_VIRADA_2020'].apply(lambda x: 1 if x == 'Sim' else 0)
    df_2020_clean['INDE_2020'] = pd.to_numeric(df_2020_clean['INDE_2020'], errors='coerce')
    df_2020_clean['PEDRA_2020'] = pd.Categorical(df_2020_clean['PEDRA_2020'])

    destaque_cols = ['DESTAQUE_IPV_2020', 'DESTAQUE_IDA_2020', 'DESTAQUE_IEG_2020']
    for col in destaque_cols:
        df_2020_clean[col] = df_2020_clean[col].apply(lambda x: 1 if isinstance(x, str) and 'Seu destaque' in x else 0)

    metric_cols = ['IAA_2020', 'IEG_2020', 'IPS_2020', 'IDA_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020']
    df_2020_clean[metric_cols] = df_2020_clean[metric_cols].apply(pd.to_numeric, errors='coerce')

    df_2020_clean = df_2020_clean.drop(columns=['TURMA_2020', 'FASE_TURMA_2020', 'INSTITUICAO_ENSINO_ALUNO_2020', 'IDADE_ALUNO_2020', 'INDE_CONCEITO_2020'])

    st.write("### Dataset Final Após Limpeza:")
    st.dataframe(df_2020_clean.head())

    st.write("### Estatísticas Descritivas do Dataset Limpo:")
    st.write(df_2020_clean.describe())
    
    
        # Limpeza e seleção dos dados
    df_2020_clean = df_2020_clean[['NOME', 'ANO_INGRESSO_2020','FASE_2020', 'PEDRA_2020', 'IAN_2020', 'DESTAQUE_IDA_2020', 'IDA_2020', 'DESTAQUE_IEG_2020', 
                        'IEG_2020', 'IAA_2020', 'IPS_2020', 'IPP_2020', 'DESTAQUE_IPV_2020', 'IPV_2020', 
                        'INDE_2020', 'PONTO_VIRADA_2020']]

    # Variáveis qualitativas
    qualitative_columns_2020 = [
        'FASE_2020','PEDRA_2020','DESTAQUE_IDA_2020', 'DESTAQUE_IEG_2020', 
        'DESTAQUE_IPV_2020', 'PONTO_VIRADA_2020']

    # Análise de Frequência
    st.subheader("Análise de Frequência")
    st.write("Porcentagem da quantidade de alunos em cada fase:")
    st.write(df_2020_clean['FASE_2020'].value_counts(normalize=True)*100)
    st.write("Porcentagem por classificação de pedra:")
    st.write(df_2020_clean['PEDRA_2020'].value_counts(normalize=True)*100)
    st.write("Destaque no Indicador de Aprendizagem (IDA):")
    st.write(df_2020_clean['DESTAQUE_IDA_2020'].value_counts(normalize=True)*100)
    st.write("Destaque no Indicador de Engajamento (IEG):")
    st.write(df_2020_clean['DESTAQUE_IEG_2020'].value_counts(normalize=True)*100)
    st.write("Destaque no Indicador de Ponto de Virada (IPV):")
    st.write(df_2020_clean['DESTAQUE_IPV_2020'].value_counts(normalize=True)*100)
    st.write("Ponto de Virada:")
    st.write(df_2020_clean['PONTO_VIRADA_2020'].value_counts(normalize=True)*100)

    # Visualizações
    st.subheader("Visualizações")
    for column in qualitative_columns_2020:
        fig, ax = plt.subplots(figsize=(4, 2))
        sns.countplot(x=column, data=df_2020_clean, palette=['#F79651', '#2A6DA6', '#A2CFE6'])
        plt.title(f'Contagem de {column}')
        st.pyplot(fig)

    # Comparação entre Variáveis Quantitativas e Categóricas
    st.subheader("Boxplot da FASE_2020 por INDE_2020")
    fig, ax = plt.subplots(figsize=(4, 2))
    sns.boxplot(x='FASE_2020', y='INDE_2020', data=df_2020_clean, palette=['#F79651', '#2A6DA6', '#A2CFE6'])
    plt.title('Boxplot da FASE_2020 por INDE_2020')
    st.pyplot(fig)

    # Análise Temporal
    st.subheader("Análise Temporal")
    quantitative_columns_2020 = ['IAN_2020', 'IDA_2020', 'IEG_2020', 'IAA_2020', 'IPS_2020', 'IPP_2020', 'IPV_2020', 'INDE_2020']
    for column in quantitative_columns_2020:
        fig, ax = plt.subplots(figsize=(4, 2))
        df_2020_clean.groupby('ANO_INGRESSO_2020')[column].mean().plot(kind='line', marker='o', color= '#2A6DA6')
        plt.title(f'Evolução de {column} ao longo dos anos', fontsize=10)
        plt.xlabel('Ano de Ingresso', fontsize=9)
        plt.ylabel(column, fontsize=9)
        plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        st.pyplot(fig)

    # Análise de Variabilidade
    st.subheader("Análise de Variabilidade")
    st.write(df_2020_clean[quantitative_columns_2020].std())

    # Visualização de Densidade
    st.subheader("Visualização de Densidade")
    for column in quantitative_columns_2020:
        fig, ax = plt.subplots(figsize=(4, 2))
        df_2020_clean[column].plot(kind='density', color='#F79651', linewidth=2)
        mean_value = df_2020_clean[column].mean()
        plt.axvline(mean_value, color='red', linestyle='--', linewidth=1, label=f'Média: {mean_value:.2f}')
        lower_bound = df_2020_clean[column].quantile(0.01)
        upper_bound = df_2020_clean[column].quantile(0.99)
        plt.xlim(lower_bound, upper_bound)
        plt.title(f'Densidade de {column}', fontsize=10)
        plt.xlabel(column, fontsize=9)
        plt.legend(fontsize=9)
        st.pyplot(fig)

























    
if selected_page == "Etapas do Desenvolvimento: Modelo Preditivo":
    
    st.title("Etapas do Desenvolvimento: Modelo Preditivo")
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")
