import sys
import os
import subprocess
import pandas as pd

# Pega o caminho absoluto da pasta onde ESTE arquivo está (Pasta do Curso)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho da pasta-mãe
pasta_mae = os.path.abspath(
    os.path.join(
        diretorio_atual, '..'
    )
)

# Configura o caminho para a Wiki
caminho_wiki = os.path.abspath(os.path.join(diretorio_atual, '..', 'Wiki'))
if os.path.exists(caminho_wiki) and caminho_wiki not in sys.path:
    sys.path.append(caminho_wiki)

# Caminho para a pasta das Planilhas
pasta_planilhas = os.path.join(diretorio_atual, 'Planilhas')

try:
    from gerador_graficos import gerar_grafico_horizontal, gerar_grafico_vertical, gerar_grafico_linhas_duplas, gerar_grafico_linhas_multiplas, gerar_grafico_pizza

    # Gráfico 01 sobre "Notificações de Incidentes recebidas pelo CERT.br"
    # nome_planilha = 'g1-aula02-slide20.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha, engine='openpyxl')
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=1,
    #         dados=df_dados,
    #         coluna_x='Totais Incidentes',
    #         coluna_y='Ano',
    #         titulo='Notificações de Incidentes recebidas pelo CERT.br',
    #         nome_arquivo='g1-aula02-slide20.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico 02 sobre "Notificações sobre Equipamentos participando em Ataques DoS"
    # nome_planilha = 'g2-aula02-slide21.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=2,
    #         dados=df_dados,
    #         coluna_x='Total',
    #         coluna_y='Ano',
    #         titulo='Notificações sobre Equipamentos participando em Ataques DoS',
    #         nome_arquivo='g2-aula02-slide21.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico 03 sobre "Categorias de Incidentes Notificados ao CERT.br -- Janeiro a Junho de 2023"
    # nome_planilha = 'aula02-g3-slide22.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=3,
    #         dados=df_dados,
    #         coluna_x='Incidentes',
    #         coluna_y='Categoria',
    #         titulo='Categorias de Incidentes Notificados ao CERT.br -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g3-slide22.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico sobre "Portas que mais sofreram varreduras (scan) ou outros ataques de sucesso -- Janeiro a Junho de 2023"
    # nome_planilha = 'aula02-g4-slide23.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=4,
    #         dados=df_dados,
    #         coluna_x='Varreduras',
    #         coluna_y='Portas',
    #         titulo='Portas que mais sofreram varreduras (scan) ou outros ataques de sucesso -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g4-slide23.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico sobre "Categorias de Tentativa de Fraude -- Janeiro a Junho de 2023"
    # nome_planilha = 'aula02-g5_g6-slide24.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=5,
    #         dados=df_dados,
    #         coluna_x='Malware',
    #         coluna_y='Mês',
    #         titulo='Categorias de Tentativa de Fraude (Malware) -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g5-slide24.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico sobre "Categorias de Tentativa de Fraude -- Janeiro a Junho de 2023"
    # nome_planilha = 'aula02-g5_g6-slide24.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=6,
    #         dados=df_dados,
    #         coluna_x='Phishing',
    #         coluna_y='Mês',
    #         titulo='Categorias de Tentativa de Fraude (Phishing) -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g6-slide24.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico sobre "Top10 Países dos Endereços IP de Origem de Scan e Tentativas de Ataque"
    # nome_planilha = 'aula02-g7-slide25.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=7,
    #         dados=df_dados,
    #         coluna_x='Incidentes',
    #         coluna_y='Países',
    #         titulo='Top10 Países dos Endereços IP de Origem de Scan e Tentativas de Ataque',
    #         nome_arquivo='aula02-g7-slide25.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico sobre "Páginas Falsas (Totais por Categorias) -- Janeiro a Junho de 2023"
    # nome_planilha = 'aula02-g8-slide26.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=8,
    #         dados=df_dados,
    #         coluna_x='Quantidade',
    #         coluna_y='Categorias',
    #         titulo='Páginas Falsas (Totais por Categorias) -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g8-slide26.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico sobre "Páginas Falsas que afetam Organizações no Exterior"
    nome_planilha = 'aula02-g09-slide27.xlsx'
    caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    if os.path.exists(caminho_planilha):
        df_dados = pd.read_excel(caminho_planilha)
    
        gerar_grafico_horizontal(
            numero_grafico=9,
            dados=df_dados,
            coluna_x='Quantidade',
            coluna_y='Categorias',
            titulo='Páginas Falsas que afetam Organizações no Exterior',
            nome_arquivo='aula02-g09-slide27.png',
            caminho_base=diretorio_atual
        )

    # Gráfico sobre "Spams Reportados ao CERT.br por Ano -- 2012 até 2023"
    # dados_grafico11 = {
    #     'Ano': [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
    #     'SpamCap': [26063, 44012, 43770, 65485, 61899, 78679, 180643, 312018, 144267, 250392, 283923, 626312]
    # }

    # gerar_grafico_horizontal (
    #     dados=dados_grafico11,
    #     coluna_x='SpamCap',
    #     coluna_y='Ano',
    #     titulo='Spams Reportados ao CERT.br por Ano -- 2012 até 2023',
    #     nome_arquivo='Spams_Reportados_por_Ano.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Total de Spams Reportados ao CERT.br por Ano -- 2012 até 2023"
    # Gráfico sobre "Total de Spams Reportados ao CERT.br por Ano -- 2012 até 2023"
    # dados_grafico12 = {
    #   'Ano': [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
    #   'Totais': [292692, 674535, 586882, 863459, 806021, 497066, 650292, 791740, 711467, 735262, 993088, 1731842]
    # }
    
    # gerar_grafico_horizontal (
    #     dados=dados_grafico12,
    #     coluna_x='Totais',
    #     coluna_y='Ano',
    #     titulo='Total de Spams Reportados ao CERT.br por Ano -- 2012 até 2023',
    #     nome_arquivo='Total_Spams_Reportados_por_Ano.png',
    #     caminho_base=diretorio_atual
    # )

    # # Gráfico sobre
    # nome_planilha = 'As_20_Portas_TCP_que_mais_sofreram_varreduras_2020.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)

    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)

    #     gerar_grafico_horizontal(
    #         numero_grafico=13,
    #         dados=df_dados,
    #         coluna_x='Totais',
    #         coluna_y='Ano',
    #         titulo='Total de Spams Reportados ao CERT.br por Ano -- 2012 até 2023',
    #         nome_arquivo='Total_Spams_Reportados_por_Ano_2.png',
    #         caminho_base=diretorio_atual
    #     )

except ImportError as e:
    print(f"❌ Erro ao importar a Wiki: {e}")
except Exception as e:
    print(f"⚠️ Erro ao tentar abrir no VS Code: {e}")