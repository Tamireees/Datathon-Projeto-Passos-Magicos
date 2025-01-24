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
    notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Passos_Magicos_dataset.ipynb"
    st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")

    st.title("Análise de Dados - Passos Mágicos")  

    # Carregar os dados do arquivo remoto
    url_dados = "https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/refs/heads/main/dados/df_clean.csv"
    df_clean = pd.read_csv(url_dados)   

    # ----------------------------------------------
    # **SEÇÃO 1: Conhecendo os Dados**
    # ----------------------------------------------
    st.header("Conhecendo os Dados")    

    # Exibir código e resultados lado a lado
    with st.expander("Ver Código - Conhecendo os Dados"):
        st.code("""
    df_inteiro_clean.to_csv('df_clean.csv', index=False)
    df_clean.shape
    df_clean.info()
    df_clean['NOME'].duplicated().sum()
    df_clean.isnull().sum()
        """, language="python") 

    st.subheader("Dimensão dos Dados")
    st.write(f"Linhas e Colunas: {df_clean.shape}") 

    st.subheader("Informações Gerais dos Dados")
    buffer = st.empty()
    buffer.write(df_clean.info(verbose=True, memory_usage="deep", buf=buffer))

    st.subheader("Duplicatas em 'NOME'")
    st.write(f"Duplicatas: {df_clean['NOME'].duplicated().sum()}")

    st.subheader("Dados Faltantes")
    st.write(df_clean.isnull().sum())

    # Função para exibir o gráfico de barras
    def plot_bar_chart(data, title, xlabel, ylabel, figsize=(10, 6)):
        plt.figure(figsize=figsize)
        sns.barplot(x=data.index, y=data.values, palette=custom_palette)
        plt.title(title, fontsize=12)
        plt.xlabel(xlabel, fontsize=10)
        plt.ylabel(ylabel, fontsize=10)
        plt.xticks(rotation=45, fontsize=9)
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot()

    # Função para exibir o gráfico de distribuição
    def plot_histogram(data, title, xlabel, ylabel, figsize=(10, 6), bins=10):
        plt.figure(figsize=figsize)
        sns.histplot(data, kde=True, palette=custom_palette, bins=bins)
        plt.title(title, fontsize=12)
        plt.xlabel(xlabel, fontsize=10)
        plt.ylabel(ylabel, fontsize=10)
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot()

    custom_palette = ['#F79651', '#2A6DA6', '#A2CFE6']

    st.title("Análise de Desempenho de Alunos")

    # 1. Saber em qual fase o aluno parou (Data de Entrada e Saída)
    st.header("Distribuição das Fases em que os Alunos Pararam")
    df_clean['FASE_PARADA'] = df_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']].bfill(axis=1).iloc[:, -1]
    fase_counts = df_clean['FASE_PARADA'].value_counts()
    plot_bar_chart(fase_counts, "Distribuição das Fases em que os Alunos Pararam", "Fase", "Número de Alunos")

    # 2. Justificativa de desistência
    st.header("Distribuição dos Motivos de Desistência")
    colunas_abordadas = [
        'IAN_2020', 'IAN_2021', 'IAN_2022', 'IDA_2020', 'IDA_2021', 'IDA_2022',
        'IEG_2020', 'IEG_2021', 'IEG_2022', 'IAA_2020', 'IAA_2021', 'IAA_2022',
        'IPS_2020', 'IPS_2021', 'IPS_2022', 'IPP_2020', 'IPP_2021', 'IPP_2022',
        'IPV_2020', 'IPV_2021', 'IPV_2022'
    ]
    df_desistencia = df_clean[df_clean['STATUS_ALUNO'] == 'Possível desistência'][colunas_abordadas]
    df_desistencia['MOTIVO_DESISTENCIA'] = df_desistencia.idxmin(axis=1)
    traducao_motivos = {
        'IAN': 'Indicador Acadêmico',
        'IDA': 'Indicador de Desempenho Acadêmico',
        'IEG': 'Indicador de Engajamento',
        'IAA': 'Indicador de Avaliação Acadêmica',
        'IPS': 'Indicador Psicossocial',
        'IPP': 'Indicador de Planejamento Pessoal',
        'IPV': 'Indicador de Visão'
    }
    df_desistencia['MOTIVO_DESISTENCIA'] = df_desistencia['MOTIVO_DESISTENCIA'].str.extract(r'(\w+)_\d+')
    df_desistencia['MOTIVO_DESISTENCIA'] = df_desistencia['MOTIVO_DESISTENCIA'].map(traducao_motivos)
    motivos_counts = df_desistencia['MOTIVO_DESISTENCIA'].value_counts()
    plot_bar_chart(motivos_counts, "Distribuição dos Motivos de Desistência - Possíveis Desistentes", "Motivos", "Número de Alunos")

    # 3. Tempo de Permanência para alunos com "Possível desistência"
    st.header("Distribuição do Tempo de Permanência - Possíveis Desistentes")
    df_desistencia['TEMPO_PERMANENCIA'] = df_desistencia['ANO_SAIDA'] - df_desistencia['ANO_INGRESSO']
    plot_histogram(df_desistencia['TEMPO_PERMANENCIA'], "Distribuição do Tempo de Permanência - Possíveis Desistentes", "Tempo de Permanência (anos)", "Número de Alunos")

    # 4. Justificativa de Permanência
    st.header("Distribuição de Índices - Justificativa de Permanência")
    df_permanencia = df_clean[df_clean['STATUS_ALUNO'] == 'Ativo'][colunas_abordadas]
    df_permanencia['MOTIVO_PERMANENCIA'] = df_permanencia.idxmin(axis=1).str.extract(r'(\w+)_\d+')
    df_permanencia['MOTIVO_PERMANENCIA'] = df_permanencia['MOTIVO_PERMANENCIA'].map(traducao_motivos)
    motivos_counts = df_permanencia['MOTIVO_PERMANENCIA'].value_counts()
    plot_bar_chart(motivos_counts, "Distribuição de Índices - Justificativa de Permanência", "Motivos", "Número de Alunos")

    # 5. Tempo de permanência dos alunos na fase 7
    st.header("Distribuição dos Anos de Permanência dos Alunos na Fase 7")
    df_fase7 = df_clean[df_clean['FASE_PARADA'] == 7]
    df_fase7['ANO_PERMANENCIA'] = df_fase7[['ANO_INGRESSO_2020', 'ANO_INGRESSO_2021', 'ANO_INGRESSO_2022']].bfill(axis=1).iloc[:, -1]
    df_fase7['PERMANENCIA_ANOS'] = 2022 - df_fase7['ANO_PERMANENCIA']
    plot_histogram(df_fase7['PERMANENCIA_ANOS'], "Distribuição dos Anos de Permanência dos Alunos na Fase 7", "Anos de Permanência", "Número de Alunos")

    # 6. Comparação entre alunos indo bem e não indo bem
    st.header("Comparação de Desempenho entre Alunos Indo Bem e Não Indo Bem")
    df_ativos = df_clean[df_clean['STATUS_ALUNO'] == 'Ativo']
    indices = ['IAN_2020', 'IAN_2021', 'IAN_2022', 'IDA_2020', 'IDA_2021', 'IDA_2022', 
               'IEG_2020', 'IEG_2021', 'IEG_2022', 'IAA_2020', 'IAA_2021', 'IAA_2022',
               'IPS_2020', 'IPS_2021', 'IPS_2022', 'IPP_2020', 'IPP_2021', 'IPP_2022', 
               'IPV_2020', 'IPV_2021', 'IPV_2022']
    df_ativos['MEDIA_INDICES'] = df_ativos[indices].mean(axis=1)
    media_global = df_ativos[indices].stack().mean()
    limite_bem = media_global
    df_ativos['STATUS_DESEMPENHO'] = ['Indo Bem' if x > limite_bem else 'Não Indo Bem' for x in df_ativos['MEDIA_INDICES']]
    df_comparacao = df_ativos.groupby('STATUS_DESEMPENHO')[indices].mean()

    # Comparações entre os grupos
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_ativos, x='STATUS_DESEMPENHO', y='MEDIA_INDICES', palette=['#A2CFE6', '#F79651'])
    plt.title('Distribuição dos Índices de Desempenho entre Alunos Indo Bem e Não Indo Bem', fontsize=12)
    plt.xlabel('Status de Desempenho', fontsize=10)
    plt.ylabel('Média dos Índices', fontsize=10)
    plt.axhline(y=media_global, color='red', linestyle='--', label=f'Média Global: {media_global:.2f}')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot()

    # Comparações entre indicadores
    df_comparacao.T.plot(kind='bar', figsize=(14, 7), color=['#A2CFE6', '#F79651'])
    plt.title('Comparação de Médias dos Indicadores entre Alunos Indo Bem e Não Indo Bem', fontsize=12)
    plt.ylabel('Média dos Indicadores', fontsize=10)
    plt.xlabel('Indicadores', fontsize=10)
    plt.xticks(rotation=45, ha='right')
    plt.axhline(y=media_global, color='red', linestyle='--', label=f'Média Global: {media_global:.2f}')
    plt.legend()
    plt.tight_layout()
    st.pyplot()

    st.write(f"Média global dos índices: {media_global:.2f}")












    
if selected_page == "Etapas do Desenvolvimento: Modelo Preditivo":
    
    st.title("Etapas do Desenvolvimento: Modelo Preditivo")
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")
