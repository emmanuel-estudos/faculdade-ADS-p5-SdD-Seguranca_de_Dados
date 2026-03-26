import sys
import os
import subprocess

# Pega o caminho absoluto da pasta onde ESTE arquivo está (Pasta do Curso)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Configura o caminho para a Wiki
caminho_wiki = os.path.abspath(os.path.join(diretorio_atual, '..', 'Wiki'))

if caminho_wiki not in sys.path:
    sys.path.append(caminho_wiki)

try:
    from gerador_graficos import gerar_grafico_h

    # Gráfico sobre "Notificações de Incidentes recebidas pelo CERT.br" (aula 02)
    # dados_grafico1 = {
    #     'Ano': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    #     'Total Incidentes': [466029, 352925, 1047031, 722205, 618343, 788674, 637443, 774850, 531039, 457270, 481652, 333905]
    # }

    # gerar_grafico_h(
    #     dados=dados_grafico1,
    #     coluna_x='Total Incidentes',
    #     coluna_y='Ano',
    #     titulo='Notificações de Incidentes recebidos pelo CERT.br',
    #     nome_arquivo='Grafico_de_Incidentes.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Notificações sobre Equipamentos particiando em ataques DoS" (aula 02)
    # dados_grafico2 = {
    #     'Ano': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    #     'Equipamentos': [309, 1030, 223935, 25360, 60432, 220188, 158407, 301308, 68200, 72730, 70517, 39821]
    # }

    # gerar_grafico_h (
    #     dados=dados_grafico2,
    #     coluna_x='Equipamentos',
    #     coluna_y='Ano',
    #     titulo='Notificações sobre Equipamentos particiando em ataques DoS',
    #     nome_arquivo='Equipamentos_em_ataques_DoS.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Incidentes Notificados ao CERT.br -- Janeiro/2023 a Junho/2023" (aula 02)
    # dados_grafico3 = {
    #     'Categorias': ['Scan', 'DoS', 'Fraude', 'Web', 'Invasão', 'Outros'],
    #     'Quantidade': [229307, 39821, 17454, 4163, 658, 42502]
    # }

    # gerar_grafico_h (
    #     dados=dados_grafico3,
    #     coluna_x='Quantidade',
    #     coluna_y='Categorias',
    #     titulo='Incidentes Notificados ao CERT.br -- Janeiro/2023 a Junho/2023',
    #     nome_arquivo='Incidentes-Janeiro_Junho_2023.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Portas que mais sofreram varreduras (scan) ou ataques sem sucesso -- Janeiro/2023 a Junho/2023" (aula 02)
    dados_grafico4 = {
        'Porta': ['22/tcp', '25/tcp', 'multi/tcp', '23/tcp', '143/tcp', '23/tcp, 37215/tcp, 60023/tcp', '445/tcp', '1433/tcp', '445/tcp, 1433/tcp', '2375/tcp, 2376/tcp', 'Outros'],
        'Quantidade': [36371, 31080, 23737, 16847, 16381, 11413, 10431, 9463, 6119, 4668, 62797]
    }

    gerar_grafico_h (
        dados=dados_grafico4,
        coluna_x='Quantidade',
        coluna_y='Porta',
        titulo='Portas mais Atacadas -- Janeiro/2023 a Junho/2023',
        nome_arquivo='Portas_mais_Atacadas-Janeiro_Junho_2023.png',
        caminho_base=diretorio_atual
    )

except ImportError as e:
    print(f"❌ Erro ao importar a Wiki: {e}")
except Exception as e:
    print(f"⚠️ Erro ao tentar abrir no VS Code: {e}")