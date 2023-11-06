# Libs
import time

# libs gráficas
import matplotlib.pyplot as plt

# Streamlit
import streamlit as st
import streamlit.components.v1 as components

# variável para a contagem automática dos gráficos
num = 0

# Configurando a página
st.set_page_config(
    page_title="Tech-Challenge",
    page_icon="💉",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Projeto criado para o *tech-challenge* do curso de pós-graduação da FIAP/Alura."
    }
)

# Função de cache dos gráficos
@st.cache_data(show_spinner=False)
def waitForResourceAvailable(src, wframe, hframe):
    with st.spinner("Carregando o gráfico. Aguarde..."):
        timer = 0
        content = components.iframe(src, width = wframe, height = hframe, scrolling = False)
        while not content:
            time.sleep(1)
            timer += 1
            if timer > 10:
                return st.markdown(f"**:red[Erro]**: Tempo de resposta esgotado! Acesse o gráfico no link: {src}")
            if content:
                return content

# Titulo de Página
st.title('Análise de dados: explorando dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) COVID19')

# Código para alinhar imagens expandidas no centro da tela e justificar textos
st.markdown(
    """
    <style>
        body {text-align: justify}
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Carregamento de imagens por cache
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Layout do aplicativo
tab0, tab1, tab2, tab3, tab4 = st.tabs(["🔷Introdução",
                                        "🌐Base de Dados",
                                        "📝Pesquisa",
                                        "💡Conclusões",
                                        "📑Referências"])

# Separando as Tabs
with tab0:
    '''
    ## Explorando dados da Pesquisa Nacional por Amostra de Domicílios COVID19 realizado em 2020

    Links importantes:

    [covid19.ibge.gov.br/pnad-covid](https://covid19.ibge.gov.br/pnad-covid/) - Pesquisa Nacional por Amostra de Domicílios (PNAD COVID19)

    [ibge.gov.br](https://www.ibge.gov.br/) - Instituto Brasileiro de Geografia e Estatística (IBGE)

    Links dos integrantes do projeto:

    [github.com/GabrielPCO](https://github.com/GabrielPCO/tech-challenge-covid) - Github Gabriel Oliveira

    [github.com/jackson-simionato](https://github.com/jackson-simionato) - Github Jackson Simionato

    gabrielpcoliveira@gmail.com - Email Gabriel Oliveira

    simionato.jackson@gmail.com - Email Jackson Simionato

    haendelf@hotmail.com - Email Haendel Oliveira

    '''
    st.divider()
    '''
    
    ## Resumo

    A Pesquisa Nacional por Amostra de Domicílios (PNAD COVID19) objetiva estimar o número de pessoas com sintomas referidos associados à síndrome gripal e monitorar os impactos da pandemia da COVID-19 no mercado de trabalho brasileiro.

    A coleta da PNAD COVID19 teve início em 4 de maio de 2020, com entrevistas realizadas por telefone em, aproximadamente, 48 mil domicílios por semana, totalizando cerca de 193 mil domicílios por mês, em todo o Território Nacional. A amostra é fixa, ou seja, os domicílios entrevistados no primeiro mês de coleta de dados permanecerão na amostra nos meses subsequentes, até o fim da pesquisa.

    O questionário se divide em duas partes, sendo uma direcionada a questões de saúde, especificamente sobre sintomas associados à síndrome gripal e outra, a questões de trabalho. 
    Nas questões de saúde, investiga-se a ocorrência de alguns dos principais sintomas da COVID19 no período de referência da pesquisa, considerando-se todos os moradores do domicílio. 
    
    Para aqueles que apresentaram algum sintoma, perguntam-se quais as providências tomadas para alivio dos sintomas; se buscaram por atendimento médico devido a esses sintomas; e o tipo de estabelecimento de saúde procurado.
    
    Nas questões de trabalho, busca-se classificar a população em idade de trabalhar nas seguintes categorias: ocupados, desocupados e pessoas fora da força de trabalho.
    Investiga-se, ainda, os seguintes aspectos: ocupação e atividade; afastamento do trabalho e o motivo do afastamento; exercício de trabalho remoto; busca por trabalho; motivo por não ter procurado trabalho; horas semanais efetivamente e habitualmente trabalhadas; assim como o rendimento efetivo e habitual do trabalho.
    
    Por fim, visando compor o rendimento domiciliar, pergunta-se se algum morador recebeu outros rendimentos não oriundos do trabalho, tais como: aposentadoria, BPC-LOAS, Bolsa Família, algum auxílio emergencial relacionado à COVID, seguro desemprego, aluguel e outros. Cabe ressaltar que a PNAD COVID19 é uma pesquisa com instrumento dinâmico de coleta das informações; portanto, o questionário está sujeito a alterações ao longo do período de sua aplicação.

    A pesquisa prevê divulgações semanais para alguns indicadores, em nível Brasil, e divulgações mensais para um conjunto mais amplo de indicadores, por Unidades da Federação.

    Os resultados da PNAD COVID19 são pioneiros no sentido de constituírem a primeira divulgação de Estatísticas Experimentais elaboradas pelo IBGE, as quais estão alinhadas com a estratégia de modernização do Instituto e permitem a ampliação das ofertas de informação para atender às necessidades de seus usuários.
    '''
    st.divider()
    '''
    ## Objetivo do trabalho

    Neste documento iremos analisar dados da PNAD COVID19 realizada no ano de 2020 a fim de compreender melhor como foi o comportamento da população na época da pandemia.

    Para isso, serão aplicados os conceitos e técnicas associados à análise exploratória de dados,
    visualização e storytelling de dados, além do uso de banco de dados (local e cloud) para manipulação de dados muito grandes (Big Data).

    Os tópicos foram divididos em três categorias principais: base de dados, pesquisa e conclusões. Cada categoria será tratada e mais aprofundada em sua respectiva aba dentro desse documento.
    '''
    st.divider()
    '''

    ## Observação

    Os demais dados, DataFrames e outras análises mais aprofundadas podem ser encontradas na página de Github dos integrantes do grupo referenciadas no início desse documento.
    '''
with tab1:
    '''

    ## Seleção dos dados

    Para a nossa análise, decidimos selecionar dados de três meses diferentes (setembro, outubro e novembro) dispostos no sistema de divulgação da PNAD no site do IBGE.
    
    Selecionamos então os microdados apontados na figura abaixo.
    '''

    img_1 = load_img('Assets/Imagens/microdados.jpg')
    st.image(img_1)
    
    '''

    Os microdados consistem no menor nível de desagregação dos dados de uma pesquisa, retratando, sob a forma de códigos numéricos, o conteúdo dos questionários, preservado o sigilo das informações. Desse modo, os microdados apresentam um formato ideal para o analista de dados manipular e criar suas próprias tabelas e gráficos.
    '''
    st.divider()
    '''

    ## Dicionário de dados

    Utilizamos então os respectivos dicionários de dados da PNAD para traduzir os microdados selecionados.
    '''

    img_2 = load_img('Assets/Imagens/dicionarios.jpg')
    st.image(img_2)

    st.divider()
    '''

    ## Criação de tabela em banco de dados relacional

    Para a nossa análise utilizamos uma quantidade relativamente massiva de dados. Desse modo, será necessário aplicar algumas técnicas especiais para o manuseio dos dados.

    Para facilitar a manipulação dos dados, decidimos criar uma tabela em banco de dados relacional para armazenar nossos dados.
    
    Escolhemos o sistema gerenciador de banco de dados PostgresSQL.
    '''
    
    img_3 = load_img('Assets/Imagens/postgres01.jpg')
    st.image(img_3)

    st.divider()
    '''

    ## Consolidação dos dados

    Como as variáveis que utilizaremos como nossas colunas são equivalentes entre os diferentes set de dados, podemos consolidar esses dados em uma mesma tabela.

    Para tal, decidimos utilizar o software KNIME que é uma plataforma livre e de código aberto de análise de dados, construção de relatórios e integração de dados. Desse modo, o processo de consolidação será mais rápido e eficiente.

    
    Utilizamos os seguintes passos para a consolidação e inserção no banco de dados:
    
    1. Leitura dos três arquivos .csv

    2. Consolidação da tabela

    3. Acesso ao banco de dados Postegres

    4. Inserção dos dados

    
    '''

    img_4 = load_img('Assets/Imagens/knime.jpg')
    st.image(img_4)

    '''

    Em seguida, visualizamos e confirmamos a alteração da tabela no banco de dados
    '''

    img_5 = load_img('Assets/Imagens/postgres02.jpg')
    st.image(img_5)

    st.divider()
with tab2:
    '''

    ## Pesquisa Nacional por Amostra de Domicílios

    Nessa seção, iremos analisar os dados colhidos na PNAD COVID19. Para isso, separamos três tópicos de interesse para nossa análise: sintomas, população e sociedade.

    Em cada tópico serão realizadas análises sobre o tema abordado, com o objetivo de descrever o comportamento e contexto da população brasileira durante a pandemia.
    
    Os dados do PNAD abrangeram cerca de 193 mil domicílios por mês de pesquisa e um total de mais de 1 milhão de registros na base de dados abrangendo três meses.
    
    A análise será separada em três categorias diferentes, sendo elas: características clínicas dos sintomas, características da população e características econômicas da sociedade. 
    '''
    tab2_01, tab2_02, tab2_03 = st.tabs(["🌎População",
                                         "🏡Sociedade",
                                         "🌡️Sintomas"])
    
    with tab2_01:
        '''

        ## Caracterizando a população

        ### Pirâmide etária

        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Como a população da pesquisa está distribuída quanto ao sexo e faixa etária?**

            A Pirâmide Etária é uma importante ferramenta de análises demográficas, pois permite caracterizar diversos aspectos da população como natalidade,
            longevidade, além de permitir traçar cenários futuros para a população do país.

            Do ponto de vista da pandemia auxilia a delimitar e quantificar grupos de risco existentes na população, como por exemplo pessoas acima dos 60 anos.

            Questionário:
            1. Sexo

            2. Idade
            '''
            if st.button(f'Programação { num }', type='secondary'):
                '''
                ### SQL

                ```sql
                with idade_data as 
                ( SELECT 
                    A003,
                    A002,
                    count(idade) as count_idade
                FROM `{project_id}.{dataset_id}.{table_id}` 
                GROUP BY A003, A002),

                grupo_idade_data as
                (SELECT
                    A003,
                    A002,
                    count_idade,
                    CASE
                        WHEN A002 <= 10 THEN '0-10'
                        WHEN A002 BETWEEN 11 AND 20 THEN '11-20'
                        WHEN A002 BETWEEN 21 AND 30 THEN '21-30'
                        WHEN A002 BETWEEN 31 AND 40 THEN '31-40'
                        WHEN A002 BETWEEN 41 AND 50 THEN '41-50'
                        WHEN A002 BETWEEN 51 AND 60 THEN '51-60'
                        WHEN A002 BETWEEN 61 AND 70 THEN '61-70'
                        WHEN A002 BETWEEN 71 AND 80 THEN '71-80'
                        WHEN A002 > 80 THEN '80+'
                    END as grupo_idade
                FROM idade_data)

                SELECT
                    A003,
                    grupo_idade,
                    SUM(count_idade) as count_grupo_idade
                FROM grupo_idade_data
                GROUP BY A003, grupo_idade
                ORDER BY A003, grupo_idade
                ```

                ### Python
                ```python
                age_groups = list(df_results.sort_values(by='grupo_idade')['grupo_idade'].unique())

                males_population = list(df_results.sort_values(by='grupo_idade').loc[df_results['sexo'] == 'Homem']['count_grupo_idade'])
                males_population = [-neg_value for neg_value in males_population]
                females_population = list(df_results.sort_values(by='grupo_idade').loc[df_results['sexo'] == 'Mulher']['count_grupo_idade'])

                # Create a subplot with two horizontal bar charts
                fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=('Homens', 'Mulheres'))

                # Add bar traces for males and females
                fig.add_trace(go.Bar(x=males_population, y=age_groups, orientation='h', name='Homens'), row=1, col=1)
                fig.add_trace(go.Bar(x=females_population, y=age_groups, orientation='h', name='Mulheres'), row=1, col=2)

                # Custom xticks
                fig.update_layout(xaxis2 = dict(
                    tickmode='array',
                    tickvals = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0],
                    ticktext = ['90,000', '80,000', '70,000', '60,000', '50,000', '40,000', '30,000', '20,000', '10,000', '0']
                    )
                )

                # Custom xticks
                fig.update_layout(xaxis1 = dict(
                    tickmode='array',
                    tickvals = [-90000, -80000, -70000, -60000, -50000, -40000, -30000, -20000, -10000, 0],
                    ticktext = ['90,000', '80,000', '70,000', '60,000', '50,000', '40,000', '30,000', '20,000', '10,000', '0']
                    )
                )

                # Customize layout
                fig.update_xaxes(title_text='Nº de entrevistados', row=1, col=1)
                fig.update_xaxes(title_text='Nº de entrevistados', row=1, col=2)

                # Set the range of the y-axis to reverse the age pyramid
                #fig.update_yaxes(categoryorder='total ascending', row=1, col=1)
                fig.update_yaxes(side='right', mirror=True, row=1, col=1)

                # Add title and labels
                fig.update_layout(title='Pirâmide etária dos entrevistados<br>PNAD COVID-19', title_x=0.5, xaxis=dict(title='Nº de entrevistados'), width=1000, margin_pad=5,
                                showlegend=False, plot_bgcolor='white')

                fig.update_xaxes(
                    mirror=True,
                    ticks='outside',
                    showline=True,
                    linecolor='black',
                    gridcolor='lightgrey'
                )
                fig.update_yaxes(
                    mirror=True,
                    ticks='outside',
                    showline=True,
                    linecolor='black',
                    gridcolor='lightgrey'
                )

                fig.layout.annotations[0].update(y=1.02)
                fig.layout.annotations[1].update(y=1.02)

                fig.show()
                ```
                '''
        if st.button(f'Carregar Gráfico { num }', type='primary'):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_1_população_Piramide_Etaria.html", 1000, 700)
            '''
            ## Análise

            Pode-se dizer que a Pirâmide Etária é saudável do ponto de vista demográfico pois a maioria da população está concentrada no meio da pirâmide, ou seja na fase adulta, o que significa
            que economicamente há pessoas disponíveis para trabalhar e, comparando com cenários de décadas passadas, há menor mortalidade entre os mais jovens.

            Ainda assim, há uma porcentagem grande da população com menos de 20 anos, principalmente homens, portanto há margem de crescimento nos próximos anos para as faixas etárias do meio da pirâmide.

            Do ponto de vista dos grupos de risco do COVID-19, os dados mostram que a maior parte dos entrevistados têm entre 61 e 70 anos e uma parcela pequena da população possui mais de 80 anos.
            Neste ponto, é importante destacar que há uma grande predominância de mulheres nas faixas etárias mais elevadas, indicando que o sexo feminino possui maior longevidade e possivelmente será o perfil
            mais comum nos casos graves envolvendo grupos de risco COVID-19.
            '''
        st.divider()

        '''
        ### Distribuição da população da pesquisa por situação de moradia
        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''        
            **Como está distribuída a população da pesquisa em questão de situação de domicílio?**

            Plotamos os dados de domicílio da população de entrevistados nos três meses avaliados, separando entre situação urbana e rural.

            Com esses dados, podemos avaliar se a questão do domicílio pode ter alguma conexão com a presença da covid-19.

            Questionário: Situação do domicílio

            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''
                
                ### SQL
                ```sql
                SELECT uf, v1022, COUNT(case v1022 when '1' then 1 else null end) AS "urbana", COUNT(case v1022 when '2' then 1 else null end) AS "rural", COUNT(v1022) AS "total"
                FROM dbo.pnad2020
                GROUP BY
                uf, v1022
                ORDER BY
                total DESC
                ```

                ### Python
                ```python
                fig_3 = px.bar(df_04_final, x="uf", y="total_por_situacao", color="situacao", title="Ditribuição da população da pesquisa por situação",
                            labels=dict(uf="Estado", total_por_situacao="Nº de entrevistados", situacao="Situação"))
                fig_3.update_layout(title_x=0.5)
                plotly.offline.plot(fig_3, filename = 'br_distribuicao_populacao.html', auto_play=False, auto_open=False)
                fig_3.show()
                ```
                '''
        if st.button(f"Carregar Gráfico { num }", type="primary"):        
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/br_distribuicao_populacao.html", 700, 700)
            '''
            
            ## Análise

            Como esperado, a maioria dos entrevistados mora em zona urbana, sendo São Paulo, Minas Gerais e Rio de Janeiro os três estados com maior número de entrevistados.

            Quanto à proporção de habitantes em zona rural e urbana por estado, destacam-se os estados do Nordeste com número elevado de habitantes em zona rural, enquanto RJ e DF tiveram
            a grande maioria de seus entrevistados com moradia em área urbana.

            Do ponto de vista da pandemia, esta é uma informação relevante pois zonas urbanas são áreas de maior circulação e concentração de pessoas, o que facilita a propagação de doenças
            como o COVID-19. Portanto, estados em que a população está mais concentrada em zonas urbanas podem ser mais vulneráveis.

            Por outro lado, zonas rurais possuem menos infraestrutura hospitalar, portanto casos graves ocorridos nessas regiões devem receber atenção especial.
            '''
        st.divider()
        
        '''### Distribuição da população por região de moradia'''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Como está distribuída a população da pesquisa nas UFs do Brasil quanto à região de moradia?**

            Com o objetivo de analisar mais a fundo a questão da distribuição da população no território brasileiro, o gráfico abaixo permite identificar os estados em que a população
            está altamente concentrada em polos político-econômicos como Capitais e Regiões Metropolitanas.

            Questionário: 
            
            1. Tipo de área (capital, região metropolitana, etc.)

            2. UF

            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''
                ### SQL

                ```sql
                SELECT 
                    uf,
                    (CASE
                        WHEN V1023 = 1 THEN 1
                        WHEN V1023 = 2 THEN 2
                        WHEN V1023 = 3 THEN 2
                        WHEN V1023 = 4 THEN 4
                    END) as V1023,
                    COUNT(CASE
                        WHEN V1023 = 1 THEN 1
                        WHEN V1023 = 2 THEN 2
                        WHEN V1023 = 3 THEN 2
                        WHEN V1023 = 4 THEN 4
                    END) as V1023

                FROM `brave-tea-400210.fase_3_tech_challenge.pnad-covid-19`

                GROUP BY uf, new_regiao_moradia
                ORDER BY uf, new_regiao_moradia
                ```

                ### Python

                ```python
                fig_3 = px.bar(df_results.sort_values(by=['n_regiao_moradia'], ascending=False), x="uf", y="n_regiao_moradia", color="new_regiao_moradia", title="Distribuição da população da pesquisa por região de moradia<br>PNAD COVID-19",
                labels=dict(uf="Estado", n_regiao_moradia="Nº de entrevistados", new_regiao_moradia="Região de moradia"))
                fig_3.update_layout(title_x=0.5, width=1200, height=700, legend_traceorder='reversed')
                fig_3.show()
                ```
                '''
        if st.button(f"Carregar Gráfico { num }", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_2_populacao_Distribuição da população da pesquisa por região de moradia.html", 1200, 700)     
            '''
            ## Análise

            Novamente, os dados mostram que o Distrito Federal e o Rio de Janeiro são duas UFs com população altamente concentrada em grandes cidades. Além deles, Goiás, Amazonas e Amapá também tiveram
            mais da metade de seus entrevistados informando que moram em Capitais ou Regiões Metropolitanas.

            Estas 5 UFs podem estar mais suscetíveis à ocorrência de grandes picos de contaminação, o que consequentemente podem gerar uma grande sobrecarga nos sistemas de saúde público e privado. Por isso, medidas de
            educação ou de redução de contato social entre os habitantes devem ser ainda mais úteis nesse contexto.
            '''
        st.divider()
        '''### Distribuição da população por cor/raça'''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Como está distribuída a população da pesquisa quanto à cor/raça nos estados brasileiros?**

            O Brasil está entre os países mais diversos do ponto de vista etnocultural, em que cada estado ou região possui seu contexto específico. Entretanto, alguns grupos são historicamente mais marginalizados
            e uma grande parcela destas populações vivem em situação de vulnerabilidade social, como é o caso dos negros e indígenas.

            Assim, é importante entender o cenário étnico de cada estado para que os esforços de controle da pandemia também estejam de acordo com os contextos locais.

            Questionário:

            1. Cor ou raça

            2. UF

            '''
            if st.button(f'Programação { num }', type='secondary'):
                '''
                ### SQL
                ```sql
                with cont_raca as 
                    (SELECT
                        uf,
                        A004,
                        COUNT(A004) as n_cor_raca
                    FROM `{project_id}.{dataset_id}.{table_id}` 
                    GROUP BY uf, A004
                    ORDER BY uf, A004)

                SELECT
                    uf,
                    A004,
                    n_cor_raca,
                    ROUND(SUM(n_cor_raca)/SUM(n_cor_raca) OVER (PARTITION BY uf),4) AS proportion_raca
                FROM
                    cont_raca
                GROUP BY
                    uf, A004, n_cor_raca
                ORDER BY uf, A004
                ```

                ### Python
                ```python
                fig_cor_raca = px.bar(df_results.sort_values(by=['proportion_raca'], ascending=False),
                    x="uf", y="proportion_raca", color="A004",
                    title="Ditribuição da população da pesquisa por cor/raça<br>PNAD COVID-19",
                    labels=dict(uf="Estado", proportion_raca="Proporção (%)", A004="Cor/Raça"))

                fig_cor_raca.update_layout(title_x=0.5, width=1200, height=700)

                fig_cor_raca.show()
                ```
                '''
        if st.button(f'Carregar gráfico { num }', type='primary'):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_4_populacao_Distribuição da populacao da pesquisa por cor-raça.html", 1200, 700)
            '''
            ### Análise

            Ao analisar o gráfico com um olhar para o país todo, os dados confirmam a miscigenação existente na população brasileira: a população parda foi a predominante entre os entrevistados.
            Da mesma forma, há uma clara segmentação no perfil de acordo com as diferentes regiões brasileiras. Nas regiões Sul e Sudeste há uma presença maior de população branca e amarela,
            bem como uma menor proporção de negros, especialmente na região Sul.

            Já nas regiões Norte e Nordeste observa-se justamente o contrário, onde há relativamente maior proporção de pardos e pretos. A região Norte também é um caso especial devido à grande quantidade de indígenas
            que moram em estados como Amazonas e Roraima. No contexto da pandemia, estes estados devem receber cuidado especial por terem populações mais suscetíveis aos impactos socioeconômicos do COVID-19 e por
            terem maior dependência do sistema público de saúde.
            '''
    with tab2_02:
        '''

        ## Dados socioeconômicos

        ### Distribuição da população quanto ao valor de aluguel pago
        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''         
            **Como estava a distribuição dos entrevistados pelo Brasil de acordo com diferentes faixas de aluguel?**

            Selecionamos os cinco principais estados por faixa de aluguel dos entrevistados. Assim, teremos uma noção da distribuição dos entrevistados da PNAD de 2020 de acordo com o local onde vivem, se em regiões mais populares ou mais nobres.

            Questionário: Número da faixa do aluguel pago

            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''
                
                ### SQL
                ```sql
                SELECT uf, f0022, COUNT(f0022) AS "faixa_do_aluguel"
                FROM dbo.pnad2020
                GROUP BY
                uf, f0022
                ORDER BY
                faixa_do_aluguel DESC
                ```

                ### Python
                ```python
                fig_1 = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],[{'type':'domain'}, {'type':'domain'}]])
                fig_1.add_trace(go.Pie(labels=faixa_01["Estado"], values=faixa_01["Quantidade"], name="301-600"),
                            1, 1)
                fig_1.add_trace(go.Pie(labels=faixa_02["Estado"], values=faixa_02["Quantidade"], name="801-1.600"),
                            1, 2)
                fig_1.add_trace(go.Pie(labels=faixa_03["Estado"], values=faixa_03["Quantidade"], name="601-800"),
                            2, 1)
                fig_1.add_trace(go.Pie(labels=faixa_04["Estado"], values=faixa_04["Quantidade"], name="101-300"),
                            2, 2)

                # Tamanho do buraco da rosca
                fig_1.update_traces(hole=0.7, hoverinfo="label+value+percent", textinfo='value')

                fig_1.update_layout(title_text="Número de entrevistados em diferentes faixas de aluguel por estado", title_x=0.5, title=dict(font=dict(size=16)),legend=dict(font=dict(size=14)),
                                    annotations=[dict(text='301-600<br>Reais', x=0.160, y=0.82, font_size=18, showarrow=False),
                                                dict(text='801-1.600<br>Reais', x=0.9, y=0.82, font_size=18, showarrow=False),
                                                dict(text='601-800<br>Reais', x=0.160, y=0.12, font_size=18, showarrow=False),
                                                dict(text='101-300<br>Reais', x=0.9, y=0.12, font_size=18, showarrow=False)
                                                ]
                                    )
                plotly.offline.plot(fig_1, filename = 'br_faixa_aluguel.html', auto_open=False)
                fig_1.show()
                ```
                '''

        if st.button(f"Carregar Gráfico { num }", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/br_faixa_aluguel.html", 700, 700)
            '''
            
            ## Análise

            Pelo gráfico, pode-se notar que a maioria dos entrevistados que pagam a maior faixa salarial estão na região Sudeste e Sul do país. 
            Santa Catarina é um estado a se destacar, pois mesmo com uma população pequena, teve grande número de entrevistados que pagam a faixa de aluguel mais alta,
            sugerindo que se trata de uma UF mais desenvolvida socioeconomicamente e com custo de vida elevado.

            Além disso, no geral a maioria dos entrevistados pagam de 301 a 600 reais de aluguel, entre os quais a maioria é de Minas Gerais. A faixa de valor mais baixa, de 101 a 300 reais, possui 4 estados
            do Nordeste entre as UFs com maior número de entrevistados, ou seja, são estados com população mais carente e que dependem ainda mais da infraestrutura de saúda pública.
            '''
        st.divider()
        '''
        ### Distribuição de sexo, idade e renda dos entrevistados
        '''
        num+=1
        with st.expander(f"Questões { num }, { num+1 } & { num+2} (clique para expandir/retrair)", expanded=False):
            '''         
            **Gráfico 6: Como estão distribuidos os entrevistados por cidade e sexo, com comparação de percentual entre homens e mulheres?**

            Questionário: 
            
            1. Qual o sexo do entrevistado?
            
            2. Em qual cidade mora o entrevistado?


            ------------------------------------------------------------------------------------------

            **Gráfico 7: Qual a renda média dos entrevistados em relação a idade e situação de domicílio?**

            Questionário:

            1. Qual o salário do entrevistado?

            2. Qual a idade do entrevistado?

            3. Situação de domicílio?

            ------------------------------------------------------------------------------------------

            **Gráfico 8: Qual o percentual de entrevistados que possuem plano de saúde, que utilizou pronto socorro do SUS/UPA e que utilizou hospital do SUS?**

            Questionário:
            
            1. Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público?
            
            2. Local que buscou atendimento foi pronto socorro do SUS/UPA?
            
            3. Local que buscou atendimento foi hospital do SUS?

            '''
        if st.button(f"Carregar Gráficos { num }, { num+1 } & { num+2}", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                st.markdown('<iframe width="1100" height="680" src="https://app.powerbi.com/view?r=eyJrIjoiNDZkY2RiNGMtYTczZi00MTIyLTk0ZWUtNDljOTdiZmI4MGM0IiwidCI6IjgxYTI4ZjEwLWUxYTEtNGJmNi04N2FlLWY1MDQ1ZTE0NjBjMCJ9" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)
                time.sleep(2)
            
            tab2_02_01, tab2_02_02, tab2_02_03 = st.tabs(["Gráfico 6","Gráfico 7","Gráfico 8"])
            
            with tab2_02_01:
                '''
                ### Análise

                Analisando os dados notamos que a pesquisa nos três de meses que utilizamos de coleta se manteve 52% de homes entrevistados e 48% de mulheres olhando para a pesquisa como um todo.

                Olhando para os maiores estados como Minas Gerais, São Paulo e Rio De Janeiro temos 25% dos entrevistados nesses estados.
                
                Analisando o grau de instrução Sergipe se destaca com o maior índice de entrevistados com o fundamental incompleto chegando a 42%, já o estado com o maior índice de formados entre fundamental, médio, superior e pôs graduação se destaca o Distrito Federal, podendo ser pela influência dos políticos que ali residem e seus familiares. 
                '''
            with tab2_02_02:
                '''
                ### Análise 

                Podemos notar que em média após os 30 anos de uma forma geral temos um aumento considerável na renda média dos entrevistados que se mantem até em média 82 anos para os moradores de regiões urbanas, já para os moradores de regiões rurais temos um comportamento diferente onde notamos com média 25 anos temos esse aumento que se estende até 76 anos em média.
                
                Sobre o grau de escolaridade temos um padrão de quanto maior o grau de instrução maior a renda média.
                '''
            with tab2_02_03:
                '''
                ### Análise

                Analisando o comportamento dos entrevistados apesar de 77 % não possuir plano de saúde temos em média 80% que buscaram hospitais e/ou clínicas particulares. 
                
                Comparando moradores de áreas urbanas e rurais, temos o seguinte cenário onde moradores de área urbanas que possuem plano de saúde são 27,4% e nas áreas rurais temos apenas 7,79% com plano de saúde.
                '''
        st.divider()
        '''
        ### Taxa de desocupação por escolaridade
        '''
        num+=3
        with st.expander(f"Questão {num} (clique para expandir/retrair)", expanded=False):
            '''
            **Qual a relação entre taxa de desocupação e escolaridade da população da pesquisa?**

            Durante a pandemia, além das questões clínicas envolvendo a doença, um grande impacto socioeconômico atingiu o mundo,
            tendo em vista que diversos setores da economia fecharam as portas ou reduziram drasticamente sua atuação para reduzir
            o contato entre pessoas.

            Consequentemente ocorreram corte de salários, demissões em massa e falência de negócios. Assim, a pandemia COVID-19
            também contribuiu para o aumento da pobreza e vulnerabilidade social da população.

            Esta análise busca entender se tais efeitos econômicos relacionados à ocupação e emprego têm relação com a escolaridade
            da população.

            Questionário:

            1. Escolaridade

            2. Na semana passada, por pelo menos uma hora, trabalhou ou fez algum bico?
            '''
            if st.button(f"Programação {num}", type="secondary"):
                '''
                ### SQL
                ```sql
                with cont_escolaridade_trabalho as (
                SELECT 
                    A005, C001, COUNT(*) as n_entrevistados
                FROM
                    `{project_id}.{dataset_id}.{table_id}`
                GROUP BY A005, C001)

                SELECT
                    A005,
                    C001,
                    n_entrevistados,
                    ROUND(SUM(n_entrevistados)/SUM(n_entrevistados) OVER (PARTITION BY A005),4) AS proportion
                FROM
                    cont_escolaridade_trabalho
                GROUP BY
                    A005, C001, n_entrevistados
                ORDER BY A005, C001 DESC
                ```

                ### Python
                ```python
                dict_escolaridade = {'1':'Sem instrução','2':'Fundamental incompleto','3':'Fundamental completo', '4':'Médio incompleto',
                     '5':'Médio completo','6':'Superior incompleto','7':'Superior completo','8':'Pós-graduação'}

                dict_trabalhou = {'1':'Sim', '2':'Não', '0':'Não aplicável'}

                df_results['escolaridade'] = df_results['escolaridade'].astype(str).replace(dict_escolaridade)
                df_results['trabalhou'] = df_results['trabalhou'].astype(str).replace(dict_trabalhou)
                df_results = df_results.loc[df_results['trabalhou'] != "Não aplicável"]
                df_results.reset_index(drop=True, inplace=True)

                df_desemprego = df_results.copy()
                n_entrevistados_escolaridade = df_desemprego.groupby('escolaridade').agg({'n_entrevistados':'sum'}).reset_index()
                n_entrevistados_escolaridade['n_entrevistados'] = n_entrevistados_escolaridade['n_entrevistados'].astype(int)

                df_desemprego = df_desemprego.loc[df_desemprego['trabalhou'] == 'Sim']
                df_desemprego['escolaridade_index'] = list(range(len(df_desemprego['escolaridade'].unique())))
                df_desemprego['desemprego'] = (1 - df_desemprego['proportion']) * 100
                df_desemprego.drop(columns=['n_entrevistados'],inplace=True)
                df_desemprego = df_desemprego.merge(n_entrevistados_escolaridade, on='escolaridade')
                
                fig = px.scatter(df_desemprego, x="escolaridade", y="desemprego",
                    size="n_entrevistados", color="escolaridade",
                    hover_name="escolaridade", size_max=60, width=1300, height=600,
                    color_discrete_sequence=px.colors.qualitative.G10,
                    labels=dict(escolaridade="Escolaridade", desemprego="Taxa de desemprego (%)", n_entrevistados="Nº entrevistados"),
                    title="Relação entre escolaridade e taxa de desemprego<br>PNAD COVID-19")

                fig.update_yaxes(range=[0, 100])
                fig.update_layout(title_x=0.5)

                fig.show()
                ```
                '''
        if st.button(f"Carregar Gráfico {num}", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_8_Relação entre escolaridade e taxa de desocupação.html", 1300, 600)
            '''
            ### Análise

            Os dados evidenciam uma clara relação inversa entre taxa de desocupação e escolaridade. Isto é, quanto maior a escolaridade
            da população menor era a taxa de desocupação durante a pandemia. Além da relação direta entre qualificação do indivíduo e
            empregabilidade, no contexto da pandemia esse fator possivelmente foi ainda mais relevante.

            Isso porque vagas que exigem maior escolaridade geralmente estão associadas a vagas em escritório e que tinha maior facilidade
            de possibilitar o trabalho remoto, reduzindo a taxa de desocupação nesse grupo da população. Da mesma forma, empregos que exigem
            menor qualificação estão mais relacionados a trabalhos manuais, que foram mais afetados pelas restrições de distanciamento social.

            Portanto, mais uma vez os dados do PNAD COVID-19 apontam que a parcela mais pobre da população estava especialmente vulnerável no 
            período da pandemia.
            '''
        st.divider()
        '''
        ### Variação das medidas de distanciamento social
        '''
        num+=1
        with st.expander(f"Questão {num} (clique para expandir/retrair)", expanded=False):
            '''
            **Como as medidas de restrição de contato social variaram entre a população da pesquisa durante os meses avaliados?**

            Antes do desenvolvimento de vacinas para o vírus da COVID-19, medidas de distanciamento social eram ferramentas essenciais
            para o controle da pandemia do ponto de vista clínico.

            Entretanto, ter efetividade neste tipo de ação depende que toda a população seja conscientizada e entenda a importância
            de tais medidas. Além disso, com o passar dos meses, foi perceptível a progressiva redução das medidas de distanciamento,
            algo natural tendo em vista todas as questões psicológicas que envolvem o distanciamento social.

            Questionário:

            1. Mês da pesquisa

            2. Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr.(a) restringiu o contato com as pessoas? 
            '''
            if st.button(f"Programação {num}", type="secondary"):
                '''
                ### SQL
                ```sql
                with cont_restricoes as
                (SELECT 
                    B011, V1013, COUNT(*) as n_entrevistados
                FROM
                    `{project_id}.{dataset_id}.{table_id}`
                WHERE B011 != 9
                GROUP BY V1013, B011
                ORDER BY V1013)

                SELECT
                    V1013,
                    B011,
                    n_entrevistados,
                    ROUND(SUM(n_entrevistados)/SUM(n_entrevistados) OVER (PARTITION BY V1013),4) AS proportion
                FROM
                    cont_restricoes
                GROUP BY
                    V1013, B011,n_entrevistados
                ORDER BY V1013
                ```

                ### Python
                ```python

                dict_restricao_contato = {'1':'Sem restrições', '2':'Poucas restrições', '3':'Restrições moderadas', '4':'Muitas restrições', '9':'Sem resposta'}
                dict_mes = {'9':'Setembro/2020', '10':'Outubro/2020', '11':'Novembro/2020'}

                df_results['mes'] = df_results['mes'].astype(str).replace(dict_mes)
                df_results['restricao_contato'] = df_results['restricao_contato'].astype(str).replace(dict_restricao_contato)

                dict_sort = {'Sem restrições':0, 'Poucas restrições':1, 'Restrições moderadas':2, 'Muitas restrições':3,'Sem resposta':4}
                df_results.sort_values(by='restricao_contato', key=lambda x: x.map(dict_sort), inplace=True)
                df_results.reset_index(drop=True, inplace=True)

                # Create a line chart using Plotly graph objects
                fig = go.Figure()

                # Variable 1
                fig.add_trace(go.Scatter(
                    x=df_results.loc[df_results['mes']=='Setembro/2020']['restricao_contato'], # x-axis
                    y=df_results.loc[df_results['mes']=='Setembro/2020']['n_entrevistados'], # y-axis
                    mode='lines+markers', # Connect data points with lines and add markers
                    name='Setembro/2020', # Name in the legend

                    line=dict(
                        color=px.colors.qualitative.G10[0],        # Change the line color to red
                        width=5),
                    
                    marker=dict(
                        symbol='circle',    # Change the marker symbol to a circle
                        size=5,            # Set the marker size
                        color=px.colors.qualitative.G10[0]),       # Set the marker color             # Set the line width
                ))

                # Variable 2
                fig.add_trace(go.Scatter(
                    x=df_results.loc[df_results['mes']=='Outubro/2020']['restricao_contato'], # x-axis
                    y=df_results.loc[df_results['mes']=='Outubro/2020']['n_entrevistados'], # y-axis
                    mode='lines+markers', # Connect data points with lines and add markers
                    name='Outubro/2020', # Name in the legend

                    line=dict(
                        color=px.colors.qualitative.G10[1],        # Change the line color to red
                        width=5),
                    
                    marker=dict(
                        symbol='circle',    # Change the marker symbol to a circle
                        size=5,            # Set the marker size
                        color=px.colors.qualitative.G10[1]),       # Set the marker color             # Set the line width
                ))

                # Variable 3
                fig.add_trace(go.Scatter(
                    x=df_results.loc[df_results['mes']=='Novembro/2020']['restricao_contato'], # x-axis
                    y=df_results.loc[df_results['mes']=='Novembro/2020']['n_entrevistados'], # y-axis
                    mode='lines+markers', # Connect data points with lines and add markers
                    name='Novembro/2020', # Name in the legend

                    line=dict(
                        color=px.colors.qualitative.G10[2],        # Change the line color to red
                        width=5),
                    
                    marker=dict(
                        symbol='circle',    # Change the marker symbol to a circle
                        size=5,            # Set the marker size
                        color=px.colors.qualitative.G10[2]),       # Set the marker color             # Set the line width
                ))

                fig.update_layout(width=1800, height=600, title='Variação das restrições de distanciamento social<br>PNAD COVID-19', title_x=0.5,
                                yaxis_title="Nº de entrevistados", xaxis_title='Nível de restrição',
                                legend=dict(x=0.03,y=0.95,bgcolor='rgba(0,0,0,0)'))

                fig.update_yaxes(tickformat=",.0f", range=[0,180000])

                fig.show()
                ```
                '''
        if st.button(f"Carregar Gráfico {num}", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_9_Variacaoo restricoes de distanciamento social.html", 1000, 500)
            '''
            ### Análise

            O gráfico de linhas acima aponta uma notícia muito positiva, de que o número de pessoas praticando nenhum tipo de restrição
            social durante a pandemia era insignificativo, mostrando que a população foi minimamente orientada.

            Por outro lado, a maior parte dos entrevistados informou estar adotando poucas restrições de distanciamento social entre setembro
            e outubro de 2020. Possivelmente a necessidade de a população continuar trabalhando e a natureza de seus empregos, 
            como é o caso do setor de serviços, não permitiu que tais pessoas pudessem adotar medidas mais restritivas.

            Outra informação relevante deste gráfico é a comparação entre os três meses analisados. Observa-se que há uma
            tendência de queda no número de entrevistados que informaram adotar medidas mais restritivas de distanciamento. Portanto, os órgãos 
            públicos e estabelecimentos de saúde em geral devem ter em mente que, com o passar do tempo em uma pandemia, a população tende a
            naturalmente afrouxar seus cuidados e voltar a viver normalmente, mesmo com o risco de infecção.

            Portanto, imunizar a população o mais rápido possível deve ser prioridade, por se tratar de uma medida muito mais efetiva.
            '''

    with tab2_03:
        '''

        ## Aspectos clínicos da pandemia COVID-19

        ### Distribuição dos entrevistados pelo Brasil que apresentaram sintomas de covid-19

        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Como estão distribuídos os entrevistados que apresentaram sintomas de COVID-19?**

            Utilizamos os dados de pesquisa dos três meses para avaliar a evolução do sintoma de febre, tosse e dor na cabeça nos estados brasileiros ao longo do tempo. Esses sintomas podem indicar a presença da covid-19 no entrevistado em questão.

            Questionário: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve dor na cabeça?

            Apenas casos nos quais a resposta foi sim para as três perguntas foram adicionados ao gráfico.

            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''

                ### SQL
                ```sql
                SELECT v1013, uf, b0011, b0012, b0015, COUNT(b0011) AS "febre_tosse_dor_cabeca"
                FROM dbo.pnad2020
                WHERE b0011 = '1' AND b0012 = '1' AND b0015 = '1'
                GROUP BY
                v1013, uf, b0011, b0012, b0015
                ORDER BY
                v1013 DESC, febre_tosse_dor_cabeca DESC
                ```

                ### Python
                ```python
                fig_2 = px.choropleth_mapbox(casos_de_febre,
                                           geojson = geo_json_br,
                                           locations='uf',
                                           featureidkey = 'id',
                                           color = 'febre_tosse_dor_cabeca',
                                           animation_frame = 'mes',
                                           hover_name = 'uf',
                                           hover_data = ['febre_tosse_dor_cabeca'],
                                           title = 'Casos de febre, tosse e dor de cabeça no Brasil entre Setembro a Novembro de 2020',
                                           color_continuous_scale='Viridis',
                                           mapbox_style = 'carto-positron',
                                           center = {'lat':-14.654012, 'lon': -56.289339},
                                           zoom = 3,
                                           opacity = 0.9, )
                fig_2.update_layout(coloraxis_colorbar_title_text = 'Número de Casos', title_x=0.5)
                fig_2.update_geos(fitbounds = 'locations', visible = False)
                plotly.offline.plot(fig_2, filename = 'br_mapa_casos_febre.html', auto_play=False)
                fig_2.show()
                ```
                '''

        if st.button(f"Carregar Gráfico { num }", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/br_mapa_casos_febre.html",700,800)      
            '''
            
            ## Análise

            Pelo gráfico, podemos notar que houve uma evolução da quantidade de pessoas que afirmaram ter febre, tosse e dor de cabeça na semana anterior à data da pesquisa. 
            Em setembro notamos uma maior concentração de casos no Centro-Oeste. De setembro para outubro podemos ver uma evolução dos sintomas no sul do país. 
            De outubro para novembro a evolução é mais visível no Norte, com a região Sudeste e Santa Catarina se mantendo com elevados número de casos.
            '''
        st.divider()
        '''
        ### Porcentagem de casos por estado
        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Qual a proporção de casos de covid-19 em relação ao número total de entrevistados dos cinco estados mais afetados?**

            Utilizamos os dados de pesquisa dos três meses para avaliar a proporção de casos de covid-19 em relação a quantidade de entrevistados nos cinco estados mais afetados.

            Questionário: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve dor na cabeça?

            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''

                ### Python
                ```python
                fig_04 = go.Figure(
                    data=go.Bar(
                        x=df_05_final["uf"].head().values,
                        y=df_05_final["total"].head().values,
                        name="Total entrevistados"
                    )
                )

                fig_04.add_trace(
                    go.Scatter(
                        x=df_05_final["uf"].head().values,
                        y=df_05_final["porcentagem"].head().values,
                        yaxis="y2",
                        name="Porcentagem casos",
                        mode="text+lines+markers",
                        texttemplate="%{y}",
                        textfont=dict(
                                color="black",
                                ),
                        marker=dict(
                            symbol="circle",
                            size=50,
                        ),
                    )
                )

                fig_04.update_traces(textfont_size=14)


                fig_04.update_layout(
                    separators=",.",
                    title_text="Porcentagem de casos de febre, tosse e dor na cabeça dos cinco estados mais afetados", 
                    title_x=0.5,
                    title=dict(font=dict(size=14)),
                    legend=dict(orientation="h"),
                    yaxis=dict(
                        title=dict(text="Total de entrevistados"),
                        side="left",
                    ),
                    yaxis2=dict(
                        title=dict(text="Porcentagem de casos"),
                        side="right",
                        overlaying="y",
                        tickmode="sync",
                        tickformat= ".2%"
                    ),
                )
                plotly.offline.plot(fig_04, filename = 'br_porcentagem_casos.html', auto_play=False, auto_open=False)
                fig_04.show()
                ```
                '''

        if st.button(f"Carregar Gráfico { num }", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/br_porcentagem_casos.html", 700, 800)
            '''
            
            ## Análise

            Pelo gráfico, podemos perceber que o estado com maior proporção de casos de covid-19 por número de entrevistados foi Roraima.

            Pela proporcionalidade, podemos notar que esses cinco estados foram os mais afetados pela covid-19 nos meses de setembro, outubro e novembro de 2020.
            '''
        st.divider()
        '''
        ### Procura de atendimento médico por entrevistados sintomáticos
        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Como está a procura por atendimento médico entre os entrevistados com sintomas de COVID-19?**

            Nesta análise, o objetivo foi quantificar os entrevistados que procuraram atendimento médico entre os que apresentaram febre, tosse ou perda olfato/paladar
            nos últimos 3 meses.

            Questionário: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve perda de olfato/paladar?

            4. Por causa disso, foi a algum estabelecimento de saúde?

            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''
                ### SQL
                ```sql
                with check_sintomas as (
                    SELECT
                        V1013,
                        B002,
                        CASE 
                        WHEN B0012 = 1 OR B0011 = 1 OR B00111 = 1 THEN 1
                        ELSE 0
                        END as sintomas,

                        COUNT (CASE 
                        WHEN B0012 = 1 OR B0011 = 1 OR B00111 = 1 THEN 1
                        ELSE 0
                        END) as count_sintomas
                    FROM `brave-tea-400210.fase_3_tech_challenge.pnad-covid-19`
                    GROUP BY V1013, sintomas, B002
                )

                SELECT
                    V1013,
                    sintomas,
                    B002,
                    count_sintomas,
                    ROUND(SUM(count_sintomas)/SUM(count_sintomas) OVER (PARTITION BY V1013),4) AS proportion
                FROM check_sintomas
                WHERE sintomas = 1 AND B002 != 9
                GROUP BY V1013, sintomas,B002, count_sintomas
                ORDER BY V1013
                ```
                '''
        if st.button(f"Carregar Gráfico { num }", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_6_Procura de atendimento por entrevistados sintomaticos.html", 700, 600)
            '''
            
            ## Análise

            Percebe-se que de setembro/2020 até novembro/2020 houve uma pequena variação no número de entrevistados que tiveram algum dos sintomas clássicos da COVID-19 (febre, tosse e perda de olfato/paladar).

            Em setembro cerca de 7,500 entrevistados tiveram algum sintoma, já em novembro esse valor foi de aproximadamente 7,000 entrevistados. Isso representa que, aproximadamente 2% da população de entrevistada
            apresentou algum dos sintomas mais comuns de COVID-19.

            Proporcionalmente, mais entrevistados procuraram atendimento médico nos meses de outubro e novembro do que em setembro. 
            
            Uma hipótese, com viés otimista, é que as pessoas estão mais conscientes dos perigos da doença e por isso estão buscando tratamento.
            
            Uma alternativa, com olhar mais pessimista, é que os casos de COVID-19 ocorridos em outubro e novembro foram mais graves e demandaram
            mais estrutura hospitalar.
            '''
        st.divider()
        '''
        ### Número de entrevistados internados por tipo de sintoma
        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Entre os sintomas mais sintomas frequentes de COVID-19, qual está mais relacionado com internações?**

            A capacidade dos sistemas de saúde, tanto públicos como privados, é um fator extremamente importante em uma pandemia, pois em picos de infecção da população pode haver falta
            de leitos e pacientes podem não receber o devido atendimento.

            Neste sentido, a Questão 07 busca entender a relação entre os sintomas e as ocorrências de internação entre a população da pesquisa, para que hospitais possam priorizar esforços
            em casos com sintomas mais graves.

            Questionário: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve perda de olfato/paladar?

            4. Ao procurar o hospital, teve que ficar internado por um dia ou mais?
            
            '''
            if st.button(f"Programação { num }", type="secondary"):
                '''
                **Obs:** este processamento foi realizado utilizando Python + Google Big Query

                ```python
                sintomas = ['B0011','B0012','B00111']

                for sintoma in sintomas:
                    query_sql = f"""
                        SELECT
                            {sintoma},
                            B005,
                            COUNT (B005) as n_entrevistados
                        FROM
                            `brave-tea-400210.fase_3_tech_challenge.pnad-covid-19`
                        WHERE
                            {sintoma} = 1 AND B005 != 0 AND B005 != 9
                        GROUP BY
                            {sintoma}, B005
                        ORDER BY 
                            B005
                    """

                    query_job = client.query(query_sql)
                    df_results = query_job.to_dataframe()

                    df_results.rename(columns={f'{sintoma}':'sintoma'}, inplace=True)
                    df_results['sintoma'] = sintoma

                    if(sintomas.index(sintoma) == 0):
                        final_df = df_results.copy()
                    else:
                        final_df = pd.concat([final_df,df_results], axis=0)
                ```
                '''

        if st.button(f"Carregar Gráfico { num }", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_7_Numero de internados de acordo com tipo de sintoma.html", 700, 600)
            '''
            
            ## Análise

            Fica claro ao analisar o gráfico que os sintomas de febre e tosse são muito mais frequentes na população da pesquisa, e possuem valores bem próximos de cerca de 3,000 pacientes cada
            entre internados e não internados. Enquanto isso, cerca de 1,400 entrevistados informaram ter sofrido com perda de olfato/paladar, possivelmente um número menor tanto por ser um sintoma mais único
            da COVID-19 como por ser um sintoma mais difícil de ser percebido pelos pacientes.

            Analisando a proporção de pacientes internados por sintoma, o sintoma de febre é também o de maior proporção, com 10.8% dos entrevistados internados, seguido de perda de olfato/paladar com 10.7%
            e por último tosse com 10.3%.

            É possível relacionar estes valores com a questão anterior, em que foi constatado que aproximadamente 2% da população da pesquisa apresentou algum tipo de sintoma COVID-19 nos três meses da análise.
            Significa que pouco mais de 0.02% da população acaba necessitando de internação por complicações de febre, tosse ou perda de olfato/paladar. Este número é um bom indicador para hospitais e autoridades,
            para entender o tamanho da demanda por leitos que pode existir em cada região do país.
            '''
        st.divider()
        '''
        ### Número de entrevistados sintomáticos por setor de trabalho
        '''
        num+=1
        with st.expander(f"Questão { num } (clique para expandir/retrair)", expanded=False):
            '''
            **Quais os setores da economia tiveram proporcionalmente mais entrevistados com sintomas de COVID-19?**

            Como já foi discutido em análises anteriores, em uma pandemia é de extrema importância caracterizar os aspectos socioeconômicos
            da população e entender como isso afeta as infecções. Para isso, esta análise busca identificar os 10 principais setores da economia 
            quanto à taxa de entrevistados sintomáticos, partindo da premissa que, por exemplo, trabalhadores do comércio
            têm mais contato com outras pessoas do que outras atividades e podem ter uma taxa maior.

            Questionário:

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve perda de olfato/paladar? 

            4. Qual é a principal atividade do local ou empresa em que você trabalha? 
            '''

            if st.button(f"Programação { num }", type="secondary"):
                '''
                ### SQL
                ```sql
                with check_sintomas as (
                SELECT
                    C007D,
                    CASE 
                    WHEN B0012 = 1 OR B0011 = 1 OR B00111 = 1 THEN 1
                    ELSE 0
                    END as sintomas,

                    COUNT (CASE 
                    WHEN B0012 = 1 OR B0011 = 1 OR B00111 = 1 THEN 1
                    ELSE 0
                    END) as count_sintomas
                FROM `brave-tea-400210.fase_3_tech_challenge.pnad-covid-19`
                GROUP BY C007D, sintomas
                )

                SELECT
                    C007D,
                    sintomas,
                    count_sintomas,
                    ROUND(SUM(count_sintomas)/SUM(count_sintomas) OVER (PARTITION BY C007D),4) AS proportion_sintoma
                FROM check_sintomas
                WHERE C007D != 0
                GROUP BY
                    C007D, sintomas, count_sintomas
                ORDER BY C007D, count_sintomas DESC
                ```

                ### Python
                ```python
                dict_atividade_trabalho = {'10':'Serviços de entregas', '18':'Administração pública','20':'Saúde',
                           '24':'Serviço doméstico','16':'Escritórios','14':'Instituições financeiras','11':'Hospedagem',
                           '15':'Imobiliárias','13':'Informação e comunicação','22':'Artes e esportes','12':'Serviços de alimentação'}

                dict_sintomas = {'1':'Com sintomas', '0':'Sem sintomas'}


                df_results = df_results.query('sintomas == 1')
                df_results.sort_values(by='proportion_sintoma',ascending=False, inplace=True)
                df_results.reset_index(drop=True, inplace=True)
                df_results = df_results.loc[:10,:]
                df_results['atividade_trabalho'] = df_results['atividade_trabalho'].astype(str).replace(dict_atividade_trabalho)
                df_results['sintomas'] = df_results['sintomas'].astype(str).replace(dict_sintomas)
                df_results['proportion_sintoma'] = df_results['proportion_sintoma'] * 100

                fig = px.bar(df_results, x="proportion_sintoma", y="atividade_trabalho", orientation='h',
                    color_discrete_sequence=px.colors.qualitative.G10, title='Sintomáticos por setor de trabalho<br>PNAD COVID-19',
                    labels=dict(atividade_trabalho='', proportion_sintoma='Proporção de sintomáticos (%)'),
                    height=400, width=700)

                fig.update_layout(yaxis=dict(autorange="reversed"), title_x=0.5)

                fig.show()
                ```
                '''  
        if st.button(f"Carregar Gráfico {num}", type="primary"):
            waitForResourceAvailable("https://cryptohub.com.br/DataFrame/questao_14_Sintomaticos por setor de trabalho.html", 700, 400)

            '''
            ### Análise

            Todos os dez setores com maiores taxas de entrevistados sintomáticos tiveram valor superior a 2%, mas no geral os valores
            ficaram próximos. Em primeiro lugar ficou o setor de entregas e encomendas, com 2.44% dos entrevistados apresentando algum dos
            sintomas mais comuns de COVID-19. 
            
            Os dados confirmam um comportamento muito observado na sociedade brasileira durante a pandemia,
            em que os Correios e empresas de entrega foram requisitados devido ao boom do comércio on-line.
            Assim, possivelmente os trabalhadores deste setor ficaram mais expostos ao vírus devido ao aumento considerável da demanda.

            Da mesma forma, os setores de Saúde e Administração Pública também podem ter sido afetados por este processo, já que atuaram
            atendendo indivíduos que precisaram de auxílio social ou atendimento médico. Neste ponto, os trabalhadores da Saúde
            devem ser tratados com cuidado especial por estarem na linha de frente do combate ao vírus e com mais trabalhadores
            do setor com sintomas de COVID-19, menor a capacidade de atendimento dos hospitais e postos de saúde.
            '''
with tab3:
    '''

    ## Conclusões

    Como apontado anteriormente neste documento, optamos por avaliar três meses de dados da Pesquisa Nacional por Amostra de Domicílios (PNAD – COVID19) de 2020. Nosso intuito com esse trabalho é ponderar e apontar as principais ações que hospitais devem tomar em caso de um novo surto de COVID-19.

    Inicialmente, caracterizamos a população do nosso foco de pesquisa. Avaliámos que a população é predominante composta por adultos, algo saudável do ponto de vista demográfico. Porém, dentre os entrevistados existe uma parcela razoável de pessoas dentro do grupo de risco da doença, principalmente mulheres de faixa etária mais elevadas.

    Outro ponto importante é que a grande maioria dos entrevistados residem em zonas urbanas de grande concentração populacional. Em especial, temos cinco estados de maior risco devido ao alto número de indivíduos residindo em grandes cidades dentro de nossa análise. São eles: Amapá, Amazonas, Distrito Federal, Goiás e Rio de Janeiro.

    Acreditamos que em relação a esses pontos as principais medidas de prevenção e controle que deveriam ser tomadas pelos hospitais são: a criação e promoção de campanhas de conscientização sobre os métodos de proteção contra a covid principalmente voltados as questões de distanciamento social, a não aglomeração, o uso de máscaras com seus cuidados derivados e a correta higienização das mãos. Esses pontos são de extrema importância para a prevenção e controle da doença, especialmente em grandes centros urbanos. Além disso, é importante o planejamento e a organização de um atendimento prioritário para mulheres de idades mais avançadas, pois essas são uma significativa parcela dos pacientes em grupo de risco da pesquisa.

    Em relação aos dados socioeconômicos pudemos notar que, em sua maioria, os entrevistados se encontram nas classes sociais baixa e média, respectivamente. Além disso, os entrevistados com menores taxas de escolaridade apresentam maiores taxas de desocupação, indicando novamente que a parcela mais pobre da população ficou especialmente vulnerável no período da pandemia. Dentre os três meses analisados, a variação do distanciamento social concentrou-se na faixa de pouca ou moderada restrição praticada por parte dos entrevistados durante a pandemia.

    Desse modo, o foco de imunização e conscientização deve ser aplicado com mais afinco principalmente nas populações mais humildes e periféricas por se tratar de uma medida muito mais efetiva dentro da nossa análise.

    Quanto aos sintomas apresentados pelos entrevistados da pesquisa, podemos notar uma clara evolução da doença em todo território nacional. Inicialmente, no mês de setembro, a maior concentração dos casos ocorreu no Centro-Oeste. Em seguida em outubro houve mais casos no sul do país. Finalmente uma migração de casos para a região norte.

    Sintomas como febre, tosse e dor na cabeça foram apresentados por um número expressivo dos entrevistados. Nesse período, os estados mais afetados por tais sintomas foram Goiás, Mato Grosso, Pará, Rondônia e Roraima. Em especial Roraima apresentou a maior proporção de casos na análise dos dados.

    Dentre os sintomas de febre, tosse, perda de olfato/paladar, observamos que a maioria dos entrevistados que apresentou um ou mais desses sintomas não procurou atendimento médico no período analisado. Entretanto, nos meses de outubro e novembro tivemos uma queda na proporção entre entrevistados que procuraram atendimento e os que não procuraram. Isso pode indicar uma maior conscientização dos perigos da doença e dos benefícios dos tratamentos dela.

    Nota-se que os sintomas de febre e tosse foram muito mais frequentes na população da pesquisa, sendo que cerca de aproximadamente 2% dos entrevistados apresentou algum desses sintomas. Isso então se torna um bom indicador para hospitais e autoridades entenderem o tamanho da demanda por leitos que pode existir em cada região do país.

    Em suma, é necessário o esclarecimento da gravidade da covid-19 e dos métodos de prevenção e tratamento da doença para que não ocorra novamente o desenvolvimento de uma pandemia em território nacional. Hospitais em geral devem estar preparados e apresentar leitos suficientes para uma demanda alta de pessoas que em geral podem apresentar sintomas de febre e tosse. É também essencial a reserva de quantidade suficiente de oxigênio hospitalar, substância vital para o tratamento eficaz de pacientes com COVID-19 hospitalizados. 

    Em conclusão, a melhor arma contra uma próxima pandemia é a urgente conscientização geral da população sobre os perigos da covid-19 para a saúde humana. Esse passo é essencial para a prevenção e diminuição dos casos da doença. Ao mesmo tempo, hospitais devem estar preparados armazenado material hospitalar adequado para o tratamento de covid-19, treinando e especializando funcionários para o combate à doença e organizando a aplicação de testes para a detecção da doença o mais rápido possível na suspeita do início de uma nova pandemia.

    '''
with tab4:
    '''

    ## Referências

    1. O IBGE APOIANDO O COMBATE À COVID-19. IBGE, 2023. Disponível em: https://covid19.ibge.gov.br/pnad-covid/. Acessado em: 15, outubro de 2023.

    2. KUNIYOSHI, Andre. Plotly Choropleth — Interactive Sao Paulo Cities Map. Medium, 2021. Disponível em: https://andre-kuniyoshi.medium.com/plotly-choropleth-ainteractive-sao-paulo-cities-map-61089cd7ba2d. Acessado em: 15, outubro de 2023.

    3. BODRUK, Thiago. Brazil GeoJson. Kaggle, 2019. Disponível em: https://www.kaggle.com/datasets/thiagobodruk/brazil-geojson. Acessado em: 15, outubro de 2023.

    4. Mapbox Choropleth Maps in Python. Plotly, 2023. Disponível em: https://plotly.com/python/mapbox-county-choropleth/. Acessado em: 15, outubro de 2023.
    
    '''