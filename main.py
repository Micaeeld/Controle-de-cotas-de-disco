import relatório as rel

usuarios = 'Relatório/Usuários.txt'
arq = 'Relatório/Relatório.txt'
if not rel.Arquivo.arquivoExiste(arq):
    rel.Arquivo.criarArquivo(arq)

rel.Menu.menu(arq, usuarios)