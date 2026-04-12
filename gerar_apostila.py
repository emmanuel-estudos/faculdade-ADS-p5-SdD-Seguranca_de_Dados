import sys
import os
import subprocess
import shutil

## Informações Específicas para a criação do Arquivo
nome_arquivo = "Apostila-Segurança_de_Dados.md"
titulo_arquivo = "Segurança de Dados"

## Pega o caminho absoluto da pasta onde ESTE arquivo está (Pasta do Curso)
diretorio_do_curso = os.path.dirname(os.path.abspath(__file__))

## Pega o caminho para a pasta dos slides
caminho_slides = os.path.join(diretorio_do_curso, 'Slides')

## Configura o caminho para a Wiki
caminho_wiki = os.path.abspath(os.path.join(diretorio_do_curso, '..', 'Wiki'))

## Carregando a Wiki com as funções
if caminho_wiki not in sys.path:
    sys.path.append(caminho_wiki)

## Criando o arquivo
try:
    from gerador import executar

    executar(
        caminho_pasta=caminho_slides, 
        nome_arquivo_personalizado=nome_arquivo,
        titulo_customizado=titulo_arquivo
    )

    ### Define as rotas: onde ele foi criado e para onde ele deve ir
    origem = os.path.join(caminho_slides, nome_arquivo)
    destino = os.path.join(diretorio_do_curso, nome_arquivo)

    ### Move o arquivo para a raiz se ele foi criado na pasta Slides
    if os.path.exists(origem):
        #### Shutil.move substitui o arquivo se ele já existir no destino
        shutil.move(origem, destino)
        print(f">> Apostila movida para a raiz: {destino}")
    
    ### Tenta abrir o arquivo que agora está na raiz
    if os.path.exists(destino):
        subprocess.run(["code", "-r", destino], shell=True)
    else:
        print(f"⚠️ Erro: O arquivo não foi encontrado em {origem}")

except ImportError as e:
    print(f"❌ Erro ao importar a Wiki: {e}")
except Exception as e:
    print(f"⚠️ Erro ao tentar abrir no VS Code: {e}")