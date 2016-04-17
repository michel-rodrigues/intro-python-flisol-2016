#!/usr/bin/env python3

from tkinter import Tk, Label, Entry, Button
from downloader import download_video

window = Tk() # cria uma janela
window.title('Youtube Downloader') # seta o título da janela
window.geometry('500x200') # seta o tamanho da janela
window.resizable(0,0) # não permite redimensionamento da janela

# label do título do programa
title = Label(window, text='Youtube Downloader', font=('Arial', 25), fg='Blue')
title.pack()

# label da mensagem de execução do programa
msg = Label(window, text='', font=('Arial', 15))

entry_url = Entry(window, width=60, justify='center') # cria uma entrada de texto
entry_url.insert(0, 'Cole aqui a URL') # seta o texto
entry_url.pack() # gerenciador de geometria
entry_url.focus_set() # obtém o foco para a entrada de texto

entry_name_video = Entry(window, width=60, justify='center')
entry_name_video.insert(0, 'Digite um nome para o vídeo')
entry_name_video.pack()

# função para o evento de clique do botão
def click_button():

	# obtém os textos
	url = entry_url.get()
	name_video = entry_name_video.get()

	# se a função retornar 'True'
	if download_video(url, name_video):
		msg['fg'] = 'Green'
		msg['text'] = 'Download feito com sucesso!'
	else:
		msg['fg'] = 'Red'
		msg['text'] = 'Ocorreu alguma falha... :('

# cria um botão
btn = Button(window, text='Download now', width=20, command=click_button)
btn.pack()

# exibe a mensagem
msg.pack()

# loop principal da aplicação
window.mainloop()
