#Importação das bibliotecas
import streamlit as st 
import pandas as pd
import joblib
from joblib import load
from nbconvert import HTMLExporter
import nbformat
import seaborn as sns
import matplotlib.pyplot as plt
from utils import novo_pipeline
import time



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
st.sidebar.markdown(
    "<h3 style='font-size:22px;'>Selecione uma Página:</h3>", 
    unsafe_allow_html=True
)

selected_page = st.sidebar.radio("", list(pages.keys()))

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

    pbi_url = r'https://app.powerbi.com/view?r=eyJrIjoiZTNmNDg3OWMtYmEwNy00YWVjLWJkZDItYmZkYTZlNTY0ZWU1IiwidCI6ImRlOTgwY2Y4LWYwYzctNGFlZC1iNjc2LTJlOTlkNjg2YzAzMyJ9 '

    st.components.v1.html(f'<iframe width="100%" height="600" src="{pbi_url}" frameborder="0" allowFullScreen="true"></iframe>', height=600)
    
    st.markdown(
        '''
        **Apresentação do Dashboard Interativo**

        Foco em Gênero, Idade e Classificações por Pedras

        **Introdução**

        Nossa apresentação do Dashboard Interativo tem como objetivo principal fornecer uma análise detalhada dos dados relacionados a gênero, idade e classificações por pedras. Este dashboard foi desenvolvido para oferecer uma visualização clara e intuitiva, permitindo aos usuários interagir e explorar os dados de forma eficiente.

        **Análise por Gênero**

        O dashboard apresenta uma segmentação detalhada dos dados por gênero, permitindo a identificação de padrões e tendências específicas entre diferentes grupos. Com isso, podemos entender melhor as dinâmicas de gênero e como elas influenciam outros fatores no contexto analisado.

        **Análise por Idade**

        A análise por faixa etária é outro aspecto crucial do nosso dashboard. As visualizações são projetadas para destacar as diferenças e semelhanças entre diferentes grupos de idade, facilitando a identificação de tendências demográficas importantes que podem impactar as decisões estratégicas.

        **Análise por Classificações de Pedras**

        Por fim, o dashboard inclui uma seção dedicada às classificações por pedras. Esta análise permite uma compreensão aprofundada das preferências e classificações associadas a diferentes tipos de pedras, proporcionando insights valiosos para diversas aplicações, como marketing, vendas e atendimento ao cliente.

        **Conclusão**

        Em resumo, nosso Dashboard Interativo oferece uma ferramenta poderosa para a análise de dados, focando em gênero, idade e classificações por pedras. Esperamos que esta apresentação demonstre a eficácia do dashboard em fornecer insights acionáveis e apoiar tomadas de decisão informadas.
        '''
    )

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

    st.write("## Acesse o Notebook Completo:")
    notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Datathon-Passos_Magicos.ipynb"
    st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")
    
    st.markdown(
            '''
            **Introdução**

            Foram utilizados três datasets neste projeto: df_2020_clean.csv, df_2021_clean.csv e df_2022_clean.csv. 
            Identificamos que seria benéfico dividir os dados por ano, pois essa abordagem nos permitiria obter uma visualização mais clara e detalhada das informações. Além disso, essa divisão facilita uma análise mais precisa ao observar as variações e tendências ao longo de diferentes períodos. Para dividir os dataframes, realizar a limpeza dos dados, gerar o mapa de correlação e criar o gráfico de contagem, seguimos uma metodologia estruturada que garantiu a integridade e a clareza dos resultados obtidos.
            ''')
    
    with st.expander('Criando Funções'):
        st.markdown(
            '''
            A função filter_columns foi utilizada para filtrar colunas de um DataFrame com base em padrões específicos. Ela recebeu um DataFrame (df) e uma lista de padrões (filters). A função verifica se os nomes das colunas contêm algum dos padrões especificados na lista de filtros. Se uma coluna contiver um dos padrões, ela será excluída do DataFrame final. Essa função foi útil para remover colunas indesejadas de forma eficiente
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem01.png')

        st.markdown(
            '''
            A função cleaning_dataset foi utilizada para limpar o DataFrame removendo linhas com valores ausentes (NaN). Nela executamos duas operações principais:
            Removemos a linhas onde todas as colunas, exceto a coluna 'NOME', contêm valores NaN.
            Removemos linhas que contêm apenas valores NaN. Com isso, garantimos que o DataFrame resultante não tivesse linhas completamente vazias, melhorando a qualidade dos dados para análise.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem02.png')

    with st.expander('Limpeza dos dados 2020'):

        st.markdown(
            '''
            Neste trecho de código, realizamos a transformação dos dados de ingresso dos alunos para o ano de 2020. As etapas foram as seguintes:

            -   Mapeamento de Anos: Criamos um dicionário (ano_map_2020) para mapear os anos de ingresso dos alunos. Em seguida, criamos um dicionário reverso (reverse_ano_map_2020) para facilitar a substituição dos valores mapeados.
            -   Substituição de Valores: Utilizamos o dicionário reverso para substituir os valores na coluna ANOS_PM_2020 do DataFrame df_2020_clean.
            -	Renomeação de Coluna: Renomeamos a coluna ANOS_PM_2020 para ANO_INGRESSO_2020 para refletir a transformação realizada.
            - 	Conversão para Datetime: Convertimos a coluna ANO_INGRESSO_2020 para o formato datetime e extraímos apenas o ano.

            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem03.png')

        st.markdown(
            '''
            Neste trecho de código, realizamos a separação da parte numérica e alfabética da coluna FASE_TURMA_2020 do DataFrame df_2020_clean. As etapas foram as seguintes:

            - 	Captura dos Números: Utilizamos a função str.extract para capturar a parte numérica da coluna FASE_TURMA_2020 e armazená-la em uma nova coluna chamada FASE_2020.
            - 	Captura das Letras: Utilizamos a função str.extract para capturar a parte alfabética da coluna FASE_TURMA_2020 e armazená-la em uma nova coluna chamada TURMA_2020
        Convertemos a coluna PONTO_VIRADA_2020 em valores binários (0 e 1), onde 'Sim' é mapeado para 1 e qualquer outro valor é mapeado para 0.
        Convertemos a coluna INDE_2020 para valores numéricos, utilizando pd.to_numeric com a opção errors='coerce' para tratar valores inválidos.
        Convertemos a coluna PEDRA_2020 para uma categoria utilizando pd.Categorical.

        Verificamos os valores únicos na coluna INDE_CONCEITO_2020 para entender melhor os dados presentes nessa coluna.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem04.png')

        st.markdown(
            '''
        Aqui, verificamos se cada valor na coluna 'DESTAQUE_IPV_2020' é uma string e contém a frase 'Seu destaque em 2020:'. Se sim, marcamos com 1; se não, marcamos com 0. Basicamente, estamos identificando quem recebeu destaque em 2020.

        Convertemos as colunas IAA_2020, IEG_2020, IPS_2020, IDA_2020, IPP_2020, IPV_2020 e IAN_2020 para valores numéricos, utilizando a função pd.to_numeric e definindo errors='coerce' para tratar erros.

        Removemos as colunas TURMA_2020, FASE_TURMA_2020, INSTITUICAO_ENSINO_ALUNO_2020, IDADE_ALUNO_2020 e INDE_CONCEITO_2020 do DataFrame df_2020_clean.
        Aplicamos essa mesma transformação para os datasets de 2021 e 2022.
        '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem05.png')

    with st.expander('Limpeza dos dados 2021 e 2022'):

        st.markdown(
            '''
            Realizamos várias operações de limpeza e transformação no DataFrame df_2021_clean. Primeiro, verificamos a contagem de valores na coluna SINALIZADOR_INGRESSANTE_2021 e a quantidade de valores nulos. Em seguida, aplicamos uma função lambda para definir o valor como 2021 se a string contiver 'Ingressante', caso contrário, definimos como 'Veterano'.

            Depois, criamos um DataFrame df_ano_veterano com os alunos veteranos e o mesclamos com os dados de 2020 para obter o ano de ingresso. Atualizamos a coluna ANO_INGRESSO_2020 para os ingressantes de 2021 que não tinham essa informação. Removemos alunos específicos e colunas desnecessárias, renomeamos a coluna ANO_INGRESSO_2020 para ANO_INGRESSO_2021, e convertimos essa coluna para o formato de ano. Por fim, identificamos que há 12 alunos sem data de entrada.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem06.png')

        st.markdown(
            '''
            Nós realizamos várias transformações no DataFrame df_2021_clean. Primeiro, transformamos a coluna PONTO_VIRADA_2021 em valores binários (0 e 1), onde 'Sim' é convertido para 1 e qualquer outro valor para 0. Em seguida, convertimos a coluna INDE_2021 para valores numéricos, tratando erros com errors='coerce'. Também transformamos as colunas NIVEL_IDEAL_2021 e PEDRA_2021 em categorias.

            Para unificar as colunas de recomendações (REC_EQUIPE_1_2021, REC_EQUIPE_2_2021, REC_EQUIPE_3_2021, REC_EQUIPE_4_2021), criamos uma nova coluna REC_AVA_UNIFICADO, que contém a recomendação mais frequente de cada linha. Removemos as colunas originais de recomendações após a unificação.

            Corrigimos a sintaxe do dicionário fase_map_2021 e criamos um dicionário reverso para mapear os textos de NIVEL_IDEAL_2021 para números correspondentes. Finalmente, substituímos os textos em NIVEL_IDEAL_2021 pela numeração correspondente.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem07.png')

        st.markdown('OBS: Fizemos o mesmo tratamento para a base de 2022.')

    with st.expander('Unindo os DataFrames'):

        st.markdown(
            '''
            Realizamos a fusão dos DataFrames df_2020_clean, df_2021_clean e df_2022_clean utilizando a coluna NOME como chave, com a opção how='outer' para incluir todos os registros de cada DataFrame. Em seguida, selecionamos as colunas de interesse para o DataFrame final df_clean, que inclui informações sobre fases, pedras, pontos de virada, anos de ingresso e várias outras métricas para os anos de 2020, 2021 e 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem08.png')

    with st.expander('Tratando Dados Nulos'):

        st.markdown(
            '''
            A coluna NOME tem 1348 entradas não nulas e é do tipo object (string).
            A coluna FASE_2020 tem 727 entradas não nulas e é do tipo object.
            A coluna PEDRA_2020 tem 727 entradas não nulas e é do tipo category.
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem09.png')

        
        st.markdown(
            '''
            Nós verificamos se há valores duplicados na coluna NOME do DataFrame df_clean e confirmamos que não há duplicatas (np.int64(0)). Em seguida, contamos o número de valores nulos em cada coluna do DataFrame. A observação final sugere que os valores nulos podem indicar alunos que desistiram de participar do projeto.
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem10.png')

    with st.expander('Explorando os Dados'):
        st.markdown(
            '''
            Definimos uma lista de colunas qualitativas qualitative_columns_total e um dicionário categories que agrupa essas colunas em categorias (FASE, PEDRA, PONTO_VIRADA, STATUS_ALUNO). Em seguida, realizamos uma análise de frequência para cada categoria, calculando a distribuição de frequências normalizadas (em porcentagem) para cada coluna dentro das categorias. 
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem11.png')

        st.markdown(
            '''
            **Distribuição de Frequências para FASE**

            Aumento na fase inicial (0): A porcentagem de indivíduos na fase inicial cresceu de 11.28% em 2020 para 22.04% em 2022, indicando um influxo significativo de novos participantes nos últimos anos.

            Redistribuição em fases intermediárias: As fases intermediárias (1 a 5) mostram estabilidade relativa, com variações moderadas. No entanto, a fase 2 diminuiu de 23.68% em 2021 para 17.98% em 2022, sugerindo uma possível dificuldade em avançar a partir dessa etapa.

            Redução em fases avançadas (6 e superiores): Observa-se uma tendência decrescente nas fases finais. A fase 8 praticamente desaparece em 2021 e 2022, o que pode indicar que estes alunos ingressaram nos cursos superiores.

            A alta concentração inicial em 2022 e a redução nas fases avançadas apontam para uma necessidade de estratégias para aumentar a progressão e retenção em níveis mais elevados.
            ''')
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem12.png')
        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem13.png')

        st.markdown(
            '''
            **Distribuição de Frequências para PONTO_VIRADA**

            Predominância do valor 0 (não atingiram o ponto de virada): A maior parte dos indivíduos não conseguiu avançar para os próximos passos, com a porcentagem de participantes que não atingiram o ponto de virada variando de 87.07% em 2020 para 86.89% em 2022.
            Leve aumento do valor 1 (atingiram o ponto de virada) em 2021: A porcentagem de indivíduos que conseguiram avançar para os próximos passos aumentou ligeiramente em 2021, alcançando 15.79%. Esse aumento pode ser reflexo de mudanças no ambiente ou na dinâmica dos participantes, como impactos externos, incluindo a pandemia de COVID-19.
            Embora a maioria dos indivíduos não tenha avançado para os próximos passos, o aumento observado em 2021 sugere que é importante monitorar fatores externos e suas influências no progresso dos alunos.
            ''')
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem14.png')
        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem15.png')

        st.markdown(
            '''
            **Distribuição de Frequências para STATUS_ALUNO**

            Alta taxa de desistência: Quase metade dos alunos (46.07%) desiste do programa, sendo um indicador crítico para avaliação. Entre os que desistem, 19.21% o fazem em 2021 e 10.46% em 2022.
            Baixa taxa de retorno: Apenas 0.96% dos alunos retornam ao programa em 2022, indicando dificuldades de reintegração.
            Proporção de ativos: Apenas 23.29% permanecem ativos, reforçando a necessidade de intervenções para melhorar a retenção.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem16.png ')

    with st.expander('Alunos Que Desistiram'):

        st.markdown(
            '''
            Criamos um gráfico de barras para visualizar a distribuição de desistências por fase e ano
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem17.png')

        st.markdown(
            '''
            A alta taxa de desistência e o baixo retorno ao programa são sinais de alerta, sugerindo a necessidade de estratégias para engajamento, suporte e acompanhamento dos alunos.

            Aumento progressivo das desistências ao longo dos anos: Há uma tendência clara de aumento nas desistências conforme o tempo passa, com picos significativos em 2022. Isso sugere que fatores externos, como a pandemia de COVID-19 ou outras mudanças no contexto educacional, podem ter influenciado negativamente o progresso dos alunos.

            Fases mais críticas: As fases iniciais e intermediárias (Fase 0 a Fase 3) parecem ser os pontos de maior risco para desistência, com aumento considerável ao longo dos anos. Isso pode indicar a necessidade de intervenções mais eficazes nessas fases, oferecendo apoio extra aos alunos para que não desistam antes de avançarem.

            Alunos mais avançados (Fase 4 a Fase 7): Apesar de uma quantidade menor de desistências nessas fases, ainda há uma preocupação, já que o aumento nas desistências de 2021 para 2022 pode ser reflexo de desafios acumulados ao longo do percurso acadêmico.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem18.png')

    with st.expander('Ano de Ingresso dos Alunos'):

        st.markdown(
            '''
            Nós definimos uma lista de colunas quantitativas quantitative_columns_total, que inclui várias métricas para os anos de 2020, 2021 e 2022, além da coluna ANO_INGRESSO. Essas colunas contêm dados numéricos que podem ser analisados estatisticamente.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem19.png')

        st.markdown(
            '''
            O ano médio de ingresso é 2019, o que é esperado, considerando que os dados são relativos a três anos consecutivos. O desvio padrão (1.78) indica que a variação dos anos de ingresso não é muito grande, a maioria dos alunos ingressou em 2019, com poucos ingressando em 2016 e 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem20.png')

    with st.expander('Correlação entre Variáveis'):

        st.markdown(
            '''
            Valores próximos de 1 indicam uma forte correlação positiva, enquanto valores próximos de -1 indicam uma forte correlação negativa.
            Valores próximos de 0 indicam pouca ou nenhuma correlação linear.
            Esse gráfico ajuda a identificar quais variáveis têm relações fortes entre si, o que pode ser útil para análises estatísticas e modelagem preditiva.

            **Maiores correlações positivas:**

            -	IDA_2021 e IDA_2022: Correlação muito alta, acima de 0.85, sugerindo forte relação entre os anos consecutivos.
            -	INDE_2021 e INDE_2022: Correlação alta, acima de 0.86, indicando consistência ou padrão similar entre essas variáveis ao longo dos anos.
            -	IEG_2021 e IEG_2022: Correlação acima de 0.87, também indicando alta relação entre os anos consecutivos para essas variáveis.

            **Maiores correlações negativas:**
            -	ANO_INGRESSO e IPP_2022: Correlação negativa forte em torno de -0.35, sugerindo uma relação inversa entre o ano de ingresso e o desempenho ou métrica associada ao IPP em 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem21.png')

    with st.expander('INDE(Indice de Desenvolvimento)'):

        st.markdown(
            '''
            Criamos gráficos de barras para visualizar as estatísticas de INDE (Índice de Desenvolvimento) para os anos de 2020, 2021 e 2022.          
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem22.png')

        st.markdown(
            '''
            O INDE_2020 apresenta a maior média (7.30), seguida de uma leve diminuição para 6.89 em 2021 e 7.03 em 2022.

            O desvio padrão menor ao longo dos anos sugere uma redução na variabilidade entre os alunos em relação à necessidade de desenvolvimento educacional, indicando que o apoio oferecido foi mais homogêneo ao longo do tempo.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem23.png')

    with st.expander('Análise Temporal '):

        st.markdown(
            '''
            Fizemos uma visualização da tendência anual das médias de várias métricas ao longo dos anos 2020, 2021 e 2022, para ajudar a identificar como essas métricas evoluíram ao longo do tempo, fornecendo insights sobre possíveis padrões ou mudanças. 

            Análise de Tendências: O código calcula as médias anuais para cada métrica (IAN, IDA, IEG, IAA, IPS, IPP, IPV, INDE).

            Identificação de Padrões: Ao visualizar as médias anuais, é possível identificar padrões, como aumentos ou diminuições consistentes em determinadas métricas. Isso pode ajudar a entender o comportamento dos dados e a tomar decisões informadas com base nas tendências observadas.

            Comparação entre Anos: Permite comparar as médias de cada métrica entre os anos 2020, 2021 e 2022. Isso é útil para avaliar o impacto de diferentes fatores ao longo do tempo e para identificar anos específicos em que ocorreram mudanças significativas.

            Visualização Intuitiva: A utilização de gráficos de linha com pontos e anotações torna a visualização das tendências mais intuitiva e fácil de interpretar.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem24.png')

        st.markdown(
            '''
            IAN (Índice de Avaliação de Necessidades): O índice IAN mostra uma tendência de queda ao longo dos três anos analisados, com uma redução de 7,43 em 2020 para 6,42 em 2022. Isso sugere uma diminuição nas necessidades dos alunos ao longo do tempo, o que pode indicar uma melhoria nas condições ou nos apoios oferecidos, resultando em menos necessidades de intervenção.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem25.png')

        st.markdown(
            '''
            IDA (Índice de Desempenho Acadêmico): O desempenho acadêmico diminui de 2020 (6,32) para 2021 (5,43), o que pode ser um reflexo de desafios enfrentados pelos alunos, como a pandemia de COVID-19. Em 2022, há uma leve recuperação para 6,07, o que pode indicar um processo de adaptação, onde os alunos começam a se recuperar do impacto das circunstâncias anteriores.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem26.png')

        st.markdown(
            '''
            IEG (Índice de Engajamento Geral): O engajamento segue uma tendência interessante: cai de 7,80 em 2020 para 6,84 em 2021, possivelmente devido ao impacto da pandemia e mudanças no formato de ensino. No entanto, há uma recuperação em 2022 para 7,88, sugerindo que os alunos estão voltando a se engajar mais, possivelmente com a retomada das atividades presenciais ou com melhorias nos métodos de ensino.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem27.png')

        st.markdown(
            '''
            IAA (Índice de Apoio Acadêmico): O apoio acadêmico se manteve bastante estável ao longo dos três anos, com pequenas variações entre 2020 (8,37), 2021 (8,16) e 2022 (8,26). Isso indica que o suporte oferecido aos alunos não foi drasticamente afetado pela pandemia e manteve-se eficaz ao longo do tempo, com uma leve queda apenas.            
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem28.png')

        st.markdown(
            '''
             IPS (Índice de Progresso Social): O progresso social apresentou uma leve melhoria ao longo dos três anos, com a média aumentando de 6,74 em 2020 para 6,90 em 2022. Isso pode refletir esforços para apoiar o desenvolvimento social dos alunos, possivelmente devido a iniciativas para lidar com os efeitos da pandemia e melhorar as condições sociais.           
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem29.png')

        st.markdown(
            '''
            IPP (Índice de Progresso Pessoal): O índice de progresso pessoal apresenta uma melhoria em 2021 (7,60), mas uma queda significativa em 2022 (6,30). Esse comportamento pode estar relacionado ao impacto prolongado da pandemia, que pode ter afetado o bem-estar emocional e pessoal dos alunos, resultando em dificuldades no desenvolvimento pessoal em 2022.            
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem30.png')

        st.markdown(
            '''
            IPV (Índice de Progresso Vital): O progresso vital mostra uma leve tendência de melhora em 2021 (7,43), mas com uma queda sutil em 2022 (7,25). Isso pode indicar que os alunos, apesar dos desafios, conseguiram manter uma boa trajetória em termos de seu progresso vital, embora com uma leve diminuição após o pico de 2021.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem31.png')

        st.markdown(
            '''
            INDE (Índice de Necessidade de Desenvolvimento Educacional): O índice INDE apresentou uma leve queda de 2020 para 2021, mas em 2022 houve uma leve recuperação para 7,03. Isso sugere que, apesar de uma ligeira diminuição na necessidade de desenvolvimento educacional em 2021, houve uma leve reversão dessa tendência em 2022, possivelmente devido a melhorias nas condições educacionais.            
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem32.png')

    with st.expander('Visualização de Densidade'):

        st.markdown(
            '''
            Analisamos a distribuição de densidade das métricas IAN, IDA, IEG, IAA, IPS, IPP, IPV e INDE para os anos de 2020, 2021 e 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem33.png')

        st.markdown(
            '''
            IAN (Índice de Aprovação de Notas): As curvas de densidade são simétricas nos três anos analisados. A maior densidade ocorre em 2022, enquanto a menor densidade é observada em 2020. Isso indica uma leve melhoria na distribuição dos índices de aprovação ao longo dos anos.

            IDA (Índice de Desempenho Acadêmico): As curvas apresentam uma assimetria, inclinadas para o lado, sugerindo a presença de outliers. A maior densidade ocorre nos anos de 2021 e 2022, com a maior concentração de dados, enquanto o ano de 2020 apresenta uma distribuição mais dispersa.

            IEG (Índice de Engajamento Geral): As curvas de densidade são simétricas nos anos de 2022 e 2020, enquanto em 2021, há uma assimetria inclinada para a esquerda. Os anos de 2022 e 2020 mostram uma maior concentração de dados próximos à média, enquanto 2021 apresenta uma dispersão maior, indicando variação no engajamento.

            IAA (Índice de Atividade Acadêmica): As curvas de densidade de 2020, 2021 e 2022 quase se sobrepõem. Isso sugere que os valores das variáveis em cada um desses anos são semelhantes, sem grandes variações entre eles.

            IPS (Índice de Participação Social): Para os valores abaixo da média combinada, as curvas são assimétricas, enquanto para os valores acima da média, as curvas se tornam simétricas. Essa diferença na distribuição pode indicar uma maior dispersão de dados em torno da média, mas uma tendência de normalidade para valores elevados.

            IPP (Índice de Participação em Projetos): Em 2022, a curva está abaixo da média combinada, enquanto em 2021 e 2020 as curvas são simétricas, com variação na densidade. A dispersão dos dados parece ser maior em 2022, com uma menor concentração de índices perto da média.

            IPV (Índice de Participação Voluntária): As curvas de densidade são simétricas nos anos de 2022 e 2020, com o pico na média combinada, enquanto em 2021, a curva é assimétrica, inclinada para o lado. O ano de 2021 apresenta uma maior dispersão, enquanto 2022 e 2020 têm maior concentração de dados próximos à média.

            INDE (Índice de Desenvolvimento Educacional): As curvas de densidade são ligeiramente simétricas, com o pico próximo à média combinada. Isso sugere que os dados estão relativamente equilibrados e próximos da média, sem grandes flutuações.
            ''')
        
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem34.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem35.png')

        with col3:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem36.png')

        with col4:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem37.png')

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem38.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem39.png')

        with col3:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem40.png')

        with col4:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem41.png')

    with st.expander('Analise de Desistências'):

        st.markdown(
            '''
            Em que fase: A análise dos dados indica que as desistências são mais comuns nas fases iniciais do curso, especialmente nas fases 0 e 1, onde a adaptação e o comprometimento podem ser maiores desafios para os alunos. À medida que os alunos progridem para as fases mais avançadas, a quantidade de desistências diminui, sugerindo que aqueles que alcançam essas fases tendem a ser mais resilientes e comprometidos.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem42.png')

        st.markdown(
            '''
            Diante das notas gerais em qual classificação estão as desistências: A análise dos motivos de desistência revela que a dimensão acadêmica é o principal fator relacionado às desistências, com uma quantidade considerável de alunos indicando dificuldades nesse aspecto. A dimensão psicossocial, embora ainda relevante, apresenta um impacto um pouco menor. Por fim, a dimensão psicopedagógica também se destaca, mas em uma proporção semelhante à acadêmica, indicando que as questões relacionadas ao aprendizado e ao apoio pedagógico têm um papel importante nas desistências.

            Essa distribuição sugere que estratégias focadas no fortalecimento acadêmico e no suporte psicopedagógico poderiam ser eficazes para reduzir as desistências entre os alunos.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem43.png')

        st.markdown(
            '''
            Tempo de Permanência para alunos com "Possível desistência”: A análise da distribuição do tempo de permanência entre os alunos que desistiram revela que a grande maioria deixou o curso nas primeiras fases, com destaque para as fases 0 e 1, que acumulam o maior número de desistências. As fases 2, 3, 4 e 5 têm um número significativamente menor de desistências, indicando que as desistências diminuem conforme o aluno avança nas fases. As fases 6 e 7 não aparecem, o que pode sugerir que os alunos que chegam a essas fases são mais resilientes ou encontram mais apoio.

            Além disso, a média de tempo de permanência dos alunos que desistiram é de apenas 0.40 anos, o que reforça a ideia de que muitas desistências acontecem logo no início do curso, possivelmente devido a dificuldades acadêmicas, psicossociais ou psicopedagógicas. Isso indica a importância de um acompanhamento mais próximo nos primeiros anos, para identificar e mitigar os fatores que levam à desistência.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem44.png')

        st.markdown(
            '''
            Tempo de permanência dos alunos na fase 7: A análise da distribuição revela que a maioria dos alunos que chegaram a essa fase permaneceu por um período curto de tempo, com muitos ficando menos de 2 anos no curso. Alguns poucos estudantes ficaram por um período de 6 anos, indicando que, embora a fase 7 represente uma fase final, nem todos os alunos têm uma trajetória longa. Além disso, há um número considerável de alunos que desistiram logo após ingressar, com períodos de permanência muito curtos, como 0 anos, o que sugere que a desistência pode ocorrer logo após a chegada à fase 7.

            O gráfico de distribuição, juntamente com os dados, sugere que a fase 7 pode ter um padrão misto: há alunos que permanecem por um tempo significativo, enquanto outros desistem rapidamente, o que pode indicar questões específicas de motivação, dificuldades acadêmicas ou outras razões externas que influenciam essa fase.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem45.png')

        st.markdown(
            '''
            Média global dos Índices: A análise desses gráficos revela que os alunos classificados como "Indo Bem" apresentam um desempenho consistentemente superior em várias dimensões, enquanto os alunos "Não Indo Bem" apresentam um desempenho mais variado e, em muitos casos, inferior à média global. Além disso, pode-se inferir que fatores acadêmicos, psicossociais e psicopedagógicos estão fortemente correlacionados ao desempenho geral dos alunos, com aqueles indo bem em uma área tendendo a ir bem nas outras também.

            Intervenções focadas nos alunos "Não Indo Bem" podem se beneficiar de uma abordagem mais personalizada, considerando suas dificuldades específicas, seja no campo acadêmico ou psicossocial.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem46.png')

    with st.expander('Criando Modelos Treino e Teste'):

        st.markdown(
            '''
            Estamos selecionando um subconjunto específico de colunas do DataFrame df_tratamento. Essas colunas foram selecionadas para focar em informações relevantes para a análise e tratamento dos dados
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem47.png')

        st.markdown(
            '''
            Categorização do Status: Criamos uma nova coluna ATIVO para indicar se o aluno está ativo ou não, e removemos a coluna original STATUS_ALUNO.

            Classificação das Dimensões: Classificamos as dimensões acadêmica, psicossocial e psicopedagógica como 'abaixo da media' ou 'excelente' com base nos valores.

            Realizamos a limpeza do DataFrame, para preparar os dados para exportação (se necessário) e analisar a distribuição dos alunos ativos e não ativos

            Essas operações ajudam a preparar os dados para análises posteriores, facilitando a interpretação e a visualização das informações.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem48.png')

        st.markdown('Separação de base treino e teste')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem49.png')

        st.markdown(
            '''
            Definimos uma classe chamada DropFeatures que herda de BaseEstimator e TransformerMixin do scikit-learn. Esta classe é um transformador personalizado que remove colunas específicas de um DataFrame.

            Essa classe pode ser útil em pipelines de pré-processamento de dados, onde a remoção de colunas específicas é necessária antes de aplicar outras transformações ou modelos.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem50.png')
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem51.png')

        st.markdown(
            '''
            Objetivo da Classe: Aplicar one-hot encoding a colunas específicas de um DataFrame. 

            Inicialização: A lista de colunas a serem transformadas é passada como argumento ao instanciar a classe.
            Ajuste (fit) e Transformação (transform): O método fit não faz nada além de retornar self, enquanto o método transform aplica one-hot encoding às colunas especificadas e concatena o resultado com o restante das colunas.

            Essa classe é útil para preparar dados categóricos para modelos de machine learning, transformando categorias em um formato numérico que pode ser utilizado pelos algoritmos
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem52.png')

        st.markdown('Utilizamos a OrdinalFeature para transformar colunas do DataFrame que contêm dados ordinais (dados que têm uma ordem natural) em valores numéricos, utilizando a codificação ordinal.')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem53.png')

        st.markdown('A Oversample foi usada para aplicar a técnica de sobremostragem (oversampling) em um DataFrame, especificamente utilizando o método SMOTE (Synthetic Minority Over-sampling Technique) para balancear a classe minoritária na coluna ATIVO.')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem54.png')

        st.markdown('Aplicamos a Pipeline nos dados:')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem55.png')

        st.markdown(
            '''
            Execução do modelo

            Treinamos o modelo de machine learning com dados de treino, avaliando seu desempenho em dados de teste para gerar várias métricas e visualizações para análise.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem56.png')

        st.markdown(
            '''
             Importamos a classe LogisticRegression, que criou uma instância do modelo de regressão logística com um estado aleatório fixo, e passou esse modelo para a função roda_modelo para treinar e avaliar o modelo com os dados de treino e teste.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem57.png')

        st.markdown(
            '''
            **Classification Report**

            **Classe 0:**
            -	Precision (Precisão): 0.98 - Aqui, 98% das previsões de classe 0 estão corretas.
            -	Recall (Revocação): 1.00 - Aqui, o modelo identificou corretamente todos os exemplos da classe 0.
            -	F1-Score: 0.99 - A média harmônica da precisão e da revocação. Um valor alto indica um bom equilíbrio entre precisão e revocação.
            -	Support: 824 - O número de ocorrências reais da classe 0 no conjunto de dados.

            **Classe 1:**
            -	Precision (Precisão): 1.00 - A precisão é perfeita, indicando que todas as previsões de classe 1 estão corretas.
            -	Recall (Revocação): 0.98 - O modelo identificou corretamente 98% dos exemplos da classe 1.
            -	F1-Score: 0.99 - A média harmônica da precisão e da revocação.
            -	Support: 824 - O número de ocorrências reais da classe 1 no conjunto de dados.

            **Métricas Globais**
            -	Accuracy (Acurácia): 0.99 - A proporção de todas as previsões corretas. Aqui, 99% das previsões do modelo estão corretas.
            -	Macro Avg (Média Macro):
            -	Precision: 0.99
            -	Recall: 0.99
            -	F1-Score: 0.99

            A média macro calcula a média das métricas para cada classe, tratando todas as classes igualmente.
            
            A média ponderada leva em conta o suporte (número de ocorrências) de cada classe, dando mais peso às classes com mais exemplos.
            -	Weighted Avg (Média Ponderada):
            -	Precision: 0.99
            -	Recall: 0.99
            -	F1-Score: 0.99

            **Resumo**

            Precisão e Revocação: O modelo tem uma precisão e revocação muito altas para ambas as classes, indicando que ele é muito eficaz em identificar corretamente ambas as classes.

            F1-Score: Alto para ambas as classes, mostrando um bom equilíbrio entre precisão e revocação.

            Acurácia: Muito alta, com 99% de todas as previsões corretas.

            Médias Macro e Ponderada: Ambas são altas, indicando que o modelo é consistente em seu desempenho em todas as classes.

            Em resumo, o modelo de regressão logística está performando excepcionalmente bem, com alta precisão, revocação e F1-score, além de uma acurácia geral de 99%.
            ''')

        col1, col2 = st.columns(2)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem58.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem59.png')

    with st.expander('DecisionTreeClassifier'):

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem60.png')

        st.markdown(
            '''
            **AUC (Área Sob a Curva)**

            Valor: 0.9997128028089357
            Interpretação: Um valor de AUC muito próximo de 1 indica que o modelo tem uma capacidade quase perfeita de distinguir entre as classes positivas e negativas. Isso sugere que o modelo está performando excepcionalmente bem.

            Métrica KS (Kolmogorov-Smirnov)
            Resultado: KstestResult(statistic=np.float64(0.007281553398058253), pvalue=np.float64(0.9999999999939724), statistic_location=np.float64(0.5), statistic_sign=np.int8(-1))

            **Interpretação:**

            Statistic: 0.007281553398058253 - Este valor representa a maior diferença entre as distribuições cumulativas das classes positivas e negativas. Um valor tão baixo indica que as distribuições das classes são muito semelhantes.
            P-value: 0.9999999999939724 - Um valor extremamente alto, indicando que a diferença entre as distribuições não é estatisticamente significativa. Em outras palavras, não há evidência de que as distribuições das classes sejam diferentes.
            Statistic Location: 0.5 - O ponto onde a maior diferença ocorre.
            Statistic Sign: -1 - Indica a direção da diferença.

            **Resumo**

            AUC: O valor extremamente alto de AUC sugere que o modelo tem uma capacidade quase perfeita de discriminação entre as classes.
            KS: O valor muito baixo da estatística KS e o p-value extremamente alto indicam que as distribuições das classes positivas e negativas são muito semelhantes, o que pode ser um sinal de que o modelo está superajustado (overfitting) ou que as classes são muito bem separadas.
            ''')

        col1, col2= st.columns(2)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem61.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem62.png')




        
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")

    with st.form("modelo_preditivo_form"):
        nome = st.text_input("Nome do Aluno")
        fase_2020 = st.number_input("Fase 2020", min_value=0, step=1)
        fase_2021 = st.number_input("Fase 2021", min_value=0, step=1)
        fase_2022 = st.number_input("Fase 2022", min_value=0, step=1)
        pedra_2020 = st.selectbox("Pedra 2020", ['Ametista', 'Quartzo', 'Ágata', 'Topázio'])
        pedra_2021 = st.selectbox("Pedra 2021", ['Ametista', 'Quartzo', 'Ágata', 'Topázio'])
        pedra_2022 = st.selectbox("Pedra 2022", ['Ametista', 'Quartzo', 'Ágata', 'Topázio'])
        ponto_virada_2020 = st.number_input("Ponto de Virada 2020", min_value=0, max_value=1, step=1)
        ponto_virada_2021 = st.number_input("Ponto de Virada 2021", min_value=0, max_value=1, step=1)
        ponto_virada_2022 = st.number_input("Ponto de Virada 2022", min_value=0, max_value=1, step=1)
        ano_ingresso = st.number_input("Ano de Ingresso", min_value=2000, step=1)
        dimensao_academica = st.selectbox("Dimensão Acadêmica", ['excelente', 'abaixo da media'])
        dimensao_psicossocial = st.selectbox("Dimensão Psicossocial", ['excelente', 'abaixo da media'])
        dimensao_psicopedagogica = st.selectbox("Dimensão Psicopedagógica", ['excelente', 'abaixo da media'])

        submitted = st.form_submit_button("Prever")
    
        if submitted:
        # Criei um DataFrame com os dados de entrada do usuário
            data = {
                'NOME' : [nome],
                'FASE_2020': [fase_2020],
                'FASE_2021': [fase_2021],
                'FASE_2022': [fase_2022],
                'PEDRA_2020': [pedra_2020],
                'PEDRA_2021': [pedra_2021],
                'PEDRA_2022': [pedra_2022],
                'PONTO_VIRADA_2020': [ponto_virada_2020],
                'PONTO_VIRADA_2021': [ponto_virada_2021],
                'PONTO_VIRADA_2022': [ponto_virada_2022],
                'ANO_INGRESSO': [ano_ingresso],
                'dimensao_academica': [dimensao_academica],
                'dimensao_psicossocial': [dimensao_psicossocial],
                'dimensao_psicopedagogica': [dimensao_psicopedagogica]
            }

            df_input = pd.DataFrame(data)

            df_prev = novo_pipeline(df_input)
            
            
            model_xgb = joblib.load(r'C:\Users\tamir\OneDrive\Área de Trabalho\DATATHON\datathon-\modelo\Model_XGB.joblib')

            predictions = model_xgb.predict(df_prev)


            st.write("Calculando...")
            animation_placeholder = st.empty()

            for _ in range(10):
                animation_placeholder.text("Carregando...")
                time.sleep(0.1)

            # Verificar o valor de predictions e exibir o texto correspondente
            if predictions[0] == 1:
                animation_placeholder.text("Probabilidade de NÃO desistencia: 90%")
            elif predictions[0] == 0:
                animation_placeholder.text("Probabilidade de desistência: 90%")
            else:
                animation_placeholder.text("Resultado indefinido")

=======
#Importação das bibliotecas
import streamlit as st 
import pandas as pd
import joblib
from joblib import load
from nbconvert import HTMLExporter
import nbformat
import seaborn as sns
import matplotlib.pyplot as plt
from utils import novo_pipeline
import time



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
st.sidebar.markdown(
    "<h3 style='font-size:22px;'>Selecione uma Página:</h3>", 
    unsafe_allow_html=True
)

selected_page = st.sidebar.radio("", list(pages.keys()))

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

    pbi_url = r'https://app.powerbi.com/view?r=eyJrIjoiZTNmNDg3OWMtYmEwNy00YWVjLWJkZDItYmZkYTZlNTY0ZWU1IiwidCI6ImRlOTgwY2Y4LWYwYzctNGFlZC1iNjc2LTJlOTlkNjg2YzAzMyJ9 '

    st.components.v1.html(f'<iframe width="100%" height="600" src="{pbi_url}" frameborder="0" allowFullScreen="true"></iframe>', height=600)
    
    st.markdown(
        '''
        **Apresentação do Dashboard Interativo**

        Foco em Gênero, Idade e Classificações por Pedras

        **Introdução**

        Nossa apresentação do Dashboard Interativo tem como objetivo principal fornecer uma análise detalhada dos dados relacionados a gênero, idade e classificações por pedras. Este dashboard foi desenvolvido para oferecer uma visualização clara e intuitiva, permitindo aos usuários interagir e explorar os dados de forma eficiente.

        **Análise por Gênero**

        O dashboard apresenta uma segmentação detalhada dos dados por gênero, permitindo a identificação de padrões e tendências específicas entre diferentes grupos. Com isso, podemos entender melhor as dinâmicas de gênero e como elas influenciam outros fatores no contexto analisado.

        **Análise por Idade**

        A análise por faixa etária é outro aspecto crucial do nosso dashboard. As visualizações são projetadas para destacar as diferenças e semelhanças entre diferentes grupos de idade, facilitando a identificação de tendências demográficas importantes que podem impactar as decisões estratégicas.

        **Análise por Classificações de Pedras**

        Por fim, o dashboard inclui uma seção dedicada às classificações por pedras. Esta análise permite uma compreensão aprofundada das preferências e classificações associadas a diferentes tipos de pedras, proporcionando insights valiosos para diversas aplicações, como marketing, vendas e atendimento ao cliente.

        **Conclusão**

        Em resumo, nosso Dashboard Interativo oferece uma ferramenta poderosa para a análise de dados, focando em gênero, idade e classificações por pedras. Esperamos que esta apresentação demonstre a eficácia do dashboard em fornecer insights acionáveis e apoiar tomadas de decisão informadas.
        '''
    )

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

    st.write("## Acesse o Notebook Completo:")
    notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Datathon-Passos_Magicos.ipynb"
    st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")
    
    st.markdown(
            '''
            **Introdução**

            Foram utilizados três datasets neste projeto: df_2020_clean.csv, df_2021_clean.csv e df_2022_clean.csv. 
            Identificamos que seria benéfico dividir os dados por ano, pois essa abordagem nos permitiria obter uma visualização mais clara e detalhada das informações. Além disso, essa divisão facilita uma análise mais precisa ao observar as variações e tendências ao longo de diferentes períodos. Para dividir os dataframes, realizar a limpeza dos dados, gerar o mapa de correlação e criar o gráfico de contagem, seguimos uma metodologia estruturada que garantiu a integridade e a clareza dos resultados obtidos.
            ''')
    
    with st.expander('Criando Funções'):
        st.markdown(
            '''
            A função filter_columns foi utilizada para filtrar colunas de um DataFrame com base em padrões específicos. Ela recebeu um DataFrame (df) e uma lista de padrões (filters). A função verifica se os nomes das colunas contêm algum dos padrões especificados na lista de filtros. Se uma coluna contiver um dos padrões, ela será excluída do DataFrame final. Essa função foi útil para remover colunas indesejadas de forma eficiente
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem01.png')

        st.markdown(
            '''
            A função cleaning_dataset foi utilizada para limpar o DataFrame removendo linhas com valores ausentes (NaN). Nela executamos duas operações principais:
            Removemos a linhas onde todas as colunas, exceto a coluna 'NOME', contêm valores NaN.
            Removemos linhas que contêm apenas valores NaN. Com isso, garantimos que o DataFrame resultante não tivesse linhas completamente vazias, melhorando a qualidade dos dados para análise.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem02.png')

    with st.expander('Limpeza dos dados 2020'):

        st.markdown(
            '''
            Neste trecho de código, realizamos a transformação dos dados de ingresso dos alunos para o ano de 2020. As etapas foram as seguintes:

            -   Mapeamento de Anos: Criamos um dicionário (ano_map_2020) para mapear os anos de ingresso dos alunos. Em seguida, criamos um dicionário reverso (reverse_ano_map_2020) para facilitar a substituição dos valores mapeados.
            -   Substituição de Valores: Utilizamos o dicionário reverso para substituir os valores na coluna ANOS_PM_2020 do DataFrame df_2020_clean.
            -	Renomeação de Coluna: Renomeamos a coluna ANOS_PM_2020 para ANO_INGRESSO_2020 para refletir a transformação realizada.
            - 	Conversão para Datetime: Convertimos a coluna ANO_INGRESSO_2020 para o formato datetime e extraímos apenas o ano.

            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem03.png')

        st.markdown(
            '''
            Neste trecho de código, realizamos a separação da parte numérica e alfabética da coluna FASE_TURMA_2020 do DataFrame df_2020_clean. As etapas foram as seguintes:

            - 	Captura dos Números: Utilizamos a função str.extract para capturar a parte numérica da coluna FASE_TURMA_2020 e armazená-la em uma nova coluna chamada FASE_2020.
            - 	Captura das Letras: Utilizamos a função str.extract para capturar a parte alfabética da coluna FASE_TURMA_2020 e armazená-la em uma nova coluna chamada TURMA_2020
        Convertemos a coluna PONTO_VIRADA_2020 em valores binários (0 e 1), onde 'Sim' é mapeado para 1 e qualquer outro valor é mapeado para 0.
        Convertemos a coluna INDE_2020 para valores numéricos, utilizando pd.to_numeric com a opção errors='coerce' para tratar valores inválidos.
        Convertemos a coluna PEDRA_2020 para uma categoria utilizando pd.Categorical.

        Verificamos os valores únicos na coluna INDE_CONCEITO_2020 para entender melhor os dados presentes nessa coluna.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem04.png')

        st.markdown(
            '''
        Aqui, verificamos se cada valor na coluna 'DESTAQUE_IPV_2020' é uma string e contém a frase 'Seu destaque em 2020:'. Se sim, marcamos com 1; se não, marcamos com 0. Basicamente, estamos identificando quem recebeu destaque em 2020.

        Convertemos as colunas IAA_2020, IEG_2020, IPS_2020, IDA_2020, IPP_2020, IPV_2020 e IAN_2020 para valores numéricos, utilizando a função pd.to_numeric e definindo errors='coerce' para tratar erros.

        Removemos as colunas TURMA_2020, FASE_TURMA_2020, INSTITUICAO_ENSINO_ALUNO_2020, IDADE_ALUNO_2020 e INDE_CONCEITO_2020 do DataFrame df_2020_clean.
        Aplicamos essa mesma transformação para os datasets de 2021 e 2022.
        '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem05.png')

    with st.expander('Limpeza dos dados 2021 e 2022'):

        st.markdown(
            '''
            Realizamos várias operações de limpeza e transformação no DataFrame df_2021_clean. Primeiro, verificamos a contagem de valores na coluna SINALIZADOR_INGRESSANTE_2021 e a quantidade de valores nulos. Em seguida, aplicamos uma função lambda para definir o valor como 2021 se a string contiver 'Ingressante', caso contrário, definimos como 'Veterano'.

            Depois, criamos um DataFrame df_ano_veterano com os alunos veteranos e o mesclamos com os dados de 2020 para obter o ano de ingresso. Atualizamos a coluna ANO_INGRESSO_2020 para os ingressantes de 2021 que não tinham essa informação. Removemos alunos específicos e colunas desnecessárias, renomeamos a coluna ANO_INGRESSO_2020 para ANO_INGRESSO_2021, e convertimos essa coluna para o formato de ano. Por fim, identificamos que há 12 alunos sem data de entrada.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem06.png')

        st.markdown(
            '''
            Nós realizamos várias transformações no DataFrame df_2021_clean. Primeiro, transformamos a coluna PONTO_VIRADA_2021 em valores binários (0 e 1), onde 'Sim' é convertido para 1 e qualquer outro valor para 0. Em seguida, convertimos a coluna INDE_2021 para valores numéricos, tratando erros com errors='coerce'. Também transformamos as colunas NIVEL_IDEAL_2021 e PEDRA_2021 em categorias.

            Para unificar as colunas de recomendações (REC_EQUIPE_1_2021, REC_EQUIPE_2_2021, REC_EQUIPE_3_2021, REC_EQUIPE_4_2021), criamos uma nova coluna REC_AVA_UNIFICADO, que contém a recomendação mais frequente de cada linha. Removemos as colunas originais de recomendações após a unificação.

            Corrigimos a sintaxe do dicionário fase_map_2021 e criamos um dicionário reverso para mapear os textos de NIVEL_IDEAL_2021 para números correspondentes. Finalmente, substituímos os textos em NIVEL_IDEAL_2021 pela numeração correspondente.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem07.png')

        st.markdown('OBS: Fizemos o mesmo tratamento para a base de 2022.')

    with st.expander('Unindo os DataFrames'):

        st.markdown(
            '''
            Realizamos a fusão dos DataFrames df_2020_clean, df_2021_clean e df_2022_clean utilizando a coluna NOME como chave, com a opção how='outer' para incluir todos os registros de cada DataFrame. Em seguida, selecionamos as colunas de interesse para o DataFrame final df_clean, que inclui informações sobre fases, pedras, pontos de virada, anos de ingresso e várias outras métricas para os anos de 2020, 2021 e 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem08.png')

    with st.expander('Tratando Dados Nulos'):

        st.markdown(
            '''
            A coluna NOME tem 1348 entradas não nulas e é do tipo object (string).
            A coluna FASE_2020 tem 727 entradas não nulas e é do tipo object.
            A coluna PEDRA_2020 tem 727 entradas não nulas e é do tipo category.
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem09.png')

        
        st.markdown(
            '''
            Nós verificamos se há valores duplicados na coluna NOME do DataFrame df_clean e confirmamos que não há duplicatas (np.int64(0)). Em seguida, contamos o número de valores nulos em cada coluna do DataFrame. A observação final sugere que os valores nulos podem indicar alunos que desistiram de participar do projeto.
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem10.png')

    with st.expander('Explorando os Dados'):
        st.markdown(
            '''
            Definimos uma lista de colunas qualitativas qualitative_columns_total e um dicionário categories que agrupa essas colunas em categorias (FASE, PEDRA, PONTO_VIRADA, STATUS_ALUNO). Em seguida, realizamos uma análise de frequência para cada categoria, calculando a distribuição de frequências normalizadas (em porcentagem) para cada coluna dentro das categorias. 
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem11.png')

        st.markdown(
            '''
            **Distribuição de Frequências para FASE**

            Aumento na fase inicial (0): A porcentagem de indivíduos na fase inicial cresceu de 11.28% em 2020 para 22.04% em 2022, indicando um influxo significativo de novos participantes nos últimos anos.

            Redistribuição em fases intermediárias: As fases intermediárias (1 a 5) mostram estabilidade relativa, com variações moderadas. No entanto, a fase 2 diminuiu de 23.68% em 2021 para 17.98% em 2022, sugerindo uma possível dificuldade em avançar a partir dessa etapa.

            Redução em fases avançadas (6 e superiores): Observa-se uma tendência decrescente nas fases finais. A fase 8 praticamente desaparece em 2021 e 2022, o que pode indicar que estes alunos ingressaram nos cursos superiores.

            A alta concentração inicial em 2022 e a redução nas fases avançadas apontam para uma necessidade de estratégias para aumentar a progressão e retenção em níveis mais elevados.
            ''')
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem12.png')
        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem13.png')

        st.markdown(
            '''
            **Distribuição de Frequências para PONTO_VIRADA**

            Predominância do valor 0 (não atingiram o ponto de virada): A maior parte dos indivíduos não conseguiu avançar para os próximos passos, com a porcentagem de participantes que não atingiram o ponto de virada variando de 87.07% em 2020 para 86.89% em 2022.
            Leve aumento do valor 1 (atingiram o ponto de virada) em 2021: A porcentagem de indivíduos que conseguiram avançar para os próximos passos aumentou ligeiramente em 2021, alcançando 15.79%. Esse aumento pode ser reflexo de mudanças no ambiente ou na dinâmica dos participantes, como impactos externos, incluindo a pandemia de COVID-19.
            Embora a maioria dos indivíduos não tenha avançado para os próximos passos, o aumento observado em 2021 sugere que é importante monitorar fatores externos e suas influências no progresso dos alunos.
            ''')
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem14.png')
        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem15.png')

        st.markdown(
            '''
            **Distribuição de Frequências para STATUS_ALUNO**

            Alta taxa de desistência: Quase metade dos alunos (46.07%) desiste do programa, sendo um indicador crítico para avaliação. Entre os que desistem, 19.21% o fazem em 2021 e 10.46% em 2022.
            Baixa taxa de retorno: Apenas 0.96% dos alunos retornam ao programa em 2022, indicando dificuldades de reintegração.
            Proporção de ativos: Apenas 23.29% permanecem ativos, reforçando a necessidade de intervenções para melhorar a retenção.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem16.png ')

    with st.expander('Alunos Que Desistiram'):

        st.markdown(
            '''
            Criamos um gráfico de barras para visualizar a distribuição de desistências por fase e ano
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem17.png')

        st.markdown(
            '''
            A alta taxa de desistência e o baixo retorno ao programa são sinais de alerta, sugerindo a necessidade de estratégias para engajamento, suporte e acompanhamento dos alunos.

            Aumento progressivo das desistências ao longo dos anos: Há uma tendência clara de aumento nas desistências conforme o tempo passa, com picos significativos em 2022. Isso sugere que fatores externos, como a pandemia de COVID-19 ou outras mudanças no contexto educacional, podem ter influenciado negativamente o progresso dos alunos.

            Fases mais críticas: As fases iniciais e intermediárias (Fase 0 a Fase 3) parecem ser os pontos de maior risco para desistência, com aumento considerável ao longo dos anos. Isso pode indicar a necessidade de intervenções mais eficazes nessas fases, oferecendo apoio extra aos alunos para que não desistam antes de avançarem.

            Alunos mais avançados (Fase 4 a Fase 7): Apesar de uma quantidade menor de desistências nessas fases, ainda há uma preocupação, já que o aumento nas desistências de 2021 para 2022 pode ser reflexo de desafios acumulados ao longo do percurso acadêmico.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem18.png')

    with st.expander('Ano de Ingresso dos Alunos'):

        st.markdown(
            '''
            Nós definimos uma lista de colunas quantitativas quantitative_columns_total, que inclui várias métricas para os anos de 2020, 2021 e 2022, além da coluna ANO_INGRESSO. Essas colunas contêm dados numéricos que podem ser analisados estatisticamente.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem19.png')

        st.markdown(
            '''
            O ano médio de ingresso é 2019, o que é esperado, considerando que os dados são relativos a três anos consecutivos. O desvio padrão (1.78) indica que a variação dos anos de ingresso não é muito grande, a maioria dos alunos ingressou em 2019, com poucos ingressando em 2016 e 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem20.png')

    with st.expander('Correlação entre Variáveis'):

        st.markdown(
            '''
            Valores próximos de 1 indicam uma forte correlação positiva, enquanto valores próximos de -1 indicam uma forte correlação negativa.
            Valores próximos de 0 indicam pouca ou nenhuma correlação linear.
            Esse gráfico ajuda a identificar quais variáveis têm relações fortes entre si, o que pode ser útil para análises estatísticas e modelagem preditiva.

            **Maiores correlações positivas:**

            -	IDA_2021 e IDA_2022: Correlação muito alta, acima de 0.85, sugerindo forte relação entre os anos consecutivos.
            -	INDE_2021 e INDE_2022: Correlação alta, acima de 0.86, indicando consistência ou padrão similar entre essas variáveis ao longo dos anos.
            -	IEG_2021 e IEG_2022: Correlação acima de 0.87, também indicando alta relação entre os anos consecutivos para essas variáveis.

            **Maiores correlações negativas:**
            -	ANO_INGRESSO e IPP_2022: Correlação negativa forte em torno de -0.35, sugerindo uma relação inversa entre o ano de ingresso e o desempenho ou métrica associada ao IPP em 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem21.png')

    with st.expander('INDE(Indice de Desenvolvimento)'):

        st.markdown(
            '''
            Criamos gráficos de barras para visualizar as estatísticas de INDE (Índice de Desenvolvimento) para os anos de 2020, 2021 e 2022.          
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem22.png')

        st.markdown(
            '''
            O INDE_2020 apresenta a maior média (7.30), seguida de uma leve diminuição para 6.89 em 2021 e 7.03 em 2022.

            O desvio padrão menor ao longo dos anos sugere uma redução na variabilidade entre os alunos em relação à necessidade de desenvolvimento educacional, indicando que o apoio oferecido foi mais homogêneo ao longo do tempo.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem23.png')

    with st.expander('Análise Temporal '):

        st.markdown(
            '''
            Fizemos uma visualização da tendência anual das médias de várias métricas ao longo dos anos 2020, 2021 e 2022, para ajudar a identificar como essas métricas evoluíram ao longo do tempo, fornecendo insights sobre possíveis padrões ou mudanças. 

            Análise de Tendências: O código calcula as médias anuais para cada métrica (IAN, IDA, IEG, IAA, IPS, IPP, IPV, INDE).

            Identificação de Padrões: Ao visualizar as médias anuais, é possível identificar padrões, como aumentos ou diminuições consistentes em determinadas métricas. Isso pode ajudar a entender o comportamento dos dados e a tomar decisões informadas com base nas tendências observadas.

            Comparação entre Anos: Permite comparar as médias de cada métrica entre os anos 2020, 2021 e 2022. Isso é útil para avaliar o impacto de diferentes fatores ao longo do tempo e para identificar anos específicos em que ocorreram mudanças significativas.

            Visualização Intuitiva: A utilização de gráficos de linha com pontos e anotações torna a visualização das tendências mais intuitiva e fácil de interpretar.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem24.png')

        st.markdown(
            '''
            IAN (Índice de Avaliação de Necessidades): O índice IAN mostra uma tendência de queda ao longo dos três anos analisados, com uma redução de 7,43 em 2020 para 6,42 em 2022. Isso sugere uma diminuição nas necessidades dos alunos ao longo do tempo, o que pode indicar uma melhoria nas condições ou nos apoios oferecidos, resultando em menos necessidades de intervenção.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem25.png')

        st.markdown(
            '''
            IDA (Índice de Desempenho Acadêmico): O desempenho acadêmico diminui de 2020 (6,32) para 2021 (5,43), o que pode ser um reflexo de desafios enfrentados pelos alunos, como a pandemia de COVID-19. Em 2022, há uma leve recuperação para 6,07, o que pode indicar um processo de adaptação, onde os alunos começam a se recuperar do impacto das circunstâncias anteriores.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem26.png')

        st.markdown(
            '''
            IEG (Índice de Engajamento Geral): O engajamento segue uma tendência interessante: cai de 7,80 em 2020 para 6,84 em 2021, possivelmente devido ao impacto da pandemia e mudanças no formato de ensino. No entanto, há uma recuperação em 2022 para 7,88, sugerindo que os alunos estão voltando a se engajar mais, possivelmente com a retomada das atividades presenciais ou com melhorias nos métodos de ensino.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem27.png')

        st.markdown(
            '''
            IAA (Índice de Apoio Acadêmico): O apoio acadêmico se manteve bastante estável ao longo dos três anos, com pequenas variações entre 2020 (8,37), 2021 (8,16) e 2022 (8,26). Isso indica que o suporte oferecido aos alunos não foi drasticamente afetado pela pandemia e manteve-se eficaz ao longo do tempo, com uma leve queda apenas.            
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem28.png')

        st.markdown(
            '''
             IPS (Índice de Progresso Social): O progresso social apresentou uma leve melhoria ao longo dos três anos, com a média aumentando de 6,74 em 2020 para 6,90 em 2022. Isso pode refletir esforços para apoiar o desenvolvimento social dos alunos, possivelmente devido a iniciativas para lidar com os efeitos da pandemia e melhorar as condições sociais.           
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem29.png')

        st.markdown(
            '''
            IPP (Índice de Progresso Pessoal): O índice de progresso pessoal apresenta uma melhoria em 2021 (7,60), mas uma queda significativa em 2022 (6,30). Esse comportamento pode estar relacionado ao impacto prolongado da pandemia, que pode ter afetado o bem-estar emocional e pessoal dos alunos, resultando em dificuldades no desenvolvimento pessoal em 2022.            
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem30.png')

        st.markdown(
            '''
            IPV (Índice de Progresso Vital): O progresso vital mostra uma leve tendência de melhora em 2021 (7,43), mas com uma queda sutil em 2022 (7,25). Isso pode indicar que os alunos, apesar dos desafios, conseguiram manter uma boa trajetória em termos de seu progresso vital, embora com uma leve diminuição após o pico de 2021.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem31.png')

        st.markdown(
            '''
            INDE (Índice de Necessidade de Desenvolvimento Educacional): O índice INDE apresentou uma leve queda de 2020 para 2021, mas em 2022 houve uma leve recuperação para 7,03. Isso sugere que, apesar de uma ligeira diminuição na necessidade de desenvolvimento educacional em 2021, houve uma leve reversão dessa tendência em 2022, possivelmente devido a melhorias nas condições educacionais.            
            '''
        )

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem32.png')

    with st.expander('Visualização de Densidade'):

        st.markdown(
            '''
            Analisamos a distribuição de densidade das métricas IAN, IDA, IEG, IAA, IPS, IPP, IPV e INDE para os anos de 2020, 2021 e 2022.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem33.png')

        st.markdown(
            '''
            IAN (Índice de Aprovação de Notas): As curvas de densidade são simétricas nos três anos analisados. A maior densidade ocorre em 2022, enquanto a menor densidade é observada em 2020. Isso indica uma leve melhoria na distribuição dos índices de aprovação ao longo dos anos.

            IDA (Índice de Desempenho Acadêmico): As curvas apresentam uma assimetria, inclinadas para o lado, sugerindo a presença de outliers. A maior densidade ocorre nos anos de 2021 e 2022, com a maior concentração de dados, enquanto o ano de 2020 apresenta uma distribuição mais dispersa.

            IEG (Índice de Engajamento Geral): As curvas de densidade são simétricas nos anos de 2022 e 2020, enquanto em 2021, há uma assimetria inclinada para a esquerda. Os anos de 2022 e 2020 mostram uma maior concentração de dados próximos à média, enquanto 2021 apresenta uma dispersão maior, indicando variação no engajamento.

            IAA (Índice de Atividade Acadêmica): As curvas de densidade de 2020, 2021 e 2022 quase se sobrepõem. Isso sugere que os valores das variáveis em cada um desses anos são semelhantes, sem grandes variações entre eles.

            IPS (Índice de Participação Social): Para os valores abaixo da média combinada, as curvas são assimétricas, enquanto para os valores acima da média, as curvas se tornam simétricas. Essa diferença na distribuição pode indicar uma maior dispersão de dados em torno da média, mas uma tendência de normalidade para valores elevados.

            IPP (Índice de Participação em Projetos): Em 2022, a curva está abaixo da média combinada, enquanto em 2021 e 2020 as curvas são simétricas, com variação na densidade. A dispersão dos dados parece ser maior em 2022, com uma menor concentração de índices perto da média.

            IPV (Índice de Participação Voluntária): As curvas de densidade são simétricas nos anos de 2022 e 2020, com o pico na média combinada, enquanto em 2021, a curva é assimétrica, inclinada para o lado. O ano de 2021 apresenta uma maior dispersão, enquanto 2022 e 2020 têm maior concentração de dados próximos à média.

            INDE (Índice de Desenvolvimento Educacional): As curvas de densidade são ligeiramente simétricas, com o pico próximo à média combinada. Isso sugere que os dados estão relativamente equilibrados e próximos da média, sem grandes flutuações.
            ''')
        
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem34.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem35.png')

        with col3:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem36.png')

        with col4:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem37.png')

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem38.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem39.png')

        with col3:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem40.png')

        with col4:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem41.png')

    with st.expander('Analise de Desistências'):

        st.markdown(
            '''
            Em que fase: A análise dos dados indica que as desistências são mais comuns nas fases iniciais do curso, especialmente nas fases 0 e 1, onde a adaptação e o comprometimento podem ser maiores desafios para os alunos. À medida que os alunos progridem para as fases mais avançadas, a quantidade de desistências diminui, sugerindo que aqueles que alcançam essas fases tendem a ser mais resilientes e comprometidos.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem42.png')

        st.markdown(
            '''
            Diante das notas gerais em qual classificação estão as desistências: A análise dos motivos de desistência revela que a dimensão acadêmica é o principal fator relacionado às desistências, com uma quantidade considerável de alunos indicando dificuldades nesse aspecto. A dimensão psicossocial, embora ainda relevante, apresenta um impacto um pouco menor. Por fim, a dimensão psicopedagógica também se destaca, mas em uma proporção semelhante à acadêmica, indicando que as questões relacionadas ao aprendizado e ao apoio pedagógico têm um papel importante nas desistências.

            Essa distribuição sugere que estratégias focadas no fortalecimento acadêmico e no suporte psicopedagógico poderiam ser eficazes para reduzir as desistências entre os alunos.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem43.png')

        st.markdown(
            '''
            Tempo de Permanência para alunos com "Possível desistência”: A análise da distribuição do tempo de permanência entre os alunos que desistiram revela que a grande maioria deixou o curso nas primeiras fases, com destaque para as fases 0 e 1, que acumulam o maior número de desistências. As fases 2, 3, 4 e 5 têm um número significativamente menor de desistências, indicando que as desistências diminuem conforme o aluno avança nas fases. As fases 6 e 7 não aparecem, o que pode sugerir que os alunos que chegam a essas fases são mais resilientes ou encontram mais apoio.

            Além disso, a média de tempo de permanência dos alunos que desistiram é de apenas 0.40 anos, o que reforça a ideia de que muitas desistências acontecem logo no início do curso, possivelmente devido a dificuldades acadêmicas, psicossociais ou psicopedagógicas. Isso indica a importância de um acompanhamento mais próximo nos primeiros anos, para identificar e mitigar os fatores que levam à desistência.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem44.png')

        st.markdown(
            '''
            Tempo de permanência dos alunos na fase 7: A análise da distribuição revela que a maioria dos alunos que chegaram a essa fase permaneceu por um período curto de tempo, com muitos ficando menos de 2 anos no curso. Alguns poucos estudantes ficaram por um período de 6 anos, indicando que, embora a fase 7 represente uma fase final, nem todos os alunos têm uma trajetória longa. Além disso, há um número considerável de alunos que desistiram logo após ingressar, com períodos de permanência muito curtos, como 0 anos, o que sugere que a desistência pode ocorrer logo após a chegada à fase 7.

            O gráfico de distribuição, juntamente com os dados, sugere que a fase 7 pode ter um padrão misto: há alunos que permanecem por um tempo significativo, enquanto outros desistem rapidamente, o que pode indicar questões específicas de motivação, dificuldades acadêmicas ou outras razões externas que influenciam essa fase.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem45.png')

        st.markdown(
            '''
            Média global dos Índices: A análise desses gráficos revela que os alunos classificados como "Indo Bem" apresentam um desempenho consistentemente superior em várias dimensões, enquanto os alunos "Não Indo Bem" apresentam um desempenho mais variado e, em muitos casos, inferior à média global. Além disso, pode-se inferir que fatores acadêmicos, psicossociais e psicopedagógicos estão fortemente correlacionados ao desempenho geral dos alunos, com aqueles indo bem em uma área tendendo a ir bem nas outras também.

            Intervenções focadas nos alunos "Não Indo Bem" podem se beneficiar de uma abordagem mais personalizada, considerando suas dificuldades específicas, seja no campo acadêmico ou psicossocial.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem46.png')

    with st.expander('Criando Modelos Treino e Teste'):

        st.markdown(
            '''
            Estamos selecionando um subconjunto específico de colunas do DataFrame df_tratamento. Essas colunas foram selecionadas para focar em informações relevantes para a análise e tratamento dos dados
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem47.png')

        st.markdown(
            '''
            Categorização do Status: Criamos uma nova coluna ATIVO para indicar se o aluno está ativo ou não, e removemos a coluna original STATUS_ALUNO.

            Classificação das Dimensões: Classificamos as dimensões acadêmica, psicossocial e psicopedagógica como 'abaixo da media' ou 'excelente' com base nos valores.

            Realizamos a limpeza do DataFrame, para preparar os dados para exportação (se necessário) e analisar a distribuição dos alunos ativos e não ativos

            Essas operações ajudam a preparar os dados para análises posteriores, facilitando a interpretação e a visualização das informações.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem48.png')

        st.markdown('Separação de base treino e teste')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem49.png')

        st.markdown(
            '''
            Definimos uma classe chamada DropFeatures que herda de BaseEstimator e TransformerMixin do scikit-learn. Esta classe é um transformador personalizado que remove colunas específicas de um DataFrame.

            Essa classe pode ser útil em pipelines de pré-processamento de dados, onde a remoção de colunas específicas é necessária antes de aplicar outras transformações ou modelos.
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem50.png')
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem51.png')

        st.markdown(
            '''
            Objetivo da Classe: Aplicar one-hot encoding a colunas específicas de um DataFrame. 

            Inicialização: A lista de colunas a serem transformadas é passada como argumento ao instanciar a classe.
            Ajuste (fit) e Transformação (transform): O método fit não faz nada além de retornar self, enquanto o método transform aplica one-hot encoding às colunas especificadas e concatena o resultado com o restante das colunas.

            Essa classe é útil para preparar dados categóricos para modelos de machine learning, transformando categorias em um formato numérico que pode ser utilizado pelos algoritmos
            ''')
        
        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem52.png')

        st.markdown('Utilizamos a OrdinalFeature para transformar colunas do DataFrame que contêm dados ordinais (dados que têm uma ordem natural) em valores numéricos, utilizando a codificação ordinal.')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem53.png')

        st.markdown('A Oversample foi usada para aplicar a técnica de sobremostragem (oversampling) em um DataFrame, especificamente utilizando o método SMOTE (Synthetic Minority Over-sampling Technique) para balancear a classe minoritária na coluna ATIVO.')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem54.png')

        st.markdown('Aplicamos a Pipeline nos dados:')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem55.png')

        st.markdown(
            '''
            Execução do modelo

            Treinamos o modelo de machine learning com dados de treino, avaliando seu desempenho em dados de teste para gerar várias métricas e visualizações para análise.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem56.png')

        st.markdown(
            '''
             Importamos a classe LogisticRegression, que criou uma instância do modelo de regressão logística com um estado aleatório fixo, e passou esse modelo para a função roda_modelo para treinar e avaliar o modelo com os dados de treino e teste.
            ''')

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem57.png')

        st.markdown(
            '''
            **Classification Report**

            **Classe 0:**
            -	Precision (Precisão): 0.98 - Aqui, 98% das previsões de classe 0 estão corretas.
            -	Recall (Revocação): 1.00 - Aqui, o modelo identificou corretamente todos os exemplos da classe 0.
            -	F1-Score: 0.99 - A média harmônica da precisão e da revocação. Um valor alto indica um bom equilíbrio entre precisão e revocação.
            -	Support: 824 - O número de ocorrências reais da classe 0 no conjunto de dados.

            **Classe 1:**
            -	Precision (Precisão): 1.00 - A precisão é perfeita, indicando que todas as previsões de classe 1 estão corretas.
            -	Recall (Revocação): 0.98 - O modelo identificou corretamente 98% dos exemplos da classe 1.
            -	F1-Score: 0.99 - A média harmônica da precisão e da revocação.
            -	Support: 824 - O número de ocorrências reais da classe 1 no conjunto de dados.

            **Métricas Globais**
            -	Accuracy (Acurácia): 0.99 - A proporção de todas as previsões corretas. Aqui, 99% das previsões do modelo estão corretas.
            -	Macro Avg (Média Macro):
            -	Precision: 0.99
            -	Recall: 0.99
            -	F1-Score: 0.99

            A média macro calcula a média das métricas para cada classe, tratando todas as classes igualmente.
            
            A média ponderada leva em conta o suporte (número de ocorrências) de cada classe, dando mais peso às classes com mais exemplos.
            -	Weighted Avg (Média Ponderada):
            -	Precision: 0.99
            -	Recall: 0.99
            -	F1-Score: 0.99

            **Resumo**

            Precisão e Revocação: O modelo tem uma precisão e revocação muito altas para ambas as classes, indicando que ele é muito eficaz em identificar corretamente ambas as classes.

            F1-Score: Alto para ambas as classes, mostrando um bom equilíbrio entre precisão e revocação.

            Acurácia: Muito alta, com 99% de todas as previsões corretas.

            Médias Macro e Ponderada: Ambas são altas, indicando que o modelo é consistente em seu desempenho em todas as classes.

            Em resumo, o modelo de regressão logística está performando excepcionalmente bem, com alta precisão, revocação e F1-score, além de uma acurácia geral de 99%.
            ''')

        col1, col2 = st.columns(2)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem58.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem59.png')

    with st.expander('DecisionTreeClassifier'):

        st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem60.png')

        st.markdown(
            '''
            **AUC (Área Sob a Curva)**

            Valor: 0.9997128028089357
            Interpretação: Um valor de AUC muito próximo de 1 indica que o modelo tem uma capacidade quase perfeita de distinguir entre as classes positivas e negativas. Isso sugere que o modelo está performando excepcionalmente bem.

            Métrica KS (Kolmogorov-Smirnov)
            Resultado: KstestResult(statistic=np.float64(0.007281553398058253), pvalue=np.float64(0.9999999999939724), statistic_location=np.float64(0.5), statistic_sign=np.int8(-1))

            **Interpretação:**

            Statistic: 0.007281553398058253 - Este valor representa a maior diferença entre as distribuições cumulativas das classes positivas e negativas. Um valor tão baixo indica que as distribuições das classes são muito semelhantes.
            P-value: 0.9999999999939724 - Um valor extremamente alto, indicando que a diferença entre as distribuições não é estatisticamente significativa. Em outras palavras, não há evidência de que as distribuições das classes sejam diferentes.
            Statistic Location: 0.5 - O ponto onde a maior diferença ocorre.
            Statistic Sign: -1 - Indica a direção da diferença.

            **Resumo**

            AUC: O valor extremamente alto de AUC sugere que o modelo tem uma capacidade quase perfeita de discriminação entre as classes.
            KS: O valor muito baixo da estatística KS e o p-value extremamente alto indicam que as distribuições das classes positivas e negativas são muito semelhantes, o que pode ser um sinal de que o modelo está superajustado (overfitting) ou que as classes são muito bem separadas.
            ''')

        col1, col2= st.columns(2)

        with col1:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem61.png')

        with col2:
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem62.png')




        
    
if selected_page == "Formulário: Modelo Preditivo":
    
    st.title("Formulário: Modelo Preditivo")

    st.markdown("""
    ##### Objetivo do Formulário: Modelo Preditivo para coleta de informações do Aluno
    Este formulário tem como objetivo coletar dados relevantes sobre um aluno para **acionar um modelo preditivo de *machine learning***. O modelo foi treinado para **analisar os dados fornecidos** e **gerar uma previsão** sobre o potencial do aluno em **concluir o curso com sucesso**.
    ###### Como usar o formulário

    1. **Preencha todos os campos:** Certifique-se de fornecer informações precisas e completas em todos os campos do formulário.Dúvidas consulte o ícone "?".
    2. **Clique em "Prever":** Após preencher todos os campos, clique no botão "Prever" para enviar os dados para o modelo.
    3. **Visualize o resultado:** O resultado da previsão será exibido logo abaixo do formulário.

    ##### Informações importantes

    * Os dados fornecidos serão utilizados exclusivamente para gerar a previsão sobre a conclusão do curso.
    * O modelo preditivo foi treinado com um conjunto de dados específico e pode não ser perfeito.
    * A previsão gerada é apenas uma estimativa e não deve ser considerada como uma decisão final.

    #####  Em caso de dúvidas

    Se você tiver alguma dúvida sobre o formulário ou o modelo preditivo, entre em contato com a equipe responsável.
    """)

    with st.form("modelo_preditivo_form"):
        nome = st.text_input("Nome do Aluno", help="Digite o nome completo do aluno")
     
        fase_2020 = st.number_input("Fase 2020", min_value=0, step=1, help= "preencha com pontuação atiginda em 2020 caso não possuir dados preencher com 0")
        fase_2021 = st.number_input("Fase 2021", min_value=0, step=1 ,help= "preencha com pontuação atiginda em 2020 caso não possuir dados neste ano por favor preencha com 0")     
        fase_2022 = st.number_input("Fase 2022", min_value=0, step=1 ,help= "preencha com pontuação atiginda em 2020 caso não possuir dados neste ano por favor preencha com 0")
       
        pedra_2020 = st.selectbox("Pedra 2020", ['Ametista', 'Quartzo', 'Ágata', 'Topázio'],help= "Selecione a pedra preciosa conquistada no ano de 2020")  
        pedra_2021 = st.selectbox("Pedra 2021", ['Ametista', 'Quartzo', 'Ágata', 'Topázio'],help= "Selecione a pedra preciosa conquistada no ano de 2021")     
        pedra_2022 = st.selectbox("Pedra 2022", ['Ametista', 'Quartzo', 'Ágata', 'Topázio'],help= "Selecione a pedra preciosa conquistada no ano de 2022")
      
        ponto_virada_2020 = st.number_input("Ponto de Virada 2020", min_value=0, max_value=1, step=1,help= "preencha com 0 ou 1 ,sendo 1 antigiu o ponto de virada e 0 não atingiu ponto de virada")      
        ponto_virada_2021 = st.number_input("Ponto de Virada 2021", min_value=0, max_value=1, step=1,help= "preencha com 0 ou 1 ,sendo 1 antigiu o ponto de virada e 0 não atingiu ponto de virada")
        ponto_virada_2022 = st.number_input("Ponto de Virada 2022", min_value=0, max_value=1, step=1,help= "preencha com 0 ou 1 ,sendo 1 antigiu o ponto de virada e 0 não atingiu ponto de virada")
    
        ano_ingresso = st.number_input("Ano de Ingresso", min_value=2018, step=1,help= "insira a data de ingresso no curso")
   
        dimensao_academica = st.selectbox("Dimensão Acadêmica", ['excelente', 'abaixo da media'],help= "Selecione Dimensão Acadêmica conquistada")
        dimensao_psicossocial = st.selectbox("Dimensão Psicossocial", ['excelente', 'abaixo da media'],help= "Selecione Dimensão Psicossocial conquistada")
        dimensao_psicopedagogica = st.selectbox("Dimensão Psicopedagógica", ['excelente', 'abaixo da media'],help= "Selecione Dimensão Psicopedagógica conquistada")

        submitted = st.form_submit_button("Prever")
    
        if submitted:
        # Criei um DataFrame com os dados de entrada do usuário
            data = {
                'NOME' : [nome],
                'FASE_2020': [fase_2020],
                'FASE_2021': [fase_2021],
                'FASE_2022': [fase_2022],
                'PEDRA_2020': [pedra_2020],
                'PEDRA_2021': [pedra_2021],
                'PEDRA_2022': [pedra_2022],
                'PONTO_VIRADA_2020': [ponto_virada_2020],
                'PONTO_VIRADA_2021': [ponto_virada_2021],
                'PONTO_VIRADA_2022': [ponto_virada_2022],
                'ANO_INGRESSO': [ano_ingresso],
                'dimensao_academica': [dimensao_academica],
                'dimensao_psicossocial': [dimensao_psicossocial],
                'dimensao_psicopedagogica': [dimensao_psicopedagogica]
            }

            df_input = pd.DataFrame(data)

            df_prev = novo_pipeline(df_input)
            model_xgb = joblib.load('notebook/Model_XGB.joblib')
            predictions = model_xgb.predict(df_prev)


            st.write("Calculando...")
            animation_placeholder = st.empty()

            for _ in range(10):
                animation_placeholder.text("Carregando...")
                time.sleep(0.1)

            # Verificar o valor de predictions e exibir o texto correspondente
            if predictions[0] == 1:
                animation_placeholder.text("Probabilidade de NÃO desistencia: 90%")
            elif predictions[0] == 0:
                animation_placeholder.text("Probabilidade de desistência: 90%")
            else:
                animation_placeholder.text("Resultado indefinido")

>>>>>>> f33ec56464708057d7954cf7393b5f2dd1ebff69
        