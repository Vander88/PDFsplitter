#Importar módulos
from tkinter import Tk, Label, Button, Menu, filedialog, messagebox
import os
import webbrowser
from PyPDF2 import PdfFileReader, PdfFileWriter


#Funcionamento do programa
def split():
    pdf_file = filedialog.askopenfilename(title='Selecione o PDF')
    
    #Coletar apenas o nome base do arquivo PDF e colocar traço antes do num
    file_base_name = os.path.basename(pdf_file.replace('.pdf', '-'))
    
    #Leitura do PDF
    pdf = PdfFileReader(pdf_file)

    #Selecionar pasta
    messagebox.showinfo("Divisor de PDFs", "A seguir: Dê dois cliques na pasta que deseja salvar e aperte OK.")
    output_path = filedialog.askdirectory(title='Selecione a pasta')

    #Ler todas as páginas contidas no arquivo e separar em arquivos diferentes
    for page_num in range(pdf.numPages):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdf.getPage(page_num))

        #Tratar o nome do arquivo e salvar
        with open(os.path.join(f'{output_path}/{file_base_name}{page_num + 1}.pdf'), 'wb') as f:
            pdfWriter.write(f)
            f.close()

    #Mensagem de conclusão
    messagebox.showinfo("Divisão de PDFs", "Operação concluída.")

    #Apagar o arquivo de origem
    msg_box = messagebox.askyesno('Exclusão', 'Deseja excluir o arquivo de origem?')
    if msg_box == True:
        os.remove(pdf_file)
    
def callback(url):
   webbrowser.open_new_tab(url)

#Seção "Sobre"
def about():
    aboutwindow = Tk()
    aboutwindow.title("Sobre")
    description = Label(aboutwindow, text="Este programa separa cada página de um PDF em arquivos diferentes.").grid(column=0, row=0)
    #logo = Image
    author = Label(aboutwindow, text="Developed by Vander88", font=('Helvetica 8 italic')).grid(column=0, row= 1)
    github_link = Label(aboutwindow, text="Contribua com o projeto pelo Github!", font= ('Helvetica 10 underline'), fg='blue', cursor='hand2')
    github_link.bind('<Button-1>', lambda e: callback(url='https://github.com/Vander88/PDFsplitter'))
    github_link.grid(column=0, row=3)

    aboutwindow.after(5000, lambda: aboutwindow.destroy()) # Destrói a janela após 5 segundos
   
#Criar janela persistente, tamanho da janela e posição
window = Tk()
window.title("PDFsplitter")

app_w = 300
app_h = 100

screen_h = window.winfo_screenheight()
screen_w = window.winfo_screenwidth()

x = (screen_w / 2) - (app_w / 2)
y = (screen_h / 2) - (app_h / 2)

window.geometry(f'{app_w}x{app_h}+{int(x)}+{int(y)}')
window.resizable(False, False)

#Intro
maintxt = Label(window, text="Bem-vindo, clique abaixo para iniciar:").grid(column=0, row=0, padx=20, pady=5)
versiontxt = Label(window, text="versão beta 0.2 ", font=("Arial", 7)).grid(column=0, row=2, pady= 10)

#Um botão escrito selecionar pdf
mainbutton = Button(window, text="Selecionar arquivo", command=split).grid(column=0, row=1, padx=5, pady=5)

#Menu "Opções>sair"
menubar = Menu(window)
menuoptions = Menu(menubar, tearoff=0)
menuoptions.add_command(label="Fechar", command=window.quit)
menubar.add_cascade(label="Opções", menu=menuoptions)

#Menu "Sobre> versão, gpl> aba de creditos a mim"
menuAbout = Menu(menubar, tearoff=0)
menuAbout.add_command(label="Sobre", command=about)
menubar.add_cascade(label="Info", menu=menuAbout)
window.config(menu=menubar)


window.mainloop()


#Verificando se o arquivo changelog já existe
if os.path.isfile('changelog.txt') != True:
    changelog_lines = ('========== Changelog ==========', '', '# Versão 0.2', '- Adição da função de remover o arquivo de origem', '', '# Versão 0.1', '- Primeira versão de testes')
    with open ('changelog.txt', 'x') as archive:
        for lines in changelog_lines:
            archive.write(str(lines) + '\n')
