import os
import win32print
import win32api
caminho = os.getcwd()
print(caminho)

lista_impressoras = win32print.EnumPrinters(2)
#(8388608, 'Xerox WorkCentre 3550 PS,Xerox WorkCentre 3550 PS,', 'Xerox WorkCentre 3550 PS', '')     
#(8388608, 'OneNote for Windows 10,Microsoft Software Printer Driver,', 'OneNote for Windows 10', '')
#(8388608, 'PDFCreator,PDFCreator,', 'PDFCreator', 'eDoc Printer')
#(8388608, 'Microsoft XPS Document Writer,Microsoft XPS Document Writer v4,', 'Microsoft XPS Document Writer', '')
#(8388608, 'Microsoft Print to PDF,Microsoft Print To PDF,', 'Microsoft Print to PDF', '')
#(8388608, 'IMP_TIMBRADO,Xerox WorkCentre 5945,', 'IMP_TIMBRADO', '')
#(8388608, 'IMP_CONTROLADORIA,Brother MFC-L6702DW Printer,', 'IMP_CONTROLADORIA', '')
#(8388608, 'IMP_COBRANÇA,Xerox WorkCentre 3550 PS,', 'IMP_COBRANÇA', '')
#(8388608, 'IMP_CENTRAL,Xerox WorkCentre 5945,', 'IMP_CENTRAL', '')
#(8388608, 'Impressora de imagem do PaperPort,Nuance Image Printer Driver,', 'Impressora de imagem do PaperPort', '')
#(8388608, 'Fax,Microsoft Shared Fax Driver,', 'Fax', '')
#(8388608, 'AnyDesk Printer,AnyDesk v4 Printer Driver,', 'AnyDesk Printer', '')

impressora = lista_impressoras[6]

win32print.SetDefaultPrinter(impressora[2])
caminho1=r'C:\Users\Compras\Documents\GitHub\patrimonio'

win32api.ShellExecute(0, "open", 'estoque-zero.xlsx', None, caminho1, 0 )
    
