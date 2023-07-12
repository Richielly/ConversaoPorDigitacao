import pyautogui as pag

# pag.hotkey('win','m') //minimizar todas as telas na area de trabalho

patrimonio = pag.locateCenterOnScreen(r'images\patrimonio.png', confidence = 0.9)


pag.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
# pag.doubleClick(chrome) // clicar duas vezes.
pag.PAUSE = 0.7
pag.click(patrimonio)

while True:
    bem = pag.locateCenterOnScreen(r'images\bem.png', confidence=0.9)

    codigo = '99999'
    nome = 'Bem teste'
    plaqueta = '99999'
    simam = '99999'
    data_inclusao_simam = '07072023'
    detalhamento = ''
    propriedade = ''
    data_aquisicao = '07072023'
    descricao = 'teste de automação'

    if (bem is None):
        continue
    else:
        pag.click(bem)
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

        break

salvar = pag.locateCenterOnScreen(r'images\salvar.png', confidence=0.9)
pag.click(salvar)

# pag.hotkey('f2')

# pag.alert('Programa finalizado!')
