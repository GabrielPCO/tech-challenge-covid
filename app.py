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

    Nessa seção, iremos analisar os dados colhidos na PNAD COVID19. Para isso, separamos três tópicos de interesse para nossa análise: sintomas, população e sociedade.

    Em cada tópico serão realizadas análises sobre o tema abordado, com o objetivo de descrever o comportamento e contexto da população brasileira durante a pandemia.
    
    Os dados do PNAD abrangeram cerca de 193 mil domicílios por mês de pesquisa e um total de mais de 1 milhão de registros na base de dados abrangendo três mese.
    
    A análise será separada em três categorias diferentes, sendo elas: características clínicas dos sintomas, características da população e características econômicas da sociedade. 
    '''
    tab2_01, tab2_02, tab2_03 = st.tabs(["🌎População",
                                         "🏡Sociedade",
                                         "🌡️Sintomas"])
    
    with tab2_01:
        '''

        ## Caracterizando a população

        ### Ditribuição da população da pesquisa por situação de moradia
        '''
        with st.expander("Questão 01 (clique para expandir/retrair)", expanded=False):
            '''        
            **Como está distribuida a população da pesquisa em questão de situação de domicílio?**

            Plotamos os dados de domicílio da população de entrevistados nos três meses avaliados, separando entre situação urbana e rural.

            Com esses dados, podemos avaliar se a questão do domicílio pode ter alguma conexão com a presença da covid-19.

            Questionário: Situação do domicílio

            '''
            if st.button("Programação 01 - população", type="secondary"):
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
        if st.button("Carregar Gráfico 01 - população", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_distribuicao_populacao.html"
                components.iframe(src, width = 700, height = 700, scrolling = False)
                time.sleep(5)
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
        '''### Ditribuição da população por região de moradia'''
        with st.expander("Questão 02 (clique para expandir/retrair)", expanded=False):
            '''
            **Como está distribuida a população da pesquisa nas UFs do Brasil quanto à região de moradia?**

            Com o objetivo de analisar mais a fundo a questão da distribuição da população no território brasileiro, o gráfico abaixo permite identificar os estados em que a população
            está altamente concentrada em polos político-econômicos como Capitais e Regiões Metropolitanas.

            Questionário: 
            
            1. Tipo de área (capital, região metropolitana, etc.)

            2. UF

            '''
            if st.button("Programação 02 - população", type="secondary"):
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
        if st.button("Carregar Gráfico 02 - população", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "grafico 5 - populacao"
                components.iframe(src, width = 700, height = 700, scrolling = False)
                time.sleep(5)
            
            '''
            ## Análise

            Novamente, os dados mostram que o Distrito Federal e o Rio de Janeiro são duas UFs com população altamente concentrada em grandes cidades. Além deles, Goiás, Amazonas e Amapá também tiveram
            mais da metade de seus entrevistados informando que moram em Capitais ou Regiões Metropolitanas.

            Estas 5 UFs podem estar mais suscetíveis à ocorrência de grandes picos de contaminação, o que consequentemente podem gerar uma grande sobrecarga nos sitemas de saúde público e privado. Por isso, medidas de
            educação ou de redução de contato social entre os habitantes devem ser ainda mais úteis nesse contexto.
            '''

    with tab2_02:
        '''

        ## Dados socioeconômicos

        ### Distribuição da população quanto ao valor de aluguel pago
        '''
        with st.expander("Questão 03 (clique para expandir/retrair)", expanded=False):
            '''         
            **Como estava a distribuição dos entrevistados pelo Brasil de acordo com diferentes faixas de aluguel?**

            Selecionamos os cinco principais estados por faixa de aluguel dos entrevistados. Assim, teremos uma noção da distribuição dos entrevistados da PNAD de 2020 de acordo com o local onde vivem, se em regiões mais populares ou mais nobres.

            Questionário: Número da faixa do aluguel pago

            '''
            if st.button("Programação 03", type="secondary"):
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

        if st.button("Carregar Gráfico 03", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_faixa_aluguel.html"
                components.iframe(src, width = 700, height = 700, scrolling = False)
                time.sleep(2)
            '''
            
            ## Análise

            Pelo gráfico, pode-se notar que a maioria dos entrevistados que pagam a maior faixa salarial estão na região Sudeste e Sul do país. 
            Santa Catarina é um estado a se destacar, pois mesmo com uma população pequena, teve grande número de entrevistados que pagam a faixa de aluguel mais alta,
            sugerindo que se trata de uma UF mais desenvolvida socioeconomicamente e com custo de vida elevado.

            Além disso, no geral a maioria dos entrevistados pagam de R$301 a R$600 reais de aluguel, entre os quais a maioria é de Minas Gerais. A faixa de valor mais baixa, de R$101 a R$300, possui 4 estados
            do Nordeste entre as UFs com maior número de entrevistados, ou seja, são estados com população mais carente e que dependem ainda mais da infraestrutura de saúda pública.
            '''
        st.divider()
    
    with tab2_03:
        '''

        ## Aspectos clínicos da pandemia COVID-19

        ### Distribuição dos entrevistados pelo Brasil que apresentaram sintomas de covid-19

        '''
        with st.expander("Questão 04 (clique para expandir/retrair)", expanded=False):
            '''
            **Como estão distribuidos os entrevistados que apresentaram sintomas de COVID-19?**

            Utilizamos os dados de pesquisa dos três meses para avaliar a evolução do sintoma de febre, tosse e dor na cabeça nos estados brasileiros ao longo do tempo. Esses sintomas podem indicar a presença da covid-19 no entrevistado em questão.

            Questionário: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve dor na cabeça?

            Apenas casos nos quais a resposta foi sim para as três perguntas foram adicionados ao gráfico.

            '''
            if st.button("Programação 04", type="secondary"):
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

        if st.button("Carregar Gráfico 04", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_mapa_casos_febre.html"
                components.iframe(src, width = 700, height = 800, scrolling = False)
                time.sleep(5)
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
        with st.expander("Questão 05 (clique para expandir/retrair)", expanded=False):
            '''
            **Qual a proporção de casos de covid-19 em relação ao numero total de entrevistados dos cinco estados mais afetados?**

            Utilizamos os dados de pesquisa dos três meses para avaliar a proporção de casos de covid-19 em relação a quantidade de entrevistados nos cinco estados mais afetados.

            Questionário: 

            1. Na semana passada teve febre?

            2. Na semana passada teve tosse?

            3. Na semana passada teve dor na cabeça?

            '''
            if st.button("Programação 05", type="secondary"):
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

        if st.button("Carregar Gráfico 05", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "https://cryptohub.com.br/DataFrame/br_porcentagem_casos.html"
                components.iframe(src, width = 700, height = 800, scrolling = False)
                time.sleep(2)
            '''
            
            ## Análise

            Pelo gráfico, podemos perceber que o estado com maior proporção de casos de covid-19 por número de entrevistados foi Roraima.

            Pela proporcionalidade, podemos notar que esses cinco estados foram os mais afetados pela covid-19 nos meses de setembro, outubro e novembro de 2020.
            
            '''
        st.divider()
        '''
        ### Procura de atendimento médico por entrevistados sintomáticos
        '''
        with st.expander("Questão 06 (clique para expandir/retrair)", expanded=False):
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
            if st.button("Programação 06", type="secondary"):
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
        if st.button("Carregar Gráfico 06", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "grafico_atendimento"
                components.iframe(src, width = 700, height = 800, scrolling = False)
                time.sleep(2)
            '''
            
            ## Análise

            Percebe-se que de Setembro/2020 até Novembro/2020 houve uma pequena variação no número de entrevistados que tiveram algum dos sintomas clássicos da COVID-19 (febre, tosse e perda de olfato/paladar).

            Em setembro cerca de 7,500 entrevistados tiveram algum sintoma, já em novembro esse valor foi de aproximadamente 7,000 entrevistados. Isso representa que, aproximadamente 2% da população de entrevistada
            apresentou algum dos sintomas mais comuns de COVID-19.

            Proporcionalmente, mais entrevistados procuraram atendimento médico nos meses de outubro e novembro do que em setembro. 
            
            Uma hipótese, com viés otimista, é que as pessoas estão mais conscientes dos perigos da doença e por isso estão buscando tratamento.
            
            Outra alternativa, com olhar mais pessimista, é que os casos de COVID-19 ocorridos em outubro e novembro foram mais graves e demandaram
            mais estrutura hospitalar.
            '''
        st.divider()
        '''
        ### Número de entrevistados internados por tipo de sintoma
        '''
        with st.expander("Questão 07 (clique para expandir/retrair)", expanded=False):
            '''
            **Entre os sintomais mais sintomas frequentes de COVID-19, qual está mais relacionado com internações?**

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
            if st.button("Programação 07", type="secondary"):
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

        if st.button("Carregar Gráfico 07", type="primary"):
            with st.spinner("Carregando o gráfico. Aguarde..."):
                src = "grafico_internacao"
                components.iframe(src, width = 700, height = 800, scrolling = False)
                time.sleep(2)
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