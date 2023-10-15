# Libs

import pandas as pd
import time

# libs gráficas
import matplotlib.pyplot as plt

# Streamlit
import streamlit as st
import streamlit.components.v1 as components

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

# Função para a leitura da base de dados
@st.cache_data
def read_csv_file(file):
    return pd.read_csv(file)

# Titulo de Página
st.title('Análise de dados: explorando dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) COVID19 realizada no ano de 2020')

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

# Carregamento de imagens por cach
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
    ## Explorando dados da Pesquisa Nacional por Amostra de Domicílios COVID19 de 2020

    Links importantes:

    [covid19.ibge.gov.br/pnad-covid](https://covid19.ibge.gov.br/pnad-covid/) - Pesquisa Nacional por Amostra de Domicílios (PNAD COVID19)

    [ibge.gov.br](https://www.ibge.gov.br/) - Instituto Brasileiro de Geografia e Estatística (IBGE)

    Links dos integrantes do projeto:

    [github.com/GabrielPCO](https://github.com/GabrielPCO/tech-challenge-ml) - Github Gabriel Oliveira

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

    O questionário se divide em duas partes, sendo uma direcionada a questões de saúde, especificamente sobre sintomas associados à síndrome gripal e outra, a questões de trabalho. Nas questões de saúde, investiga-se a ocorrência de alguns dos principais sintomas da COVID19 no período de referência da pesquisa, considerando-se todos os moradores do domicílio. Para aqueles que apresentaram algum sintoma, perguntam-se quais as providências tomadas para alivio dos sintomas; se buscaram por atendimento médico devido a esses sintomas; e o tipo de estabelecimento de saúde procurado. Nas questões de trabalho, busca-se classificar a população em idade de trabalhar nas seguintes categorias: ocupados, desocupados e pessoas fora da força de trabalho. Investiga-se, ainda, os seguintes aspectos: ocupação e atividade; afastamento do trabalho e o motivo do afastamento; exercício de trabalho remoto; busca por trabalho; motivo por não ter procurado trabalho; horas semanais efetivamente e habitualmente trabalhadas; assim como o rendimento efetivo e habitual do trabalho. Por fim, visando compor o rendimento domiciliar, pergunta-se se algum morador recebeu outros rendimentos não oriundos do trabalho, tais como: aposentadoria, BPC-LOAS, Bolsa Família, algum auxílio emergencial relacionado à COVID, seguro desemprego, aluguel e outros. Cabe ressaltar que a PNAD COVID19 é uma pesquisa com instrumento dinâmico de coleta das informações; portanto, o questionário está sujeito a alterações ao longo do período de sua aplicação.

    A pesquisa prevê divulgações semanais para alguns indicadores, em nível Brasil, e divulgações mensais para um conjunto mais amplo de indicadores, por Unidades da Federação.

    Os resultados da PNAD COVID19 são pioneiros no sentido de constituírem a primeira divulgação de Estatísticas Experimentais elaboradas pelo IBGE, as quais estão alinhadas com a estratégia de modernização do Instituto e permitem a ampliação das ofertas de informação para atender às necessidades de seus usuários.
    
    
    Neste documento iremos analisar dados da PNAD COVID19 realizada no ano de 2020 a fim de compreender melhor como foi o comportamento da população na época da pandemia.

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

    Para facilitar a manipulação dos dados, decidimos criar uma tabela em banco de dados relacional para armazenar nosso dados.
    
    Escolhemos o sistema gerenciador de banco de dados PostgresSQL.
    '''
    
    img_3 = load_img('Assets/Imagens/postgres01.jpg')
    st.image(img_3)

    st.divider()
    '''

    ## Consolidação dos dados

    Como as variáves que utilizaremos como nossas colunas são equivalente entre os diferentes set de dados, podemos consolidar esses dados em uma mesma tabela.

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

    Como descrito anteriormente, foram obtidos dados de cerca de 193 mil domicílios por mês de pesquisa.
    
    O questionário foi dividido em partes de modo que em nosso trabalho analisaremos alguma das questões em três categorias diferentes, sendo elas: características clínicas dos sintomas, características da população e características econômicas da sociedade. 
    '''
    tab2_01, tab2_02, tab2_03 = st.tabs(["🌡️Sintomas",
                                         "👥População",
                                         "🏘️Sociedade"])
    with tab2_01:
        '''

        ## Evolução dos sintomas de covid-19

        '''
        with st.expander("Análise Sintoma 01", expanded=False):
            '''

            ## Análise Sintoma 01

            Utilizamos os dados de pesquisa dos três meses para avaliar a evolução do sintoma de febre, tosse e dor no peito nos estados brasileiros ao longo do tempo.

            Questões: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve dor no peito?

            Apenas casos nos quais a resposta foi sim para as três perguntas foram adicionados ao gráfico.

            '''
            if st.button("Programação Sintoma 01", type="secondary"):
                '''

                ### SQL
                ```sql
                SELECT mes, uf, b0011, b0012, b0016, COUNT(b0011) AS "febre_tosse_dor_peito"
                FROM dbo.pnad2020_month
                WHERE b0011 = '1' AND b0012 = '1' AND b0016 = '1'
                GROUP BY
                mes, uf, b0011, b0012, b0016
                ORDER BY
                mes DESC, febre_tosse_dor_peito DESC
                ```

                ### Python
                ```python
                fig_2 = px.choropleth_mapbox(casos_de_febre,
                                           geojson = geo_json_br,
                                           locations='uf',
                                           featureidkey = 'id',
                                           color = 'febre_tosse_dor_peito',
                                           animation_frame = 'mes',
                                           hover_name = 'uf',
                                           hover_data = ['febre_tosse_dor_peito'],
                                           title = 'Casos de febre, tosse e dor no peito no Brasil entre Setembro a Novembro de 2020',
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

        if st.button("Carregar Gráfico Sintoma 01", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_mapa_casos_febre.html"
                components.iframe(src, width = 700, height = 800, scrolling = False)
                time.sleep(5)
            '''
            
            ## Análise

            Pelo gráfico, podemos notar que houve uma evolução da quantidade de pessoas que afirmaram ter febre, tosse e dor no peito na semana passada a data da pesquisa. De setembro para outubro podemos ver uma evolução maior do sintoma no norte do país. De outubro para novembro a evolução é mais visível no sul e sudoeste.
            
            '''
        st.divider()
    with tab2_02:
        '''

        ## Dados da população
        '''
        with st.expander("Análise População 01", expanded=False):
            '''

            ### Ditribuição da população da pesquisa por situação

            Plotamos os dados de domicílio da população de entrevistados nos três meses avaliados, separando entre situação urbana e rural.

            Questão: Situação do domicílio

            '''
            if st.button("Programação População 01", type="secondary"):
                '''
                
                ### SQL
                ```sql
                SELECT uf, v1022, COUNT(case v1022 when '1' then 1 else null end) AS "urbana", COUNT(case v1022 when '2' then 1 else null end) AS "rural", COUNT(v1022) AS "total"
                FROM dbo.pnad2020_month
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
        if st.button("Carregar Gráfico População 01", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_distribuicao_populacao.html"
                components.iframe(src, width = 700, height = 700, scrolling = False)
                time.sleep(5)
            '''
            
            ## Análise

            Pelo gráfico, podemos notar que a maioria dos entrevistados está em situação de domicílio urbano, sendo a maioria dos estados de Minas Gerais, São Paulo e Rio de Janeiro.

            '''
        st.divider()
    with tab2_03:
        '''

        ## Dados sociais e econômicos
        '''
        with st.expander("Análise Social 01", expanded=False):
            '''

            ### Número de entrevistados em diferentes faixas de aluguel por estado

            Selecionamos os cinco principais estados por faixa de aluguel dos entrevistados.

            Questão: Número da faixa do aluguel pago

            '''
            if st.button("Programação Social 01", type="secondary"):
                '''
                
                ### SQL
                ```sql
                SELECT uf, f0022, COUNT(f0022) AS "faixa_do_aluguel"
                FROM dbo.pnad2020_month
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

        if st.button("Carregar Gráfico Sociedade 01", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_faixa_aluguel.html"
                components.iframe(src, width = 700, height = 700, scrolling = False)
                time.sleep(2)
            '''
            
            ## Análise

            Pelo gráfico, podemos notar que a maioria dos entrevistados que pagam a maior faixa salarial estão na região sudeste e logo em seguida a região sul e centro-oeste.

            Além disso, a maioria dos entrevistados pagam a faixa de 301-600 reais de aluguel, dentro dos quaia a maioria é de Minas Gerais.
            '''
        st.divider()
with tab3:
    '''

    ## Em Construção...
    '''
with tab4:
    '''

    ## Referências

    1. O IBGE APOIANDO O COMBATE À COVID-19. IBGE, 2023. Disponível em: https://covid19.ibge.gov.br/pnad-covid/. Acessado em: 15, outubro de 2023.

    2. KUNIYOSHI, Andre. Plotly Choropleth — Interactive Sao Paulo Cities Map. Medium, 2021. Disponível em: https://andre-kuniyoshi.medium.com/plotly-choropleth-ainteractive-sao-paulo-cities-map-61089cd7ba2d. Acessado em: 15, outubro de 2023.

    3. BODRUK, Thiago. Brazil GeoJson. Kaggle, 2019. Disponível em: https://www.kaggle.com/datasets/thiagobodruk/brazil-geojson. Acessado em: 15, outubro de 2023.

    4. Mapbox Choropleth Maps in Python. Plotly, 2023. Disponível em: https://plotly.com/python/mapbox-county-choropleth/. Acessado em: 15, outubro de 2023.
    
    '''