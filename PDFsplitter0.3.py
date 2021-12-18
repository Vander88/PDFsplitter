#Importar módulos
from tkinter import Tk, Label, Button, Menu, filedialog, messagebox
import os
import webbrowser
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger, pdf


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

def merge():

    pdf_files = filedialog.askopenfilenames(title='Selecione os arquivos PDF que deseja fundir')
    lista = list(pdf_files)
    merge = PdfFileMerger()
    
    #Selecionar pasta de saída
    messagebox.showinfo("Divisor de PDFs", "A seguir: Dê dois cliques na pasta que deseja salvar e aperte OK.")
    output_path = filedialog.askdirectory(title='Selecione a pasta')

    for item in lista:
        if item.endswith('pdf'):
            merge.append(item)
    
    merge.write(f'{output_path}/ResultadoFusao.pdf')
    merge.close()

    #Mensagem de conclusão
    messagebox.showinfo("Fusão de PDFs", "Operação concluída.")

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
    versiontxt = Label(aboutwindow, text="versão beta 0.3", font=("Arial", 7)).grid(column=0, row=4)
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
welcome_txt = Label(window, text="Selecione uma das opções abaixo:").grid(column=0,columnspan=10, row= 0, pady=5, padx=30)

#Um botão escrito selecionar pdf
split_btn = Button(window, text="Separar PDF", command=split, width= 8, height= 2).grid(column= 1, row=1, padx= 30)
merge_btn = Button(window, text="Fundir PDF", command=merge, width= 8, height= 2).grid(column= 3, row=1)

#Menu "Opções>sair"
menubar = Menu(window)
menuoptions = Menu(menubar, tearoff=0)
menuoptions.add_command(label="Fechar", command=window.quit)

#Menu "Sobre> versão, gpl> aba de creditos a mim"
menuAbout = Menu(menubar, tearoff=0)
menuAbout.add_command(label="Sobre", command=about)
menubar.add_cascade(label="Info", menu=menuAbout)
window.config(menu=menubar)


window.mainloop()
