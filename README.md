# Organizador de Arquivos

Este é um script Python que organiza arquivos em pastas específicas com base em suas extensões e data de modificação. Ele move arquivos de uma pasta desorganizada para subpastas organizadas por categorias, como Imagens, Documentos, Vídeos, Áudio e mais.

## 📂 Como funciona?
O script percorre todos os arquivos de uma pasta de origem, identifica a extensão de cada arquivo e move-o para uma pasta correspondente dentro da pasta de destino. Os arquivos também são organizados em subpastas baseadas na data de modificação (YYYY-MM). Se a pasta de destino não existir, ela será criada automaticamente.

## 🚀 Requisitos

- Python 3
- Bibliotecas padrão do Python (`os`, `shutil`, `tkinter`, `datetime`)

## 📌 Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.

```bash
git clone https://github.com/JoelsonBotelho/OrganizadorDeArquivos.git
cd OrganizadorDeArquivos
```

2. Instale as dependências (se necessário):

```bash
pip install -r requirements.txt
```

3. Execute o script principal para abrir a interface gráfica:

```bash
python interface.py
```

4. Selecione a pasta que deseja organizar e aguarde a conclusão!

## 📂 Estrutura das Pastas

Os arquivos serão organizados nas seguintes categorias:

- `Imagens`: `.jpg`, `.png`, `.gif`, etc.
- `Pdfs`: `.pdf`
- `Documentos`: `.txt`, `.docx`, `.xlsx`, etc.
- `Videos`: `.mp4`, `.avi`, `.mkv`, etc.
- `Áudio`: `.mp3`, `.wav`, `.flac`, etc.
- `Binários`: `.exe`, `.zip`, `.rar`, etc.

Dentro de cada categoria, os arquivos serão organizados por ano e mês de modificação no formato `YYYY-MM`.

## 🎨 Interface Gráfica
O script agora conta com uma interface gráfica feita com `Tkinter`, permitindo que o usuário selecione a pasta e organize os arquivos com um clique.

## 🛠 Melhorias Futuras
- Adicionar suporte para categorias personalizadas via configuração externa.
- Criar logs detalhados para auditoria.
- Permitir execução automática em segundo plano.

Criado por [Joelson Botelho](https://github.com/JoelsonBotelho) 😊

