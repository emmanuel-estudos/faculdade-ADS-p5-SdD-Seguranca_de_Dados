import sys
import os

# Pega o caminho absoluto da pasta onde ESTE arquivo está (Pasta do Curso)
diretorio_do_curso = os.path.dirname(os.path.abspath(__file__))

# Configura o caminho para a Wiki
caminho_wiki = os.path.abspath(os.path.join(diretorio_do_curso, '..', 'Wiki'))

if caminho_wiki not in sys.path:
    sys.path.append(caminho_wiki)

try:
    from gerador import executar

    executar(
        caminho_pasta=diretorio_do_curso, 
        nome_arquivo_personalizado="Apostila-Segurança_de_Dados.md",
        titulo_customizado="Segurança de Dados"
    )
except ImportError as e:
    print(f"❌ Erro ao importar a Wiki: {e}")