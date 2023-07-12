import pyautogui as pag
import read_file
# pag.hotkey('win','m') //minimizar todas as telas na area de trabalho

rf = read_file.Read_file()

patrimonio = pag.locateCenterOnScreen(r'images\patrimonio.png', confidence = 0.9)

pag.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
# pag.doubleClick(chrome) // clicar duas vezes.
pag.PAUSE = 0.7
pag.click(patrimonio)
nome_arquivo = r'C:\Users\Equiplano\PycharmProjects\ConversaoPorDigitacao\dist\Bem.txt'

bem = pag.locateCenterOnScreen(r'images\bem.png', confidence=0.9)

# if (bem is None):
#     continue

print(rf.ler_arquivo_texto(nome_arquivo))
pag.click(bem)
for linha in rf.ler_arquivo_texto(nome_arquivo):

    print(linha)

    codigo = linha[0]
    nome = linha[1]
    plaqueta = linha[2]
    simam = linha[3]
    data_inclusao_simam = linha[4]
    detalhamento = ''
    propriedade = ''
    data_aquisicao = linha[5]
    descricao = linha[6]

    pag.write(codigo)
    pag.press('tab')
    pag.write(nome)
    pag.press('tab')
    pag.write(plaqueta)
    pag.press('tab')
    pag.write(simam)
    pag.press('tab')
    pag.write(data_inclusao_simam)
    pag.press('tab')
    pag.press('down')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('down')
    pag.press('tab')
    pag.write(data_aquisicao)
    pag.press('tab')
    pag.press('down')
    pag.press('tab')
    pag.press('down')
    pag.press('tab')
    pag.press('down')
    pag.press('tab')
    pag.write(descricao)

    salvar = pag.locateCenterOnScreen(r'images\salvar.png', confidence=0.9)
    pag.click(salvar)

    novo = pag.locateCenterOnScreen(r'images\novo.png', confidence=0.9)
    pag.click(novo)


# pag.hotkey('f2')

# pag.alert('Programa finalizado!')


#  pyinstaller --name digitacao --onefile --icon=img.ico --noconsole main.py
# flet pack --name redirect_port --icon=img.ico main.py