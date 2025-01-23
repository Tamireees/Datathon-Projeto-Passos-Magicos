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

## Dados por Relatório

### **2018:**
* Impacto Social: Atendeu 355 alunos diretamente e beneficiou 1420 pessoas.
* Programas Iniciais: Desenvolveu turmas de alfabetização, Ensino Fundamental I e II, e projetos de protagonismo juvenil para estudantes avançados.
* Atividades Culturais: Organizou passeios a museus e outros espaços culturais, promovendo um aprendizado além das salas de aula.
* Colaboração Institucional: Recebeu apoio de empresas como Microsoft (doações de software) e CIESP, que premiou Michelle Ivanoff com o Prêmio Excelência Mulher​.

### **2019**
* Aumento de Impacto: Expandiu para 812 alunos atendidos diretamente e beneficiou 3248 pessoas.
  
**Novas Iniciativas:**
* Parceria com o Programa Paidéia (USP), oferecendo cursos como Sustentabilidade e Programação, impactando diretamente 40 adolescentes.
* Introdução de turmas do Ensino Médio e foco em preparação para vestibulares.
* Suporte Ampliado: Implementou três níveis de acompanhamento psicológico (individual, em grupo e oficinas) para alunos e familiares​.
* Empresas e Colaborações: Firmou parcerias com Itaú Social e outras instituições para financiar projetos e estruturar atividades educacionais.

### **2020**
**Resiliência Durante a Pandemia:**
* Adaptação total para ensino online, com fornecimento de equipamentos e planos de internet para famílias em situação de vulnerabilidade.
* Atendeu 841 alunos e expandiu o suporte a cerca de 654 domicílios com uma pesquisa socioeconômica detalhada.
* Iniciativas Emergenciais: Distribuiu mais de 2000 cestas básicas e criou campanhas de saúde pública para prevenir a COVID-19.
* Colaborações e Apoio: Parcerias com Google for Education e Santander Universidades viabilizaram recursos tecnológicos para ensino remoto​.

### **2021**
**Gestão e Transparência:**
* Recebeu certificações importantes como o Selo Doar e o Selo de Gestão e Confiança VOA.
* Manteve as atividades online com 763 alunos atendidos e expandiu a formação de professores em ensino remoto.
  
**Novos Projetos:**
* Cursos técnicos em parceria com SENAI, abrangendo áreas como tecnologia e programação.
* Inclusão de 11 programas complementares, como Clube do Livro, que beneficiou 241 alunos​.

### **2022**
**Comemoração de 30 Anos:**
* Impactou diretamente mais de 1000 alunos, com crescimento do Programa de Aceleração do Conhecimento.
* Superação do aprendizado prejudicado pela pandemia, com foco em recuperação escolar.

**Parcerias e Iniciativas:**
* Bolsas de estudo para 71 universitários, em colaboração com Estácio de Sá e FIAP.
* Ampliação da assistência social, com ênfase no fortalecimento dos laços familiares​.
* 
### **2023**
**Expansão Estrutural:**
* Inauguração de uma nova unidade no Centro de Embu-Guaçu, com seis salas de aula, biblioteca e áreas específicas para psicologia e psicopedagogia.
* Atendeu 1100 alunos com mais de 11.500 horas de aula no PAC.
  
**Resultados Educacionais:**
* Acompanhou a evolução de desempenho dos alunos, com uma média de 77% de melhoria nas notas ao longo do ano.
* Empresas Parceiras: Parcerias com Omie, Itaú, e a comunidade local viabilizaram os novos espaços e expansão do impacto​.


''')

if selected_page == "Dashboard Interativo":
    
    st.title("Dashboard Interativo")   
    
     




    
if selected_page == "Etapas do Desenvolvimento: Análise de Dados":

    st.title("Etapas do Desenvolvimento:")
    
    # 2. Link para o notebook no GitHub
    st.write("### Acesse o Notebook Completo:")
    notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/Datathon-Passos_Magicos.ipynb"
    st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")

    st.title("Análise de Dados - Passos Mágicos")  

    # Carregar os dados do arquivo remoto
    url_dados = "https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/df_clean_datathon.csv"
    df_inteiro_clean = pd.read_csv(url_dados)   

    # ----------------------------------------------
    # **SEÇÃO 1: Conhecendo os Dados**
    # ----------------------------------------------
    st.header("Conhecendo os Dados")    

    # Exibir código e resultados lado a lado
    with st.expander("Ver Código - Conhecendo os Dados"):
        st.code("""
    df_inteiro_clean.to_csv('df_clean_datathon.csv', index=False)
    df_inteiro_clean.shape
    df_inteiro_clean.info()
    df_inteiro_clean['NOME'].duplicated().sum()
    df_inteiro_clean.isnull().sum()
        """, language="python") 

    st.subheader("Dimensão dos Dados")
    st.write(f"Linhas e Colunas: {df_inteiro_clean.shape}") 

    st.subheader("Informações Gerais dos Dados")
    buffer = st.empty()
    buffer.write(df_inteiro_clean.info(verbose=True, memory_usage="deep", buf=buffer))

    st.subheader("Duplicatas em 'NOME'")
    st.write(f"Duplicatas: {df_inteiro_clean['NOME'].duplicated().sum()}")

    st.subheader("Dados Faltantes")
    st.write(df_inteiro_clean.isnull().sum())

    # ----------------------------------------------
    # **SEÇÃO 2: Tratamento e Limpeza de Dados**
    # ----------------------------------------------
    st.header("Tratamento e Limpeza de Dados")

    with st.expander("Ver Código - Tratamento e Limpeza"):
        st.code("""
    def classificar_aluno(row):
        if row['ANO_INGRESSO_2022'] == 2022:
            return 'Ingressou em 2022'
        elif row['ANO_INGRESSO_2021'] == 2021 and row.isnull().sum() > 0:
            return 'Possível desistência'
        return 'Ativo'

    df_inteiro_clean['STATUS_ALUNO'] = df_inteiro_clean.apply(classificar_aluno, axis=1)
    df_inteiro_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']] = df_inteiro_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']].applymap(lambda x: int(x) if pd.notna(x) else x)
        """, language="python")

    # Aplicando as transformações
    def classificar_aluno(row):
        if row['ANO_INGRESSO_2022'] == 2022:
            return 'Ingressou em 2022'
        elif row['ANO_INGRESSO_2021'] == 2021 and row.isnull().sum() > 0:
            return 'Possível desistência'
        return 'Ativo'

    df_inteiro_clean['STATUS_ALUNO'] = df_inteiro_clean.apply(classificar_aluno, axis=1)
    df_inteiro_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']] = df_inteiro_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']].applymap(
        lambda x: int(x) if pd.notna(x) else x
    )

    # Mostrar os dados tratados
    st.subheader("Dados Tratados")
    st.write(df_inteiro_clean.head(20))

    # ----------------------------------------------
    # **SEÇÃO 3: Explorando os Dados**
    # ----------------------------------------------
    st.header("Explorando os Dados")

    # Variáveis qualitativas
    categories = {
        'FASE': ['FASE_2020', 'FASE_2021', 'FASE_2022'],
        'PEDRA': ['PEDRA_2020', 'PEDRA_2021', 'PEDRA_2022'],
        'PONTO_VIRADA': ['PONTO_VIRADA_2020', 'PONTO_VIRADA_2021', 'PONTO_VIRADA_2022'],
        'STATUS_ALUNO': ['STATUS_ALUNO']
    }

    # Análise de Frequências
    st.subheader("Distribuição de Frequências - Variáveis Qualitativas")
    for category, cols in categories.items():
        st.write(f"**{category}:**")
        st.write(df_inteiro_clean[cols].apply(pd.Series.value_counts))

    # Gráficos de Distribuição
    st.subheader("Gráficos de Distribuição - Variáveis Qualitativas")
    for col_group in categories.values():
        if all(col in df_inteiro_clean.columns for col in col_group):
            melted_data = pd.melt(
                df_inteiro_clean[col_group].reset_index(),
                id_vars=['index'],
                var_name='Ano',
                value_name=col_group[0]
            )
            plt.figure(figsize=(8, 5))
            sns.countplot(
                data=melted_data,
                x=col_group[0],
                hue='Ano',
                palette=['#F79651', '#2A6DA6', '#A2CFE6']
            )
            plt.title(f"Distribuição de Frequências - {col_group[0]}")
            st.pyplot(plt)

    # Continue construindo as outras seções: Proporções, Quantitativas, Outliers, Correlação, Temporal...

    # ----------------------------------------------
    # **SEÇÃO 4: Visualização de Densidade**
    # ----------------------------------------------
    st.header("Visualização de Densidade - Variáveis Quantitativas")

    quantitative_columns = [
        'IAN_2020', 'IDA_2020', 'IEG_2020', 'IAA_2020',
        'IPS_2020', 'IPP_2020', 'IPV_2020', 'INDE_2020'
    ]

    for col_base in ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPP', 'IPV', 'INDE']:
        cols = [f"{col_base}_{year}" for year in [2020, 2021, 2022]]
        plt.figure(figsize=(8, 5))
        sns.kdeplot(data=df_inteiro_clean[cols], fill=True)
        plt.title(f'Densidade - {col_base}')
        st.pyplot(plt)













    
if selected_page == "Etapas do Desenvolvimento: Modelo Preditivo":
    
    st.title("Etapas do Desenvolvimento: Modelo Preditivo")
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")
