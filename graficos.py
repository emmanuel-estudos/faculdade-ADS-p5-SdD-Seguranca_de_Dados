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
    from gerador_graficos import gerar_grafico_horizontal, gerar_grafico_vertical, gerar_grafico_linhas_duplas, gerar_grafico_linhas_multiplas, gerar_grafico_pizza

    # Gráfico sobre "Notificações de Incidentes recebidas pelo CERT.br" (aula 02)
    # dados_grafico1 = {
    #     'Ano': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    #     'Total Incidentes': [466029, 352925, 1047031, 722205, 618343, 788674, 637443, 774850, 531039, 457270, 481652, 333905]
    # }

    # gerar_grafico_horizontal(
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

    # gerar_grafico_horizontal (
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

    # gerar_grafico_horizontal (
    #     dados=dados_grafico3,
    #     coluna_x='Quantidade',
    #     coluna_y='Categorias',
    #     titulo='Incidentes Notificados ao CERT.br -- Janeiro/2023 a Junho/2023',
    #     nome_arquivo='Incidentes-Janeiro_Junho_2023.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Portas que mais sofreram varreduras (scan) ou ataques sem sucesso -- Janeiro/2023 a Junho/2023" (aula 02)
    # dados_grafico4 = {
    #     'Porta': ['22/tcp', '25/tcp', 'multi/tcp', '23/tcp', '143/tcp', '23/tcp, 37215/tcp, 60023/tcp', '445/tcp', '1433/tcp', '445/tcp, 1433/tcp', '2375/tcp, 2376/tcp', 'Outros'],
    #     'Quantidade': [36371, 31080, 23737, 16847, 16381, 11413, 10431, 9463, 6119, 4668, 62797]
    # }

    # gerar_grafico_horizontal (
    #     dados=dados_grafico4,
    #     coluna_x='Quantidade',
    #     coluna_y='Porta',
    #     titulo='Portas mais Atacadas -- Janeiro/2023 a Junho/2023',
    #     nome_arquivo='Portas_mais_Atacadas-Janeiro_Junho_2023.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Incidentes de MALWARE Notificados ao CERT.br -- Janeiro até Junho de 2023"
    # dados_grafico5 = {
    #     'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    #     'Malware': [65, 79, 43, 43, 62, 50]
    # }

    # gerar_grafico_horizontal (
    #     dados=dados_grafico5,
    #     coluna_x='Malware',
    #     coluna_y='Mês',
    #     titulo='Incidentes de MALWARE Notificados ao CERT.br -- Janeiro até Junho de 2023',
    #     nome_arquivo='Malwares-Janeiro_Junho_2023.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Incidentes de PHISHING Notificados ao CERT.br -- Janeiro até Junho de 2023"
    # dados_grafico6 = {
    #     'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    #     'Phishing': [2778, 2431, 2944, 2626, 3569, 2764]
    # }

    # gerar_grafico_horizontal (
    #     dados=dados_grafico6,
    #     coluna_x='Phishing',
    #     coluna_y='Mês',
    #     titulo='Incidentes de PHISHING Notificados ao CERT.br -- Janeiro até Junho de 2023',
    #     nome_arquivo='Phishings-Janeiro_Junho_2023.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Top10 Países dos endereços IP de origem de varredura de ataque"
    # dados_grafico7 = {
    #     'País': ['Brasil (BR)', 'China (CN)', 'Estados Unidos (US)', 'Coreia do Sul (KR)', 'Taiwan (TW)', 'Hong Kong (HK)', 'Rússia (RU)', 'Índia (IN)', 'Países Baixos (NL)', 'Vietnã (VN)'],
    #     'Incidentes': [178984, 40966, 31091, 11943, 10751, 5828, 5270, 3719, 3334, 2886]
    # }

    # gerar_grafico_horizontal (
    #     dados=dados_grafico7,
    #     coluna_x='Incidentes',
    #     coluna_y='País',
    #     titulo='Top10 Países com mais endereços IPs de Varredura de Ataque',
    #     nome_arquivo='Top10-paises_IP_ataque.png',
    #     caminho_base=diretorio_atual
    # )

    # Gráfico sobre "Páginas Falsas -- Janeiro até Junho de 2023"
    # dados_grafico8 = {
    #     'Categoria': ['Financeiro', 'Webmail Corporativo', 'Varejo', 'Fidelidade', 'Serviços de Nuvem', 'Governo', 'Pagamento', 'Provedor', 'Redes Sociais', 'Criptomoeda', 'Seguro e Saúde', 'Infra de Nuvem', 'Outras'],
    #     'Quantidade': [3950, 1030, 642, 604, 306, 192, 128, 102, 77, 45, 5, 4, 14]
    # }

    # gerar_grafico_horizontal (
    #     dados=dados_grafico8,
    #     coluna_x='Quantidade',
    #     coluna_y='Categoria',
    #     titulo='Páginas Falsas - Janeiro até Junho de 2023',
    #     nome_arquivo='Paginas_Falsas-Janeiro_Junho_2023.png',
    #     caminho_base=diretorio_atual
    # )

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
    dados_grafico12 = {
      'Ano': [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
      'Totais': [292692, 674535, 586882, 863459, 806021, 497066, 650292, 791740, 711467, 735262, 993088, 1731842]
    }
    
    gerar_grafico_horizontal (
        dados=dados_grafico12,
        coluna_x='Totais',
        coluna_y='Ano',
        titulo='"Total de Spams Reportados ao CERT.br por Ano -- 2012 até 2023"',
        nome_arquivo='Total_Spams_Reportados_por_Ano.png',
        caminho_base=diretorio_atual
    )

except ImportError as e:
    print(f"❌ Erro ao importar a Wiki: {e}")
except Exception as e:
    print(f"⚠️ Erro ao tentar abrir no VS Code: {e}")