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
exist = pag.locateCenterOnScreen(r'images\exist.png', confidence=0.9)
# if (bem is None):
#     continue

def seq_tab(parm):
    for step in range(parm):
        pag.press('tab')
def choice(parm):
    for step in range(parm):
        pag.press('down')
def tab(inf):
    if not inf:
        pag.press('tab')
    else:
        pag.press('tab')
        pag.write(inf)

print(rf.ler_arquivo_texto(nome_arquivo))
pag.click(bem)
for linha in rf.ler_arquivo_texto(nome_arquivo):

    print(linha)

    codigo = linha[0]
    nome = linha[1]
    plaqueta = linha[2]
    simam = linha[3]
    data_inclusao_simam = linha[4]
    detalhamento = 'Fonógrafo'
    propriedade = 'próprio'
    data_aquisicao = linha[5]
    descricao = linha[6]

    pag.write(codigo)
    if not (exist is None):
        tab(nome)
        tab(plaqueta)
        tab(simam)
        tab(data_inclusao_simam)
        tab(detalhamento)
        seq_tab(3)
        tab(propriedade)
        tab(data_aquisicao)
        seq_tab(1)
        choice(1)
        seq_tab(1)
        choice(1)
        seq_tab(1)
        choice(1)
        tab(descricao)

        salvar = pag.locateCenterOnScreen(r'images\salvar.png', confidence=0.9)
        pag.click(salvar)

        novo = pag.locateCenterOnScreen(r'images\novo.png', confidence=0.9)
        pag.click(novo)
    else:
        novo = pag.locateCenterOnScreen(r'images\novo.png', confidence=0.9)
        pag.click(novo)
# pag.hotkey('f2')

pag.alert('Programa finalizado!')

#  pyinstaller --name digitacao --onefile --icon=img.ico --noconsole main.py
# flet pack --name redirect_port --icon=img.ico main.py