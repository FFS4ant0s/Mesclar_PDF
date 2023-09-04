import PyPDF2
import os

merger = PyPDF2.PdfMerger()  # Mesclador de arquivos

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort() # Ordenando arquivos

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")


merger.write("PDF_final.pdf")