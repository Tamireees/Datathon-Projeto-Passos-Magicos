     
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

language = st.sidebar.selectbox("Choose Language / Escolha o Idioma", ["Português", "English"])

content = {
    "Português": {
        "intro_title": "Datathon: Introdução da Atividade",
        "dashboard_title": "Dashboard Interativo",
        "analysis_title": "Etapas do Desenvolvimento: Análise de Dados",
        "model_title": "Etapas do Desenvolvimento: Modelo Preditivo",
        "form_title": "Formulário de Previsão",
        # demais textos
    },
    "English": {
        "intro_title": "Datathon: Introduction to the Activity",
        "dashboard_title": "Interactive Dashboard",
        "analysis_title": "Development Steps: Data Analysis",
        "model_title": "Development Steps: Predictive Model",
        "form_title": "Prediction Form",
        # demais textos
    }
}

pages = {
    content[language]["intro_title"]: "main",
    content[language]["dashboard_title"]: "dashboard",
    content[language]["analysis_title"]: "analysis",
    content[language]["model_title"]: "model",
    content[language]["form_title"]: "form"
}

selected_page = st.sidebar.radio("Navigation", list(pages.keys()))



if selected_page == content[language]["intro_title"]:
    if language == "Português":
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

### **2023**
**Expansão Estrutural:**
* Inauguração de uma nova unidade no Centro de Embu-Guaçu, com seis salas de aula, biblioteca e áreas específicas para psicologia e psicopedagogia.
* Atendeu 1100 alunos com mais de 11.500 horas de aula no PAC.
  
**Resultados Educacionais:**
* Acompanhou a evolução de desempenho dos alunos, com uma média de 77% de melhoria nas notas ao longo do ano.
* Empresas Parceiras: Parcerias com Omie, Itaú, e a comunidade local viabilizaram os novos espaços e expansão do impacto​.
        ''')

    elif language == "English":
        st.title("Datathon: Activity Introduction")
         
        st.markdown('''
The Datathon aims to create data-driven proposals to highlight the impact of the NGO Passos Mágicos on the social transformation of vulnerable children and youth.

The NGO promotes education as a tool for change, serving students in the municipality of Embu-Guaçu. The competition offers two delivery options:

### Analytical Proposal:

Create an interactive dashboard and storytelling to demonstrate the NGO's impacts.
Analyze student performance and create useful indicators for decision making.
Deliver insights on the students' socioeconomic and educational profiles.

### Predictive Proposal:

Develop a predictive model to analyze student behavior.
Use techniques like machine learning or deep learning to propose innovative solutions.
Deploy the predictive model on a platform such as Streamlit.
Participants can choose to submit only one proposal or both. The delivery should include the report and/or implemented predictive model with GitHub links.
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
            st.title("Getting to Know the Passos Mágicos Project") 
         
        st.markdown('''
## Based on Common Objectives and Principles

The Passos Mágicos Association is a non-profit organization operating since 1992 with the goal of transforming the lives of vulnerable children and youth in the municipality of Embu-Guaçu. Founded by Michelle Flues Ivanoff, Dimitri Ivanoff, and collaborators, the NGO arose from the desire to offer educational and cultural opportunities that promote autonomy and positive community impact. The project grew from volunteer actions in orphanages to a formal association in 2016, allowing the expansion of its activities.

### **Mission, Vision, and Principles**

* Mission: Transform lives through education, offering tools to create opportunities for a dignified future.
* Vision: Build a Brazil where all children and youth have the same conditions to realize their dreams and become transformative agents.
* Principles: Love for others, empathy, gratitude, belonging, pursuit of knowledge, and education that transforms.

### **Methodology and Steps**

The Passos Mágicos methodology is based on four main pillars:

1. Quality Education: Classes in Portuguese, mathematics, English, and literacy, with groups organized by knowledge level rather than age. This is complemented by interactive and dynamic classes that encourage learning and curiosity.
2. Psychological Assistance: Provides emotional support for students and families, with individual and group monitoring, as well as workshops to improve interpersonal relationships.
3. Broadening Worldview: Conducts extracurricular activities such as visits to museums, parks, and cultural events, which expand children's horizons.
4. Protagonism: Students are encouraged to develop autonomy and lead initiatives within the NGO, including the possibility of scholarships in private schools and universities for those with good performance.

### **The NGO Implements Innovative Programs Such As:**

* Knowledge Acceleration Program (PAC): An educational journey with 7 phases focused on integral development, offering complementary classes, psychological support, and scholarships.
* Strategic Partnerships: Collaborations with institutions like USP (Paidéia Program), SENAI, FIAP, and private companies such as Itaú, Santander, and Estácio de Sá. These partnerships provide scholarships, training, and access to technologies to enhance educational impact.

## Data by Report

### **2018:**
* Social Impact: Directly served 355 students and benefited 1420 people.
* Initial Programs: Developed literacy classes, Elementary School I and II, and youth protagonism projects for advanced students.
* Cultural Activities: Organized trips to museums and other cultural spaces, promoting learning beyond the classroom.
* Institutional Collaboration: Received support from companies like Microsoft (software donations) and CIESP, which awarded Michelle Ivanoff with the Women's Excellence Award​.

### **2019**
* Increased Impact: Expanded to 812 directly served students and benefited 3248 people.
  
**New Initiatives:**
* Partnership with the Paidéia Program (USP), offering courses such as Sustainability and Programming, directly impacting 40 teenagers.
* Introduction of High School classes and focus on university entrance exam preparation.
* Expanded Support: Implemented three levels of psychological monitoring (individual, group, and workshops) for students and families​.
* Companies and Collaborations: Formed partnerships with Itaú Social and other institutions to finance projects and structure educational activities.

### **2020**
**Resilience During the Pandemic:**
* Full adaptation to online teaching, providing equipment and internet plans for families in vulnerable situations.
* Served 841 students and expanded support to about 654 households with a detailed socioeconomic survey.
* Emergency Initiatives: Distributed more than 2000 basic food baskets and created public health campaigns to prevent COVID-19.
* Collaborations and Support: Partnerships with Google for Education and Santander Universities enabled technological resources for remote teaching​.

### **2021**
**Management and Transparency:**
* Received important certifications such as the Doar Seal and the VOA Management and Trust Seal.
* Maintained online activities with 763 students served and expanded teacher training in remote teaching.
  
**New Projects:**
* Technical courses in partnership with SENAI, covering areas such as technology and programming.
* Inclusion of 11 complementary programs, such as the Book Club, which benefited 241 students​.

### **2022**
**30th Anniversary Celebration:**
* Directly impacted more than 1000 students, with growth in the Knowledge Acceleration Program.
* Overcame learning loss caused by the pandemic, focusing on school recovery.

**Partnerships and Initiatives:**
* Scholarships for 71 university students, in collaboration with Estácio de Sá and FIAP.
* Expanded social assistance, emphasizing strengthening family ties​.

### **2023**
**Structural Expansion:**
* Inauguration of a new unit in downtown Embu-Guaçu, with six classrooms, library, and dedicated areas for psychology and psycho-pedagogy.
* Served 1100 students with over 11,500 hours of classes in PAC.
  
**Educational Results:**
* Monitored students' performance evolution, with an average 77% improvement in grades throughout the year.
* Partner Companies: Partnerships with Omie, Itaú, and the local community enabled new spaces and expansion of impact​.
        ''')




if selected_page == content[language]["dashboard_title"]:
    
    st.title(content[language]["dashboard_title"])

    pbi_url = r'https://app.powerbi.com/view?r=eyJrIjoiZTNmNDg3OWMtYmEwNy00YWVjLWJkZDItYmZkYTZlNTY0ZWU1IiwidCI6ImRlOTgwY2Y4LWYwYzctNGFlZC1iNjc2LTJlOTlkNjg2YzAzMyJ9 '

    st.components.v1.html(f'<iframe width="100%" height="600" src="{pbi_url}" frameborder="0" allowFullScreen="true"></iframe>', height=600)
    
    if language == "Português":
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

            Em resumo, nosso Dashboard Interativo oferece uma ferramenta poderosa para a análise de dados, focando em gênero, idade e classificações por pedras. Esperamos que esta apresentação demonstre a eficácia do dashboard em fornecer insights acionáveis e apoiar tomadas de decisão informadas.
            '''
        )
    else:
        st.markdown(
            '''
            **Interactive Dashboard Presentation**

            Focus on Gender, Age, and Stone Classifications

            **Introduction**

            Our Interactive Dashboard presentation aims to provide a detailed analysis of data related to gender, age, and stone classifications. This dashboard was developed to offer clear and intuitive visualization, allowing users to interact and explore data efficiently.

            **Gender Analysis**

            The dashboard presents detailed segmentation of data by gender, enabling the identification of specific patterns and trends among different groups. This helps to better understand gender dynamics and how they influence other factors in the analyzed context.

            **Age Analysis**

            Age range analysis is another crucial aspect of our dashboard. The visualizations are designed to highlight differences and similarities among different age groups, facilitating the identification of important demographic trends that may impact strategic decisions.

            **Stone Classifications Analysis**

            Finally, the dashboard includes a section dedicated to stone classifications. This analysis allows an in-depth understanding of preferences and classifications associated with different types of stones, providing valuable insights for various applications such as marketing, sales, and customer service.

            **Conclusion**

            In summary, our Interactive Dashboard offers a powerful tool for data analysis, focusing on gender, age, and stone classifications. We hope this presentation demonstrates the dashboard's effectiveness in providing actionable insights and supporting informed decision-making.
            '''
        )
 
        

if selected_page == content[language]["analysis_title"]:  

    if language == "Português":

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

    else:
               
        st.title("Development Stages:")

        st.write("## Access the Full Notebook:")
        notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Passos_Magicos_dataset.ipynb"
        st.markdown(f"[Click here to access the notebook]({notebook_url})")

        st.write("## Descriptive Data Analysis:")
    with st.expander("## Introduction"):
        st.markdown('''
        This document presents the analyses carried out on the educational performance of students from the NGO "Passos Mágicos" 
        during the years 2020, 2021, and 2022. The objective was to understand patterns of progress, dropouts, and factors influencing student learning. The data analyzed includes various indicators such as academic performance, engagement, level adequacy, and psychosocial aspects.''')

    with st.expander("## **Data Analysis**"):
        st.markdown('''
    *Data Treatment and Organization*
    The data was organized and analyzed through the following steps:
    * Temporal Segmentation: The dataset was divided by year to facilitate initial processing.
    * Standardization: Variables were unified and transformed into a single standardized dataframe.
    * New Metrics: Additional columns were created to identify dropouts and facilitate performance analysis.
    **Analyzed Variables**
    The study used the following main indicators:
    * Phase: Student learning level (0 to 8).
    * Stone: Student classification based on the Educational Development Index (INDE).
    * Turning Point: Indicates achievement of a significant educational milestone in the respective year.
    * IAN: Level Adequacy Indicator.
    * IDA: Learning Indicator.
    * IEG: Engagement Indicator.
    * IAA: Self-Assessment Indicator.
    * IPS: Psychosocial Indicator.
    * IPP: Psychopedagogical Indicator.
    * IPV: Turning Point Indicator.
    * INDE: Educational Development Index, a consolidated metric weighted by the other indicators.''')
    with st.expander("## **Analysis Results**"):
        st.markdown('''
    *Student Frequency by Phase*
    * 2020: Most students were concentrated in phases 1 to 3.
    * 2021 and 2022: Phases 0 to 3 showed balanced distributions, but there was a significant drop in the number of students from phase 4 onward. In all years, student numbers halved with each phase advancement.
    *Stone Distribution (INDE Classification)*
    Classifications are based on the following intervals:
    * Quartz: 2.405 to 5.506
    * Agate: 5.506 to 6.868
    * Amethyst: 6.868 to 8.230
    * Topaz: 8.230 to 9.294
    * 2020: A considerable number of students were classified as Quartz and Amethyst, indicating a good distribution across extremes.
    * 2021 and 2022: Most students were classified as Amethyst and Topaz, demonstrating overall high performance.
    *Turning Point Indicator*
    Although many students performed well in their respective phases, most did not reach the turning point in the three years analyzed.
    *Dropouts: Temporal Impact and Academic Profile*
    * Temporal Analysis:
        * 2021 had the highest dropout rate, a phenomenon largely associated with the impacts of the COVID-19 pandemic.
    * Dropout Profile:
        * Most dropouts occurred among students in the initial phases (phases 0 to 3), highlighting greater vulnerability at this academic stage. Conversely, dropout rates were significantly lower in the more advanced phases.
    * Student Classification:
        * Active (314): Students enrolled throughout the three analyzed years (2020, 2021, and 2022).
        * Returned in 2022 (13): Students who participated in 2020, were absent in 2021 (classified as missing), and returned in 2022.
    * Dropouts:
        * Dropouts in 2022: 141 dropout cases were recorded.
        * Previous Years: By 2021, a total of 880 dropouts had occurred, with 259 cases in 2021 alone.
    * Analysis Highlights:
        * The analysis highlights the temporal impact of dropouts, pointing to the early phases as the most critical in terms of academic attrition. It also reinforces the role of external events, such as the pandemic, on student behavior and engagement.
    *Overall Performance (INDE)*
    * The INDE analysis showed that most students performed above average in all years, with a gradual increase in high scores from 2020 to 2022.
    *Outliers in Indicators*
    * IEG (Engagement): Many students scored below average, indicating engagement challenges.
    * IAA (Self-Assessment): Few students rated themselves poorly, suggesting confidence in their progress.
    * IPS (Psychosocial): 2021 had the worst results, possibly due to difficulties imposed by the pandemic.
    * IPP (Psychopedagogical): Low scores predominated in 2020 and 2021, but significant improvement was seen in 2022.
    *Correlation Between Indicators*
    * The assessment indicators showed high correlation with INDE, reinforcing the importance of these factors for educational development.
    *Annual Trend*
    * 2020: Highest overall average score.
    * 2021: Lowest performance, reflecting pandemic difficulties.
    * 2022: Significant recovery, with an increase in new enrollments and overall performance improvement.
    ''')
    with st.expander("## **Conclusion**"):
        st.markdown('''
    The analyses revealed important patterns in the progress and challenges faced by students of the NGO Passos Mágicos:
    * Most students progress well over the years, but the early phases show higher dropout rates.
    * The pandemic negatively impacted engagement, psychosocial, and psychopedagogical performance in 2021.
    * Indicators such as IEG and INDE are crucial for monitoring academic development.
    ''')
    with st.expander("## **Improvement Suggestions for the NGO**"):
        st.markdown('''
    * Reducing Dropouts in Early Phases: Implement personalized incentive programs for students in phases 0 to 3, such as individualized mentoring, financial support, and family follow-up.
    * Academic Engagement: Develop interactive activities adapted to the students' reality to improve engagement, especially for those with low IEG scores.
    * Psychosocial Support: Increase psychological support to minimize the effects of external crises, such as the pandemic, by offering more frequent follow-up sessions.
    * Continuous Monitoring: Implement a monitoring system that regularly evaluates student progress and identifies dropout risks early.
    * Family Integration: Involve families in the educational process through workshops and meetings to raise awareness about the importance of academic continuity.
    With these strategies, the NGO Passos Mágicos is expected to increase student retention and create a greater educational and social impact for its beneficiaries.
    ''')
    # Load data from remote file
    url_dados = "https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/refs/heads/main/dados/df_clean.csv"
    df_clean = pd.read_csv(url_dados)
    st.header("Getting to Know the Data")    
    # Display code and results side by side
    with st.expander("Getting to Know the Data"):
        st.dataframe(df_clean.head(20))
        st.code(            """
    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 1348 entries, 0 to 1347
    Data columns (total 40 columns):
     #   Column                    Non-Null Count  Dtype   
    ---  ------                    --------------  -----   
     0   NAME                      1348 non-null   object  
     1   PHASE_2020                727 non-null    float64 
     2   PHASE_2021                684 non-null    float64 
     3   PHASE_2022                862 non-null    float64 
     4   STONE_2020                727 non-null    category
     5   STONE_2021                684 non-null    category
     6   STONE_2022                862 non-null    category
     7   TURNING_POINT_2020        727 non-null    float64 
     8   TURNING_POINT_2021        684 non-null    float64 
     9   TURNING_POINT_2022        862 non-null    float64 
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
     38  psychosocial_dimension     1348 non-null   float64 
     39  psychopedagogical_dimension 1348 non-null  float64 
    dtypes: category(3), float64(35), object(2)
    """, language="python")        
    
        st.subheader("Data Dimensions")
        st.write(f"Rows and Columns: {df_clean.shape}") 
        st.subheader("Duplicates in 'NONE'")
        st.write(f"Duplicates: {df_clean['NOME'].duplicated().sum()}")
        st.markdown("* ### Correlation Between Quantitative Variables")
        st.markdown("""Here we explore the correlation between numerical variables.""", unsafe_allow_html=True)
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
            fig.patch.set_alpha(0)
            st.pyplot(fig)
        def plot_histogram(data, title, xlabel, ylabel, figsize=(6, 3), bins=10):
            fig, ax = plt.subplots(figsize=figsize, facecolor='none')
            sns.histplot(data, kde=True, palette=custom_palette, bins=bins, ax=ax)
            plt.style.use('dark_background')
            ax.set_title(title, fontsize=12, color="white")
            ax.set_xlabel(xlabel, fontsize=10, color="white")
            ax.set_ylabel(ylabel, fontsize=10, color="white")
            ax.tick_params(axis='x', colors="white")
            ax.tick_params(axis='y', colors="white")
            sns.set_style("darkgrid", {"axes.facecolor": "none"})
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            fig.patch.set_alpha(0)
            st.pyplot(fig)
        custom_palette = ['#F79651', '#2A6DA6', '#A2CFE6']
        
    st.title("Student Performance Analysis")
    st.header("Distribution of Phases Where Students Stopped")
    df_clean['FASE_PARADA'] = df_clean[['FASE_2020', 'FASE_2021', 'FASE_2022']].bfill(axis=1).iloc[:, -1]
    fase_counts = df_clean['FASE_PARADA'].value_counts()
    plot_bar_chart(fase_counts, "Distribution of Phases Where Students Stopped", "Phase", "Number of Students")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    df_clean['academic_dimension'] = df_clean[[
        'IAN_2020', 'IDA_2020', 'IEG_2020',
        'IAN_2021', 'IDA_2021', 'IEG_2021',
        'IAN_2022', 'IDA_2022', 'IEG_2022']].mean(axis=1)
    df_clean['psychosocial_dimension'] = df_clean[[
        'IAA_2020', 'IPS_2020',
        'IAA_2021', 'IPS_2021',
        'IAA_2022', 'IPS_2022']].mean(axis=1)
    df_clean['psychopedagogical_dimension'] = df_clean[[
        'IPP_2020', 'IPV_2020',
        'IPP_2021', 'IPV_2021',
        'IPP_2022', 'IPV_2022']].mean(axis=1)
    df_dropout = df_clean[df_clean['STATUS_ALUNO'] == 'Desistencia']
    df_dropout['DROPOUT_REASON'] = df_dropout[[
        'academic_dimension', 'psychosocial_dimension', 'psychopedagogical_dimension']].idxmin(axis=1)
    reason_translation = {
        'academic_dimension': 'Academic Indicator',
        'psychosocial_dimension': 'Psychosocial Indicator',
        'psychopedagogical_dimension': 'Psychopedagogical Indicator'
    }
    df_dropout['DROPOUT_REASON'] = df_dropout['DROPOUT_REASON'].map(reason_translation)
    reason_counts = df_dropout['DROPOUT_REASON'].value_counts()
    st.header("Distribution of Dropout Reasons")
    plot_bar_chart(reason_counts, "Distribution of Dropout Reasons - Possible Dropouts", "Reasons", "Number of Students")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.header("Distribution of Dropout Reasons - Detailed Indicators")
    columns_used = [
        'IAN_2020', 'IAN_2021', 'IAN_2022', 'IDA_2020', 'IDA_2021', 'IDA_2022',
        'IEG_2020', 'IEG_2021', 'IEG_2022', 'IAA_2020', 'IAA_2021', 'IAA_2022',
        'IPS_2020', 'IPS_2021', 'IPS_2022', 'IPP_2020', 'IPP_2021', 'IPP_2022',
        'IPV_2020', 'IPV_2021', 'IPV_2022'
    ]
    df_dropout = df_clean[df_clean['STATUS_ALUNO'] == 'Desistencia'][columns_used]
    df_dropout['DROPOUT_REASON'] = df_dropout.idxmin(axis=1)
    reason_map = {
        'IAN': 'Academic Indicator',
        'IDA': 'Academic Performance Indicator',
        'IEG': 'Engagement Indicator',
        'IAA': 'Academic Evaluation Indicator',
        'IPS': 'Psychosocial Indicator',
        'IPP': 'Personal Planning Indicator',
        'IPV': 'Vision Indicator'
    }
    df_dropout['DROPOUT_REASON'] = df_dropout['DROPOUT_REASON'].str.extract(r'(\w+)_\d+')
    df_dropout['DROPOUT_REASON'] = df_dropout['DROPOUT_REASON'].map(reason_map)
    reason_counts = df_dropout['DROPOUT_REASON'].value_counts()
    plot_bar_chart(reason_counts, "Distribution of Dropout Reasons - Detailed Indicators", "Reasons", "Number of Students")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.header("Distribution of Indexes - Justification for Retention")
    df_retained = df_clean[df_clean['STATUS_ALUNO'] == 'Ativo'][columns_used]
    df_retained['RETENTION_REASON'] = df_retained.idxmin(axis=1).str.extract(r'(\w+)_\d+')
    df_retained['RETENTION_REASON'] = df_retained['RETENTION_REASON'].map(reason_map)
    reason_counts = df_retained['RETENTION_REASON'].value_counts()
    plot_bar_chart(reason_counts, "Distribution of Indexes - Justification for Retention", "Reasons", "Number of Students")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.header("Years of Retention Distribution for Students in Phase 7")
    df_phase7 = df_clean[df_clean['FASE_PARADA'] == 7]
    df_phase7['YEAR_RETENTION'] = df_phase7[['ANO_INGRESSO']].bfill(axis=1).iloc[:, -1]
    df_phase7['YEARS_IN_PROGRAM'] = 2022 - df_phase7['YEAR_RETENTION']
    plot_histogram(df_phase7['YEARS_IN_PROGRAM'], "Years of Retention Distribution for Students in Phase 7", "Years of Retention", "Number of Students")
    st.header("Performance Comparison: Performing vs Underperforming Students")
    df_active = df_clean[df_clean['STATUS_ALUNO'] == 'Ativo']
    df_active['AVG_INDICATORS'] = df_active[columns_used].mean(axis=1)
    global_avg = df_active[columns_used].stack().mean()
    df_active['PERFORMANCE_STATUS'] = ['Performing' if x > global_avg else 'Underperforming' for x in df_active['AVG_INDICATORS']]
    df_comparison = df_active.groupby('PERFORMANCE_STATUS')[columns_used].mean()
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
    sns.boxplot(data=df_active, x='PERFORMANCE_STATUS', y='AVG_INDICATORS', palette=['#A2CFE6', '#F79651'], ax=ax)
    plt.title('Performance Index Distribution: Performing vs Underperforming Students', fontsize=12, color="white")
    plt.xlabel('Performance Status', fontsize=10, color="white")
    plt.ylabel('Average Index Score', fontsize=10, color="white")
    plt.xticks(rotation=45, ha='right', color="white")
    plt.axhline(y=global_avg, color='red', linestyle='--', label=f'Global Average: {global_avg:.2f}')
    plt.legend(labelcolor="white") 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    fig.patch.set_alpha(0)
    sns.set_style("darkgrid", {"axes.facecolor": "none"}) 
    plt.gca().set_facecolor('none') 
    st.pyplot(fig, transparent=True)
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
    df_comparison.T.plot(kind='bar', color=['#A2CFE6', '#F79651'], ax=ax)
    plt.title('Average Indicators Comparison: Performing vs Underperforming Students', fontsize=12, color="white")
    plt.ylabel('Average Indicator Scores', fontsize=10, color="white")
    plt.xlabel('Indicators', fontsize=10, color="white")
    plt.xticks(rotation=45, ha='right', color="white")
    plt.axhline(y=global_avg, color='red', linestyle='--', label=f'Global Average: {global_avg:.2f}')
    plt.legend(labelcolor="white")  
    plt.tight_layout()
    sns.set_style("darkgrid", {"axes.facecolor": "none"})
    fig.patch.set_alpha(0) 
    st.pyplot(fig, transparent=True)
    st.write(f"Global average of indices: {global_avg:.2f}")





if selected_page == content[language]["model_title"]:  

    if language == "Português":
      
        st.title("Etapas do Desenvolvimento: Modelo Preditivo")

        st.write("## Acesse o Notebook Completo:")
        notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Datathon-Passos_Magicos.ipynb"
        st.markdown(f"[Clique aqui para acessar o notebook]({notebook_url})")


        st.markdown(
                ''' 
                ### **Introdução**
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

    else:
        st.title("Development Stages: Predictive Model")
        st.write("## Access the Full Notebook:")
        notebook_url = "https://github.com/Tamireees/Datathon-Projeto-Passos-Magicos/blob/main/notebook/Datathon-Passos_Magicos.ipynb"
        st.markdown(f"[Click here to access the notebook]({notebook_url})")
        
        st.markdown(
            '''
            ### **Introduction**
            
            Three datasets were used in this project: df_2020_clean.csv, df_2021_clean.csv, and df_2022_clean.csv. 
            We found it beneficial to split the data by year, as this approach allowed for a clearer and more detailed view of the information. 
            Additionally, this separation facilitated a more accurate analysis of variations and trends across different periods. 
            To split the dataframes, clean the data, generate the correlation map, and create the count plot, 
            we followed a structured methodology that ensured the integrity and clarity of the results obtained.
            ''')
        
        with st.expander('Creating Functions'):
            st.markdown(
                '''
                The `filter_columns` function was used to filter DataFrame columns based on specific patterns. 
                It takes a DataFrame (`df`) and a list of patterns (`filters`). 
                The function checks whether the column names contain any of the specified patterns. 
                If a column matches, it is excluded from the final DataFrame. 
                This function was useful for efficiently removing unwanted columns.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem01.png')
            st.markdown(
                '''
                The `cleaning_dataset` function was used to clean the DataFrame by removing rows with missing values (NaN). 
                It performed two main operations:
                - Removed rows where all columns except 'NOME' had NaN values.
                - Removed rows that contained only NaN values.
                This ensured that the resulting DataFrame had no fully empty rows, improving data quality for analysis.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem02.png')
        with st.expander('Data Cleaning 2020'):
        
            st.markdown(
                '''
                In this code snippet, we performed transformations on the 2020 student admission data. The steps included:
                - **Year Mapping**: We created a dictionary (`ano_map_2020`) to map students' admission years. Then, a reverse dictionary (`reverse_ano_map_2020`) was created for substitution.
                - **Value Replacement**: Used the reverse dictionary to replace values in the `ANOS_PM_2020` column in `df_2020_clean`.
                - **Column Renaming**: Renamed `ANOS_PM_2020` to `ANO_INGRESSO_2020` to reflect the transformation.
                - **Datetime Conversion**: Converted the `ANO_INGRESSO_2020` column to datetime and extracted only the year.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem03.png')
            st.markdown(
                '''
                In this code, we separated the numeric and alphabetic parts of the `FASE_TURMA_2020` column in `df_2020_clean`:
                - **Number Extraction**: Used `str.extract` to get the numeric part and saved it in `FASE_2020`.
                - **Letter Extraction**: Used `str.extract` to get the alphabetic part and saved it in `TURMA_2020`.
                Then:
                - Converted `PONTO_VIRADA_2020` to binary values (0 and 1), mapping 'Sim' to 1 and others to 0.
                - Converted `INDE_2020` to numeric using `pd.to_numeric`, with `errors='coerce'`.
                - Converted `PEDRA_2020` to a categorical type with `pd.Categorical`.
                Finally, we checked unique values in the `INDE_CONCEITO_2020` column to better understand the data.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem04.png')
            st.markdown(
                '''
                Here, we checked if each value in the `DESTAQUE_IPV_2020` column is a string containing the phrase 'Seu destaque em 2020:'. 
                If so, we marked it with 1; otherwise, with 0 — identifying who was highlighted in 2020.
                Then, we converted the following columns to numeric using `pd.to_numeric(errors='coerce')`: 
                `IAA_2020`, `IEG_2020`, `IPS_2020`, `IDA_2020`, `IPP_2020`, `IPV_2020`, and `IAN_2020`.
                We removed the following columns: `TURMA_2020`, `FASE_TURMA_2020`, `INSTITUICAO_ENSINO_ALUNO_2020`, 
                `IDADE_ALUNO_2020`, and `INDE_CONCEITO_2020`.
                The same transformations were applied to the 2021 and 2022 datasets.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem05.png')
        with st.expander('Data Cleaning 2021 and 2022'):
        
            st.markdown(
                '''
                We performed several cleaning and transformation steps on `df_2021_clean`. 
                First, we checked the value counts and null values in the `SINALIZADOR_INGRESSANTE_2021` column. 
                Then, we applied a lambda function to set the value to 2021 if it contains 'Ingressante', otherwise to 'Veterano'.
                Next, we created `df_ano_veterano` with veteran students and merged it with the 2020 data to retrieve the year of admission. 
                We updated the `ANO_INGRESSO_2020` column for 2021 entrants missing this info.
                We removed specific students and unnecessary columns, renamed `ANO_INGRESSO_2020` to `ANO_INGRESSO_2021`, 
                and converted it to a datetime year. Finally, we identified 12 students with no entry date.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem06.png')
            st.markdown(
                '''
                We performed several transformations on `df_2021_clean`:
                - Converted `PONTO_VIRADA_2021` to binary (0 and 1).
                - Converted `INDE_2021` to numeric with `errors='coerce'`.
                - Converted `NIVEL_IDEAL_2021` and `PEDRA_2021` to categorical.
                We unified recommendation columns (`REC_EQUIPE_1_2021`, ..., `REC_EQUIPE_4_2021`) into a new column `REC_AVA_UNIFICADO`, 
                which contains the most frequent recommendation per row. Then, we dropped the original recommendation columns.
                We fixed the `fase_map_2021` dictionary syntax and created a reverse mapping dictionary to map `NIVEL_IDEAL_2021` 
                text values to numbers, replacing the text values accordingly.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem07.png')
            st.markdown('NOTE: The same processing was applied to the 2022 dataset.')
        with st.expander('Merging DataFrames'):
        
            st.markdown(
                '''
                We merged `df_2020_clean`, `df_2021_clean`, and `df_2022_clean` using the `NOME` column as the key, 
                with `how='outer'` to include all records. Then, we selected the relevant columns for the final DataFrame `df_clean`, 
                including information about phases, milestones, turning points, entry years, and several metrics for 2020, 2021, and 2022.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem08.png')
        with st.expander('Handling Missing Data'):
        
            st.markdown(
                '''
                The `NOME` column has 1348 non-null entries and is of type object (string).
                The `FASE_2020` column has 727 non-null entries and is of type object.
                The `PEDRA_2020` column has 727 non-null entries and is of type category.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem09.png')
            st.markdown(
                '''
                We checked for duplicate values in the `NOME` column of `df_clean` and confirmed that there were no duplicates (`np.int64(0)`). 
                Then, we counted the number of missing values in each column. The final observation suggests that the null values 
                may indicate students who dropped out of the project.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem10.png')  
        with st.expander('Exploring the Data'):
            st.markdown(
                '''
                We defined a list of qualitative columns `qualitative_columns_total` and a dictionary `categories` that groups these columns into categories (PHASE, STONE, TURNING_POINT, STUDENT_STATUS). Then, we performed a frequency analysis for each category, calculating the normalized frequency distribution (in percentage) for each column within the categories.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem11.png')

            st.markdown(
                '''
                **Frequency Distribution for PHASE**

                Increase in the initial phase (0): The percentage of individuals in the initial phase grew from 11.28% in 2020 to 22.04% in 2022, indicating a significant influx of new participants in recent years.

                Redistribution in intermediate phases: Intermediate phases (1 to 5) show relative stability with moderate variations. However, phase 2 decreased from 23.68% in 2021 to 17.98% in 2022, suggesting a potential difficulty in progressing beyond this stage.

                Decrease in advanced phases (6 and above): There is a downward trend in the final phases. Phase 8 nearly disappears in 2021 and 2022, which may indicate that these students have enrolled in higher education.

                The high initial concentration in 2022 and the decrease in advanced phases point to a need for strategies to increase progression and retention at higher levels.
                ''')

            col1, col2, col3 = st.columns(3)
            with col1:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem12.png')
            with col2:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem13.png')
            st.markdown(
                '''
                **Frequency Distribution for TURNING_POINT**
                
                Predominance of value 0 (did not reach the turning point): Most individuals did not progress to the next steps, with the percentage of participants who did not reach the turning point ranging from 87.07% in 2020 to 86.89% in 2022.
                Slight increase of value 1 (reached the turning point) in 2021: The percentage of individuals who managed to progress to the next steps slightly increased in 2021, reaching 15.79%. This increase may reflect changes in the environment or participant dynamics, such as external impacts, including the COVID-19 pandemic.
                Although most individuals did not advance, the observed increase in 2021 suggests it is important to monitor external factors and their influence on student progress.
                ''')
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem14.png')
            with col2:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem15.png')
            st.markdown(
                '''
                **Frequency Distribution for STUDENT_STATUS**
                
                High dropout rate: Nearly half of the students (46.07%) drop out of the program, which is a critical indicator for evaluation. Among those who drop out, 19.21% did so in 2021 and 10.46% in 2022.
                Low return rate: Only 0.96% of students returned to the program in 2022, indicating reintegration difficulties.
                Active proportion: Only 23.29% remain active, reinforcing the need for interventions to improve retention.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem16.png')

        with st.expander('Students Who Dropped Out'):
        
            st.markdown(
                '''
                We created a bar chart to visualize the distribution of dropouts by phase and year.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem17.png')

            st.markdown(
                '''
                The high dropout rate and low return to the program are warning signs, suggesting the need for strategies for student engagement, support, and follow-up.

                Progressive increase in dropouts over the years: There is a clear trend of increasing dropouts over time, with significant peaks in 2022. This suggests that external factors such as the COVID-19 pandemic or other changes in the educational context may have negatively impacted student progress.

                Most critical phases: The initial and intermediate phases (Phase 0 to Phase 3) appear to be the highest risk points for dropout, with a considerable increase over the years. This may indicate the need for more effective interventions in these phases, offering additional support to prevent early dropout.

                More advanced students (Phase 4 to Phase 7): Although fewer dropouts occur in these phases, there is still concern, since the increase in dropouts from 2021 to 2022 may reflect accumulated challenges over the academic journey.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem18.png')

        with st.expander('Student Admission Year'):
        
            st.markdown(
                '''
                We defined a list of quantitative columns `quantitative_columns_total`, which includes various metrics for the years 2020, 2021, and 2022, in addition to the `ADMISSION_YEAR` column. These columns contain numerical data that can be statistically analyzed.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem19.png')

            st.markdown(
                '''
                The average admission year is 2019, which is expected considering the data covers three consecutive years. The standard deviation (1.78) indicates that the variation in admission years is not very large; most students were admitted in 2019, with a few admitted in 2016 and 2022.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem20.png')

        with st.expander('Correlation Between Variables'):
        
            st.markdown(
                '''
                Values close to 1 indicate a strong positive correlation, while values close to -1 indicate a strong negative correlation.
                Values near 0 indicate little or no linear correlation.
                This chart helps identify which variables have strong relationships, which can be useful for statistical analysis and predictive modeling.

                **Strongest positive correlations:**

                - IDA_2021 and IDA_2022: Very high correlation, above 0.85, suggesting a strong relationship between consecutive years.
                - INDE_2021 and INDE_2022: High correlation, above 0.86, indicating consistency or similar patterns across the years.
                - IEG_2021 and IEG_2022: Correlation above 0.87, also indicating a high relationship between consecutive years for these variables.

                **Strongest negative correlations:**
                - ADMISSION_YEAR and IPP_2022: Strong negative correlation around -0.35, suggesting an inverse relationship between admission year and performance or the metric associated with IPP in 2022.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem21.png')

        with st.expander('INDE (Development Index)'):
        
            st.markdown(
                '''
                We created bar charts to visualize INDE (Development Index) statistics for the years 2020, 2021, and 2022.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem22.png')

            st.markdown(
                '''
                INDE_2020 shows the highest average (7.30), followed by a slight decrease to 6.89 in 2021 and 7.03 in 2022.

                The lower standard deviation over the years suggests a reduction in variability among students regarding the need for educational development, indicating that the support provided became more consistent over time.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem23.png')

        with st.expander('Temporal Analysis'):
        
            st.markdown(
                '''
                We visualized the annual trend of average values for various metrics across the years 2020, 2021, and 2022, to help identify how these metrics evolved over time and to provide insights into patterns or changes.

                **Trend Analysis**: The code calculates yearly averages for each metric (IAN, IDA, IEG, IAA, IPS, IPP, IPV, INDE).

                **Pattern Identification**: By visualizing annual averages, it's possible to spot trends such as consistent increases or decreases in certain metrics. This helps understand data behavior and make informed decisions based on observed trends.

                **Year-to-Year Comparison**: Enables comparison of each metric’s averages across 2020, 2021, and 2022. Useful for evaluating the impact of different factors over time and identifying years with significant changes.

                **Intuitive Visualization**: The use of line charts with points and annotations makes trend visualization more intuitive and easy to interpret.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem24.png')    

            st.markdown(
                '''
                IAN (Needs Assessment Index): The IAN index shows a downward trend over the three years analyzed, decreasing from 7.43 in 2020 to 6.42 in 2022. This suggests a reduction in students' needs over time, which may indicate an improvement in conditions or support provided, resulting in fewer intervention requirements.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem25.png')

            st.markdown(
                '''
                IDA (Academic Performance Index): Academic performance decreased from 2020 (6.32) to 2021 (5.43), which may reflect challenges faced by students, such as the COVID-19 pandemic. In 2022, there is a slight recovery to 6.07, possibly indicating an adaptation process as students begin to recover from earlier circumstances.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem26.png')

            st.markdown(
                '''
                IEG (General Engagement Index): Engagement follows an interesting trend: it dropped from 7.80 in 2020 to 6.84 in 2021, possibly due to the pandemic’s impact and changes in the learning format. However, there was a recovery in 2022 to 7.88, suggesting students are becoming more engaged again, perhaps due to the return of in-person activities or improvements in teaching methods.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem27.png')

            st.markdown(
                '''
                IAA (Academic Support Index): Academic support remained quite stable over the three years, with minor variations: 2020 (8.37), 2021 (8.16), and 2022 (8.26). This indicates that the support provided to students was not drastically affected by the pandemic and remained effective over time.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem28.png')

            st.markdown(
                '''
                IPS (Social Progress Index): Social progress showed a slight improvement over the three years, with the average increasing from 6.74 in 2020 to 6.90 in 2022. This may reflect efforts to support students’ social development, possibly through initiatives to address the pandemic’s effects and improve social conditions.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem29.png')

            st.markdown(
                '''
                IPP (Personal Progress Index): The personal progress index improved in 2021 (7.60) but had a significant drop in 2022 (6.30). This trend may be related to the prolonged impact of the pandemic, which could have affected students’ emotional and personal well-being, resulting in difficulties in personal development in 2022.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem30.png')

            st.markdown(
                '''
                IPV (Vital Progress Index): Vital progress shows a slight upward trend in 2021 (7.43), followed by a small decline in 2022 (7.25). This suggests that students, despite challenges, managed to maintain a good trajectory in their vital progress, although with a slight drop after the 2021 peak.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem31.png')

            st.markdown(
                '''
                INDE (Educational Development Needs Index): The INDE index saw a slight decline from 2020 to 2021, but in 2022 there was a slight recovery to 7.03. This suggests that, despite a brief decrease in development needs in 2021, the trend slightly reversed in 2022, possibly due to improvements in educational conditions.
                '''
            )
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem32.png')

        with st.expander('Density Visualization'):
        
            st.markdown(
                '''
                We analyzed the density distribution of the metrics IAN, IDA, IEG, IAA, IPS, IPP, IPV, and INDE for the years 2020, 2021, and 2022.
                ''')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem33.png')

            st.markdown(
                '''
                IAN (Grade Approval Index): The density curves are symmetrical across the three years analyzed. The highest density occurs in 2022, while the lowest is in 2020. This indicates a slight improvement in the distribution of approval indices over the years.

                IDA (Academic Performance Index): The curves show skewness, suggesting the presence of outliers. The highest density is observed in 2021 and 2022, with greater data concentration, while 2020 shows a more dispersed distribution.

                IEG (General Engagement Index): The density curves are symmetrical in 2022 and 2020, while 2021 shows a left-skewed distribution. 2022 and 2020 present higher data concentration near the mean, while 2021 is more dispersed, indicating variability in engagement.

                IAA (Academic Activity Index): The density curves for 2020, 2021, and 2022 nearly overlap. This suggests similar variable values across the years, without significant variation.

                IPS (Social Participation Index): Below the combined mean, the curves are skewed, while above the mean they become symmetrical. This may indicate greater data dispersion around the mean but a tendency toward normality at higher values.

                IPP (Project Participation Index): In 2022, the curve falls below the combined mean, while in 2021 and 2020 the curves are symmetrical with density variation. Data appears more dispersed in 2022, with lower concentration near the mean.

                IPV (Voluntary Participation Index): The density curves are symmetrical in 2022 and 2020, with a peak at the combined mean, while 2021 is skewed. 2021 shows greater dispersion, while 2022 and 2020 have more data concentrated around the mean.

                INDE (Educational Development Index): The curves are slightly symmetrical, with a peak near the combined mean. This suggests the data is relatively balanced and close to the average, with no major fluctuations.
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

        with st.expander('Dropout Analysis'):
        
            st.markdown(
                '''
                Stage of dropout: The data analysis shows that dropouts are more common in the early stages of the course, especially in stages 0 and 1, where adaptation and commitment may be more challenging for students. As students progress to more advanced stages, dropout rates decrease, suggesting that those reaching later stages tend to be more resilient and committed.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem42.png')

            st.markdown(
                '''
                Dropout classification based on general grades: The analysis of dropout reasons reveals that the academic dimension is the main factor, with a considerable number of students indicating difficulties in this area. The psychosocial dimension, while still relevant, has a slightly lower impact. Lastly, the psychopedagogical dimension is also significant, on par with academic issues, indicating that learning and pedagogical support challenges play an important role in dropouts.

                This distribution suggests that strategies focused on strengthening academic skills and improving psychopedagogical support could be effective in reducing student dropout rates.
                ''')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem43.png')


            st.markdown(
                '''
                **Length of Stay for Students with “Possible Dropout”:**  

                The analysis of the distribution of time spent in the course by students who dropped out reveals that the vast majority left during the early phases, especially phases 0 and 1, which account for the highest number of dropouts. Phases 2, 3, 4, and 5 show significantly fewer dropouts, indicating that dropout rates decrease as students progress. Phases 6 and 7 do not appear, which may suggest that students who reach these phases are more resilient or receive better support.

                Furthermore, the average time spent in the course by students who dropped out is only 0.40 years, reinforcing the idea that many dropouts occur early on, possibly due to academic, psychosocial, or psychopedagogical challenges. This highlights the importance of closer monitoring in the early years to identify and mitigate dropout factors.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem44.png')

            st.markdown(
                '''
                **Time Spent by Students in Phase 7:**  
                
                The analysis shows that most students who reached this phase remained in the course for a short time, with many staying less than 2 years. A few students stayed for up to 6 years, indicating that although phase 7 represents a final phase, not all students have long trajectories. Additionally, a considerable number of students dropped out shortly after entering, with very short durations like 0 years, suggesting that dropout can happen right after reaching phase 7.

                The distribution chart and data suggest that phase 7 may have a mixed pattern: some students stay for a long time, while others drop out quickly, possibly due to motivation, academic difficulties, or external factors.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem45.png')

            st.markdown(
                '''
                **Global Average of Indices:**  
                
                The analysis reveals that students classified as "Doing Well" consistently perform better across various dimensions, while those "Not Doing Well" show more variability and often perform below the global average. Academic, psychosocial, and psychopedagogical factors are strongly correlated with overall performance—students who do well in one area tend to do well in others.

                Interventions for "Not Doing Well" students may benefit from personalized approaches, targeting specific difficulties, whether academic or psychosocial.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem46.png')

        with st.expander('Creating Training and Test Models'):
        
            st.markdown(
                '''
                We are selecting a specific subset of columns from the `df_tratamento` DataFrame. These columns were chosen to focus on relevant information for data analysis and processing.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem47.png')

            st.markdown(
                '''
                **Status Categorization:** We created a new column called `ATIVO` to indicate whether the student is active or not, and removed the original `STATUS_ALUNO` column.

                **Classification of Dimensions:** Academic, psychosocial, and psychopedagogical dimensions were categorized as 'below average' or 'excellent' based on values.

                We cleaned the DataFrame to prepare the data for export (if needed) and to analyze the distribution of active vs inactive students.

                These operations help prepare the data for further analysis, making interpretation and visualization easier.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem48.png')

            st.markdown('Training and test dataset split')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem49.png')

            st.markdown(
                '''
                We defined a class called `DropFeatures` that inherits from `BaseEstimator` and `TransformerMixin` from scikit-learn.  
                This custom transformer removes specific columns from a DataFrame.

                This class is useful in preprocessing pipelines where certain columns need to be dropped before applying other transformations or models.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem50.png')
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem51.png')

            st.markdown(
                '''
                **Purpose of the Class:** To apply one-hot encoding to specific columns in a DataFrame.

                **Initialization:** The list of columns to be transformed is passed as an argument when instantiating the class.  
                **Fit and Transform:** The `fit` method does nothing and just returns `self`, while `transform` applies one-hot encoding to the specified columns and concatenates the result with the rest of the DataFrame.

                This class is useful for preparing categorical data for machine learning models by transforming categories into a numerical format usable by algorithms.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem52.png')

            st.markdown('We used `OrdinalFeature` to convert ordinal columns (data with a natural order) in the DataFrame into numerical values using ordinal encoding.')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem53.png')

            st.markdown('`Oversample` was used to apply oversampling using SMOTE (Synthetic Minority Over-sampling Technique) to balance the minority class in the `ATIVO` column.')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem54.png')

            st.markdown('We applied the pipeline to the data:')

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem55.png')

            st.markdown(
                '''
                **Model Execution:**  
                We trained the machine learning model using training data and evaluated its performance on test data, generating various metrics and visualizations for analysis.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem56.png')

            st.markdown(
                '''
                We imported the `LogisticRegression` class, created an instance of the logistic regression model with a fixed random state, and passed it to the `roda_modelo` function to train and evaluate the model using the training and test datasets.
                '''
            )

            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem57.png')

            st.markdown(
                '''
                **Classification Report**

                **Class 0:**
                - Precision: 0.98 – 98% of predictions for class 0 are correct.
                - Recall: 1.00 – The model correctly identified all class 0 examples.
                - F1-Score: 0.99 – The harmonic mean of precision and recall.
                - Support: 824 – Number of true instances of class 0 in the dataset.

                **Class 1:**
                - Precision: 1.00 – All predictions for class 1 are correct.
                - Recall: 0.98 – The model correctly identified 98% of class 1 instances.
                - F1-Score: 0.99
                - Support: 824

                **Global Metrics**
                - Accuracy: 0.99 – 99% of all predictions are correct.
                - Macro Avg:
                    - Precision: 0.99
                    - Recall: 0.99
                    - F1-Score: 0.99

                Macro average treats all classes equally.
                Weighted average accounts for the number of instances in each class.

                - Weighted Avg:
                    - Precision: 0.99
                    - Recall: 0.99
                    - F1-Score: 0.99

                **Summary:**  
                - High precision and recall for both classes.
                - F1-Score close to 1 indicates a strong balance.
                - Overall accuracy is very high.
                - Both macro and weighted averages are strong, reflecting consistent model performance.
                '''
            )

            col1, col2 = st.columns(2)

            with col1:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem58.png')

            with col2:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem59.png')

        with st.expander('DecisionTreeClassifier'):
        
            st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem60.png')

            st.markdown(
                '''
                **AUC (Area Under the Curve)**  
                - Value: 0.9997  
                - Interpretation: A value very close to 1 indicates an almost perfect ability to distinguish between positive and negative classes. The model is performing exceptionally well.

                **KS Metric (Kolmogorov-Smirnov Test)**
                - Result:  
                  `KstestResult(statistic=0.0073, pvalue=0.99999999999, statistic_location=0.5, statistic_sign=-1)`

                **Interpretation:**
                - Statistic: 0.0073 – The maximum difference between the cumulative distributions of the two classes is very small.
                - P-value: ~1.0 – The difference is not statistically significant.
                - Statistic Location: 0.5 – Where the max difference occurs.
                - Statistic Sign: -1 – Indicates direction of the difference.

                **Summary:**  
                - AUC: Extremely high, suggesting excellent class separation.
                - KS: Very low statistic and extremely high p-value suggest the distributions are similar, which may imply overfitting or that the classes are highly separable.
                '''
            )

            col1, col2 = st.columns(2)

            with col1:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem61.png')

            with col2:
                st.image('https://raw.githubusercontent.com/Tamireees/Datathon-Projeto-Passos-Magicos/main/midias/imagem62.png')        





if selected_page == content[language]["form_title"]:
    if language == "Português":


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
    else:
        st.title("Form: Predictive Model")

        with st.form("predictive_model_form"):
            name = st.text_input("Student Name")
            phase_2020 = st.number_input("Phase 2020", min_value=0, step=1)
            phase_2021 = st.number_input("Phase 2021", min_value=0, step=1)
            phase_2022 = st.number_input("Phase 2022", min_value=0, step=1)
            stone_2020 = st.selectbox("Stone 2020", ['Amethyst', 'Quartz', 'Agate', 'Topaz'])
            stone_2021 = st.selectbox("Stone 2021", ['Amethyst', 'Quartz', 'Agate', 'Topaz'])
            stone_2022 = st.selectbox("Stone 2022", ['Amethyst', 'Quartz', 'Agate', 'Topaz'])
            turning_point_2020 = st.number_input("Turning Point 2020", min_value=0, max_value=1, step=1)
            turning_point_2021 = st.number_input("Turning Point 2021", min_value=0, max_value=1, step=1)
            turning_point_2022 = st.number_input("Turning Point 2022", min_value=0, max_value=1, step=1)
            admission_year = st.number_input("Year of Admission", min_value=2000, step=1)
            academic_dimension = st.selectbox("Academic Dimension", ['excellent', 'below average'])
            psychosocial_dimension = st.selectbox("Psychosocial Dimension", ['excellent', 'below average'])
            psychopedagogical_dimension = st.selectbox("Psychopedagogical Dimension", ['excellent', 'below average'])

            submitted = st.form_submit_button("Predict")

            if submitted:
                # Create a DataFrame with user input data
                data = {
                    'NAME': [name],
                    'PHASE_2020': [phase_2020],
                    'PHASE_2021': [phase_2021],
                    'PHASE_2022': [phase_2022],
                    'STONE_2020': [stone_2020],
                    'STONE_2021': [stone_2021],
                    'STONE_2022': [stone_2022],
                    'TURNING_POINT_2020': [turning_point_2020],
                    'TURNING_POINT_2021': [turning_point_2021],
                    'TURNING_POINT_2022': [turning_point_2022],
                    'ADMISSION_YEAR': [admission_year],
                    'academic_dimension': [academic_dimension],
                    'psychosocial_dimension': [psychosocial_dimension],
                    'psychopedagogical_dimension': [psychopedagogical_dimension]
                }

                df_input = pd.DataFrame(data)

                df_prev = novo_pipeline(df_input)

                model_xgb = joblib.load(r'C:\Users\tamir\OneDrive\Desktop\DATATHON\datathon-\modelo\Model_XGB.joblib')

                predictions = model_xgb.predict(df_prev)

                st.write("Calculating...")
                animation_placeholder = st.empty()

                for _ in range(10):
                    animation_placeholder.text("Loading...")
                    time.sleep(0.1)

                # Check the value of predictions and display the corresponding text
                if predictions[0] == 1:
                    animation_placeholder.text("Probability of NOT dropping out: 90%")
                elif predictions[0] == 0:
                    animation_placeholder.text("Probability of dropping out: 90%")
                else:
                    animation_placeholder.text("Undefined result")

