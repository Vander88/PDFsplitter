#Importar módulos
from tkinter import Tk, Label, Button, Menu, filedialog, messagebox
import os
import webbrowser
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


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


main = int(input("Selecione uma das opções abaixo:\n(1)Separar PDF\n(2)Fundir PDFs\n:"))
if main == 1:
    split()
elif main == 2:
    merge()
else:
    print('Inválido.')
    
