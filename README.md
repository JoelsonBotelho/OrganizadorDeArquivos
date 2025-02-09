# Organizador de Arquivos

Este é um script Python simples para organizar arquivos em pastas específicas com base em suas extensões. Ele move arquivos de uma pasta desorganizada para subpastas organizadas por categorias, como Imagens, Documentos, Vídeos, Áudio e mais.

## 📂 Como funciona?
O script percorre todos os arquivos de uma pasta de origem, identifica a extensão de cada arquivo e move-o para uma pasta correspondente dentro da pasta de destino. Se a pasta de destino não existir, ela será criada automaticamente.

## 🚀 Requisitos

- Python 3
- Biblioteca padrão do Python (`os`, `shutil`)

## 📌 Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.

```bash
git clone https://github.com/JoelsonBotelho/OrganizadorDeArquivos.git
cd OrganizadorDeArquivos
```

2. Edite o caminho da pasta de origem e da pasta de destino no código:

```python
pasta_origem = "/caminho/para/sua/pasta"
pasta_destino = "/caminho/para/sua/pasta/organizada"
```

3. Execute o script:

```bash
python organizador.py
```

4. Seus arquivos serão movidos para pastas organizadas automaticamente!

## 📂 Estrutura das Pastas

Os arquivos serão organizados nas seguintes categorias:

- `Imagens`: `.jpg`, `.png`, `.gif`, etc.
- `Pdfs`: `.pdf`
- `Documentos`: `.txt`, `.docx`, `.xlsx`, etc.
- `Videos`: `.mp4`, `.avi`, `.mkv`, etc.
- `Arquivos de Audio`: `.mp3`, `.wav`, `.flac`, etc.
- `Binários`: `.exe`, `.zip`, `.rar`, etc.

Além disso, dentro de cada categoria, os arquivos serão organizados por ano e mês de modificação no formato YYYY-MM.

## 🛠 Melhorias Futuras
- Adicionar suporte para categorias personalizadas via configuração externa.
- Criar uma interface gráfica para facilitar o uso.
- Permitir execução automática em segundo plano.

Criado por [Joelson Botelho](https://github.com/JoelsonBotelho) 😊

