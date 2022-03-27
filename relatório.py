class Arquivo:
    def arquivoExiste(nome):
        try:
            arq = open(nome, 'rt', encoding='utf_8')
            arq.close()
        except FileNotFoundError:
            return False
        else:
            return True


    def criarArquivo(nome):
        try:
            arq = open(nome, 'wt+')
            arq.close()
        except:
            print('Houve um erro na criação do arquivo')
        else:
            print(f'Arquivo {nome} criado com sucesso.')
            

class Menu():
    def nomes(nome):
        usuarios = []
        try:
            arq = open(nome)
        except:
            print(f'Erro ao ler o arquivo {nome}')
        else:
            for linha in arq:
                dado = linha.split()
                usuarios.append(dado[0])
            return usuarios


    def mb(nome):
        mbs = []
        try:
            arq = open(nome)
        except:
            print(f'Erro ao ler o arquivo {nome}')
        else:
            for linha in arq:
                números = [float(temp)for temp in linha.split() if temp.isdigit()]
                for n in números:
                    n /= 1000000
                    mbs.append(round(n, 2))
            arq.close()
            return mbs
    

    def TotaleMedia(nome):
        valores = Menu.mb(nome)
        total = round(sum(valores), 2)
        media = total / len(valores)
        return total, round(media, 2)
    

    def porcentagem(nome):
        valores = Menu.mb(nome)
        números = []
        for n in valores:
            números.append(n*100/sum(valores))
        return números


    def menu(arq1, arq2):
        n_pessoas = len(Menu.nomes(arq2))
        p = 0
        try:
            arq = open(arq1, 'w')
        except:
            print(f'Erro ao ler o arquivo {arq1}')
        else:
            arq.write('ACME Inc.        Uso do espaco em disco pelos usuarios\n')
            arq.write('-'*60)
            arq.write('\nNr.  Usuario       Espaco utilizado    '+'%'+' do uso\n')

            for c in range(1, n_pessoas+1):
                arq.write(f'{c:<5}')
                arq.write(f'{Menu.nomes(arq2)[p]:<15}')
                arq.write(f'{Menu.mb(arq2)[p]:^8} MB\t\t')
                arq.write(f'{Menu.porcentagem(arq2)[p]:.2f}%\n')
                p += 1
                
            arq.write('\n')
            arq.write(f'Espaco total ocupado: {Menu.TotaleMedia(arq2)[0]} MB\n')
            arq.write(f'Espaco medio ocupado: {Menu.TotaleMedia(arq2)[1]} MB')
        finally:
            arq.close()