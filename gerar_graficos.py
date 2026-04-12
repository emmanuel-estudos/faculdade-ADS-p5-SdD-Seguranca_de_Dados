import sys
import os
import subprocess
import pandas as pd

NUMERO_GRAFICO = 0
numero_grafico = NUMERO_GRAFICO

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
    from gerador_graficos import gerar_grafico_horizontal, gerar_grafico_barras_verticais, gerar_grafico_linhas_duplas, gerar_grafico_linhas_multiplas, gerar_grafico_pizza, gerar_grafico_multiplas_barras_horizontais

    # Gráfico 01 sobre "Notificações de Incidentes recebidas pelo CERT.br"
    numero_grafico = numero_grafico + 1
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
    numero_grafico = numero_grafico + 1
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
    numero_grafico = numero_grafico + 1
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

    # Gráfico 04 sobre "Portas que mais sofreram varreduras (scan) ou outros ataques de sucesso -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
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

    # Gráfico 05 sobre "Categorias de Tentativa de Fraude -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
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

    # Gráfico 06 sobre "Categorias de Tentativa de Fraude -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
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

    # Gráfico 07 sobre "Top10 Países dos Endereços IP de Origem de Scan e Tentativas de Ataque"
    numero_grafico = numero_grafico + 1
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

    # Gráfico 08 sobre "Páginas Falsas (Totais por Categorias) -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
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

    # Gráfico 09 sobre "Páginas Falsas que afetam Organizações no Exterior"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g09-slide27.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=9,
    #         dados=df_dados,
    #         coluna_x='Quantidade',
    #         coluna_y='Categorias',
    #         titulo='Páginas Falsas que afetam Organizações no Exterior',
    #         nome_arquivo='aula02-g09-slide27.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico 10 sobre "Países de Alocação de Endereços IP onde as Páginas Falsas estão Hospedados -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g10-slide28.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=10,
    #         dados=df_dados,
    #         coluna_x='Quantidade',
    #         coluna_y='País',
    #         titulo='Países de Alocação de Endereços IP onde as Páginas Falsas estão Hospedados -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g10-slide28.png',
    #         caminho_base=diretorio_atual
    #     )
    
    # Gráfico 11 sobre "Sistemas Autônomos (AS) dos Endereços IP onde as Páginas estão Hospedadas -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g11-slide29.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    # if os.path.exists(caminho_planilha):
    #     df_dados = pd.read_excel(caminho_planilha)
    
    #     gerar_grafico_horizontal(
    #         numero_grafico=numero_grafico,
    #         dados=df_dados,
    #         coluna_x='Quantidade',
    #         coluna_y='Sistema',
    #         titulo='Sistemas Autônomos (AS) dos Endereços IP onde as Páginas estão Hospedadas -- Janeiro a Junho de 2023',
    #         nome_arquivo='aula02-g11-slide29.png',
    #         caminho_base=diretorio_atual
    #     )

    # Gráfico 12 sobre "Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - TOTAL"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g12_g13_g14-slide30.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     coluna_x='Porcentagem_Total',
    #     coluna_y='Categorias',
    #     titulo='Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - TOTAL',
    #     nome_arquivo='aula02-g12-slide30.png',
    #     caminho_base=diretorio_atual,
    #     porcentagem=True,
    #     quantidade_total=2132
    # )

    # Gráfico 13 sobre "Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - BRASIL"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g12_g13_g14-slide30.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     coluna_x='Porcentagem_Brasil',
    #     coluna_y='Categorias',
    #     titulo='Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - BRASIL',
    #     nome_arquivo='aula02-g13-slide30.png',
    #     caminho_base=diretorio_atual,
    #     porcentagem=True,
    #     quantidade_total=2014
    # )

    # Gráfico 14 sobre "Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - EXTERIOR"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g12_g13_g14-slide30.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     coluna_x='Porcentagem_Exterior',
    #     coluna_y='Categorias',
    #     titulo='Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - EXTERIOR',
    #     nome_arquivo='aula02-g14-slide30.png',
    #     caminho_base=diretorio_atual,
    #     porcentagem=True,
    #     quantidade_total=118
    # )

    # Gráfico 15 sobre "Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - TOTAL -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g15_g16_g17-slide30.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     coluna_x='Porcentagem_Total',
    #     coluna_y='Categoria',
    #     titulo='Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - TOTAL -- Janeiro a Junho de 2023',
    #     nome_arquivo='aula02-g15-slide30.png',
    #     caminho_base=diretorio_atual,
    #     porcentagem=True,
    #     quantidade_total=745
    # )
    
    # Gráfico 16 sobre "Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - BRASIL -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g15_g16_g17-slide30.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     coluna_x='Porcentagem_Brasil',
    #     coluna_y='Categoria',
    #     titulo='Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - BRASIL -- Janeiro a Junho de 2023',
    #     nome_arquivo='aula02-g16-slide30.png',
    #     caminho_base=diretorio_atual,
    #     porcentagem=True,
    #     quantidade_total=739
    # )

    # Gráfico 17 sobre "Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - EXTERIOR -- Janeiro a Junho de 2023"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g15_g16_g17-slide30.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     coluna_x='Porcentagem_Exterior',
    #     coluna_y='Categoria',
    #     titulo='Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - EXTERIOR -- Janeiro a Junho de 2023',
    #     nome_arquivo='aula02-g17-slide30.png',
    #     caminho_base=diretorio_atual,
    #     porcentagem=True,
    #     quantidade_total=6
    # )

    # arrumando a contagem de gráficos, porque 2 foram pulados
    numero_grafico = numero_grafico + 2

    # Gráfico 20 sobre "Spams Reportados ao CERT.br por Ano -- 2012 a 2023"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g20-slide34.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_multiplas_barras_horizontais(
    #     numero_grafico=numero_grafico,
    #     dados=df_dados,
    #     colunas_x=['SpamCop', 'Total'],
    #     coluna_y='Ano',
    #     titulo='Spams Reportados ao CERT.br por Ano -- 2012 a 2023',
    #     nome_arquivo='aula02-g20-slide34.png',
    #     caminho_base=diretorio_atual,
    # )

    # Gráfico 21 sobre "Incidentes Reportados por Tipo -- Janeiro a Dezembro de 2020"
    numero_grafico = numero_grafico + 1
    # nome_planilha = 'aula02-g21-slide35.xlsx'
    # caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    # df_dados = pd.read_excel(caminho_planilha)
    
    # gerar_grafico_pizza(
    #    numero_grafico=numero_grafico,
    #    dados=df_dados,
    #    coluna_x='Porcentagem',
    #    coluna_y='Tipos de Ataque',
    #    titulo='Incidentes Reportados por Tipo -- Janeiro a Dezembro de 2020',
    #    nome_arquivo='aula02-g21-slide35.png',
    #    caminho_base=diretorio_atual
    # )

    # Gráfico 22 sobre "Top10 de ASNs Origem de Ataques -- 2020"
    numero_grafico = numero_grafico + 1
    nome_planilha = 'aula02-g22-slide38.xlsx'
    caminho_planilha = os.path.join(pasta_planilhas, nome_planilha)
    
    gerar_grafico_barras_verticais(
        numero_grafico=numero_grafico,
        dados=caminho_planilha,
        coluna_x='ASN',
        coluna_y='Incidentes',
        titulo='Top10 de ASNs Origem de Ataques -- 2020',
        nome_arquivo='aula02-g22-slide38.png',
        caminho_base=diretorio_atual,
        mostrar_percentual=True
    )

except FileNotFoundError:
    print(f"❌ Erro: A planilha não foi encontrada.")
    print(f"   Caminho tentado: {caminho_planilha}")
except ImportError as e:
    print(f"❌ Erro ao importar a Wiki: {e}")
except Exception as e:
    print(f"⚠️ Ocorreu um erro inesperado: {e}")