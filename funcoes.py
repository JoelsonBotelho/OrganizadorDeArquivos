import os
import shutil
from datetime import datetime

def get_categorias():
    """ Retorna um dicionário com as categorias e suas extensões. """
    return {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".raw", ".svg"],
        "Pdfs": [".pdf"],
        "Documentos": [".txt", ".docx", ".odt", ".doc", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp"],
        "Videos": [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".webm", ".mpg", ".mpeg", ".m4v"],
        "Áudio": [".mp3", ".wav", ".aiff", ".flac", ".ogg", ".m4a", ".wma"],
        "Binários": [".exe", ".dll", ".sys", ".msi", ".cab", ".iso", ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".apk", ".ipa"]
    }

def criar_pastas(pasta_destino, categorias):
    """ Cria as pastas de destino se não existirem. """
    for pasta in categorias.keys():
        os.makedirs(os.path.join(pasta_destino, pasta), exist_ok=True)

def mover_arquivo(caminho_arquivo, arquivo, pasta_destino, categorias):
    """ Move um arquivo para a pasta correta com base na sua categoria e data. """
    extensao = os.path.splitext(arquivo)[1].lower()
    timestamp = os.path.getmtime(caminho_arquivo)
    data_modificacao = datetime.fromtimestamp(timestamp)
    pasta_data = f"{data_modificacao.year}-{data_modificacao.month:02d}"

    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            caminho_categoria = os.path.join(pasta_destino, categoria, pasta_data)
            os.makedirs(caminho_categoria, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(caminho_categoria, arquivo))
            return f"Movido: {arquivo} -> {categoria}/{pasta_data}"
    
    return f"Sem categoria: {arquivo}"

def organizar_arquivos(pasta_origem):
    """ Organiza os arquivos da pasta de origem. """
    if not os.path.exists(pasta_origem):
        return "A pasta de origem não existe."

    pasta_destino = os.path.join(pasta_origem, "Transferências_Organizadas")
    categorias = get_categorias()
    criar_pastas(pasta_destino, categorias)

    logs = []
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            logs.append(mover_arquivo(caminho_arquivo, arquivo, pasta_destino, categorias))

    return logs
