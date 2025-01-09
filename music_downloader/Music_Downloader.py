import tkinter as tk
from tkinter import messagebox
import yt_dlp
import os
import threading
from PIL import Image, ImageTk  # Importar o Pillow para manipulação de imagens

# Função para abrir a pasta de downloads
def abrir_pasta():
    pasta = "C:/Users/lucia/Music/Download_musics/"
    os.startfile(pasta)

# Função para baixar música com nome exibido e barra de progresso
def baixar_musica(url: str, destino: str = "C:/Users/lucia/Music/Download_musics/", progresso_texto=None, progresso_label=None, musicas_baixadas=None):
    """
    Baixa uma música de uma URL e converte para MP3.
    :param url: URL do vídeo (ex.: YouTube)
    :param destino: Pasta onde o arquivo será salvo.
    :param progresso_texto: Listbox para registrar o progresso.
    :param progresso_label: Label para atualizar o contador de músicas.
    :param musicas_baixadas: Contador de músicas baixadas.
    """
    # Função para extrair apenas o nome do arquivo sem o caminho
    def extrair_nome_video_com_extensao(caminho):
        return os.path.basename(caminho)  # Pega o nome do arquivo com a extensão

    # Cria a pasta de destino se não existir
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Variável de controle para garantir que o nome do arquivo seja exibido apenas uma vez
    arquivo_exibido = False
    nome_video = ''  # Adicionando a inicialização de nome_video
    total_musicas = len(entry_urls.get("1.0", tk.END).splitlines())  # Total de músicas a serem bai

    # Funções para capturar o título e atualizar o progresso
    def atualizar_progresso(d):
        nonlocal arquivo_exibido, nome_video, musicas_baixadas, total_musicas

        if 'filename' in d:
            nome_video = extrair_nome_video_com_extensao(d['filename'])  # Extrai o nome do vídeo com a extensão
            if not arquivo_exibido:  # Exibe o nome apenas uma vez
                progresso_texto.insert(tk.END, f"Iniciando download: {nome_video}\n", 'iniciando')  # Usando tag para cor
                arquivo_exibido = True  # Marca que o nome já foi exibido

        if d.get('status') == 'finished':  # Quando o download é concluído
            progresso_texto.insert(tk.END, f"Download de {nome_video} concluído!\n", 'concluido')  # Usando tag para cor
            progresso_texto.insert(tk.END, "\n")  # Adiciona uma linha em branco após a conclusão

            # Atualiza o contador de músicas baixadas
            musicas_baixadas[0] += 1  # Incrementa o contador
            progresso_label.config(text=f"Progresso: {musicas_baixadas[0]}/{total_musicas}")  # Atualiza a label

        # Faz o log descer automaticamente para a última linha
        progresso_texto.see(tk.END)


    opcoes = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{destino}%(title)s.%(ext)s',  # Usando template para nome de arquivo com extensão
        'quiet': True,
        'progress_hooks': [atualizar_progresso],  # Hook para atualizar o progresso
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
    except Exception as e:
        progresso_texto.insert(tk.END, f"Erro ao baixar {url}: {e}\n", 'erro')
        progresso_texto.see(tk.END)  # Faz o log descer mesmo em caso de erro

# Função para baixar múltiplas músicas
def baixar_lista_musicas(urls: list, destino: str, progresso_texto: tk.Text, progresso_label: tk.Label):
    musicas_baixadas = [0]  # Lista para mutabilidade e controle do contador
    for url in urls:
        progresso_texto.insert(tk.END, f"Buscando {url}...\n", 'buscando')
        progresso_texto.see(tk.END)  # Faz o log descer enquanto busca
        baixar_musica(url, destino, progresso_texto, progresso_label, musicas_baixadas)
    progresso_texto.insert(tk.END, "Todos os downloads concluídos!\n", 'finish')
    progresso_texto.insert(tk.END, "\n")  # Adiciona uma linha em branco após todos os downloads

# Função para iniciar o download em uma thread
def iniciar_download(progresso_label):
    lista_urls = entry_urls.get("1.0", tk.END).splitlines()
    if not lista_urls:
        messagebox.showerror("Erro", "Por favor, insira pelo menos uma URL!")
        return
    
    progresso_texto.delete(1.0, tk.END)  # Limpa o progresso
    progresso_label.config(text=f"Progresso: 0/{len(lista_urls)}")  # Reseta o contador para 0/0

    # Passar lista de URLs e também a referência para atualizar o contador
    thread = threading.Thread(target=baixar_lista_musicas, args=(lista_urls, "C:/Users/lucia/Music/Download_musics/", progresso_texto, progresso_label))
    thread.start()

# Função para criar um botão arredondado
def criar_botao(parent, texto, comando):
    return tk.Button(parent, text=texto, font=("Arial", 12, "bold"), fg="white", bg="#4CAF50", 
                     activebackground="#45a049", relief="flat", command=comando, 
                     padx=20, pady=10, bd=0, highlightthickness=0)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Downloader de Músicas")
root.geometry("1024x640")  # Aumentando a janela
root.config(bg="#f9f9f9")

# Frame superior
frame_top = tk.Frame(root, bg="#f9f9f9")
frame_top.pack(pady=20, fill="x")  # Preenche toda a largura

# Título
label_titulo = tk.Label(frame_top, text="Baixe suas músicas", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333")
label_titulo.pack(side="left", padx=10)  # Alinha à esquerda

# Carregar e redimensionar a imagem com o Pillow
img_pasta = Image.open("music_folder.png")  # Certifique-se de que o arquivo existe no mesmo diretório
img_pasta = img_pasta.resize((25, 25))  # Ajuste o tamanho da imagem
img_pasta = ImageTk.PhotoImage(img_pasta)

# Criar o botão com a imagem redimensionada
btn_abrir_pasta = tk.Button(frame_top, image=img_pasta, command=abrir_pasta, bg="#f9f9f9", bd=0, relief="flat")
btn_abrir_pasta.pack(side="right", padx=10)  # Coloca o botão à direita

# Caixa de texto para inserir URLs
label_urls = tk.Label(root, text="Insira as URLs dos vídeos:", font=("Arial", 12), bg="#f9f9f9", fg="#333")
label_urls.pack(pady=5)

entry_urls = tk.Text(root, height=6, width=60, font=("Arial", 12), bd=2, relief="solid", wrap=tk.WORD)
entry_urls.pack(pady=10)

# Botão de iniciar o download
btn_iniciar = criar_botao(root, "Iniciar Download", lambda: iniciar_download(label_progresso))
btn_iniciar.pack(pady=20)

# Frame para progresso
frame_progresso = tk.Frame(root, bg="#f9f9f9")
frame_progresso.pack(pady=5)

# Lista de progresso
label_progresso = tk.Label(frame_progresso, text="Progresso: 0/0", font=("Arial", 12), bg="#f9f9f9", fg="#333")
label_progresso.pack(pady=5)

progresso_texto = tk.Text(frame_progresso, height=15, width=80, font=("Arial", 12), bg="#f0f0f0", fg="#333", wrap=tk.WORD, bd=2, relief="solid")
progresso_texto.pack(pady=5)

# Configuração das tags de cores no log
progresso_texto.tag_config('iniciando', foreground='#4CAF50')  # Verde para iniciar
progresso_texto.tag_config('concluido', foreground='#2196F3')  # Azul para concluído
progresso_texto.tag_config('erro', foreground='#FF5722')  # Vermelho para erro
progresso_texto.tag_config('buscando', foreground='#FF9800')  # Laranja para buscando
progresso_texto.tag_config('finish', foreground='#FFBF00')  # amarelo para concluído

# Inicia a interface
root.mainloop()