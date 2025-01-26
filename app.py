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
    
    

    col1, col2 = st.columns([1, 3])  

    with col1:
        st.image("logo.png", width=300) 
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
    
    st.write("## Acesse o Notebook Completo:")
    notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Passos_Magicos_dataset.ipynb"
    st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")

    st.write("## Análise Descritiva dos Dados:")
    with st.expander("## Introdução"):
        st.markdown( '''
Este documento apresenta as análises realizadas sobre o desempenho educacional dos alunos da ONG "Passos Mágicos" 
durante os anos de 2020, 2021 e 2022. O objetivo foi compreender os padrões de progresso, desistências, e os fatores que influenciam o aprendizado dos alunos. Os dados analisados incluem diversos indicadores, como desempenho acadêmico, engajamento, adequação ao nível e aspectos psicossociais.''')

    with st.expander("## **Análise dos Dados**"):
        st.markdown( '''
*Tratamento e Organização dos Dados*

Os dados foram organizados e analisados conforme os seguintes passos:
* Segmentação Temporal: O dataset foi dividido por ano para facilitar o tratamento inicial.
* Padronização: As variáveis foram unificadas e transformadas em um único dataframe padronizado.
* Novas Métricas: Foram criadas colunas adicionais para identificar desistências e facilitar a análise de desempenho.

**Variáveis Analisadas**

O estudo utilizou os seguintes indicadores principais:
* Fase: Nível de aprendizado do aluno (0 a 8).
* Pedra: Classificação do aluno com base no Índice de Desenvolvimento Educacional (INDE).
* Ponto de Virada: Indicação do alcance de um marco educacional significativo no ano correspondente.
* IAN: Indicador de Adequação ao Nível.
* IDA: Indicador de Aprendizado.
* IEG: Indicador de Engajamento.
* IAA: Indicador de Autoavaliação.
* IPS: Indicador Psicossocial.
* IPP: Indicador Psicopedagógico.
* IPV: Indicador de Ponto de Virada.
* INDE: Índice de Desenvolvimento Educacional, 
métrica consolidada ponderada pelos demais indicadores.''')

    with st.expander("## **Resultados da Análise**"):
        st.markdown( '''
*Frequência de Alunos por Fase*
* 2020: A maior concentração de alunos estava nas fases 1 a 3.
* 2021 e 2022: As fases 0 a 3 apresentaram distribuições equilibradas, mas houve uma queda expressiva no número de alunos 
a partir da fase 4. Em todos os anos, a quantidade de alunos reduzia pela metade a cada avanço de fase.

*Distribuição das Pedras (Classificação pelo INDE)*

As classificações são baseadas nos seguintes intervalos:
* Quartzo: 2,405 a 5,506
* Ágata: 5,506 a 6,868
* Ametista: 6,868 a 8,230
* Topázio: 8,230 a 9,294

* 2020: Houve um número considerável de alunos classificados como Quartzo e Ametista, indicando uma boa distribuição entre os extremos.

* 2021 e 2022: A maior parte dos alunos foi classificada como Ametista e Topázio, demonstrando um desempenho geral elevado.

*Indicador Ponto de Virada*

Embora muitos alunos apresentassem bom desempenho em suas respectivas fases, a maioria não atingiu o ponto de virada nos três anos
analisados.


*Desistências: Impactos Temporais e Perfil Acadêmico*

* Análise Temporal:
    * O ano de 2021 apresentou o maior índice de desistências, um fenômeno amplamente associado aos impactos da pandemia de COVID-19.

* Perfil das Desistências:
    * A maioria das desistências ocorreu entre estudantes nas fases iniciais do curso (fases 0 a 3), evidenciando maior 
    vulnerabilidade nesse estágio acadêmico. Por outro lado, os índices de desistências nas fases mais avançadas foram 
    significativamente menores.

* Classificação dos Alunos:

    * Ativos (314): Estudantes que permaneceram matriculados durante os três anos analisados (2020, 2021 e 2022).
    * Retornaram em 2022 (13): Alunos que participaram em 2020, não estiveram presentes em 2021 (classificados como ausentes) 
    e retornaram em 2022.

* Desistências:
    * Desistências em 2022: Foram registrados 141 casos de desistências.
    * Desistências em anos anteriores: Até 2021, acumulou-se um total de 880 desistências, sendo 259 casos apenas no ano de 2021.
* Destaques da Análise:
    * A análise evidencia o impacto temporal das desistências, destacando as fases iniciais como as mais críticas em termos de 
    evasão acadêmica. Além disso, reforça o papel de eventos externos, como a pandemia, no comportamento e engajamento dos estudantes.


*Desempenho Geral (INDE)*

* A análise do INDE mostrou que a maioria dos alunos teve desempenho acima da média em todos os anos, com um aumento gradual de 
notas altas entre 2020 e 2022.

*Outliers nos Indicadores*

* IEG (Engajamento): Muitos alunos apresentaram notas abaixo da média, indicando desafios de engajamento.
* IAA (Autoavaliação): Poucos alunos se autoavaliaram negativamente, sugerindo confiança no próprio progresso.
* IPS (Psicossocial): O ano de 2021 teve os piores resultados, possivelmente devido às dificuldades impostas pela pandemia.
* IPP (Psicopedagógico): Notas baixas predominam em 2020 e 2021, mas houve melhora significativa em 2022.

*Correlação entre Indicadores*

* Os indicadores de avaliação apresentaram alta correlação com o INDE, reforçando a importância desses fatores para o 
desenvolvimento educacional.

*Tendência Anual*

* 2020: Maior média geral de notas.
* 2021: Desempenho mais baixo, refletindo as dificuldades da pandemia.
* 2022: Recuperação significativa, com aumento de novos ingressos e melhoria no desempenho geral.

''')

    with st.expander("## **Conclusão**"):
        st.markdown( '''
As análises revelaram padrões importantes no progresso e nos desafios enfrentados pelos alunos da ONG Passos Mágicos:

* A maioria dos alunos progride bem ao longo dos anos, mas as fases iniciais apresentam maior índice de desistência.
* A pandemia impactou negativamente o engajamento, o desempenho psicossocial e o psicopedagógico em 2021.
* Indicadores como IEG e INDE são cruciais para monitorar o desenvolvimento acadêmico.

''')
        
    with st.expander("## **Especulação de Melhorias para a ONG**"):
        st.markdown( '''

* Redução de Desistências nas Fases Iniciais: Implementar programas de incentivo personalizados para alunos das fases 0 a 3, 
como mentoria individualizada, apoio financeiro e acompanhamento familiar.

* Engajamento Acadêmico: Desenvolver atividades interativas e adaptadas à realidade dos alunos para melhorar o engajamento, 
especialmente para aqueles com baixos índices de IEG.

* Apoio Psicossocial: Aumentar o suporte psicológico para minimizar os efeitos de crises externas, como a pandemia, oferecendo 
sessões de acompanhamento mais frequentes.

* Monitoramento Contínuo: Implementar um sistema de monitoramento que avalie regularmente o progresso dos alunos e identifique 
precocemente os riscos de desistência.

* Integração Familiar: Envolver as famílias no processo educacional, promovendo workshops e reuniões para conscientizar sobre a 
importância da continuidade acadêmica.

Com essas estratégias, espera-se que a ONG Passos Mágicos possa aumentar a retenção dos alunos e promover um impacto ainda maior 
na formação educacional e social dos beneficiários.

''')
        
    # Carregar os dados do arquivo remoto
    url_dados = "https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/refs/heads/main/dados/df_clean.csv"
    df_clean = pd.read_csv(url_dados)   


    st.header("Conhecendo os Dados")    

    # Exibir código e resultados lado a lado
    with st.expander("Conhecendo os Dados"):
        st.dataframe(df_clean.head(20))
        st.code("""
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1348 entries, 0 to 1347
Data columns (total 40 columns):
 #   Column                    Non-Null Count  Dtype   
---  ------                    --------------  -----   
 0   NOME                      1348 non-null   object  
 1   FASE_2020                 727 non-null    float64 
 2   FASE_2021                 684 non-null    float64 
 3   FASE_2022                 862 non-null    float64 
 4   PEDRA_2020                727 non-null    category
 5   PEDRA_2021                684 non-null    category
 6   PEDRA_2022                862 non-null    category
 7   PONTO_VIRADA_2020         727 non-null    float64 
 8   PONTO_VIRADA_2021         684 non-null    float64 
 9   PONTO_VIRADA_2022         862 non-null    float64 
 10  IAN_2020                  727 non-null    float64 
 11  IAN_2021                  684 non-null    float64 
 12  IAN_2022                  862 non-null    float64 
 13  IDA_2020                  727 non-null    float64 
 14  IDA_2021                  684 non-null    float64 
 15  IDA_2022                  862 non-null    float64 
 16  IEG_2020                  727 non-null    float64 
 17  IEG_2021                  684 non-null    float64 
 18  IEG_2022                  862 non-null    float64 
 19  IAA_2020                  727 non-null    float64 
...
 38  dimensao_psicossocial     1348 non-null   float64 
 39  dimensao_psicopedagogica  1348 non-null   float64 
dtypes: category(3), float64(35), object(2)
        """, language="python") 
        
        
        st.subheader("Dimensão dos Dados")
        st.write(f"Linhas e Colunas: {df_clean.shape}") 

        st.subheader("Duplicatas em 'NOME'")
        st.write(f"Duplicatas: {df_clean['NOME'].duplicated().sum()}")

        st.markdown("* ### Correlação entre Variáveis Quantitativas")
        st.markdown("""Aqui exploramos a correlação entre variáveis numéricas.""", unsafe_allow_html=True)
        quantitative_columns_total = [
        'ANO_INGRESSO',  
        'IAN_2020', 'IAN_2021', 'IAN_2022', 'IDA_2020', 'IDA_2021', 'IDA_2022', 
        'IEG_2020', 'IEG_2021', 'IEG_2022', 'IAA_2020', 'IAA_2021', 'IAA_2022',
        'IPS_2020', 'IPS_2021', 'IPS_2022', 'IPP_2020', 'IPP_2021', 'IPP_2022', 
        'IPV_2020', 'IPV_2021', 'IPV_2022', 'INDE_2020', 'INDE_2021', 'INDE_2022'
]   
        corr = df_clean[quantitative_columns_total].corr()
        plt.figure(figsize=(15, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        st.pyplot(plt)



   
    def plot_bar_chart(data, title, xlabel, ylabel, figsize=(6, 3)):
        fig, ax = plt.subplots(figsize=figsize, facecolor='none')  
        sns.barplot(x=data.index, y=data.values, palette=custom_palette, ax=ax)
        plt.style.use('dark_background')
        ax.set_title(title, fontsize=12, color="white")
        ax.set_xlabel(xlabel, fontsize=10, color="white")
        ax.set_ylabel(ylabel, fontsize=10, color="white")
        ax.tick_params(axis='x', rotation=45, labelsize=9, colors="white")
        ax.tick_params(axis='y', colors="white")
        sns.set_style("darkgrid", {"axes.facecolor": "none"})  
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        fig.patch.set_alpha(0)  # Fundo da figura transparente
        st.pyplot(fig)

    def plot_histogram(data, title, xlabel, ylabel, figsize=(6, 3), bins=10):
        fig, ax = plt.subplots(figsize=figsize, facecolor='none')  # Fundo transparente
        sns.histplot(data, kde=True, palette=custom_palette, bins=bins, ax=ax)
        plt.style.use('dark_background')
        ax.set_title(title, fontsize=12, color="white")
        ax.set_xlabel(xlabel, fontsize=10, color="white")
        ax.set_ylabel(ylabel, fontsize=10, color="white")
        ax.tick_params(axis='x', colors="white")
        ax.tick_params(axis='y', colors="white")
        sns.set_style("darkgrid", {"axes.facecolor": "none"})  # Transparente nos eixos
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        fig.patch.set_alpha(0)  # Fundo da figura transparente
        st.pyplot(fig)


    custom_palette = ['#F79651', '#2A6DA6', '#A2CFE6']

    st.title("Análise de Desempenho de Alunos")

    st.header("Distribuição das Fases em que os Alunos Pararam")
    df_clean['FASE_PARADA'] = df_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']].bfill(axis=1).iloc[:, -1]
    fase_counts = df_clean['FASE_PARADA'].value_counts()
    plot_bar_chart(fase_counts, "Distribuição das Fases em que os Alunos Pararam", "Fase", "Número de Alunos")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    df_clean['dimensao_academica'] = df_clean[
        ['IAN_2020', 'IDA_2020', 'IEG_2020',
        'IAN_2021', 'IDA_2021', 'IEG_2021',
        'IAN_2022', 'IDA_2022', 'IEG_2022']
    ].mean(axis=1)

    df_clean['dimensao_psicossocial'] = df_clean[
        ['IAA_2020', 'IPS_2020',
        'IAA_2021', 'IPS_2021',
        'IAA_2022', 'IPS_2022']
    ].mean(axis=1)

    df_clean['dimensao_psicopedagogica'] = df_clean[
        ['IPP_2020', 'IPV_2020',
        'IPP_2021', 'IPV_2021',
        'IPP_2022', 'IPV_2022']
    ].mean(axis=1)

    df_desistencia = df_clean[df_clean['STATUS_ALUNO'] == 'Desistencia']

    df_desistencia['MOTIVO_DESISTENCIA'] = df_desistencia[
        ['dimensao_academica', 'dimensao_psicossocial', 'dimensao_psicopedagogica']
    ].idxmin(axis=1)

    traducao_dimensoes = {
        'dimensao_academica': 'Indicador Acadêmico',
        'dimensao_psicossocial': 'Indicador Psicossocial',
        'dimensao_psicopedagogica': 'Indicador Psicopedagógico'
    }
    df_desistencia['MOTIVO_DESISTENCIA'] = df_desistencia['MOTIVO_DESISTENCIA'].map(traducao_dimensoes)

    motivos_counts = df_desistencia['MOTIVO_DESISTENCIA'].value_counts()
    st.header("Distribuição dos Motivos de Desistência")
    plot_bar_chart(motivos_counts, "Distribuição dos Motivos de Desistência - Possíveis Desistentes", "Motivos", "Número de Alunos")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    st.header("Distribuição dos Motivos de Desistência")
    colunas_abordadas = [
        'IAN_2020', 'IAN_2021', 'IAN_2022', 'IDA_2020', 'IDA_2021', 'IDA_2022',
        'IEG_2020', 'IEG_2021', 'IEG_2022', 'IAA_2020', 'IAA_2021', 'IAA_2022',
        'IPS_2020', 'IPS_2021', 'IPS_2022', 'IPP_2020', 'IPP_2021', 'IPP_2022',
        'IPV_2020', 'IPV_2021', 'IPV_2022'
    ]
    df_desistencia = df_clean[df_clean['STATUS_ALUNO'] == 'Desistencia'][colunas_abordadas]
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

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.header("Distribuição de Índices - Justificativa de Permanência")
    df_permanencia = df_clean[df_clean['STATUS_ALUNO'] == 'Ativo'][colunas_abordadas]
    df_permanencia['MOTIVO_PERMANENCIA'] = df_permanencia.idxmin(axis=1).str.extract(r'(\w+)_\d+')
    df_permanencia['MOTIVO_PERMANENCIA'] = df_permanencia['MOTIVO_PERMANENCIA'].map(traducao_motivos)
    motivos_counts = df_permanencia['MOTIVO_PERMANENCIA'].value_counts()
    plot_bar_chart(motivos_counts, "Distribuição de Índices - Justificativa de Permanência", "Motivos", "Número de Alunos")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    st.header("Distribuição dos Anos de Permanência dos Alunos na Fase 7")
    df_fase7 = df_clean[df_clean['FASE_PARADA'] == 7]
    df_fase7['ANO_PERMANENCIA'] = df_fase7[['ANO_INGRESSO']].bfill(axis=1).iloc[:, -1]
    df_fase7['PERMANENCIA_ANOS'] = 2022 - df_fase7['ANO_PERMANENCIA']
    plot_histogram(df_fase7['PERMANENCIA_ANOS'], "Distribuição dos Anos de Permanência dos Alunos na Fase 7", "Anos de Permanência", "Número de Alunos")


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

    fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
    sns.boxplot(data=df_ativos, x='STATUS_DESEMPENHO', y='MEDIA_INDICES', palette=['#A2CFE6', '#F79651'], ax=ax)
    plt.title('Distribuição dos Índices de Desempenho entre Alunos Indo Bem e Não Indo Bem', fontsize=12, color="white")
    plt.xlabel('Status de Desempenho', fontsize=10, color="white")
    plt.ylabel('Média dos Índices', fontsize=10, color="white")
    plt.xticks(rotation=45, ha='right', color="white")
    plt.axhline(y=media_global, color='red', linestyle='--', label=f'Média Global: {media_global:.2f}')
    plt.legend(labelcolor="white") 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    fig.patch.set_alpha(0)
    sns.set_style("darkgrid", {"axes.facecolor": "none"}) 
    plt.gca().set_facecolor('none') 
    st.pyplot(fig, transparent=True) 

    # Comparações entre indicadores
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
    df_comparacao.T.plot(kind='bar', color=['#A2CFE6', '#F79651'], ax=ax)
    plt.title('Comparação de Médias dos Indicadores entre Alunos Indo Bem e Não Indo Bem', fontsize=12, color="white")
    plt.ylabel('Média dos Indicadores', fontsize=10, color="white")
    plt.xlabel('Indicadores', fontsize=10, color="white")
    plt.xticks(rotation=45, ha='right', color="white")
    plt.axhline(y=media_global, color='red', linestyle='--', label=f'Média Global: {media_global:.2f}')
    plt.legend(labelcolor="white")  
    plt.tight_layout()
    sns.set_style("darkgrid", {"axes.facecolor": "none"})
    fig.patch.set_alpha(0) 
    st.pyplot(fig, transparent=True)
    st.write(f"Média global dos índices: {media_global:.2f}")



    
if selected_page == "Etapas do Desenvolvimento: Modelo Preditivo":
    
    st.title("Etapas do Desenvolvimento: Modelo Preditivo")
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")
