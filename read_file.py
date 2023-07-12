
class Read_file:
    def ler_arquivo_texto(self, nome_arquivo):
        linhas = []
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                valores = linha.split('|')
                linhas.append(valores)
        return linhas


