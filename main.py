import pyautogui as pag
import read_file
from time import sleep as slp
# pag.hotkey('win','m') //minimizar todas as telas na area de trabalho

rf = read_file.Read_file()

patrimonio = pag.locateCenterOnScreen(r'images\patrimonio.png', confidence = 0.9)

pag.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
# pag.doubleClick(chrome) // clicar duas vezes.
pag.PAUSE = 0.6
pag.click(patrimonio)
nome_arquivo = r'C:\Users\Equiplano\PycharmProjects\ConversaoPorDigitacao\dist\Bem.txt'

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

bem = pag.locateCenterOnScreen(r'images\bem.png', confidence=0.9)
pag.click(bem)
slp(1)

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
    seq_tab(1)
    exist = pag.locateCenterOnScreen(r'images\exist.png', confidence=0.9)
    if (exist is None):
        novo = pag.locateCenterOnScreen(r'images\novo.png', confidence=0.9)
        pag.click(novo)
        sim = pag.locateCenterOnScreen(r'images\btn_sim.png', confidence=0.9)
        pag.click(sim)
    else:
        pag.click(exist)
        pag.write(nome)

        img_plaqueta = pag.locateCenterOnScreen(r'images\plaqueta.png', confidence=0.9)
        pag.click(img_plaqueta)
        pag.write(plaqueta)

        img_codSimAm = pag.locateCenterOnScreen(r'images\codSimAm.png', confidence=0.9)
        pag.click(img_codSimAm)
        pag.write(simam)

        img_dataInclusaoSimAm = pag.locateCenterOnScreen(r'images\dataInclusaoSimAm.png', confidence=0.9)
        pag.click(img_dataInclusaoSimAm)
        pag.write(data_inclusao_simam)

        img_detalhamento = pag.locateCenterOnScreen(r'images\detalhamento.png', confidence=0.9)
        pag.click(img_detalhamento)
        slp(1)
        pag.write(detalhamento)

        img_propriedade = pag.locateCenterOnScreen(r'images\propriedade.png', confidence=0.9)
        pag.click(img_propriedade)
        pag.write(propriedade)

        img_dataAquisicao = pag.locateCenterOnScreen(r'images\dataAquisicao.png', confidence=0.9)
        pag.click(img_dataAquisicao)
        pag.write(data_aquisicao)

        img_grupo = pag.locateCenterOnScreen(r'images\grupo.png', confidence=0.9)
        pag.click(img_grupo)
        choice(1)

        img_subGrupo = pag.locateCenterOnScreen(r'images\subGrupo.png', confidence=0.9)
        pag.click(img_subGrupo)
        choice(1)

        img_classe = pag.locateCenterOnScreen(r'images\classe.png', confidence=0.9)
        pag.click(img_classe)
        choice(1)

        img_descricao = pag.locateCenterOnScreen(r'images\descricao.png', confidence=0.9)
        pag.click(img_descricao)
        pag.write(descricao)

        salvar = pag.locateCenterOnScreen(r'images\salvar.png', confidence=0.9)
        pag.click(salvar)
        pag.screenshot(f'images\{codigo}.png')
        novo = pag.locateCenterOnScreen(r'images\novo.png', confidence=0.9)
        pag.click(novo)

# pag.hotkey('f2')

pag.alert('Programa finalizado!')

#  pyinstaller --name digitacao --onefile --icon=img.ico --noconsole main.py
# flet pack --name redirect_port --icon=img.ico main.py