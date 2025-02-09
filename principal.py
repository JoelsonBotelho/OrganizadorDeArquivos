import os
import shutil
from datetime import datetime

# Defina a pasta onde estão os arquivos bagunçados
pasta_origem = "/Users/joelsonbotelho/Desktop/Transferências"  # <- Altere para o caminho real

# Defina a pasta de destino onde os arquivos serão organizados
pasta_destino = "/Users/joelsonbotelho/Desktop/Transferências/Transferências_Organizadas"

# Dicionário com tipos de arquivos e suas respectivas pastas
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".raw", ".svg"],
    "Pdfs": [".pdf"],
    "Documentos": [".txt", ".docx", ".odt", ".doc", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".webm", ".mpg", ".mpeg", ".m4v", ".m4a"],
    "Arquivos de Audio": [".mp3", ".wav", ".aiff", ".flac", ".ogg", ".m4a", ".wma", ".ape"],
    "Binários": [".exe", ".dll", ".sys", ".msi", ".cab", ".msi", ".iso", ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".apk", ".ipa", ".ipa", ".dll", ".pdb", ".ilk", ".pdb", ".lib", ".a", ".o", ".so", ".dylib", ".dll", ".exe", ".msi", ".pdb", ".ilk"],
}

# Criar as pastas se não existirem
for pasta in categorias.keys():
    os.makedirs(os.path.join(pasta_destino, pasta), exist_ok=True)

# Percorrer todos os arquivos na pasta de origem
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    # Verificar se é um arquivo (e não uma pasta)
    if os.path.isfile(caminho_arquivo):
        extensao = os.path.splitext(arquivo)[1].lower()  # Pega a extensão do arquivo

        # Descobrir a data de modificação do arquivo
        timestamp = os.path.getmtime(caminho_arquivo)
        data_modificacao = datetime.fromtimestamp(timestamp)
        pasta_data = f"{data_modificacao.year}-{data_modificacao.month:02d}"

        # Verificar em qual categoria ele pertence
        for categoria, extensoes in categorias.items():
            if extensao in extensoes:
                
                caminho_categoria = os.path.join(pasta_destino, categoria, pasta_data)
                
                # Criar a pasta se não existir
                os.makedirs(caminho_categoria, exist_ok=True)

                # Mover o arquivo para a pasta da categoria
                destino = os.path.join(caminho_categoria, arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} -> {categoria}/{pasta_data}")
                break

print("Organização concluída!")
