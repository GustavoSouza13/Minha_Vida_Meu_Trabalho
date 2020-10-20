import os
import time
import random

def status(ListaInfo,cargoTrabalho):
    ListaCampos = ["vida:","fome:","sede:","dinheiro:","exp:"]
    arquivo = "arq01.txt"
    ListaPosicao = procurarCampo(ListaCampos,arquivo)
    
    divisao1 = "| |"
    divisao2 = "| |"
    divisao3 = "|"
    if ListaInfo[ListaPosicao[0]] < 100:
        divisao1 = " " + divisao1
    if ListaInfo[ListaPosicao[0]] < 10:
        divisao1 = " " + divisao1
        
    if ListaInfo[ListaPosicao[1]] < 100:
        divisao2 = " " + divisao2
    if ListaInfo[ListaPosicao[1]] < 10:
        divisao2 = " " + divisao2

    if ListaInfo[ListaPosicao[2]] < 100:
        divisao3 = " " + divisao3
    if ListaInfo[ListaPosicao[2]] < 10:
        divisao3 = " " + divisao3
    print("|-----------| |-----------| |-----------|")
    print("| Vida:",ListaInfo[ListaPosicao[0]],divisao1,"Fome:",ListaInfo[ListaPosicao[1]],divisao2,"Sede:",ListaInfo[ListaPosicao[2]],divisao3)
    print("|-----------| |-----------| |-----------|\n")

    print("Cargo:",cargoTrabalho,"\n")
    print("Dinheiro:",ListaInfo[ListaPosicao[3]],"\n")
    print("Exp:",ListaInfo[ListaPosicao[4]],"\n")

def trabalhar(ListaInfo,cargoTrabalho): 
    trab = "sim"

    while trab.lower() == "sim" or trab.lower() == "s":
        ListaCampos = ["vida:","fome:","sede:","dinheiro:","exp:"]
        arquivo = "arq01.txt"
        ListaPosicao = procurarCampo(ListaCampos,arquivo)
        ListaTrabalhando = ["trabalhandovez:","trabalhandodinheiro:","trabalhandoexp:"]
        ListaTrabalhando = procurarCampo(ListaTrabalhando,arquivo)

        tarefa = tarefas(cargoTrabalho)

        if ListaInfo[ListaPosicao[0]] > 0 and ListaInfo[ListaPosicao[1]] > 0 and ListaInfo[ListaPosicao[2]] > 0:
            print("Cargo atual:",cargoTrabalho,"\n")
            for i in range(0,ListaInfo[ListaTrabalhando[0]],1):
                print(tarefa)
                time.sleep(1)

            num = random.randrange(0,101)

            # Bonus para cada vez que trabalha.

            if num >= 70:
                num = random.randrange(0,ListaInfo[ListaTrabalhando[0]])
            else:
                num = 0

            # Altera os dados de vida, fome, sede, dinheiro e exp. (No programa)

            ListaInfo[ListaPosicao[3]] += ListaInfo[ListaTrabalhando[1]] + num
            ListaInfo[ListaPosicao[4]] += ListaInfo[ListaTrabalhando[2]] + num
            
            ListaInfo[ListaPosicao[0]] -= random.randrange(2,4)
            ListaInfo[ListaPosicao[1]] -= random.randrange(2,4)
            ListaInfo[ListaPosicao[2]] -= random.randrange(2,4)

            # Executa pensamentos que pode ter e possue duas respostas, dependendo pode dar um bônus ou prejuizo.

            num = random.randrange(0,101)

            if num >= 65:
                ListaPerguntas, ListaRespostas, ListaFrases, ListaBoosts, ListaCamposBoost = perguntas(cargoTrabalho,ListaCampos)

                num1 = random.randrange(0,len(ListaPerguntas))
                num2 = num1 * 2

                print("\nPensamento:",ListaPerguntas[num1],"\n")
                print("Respostas:\n")

                contador = 1
                for i in range(0,2,1):
                    print(contador,"-",ListaRespostas[num2])
                    num2 += 1
                    contador += 1
                num2 -= contador

                escolha = int(input("\nO que fazer (Digite o número correspondente): "))
                num3 = num2+escolha

                print("\n-- Acontecimento --\n")
                print(ListaFrases[num3],"\n")

                if ListaBoosts[num3] != "0":
                    print("Pela sua resposta:",ListaBoosts[num3])
                    
                    for j in range(0,len(ListaCampos),1):
                        if ListaCamposBoost[num3] in ListaCampos[j]:
                            final = int(ListaBoosts[num3].find(" "))
                            quant = ListaBoosts[num3]
                            quant = int(quant[0:final])
                            ListaInfo[ListaPosicao[j]] += quant
                print("----------------------------------------")

            # Se a vida, fome, sede, dinheiro ou exp fica abaixo de 1, muda para 0.

            for j in range(0,5,1):
                if ListaInfo[ListaPosicao[j]] < 1:
                    ListaInfo[ListaPosicao[j]] = 0

            # Se a vida, fome ou sede fica acima do limite, muda para o limite.

            for k in range(0,3,1):
                if ListaInfo[ListaPosicao[k]] > ListaInfo[k+6]:
                    ListaInfo[ListaPosicao[k]] = ListaInfo[k+6]

            print("\nDinheiro atual: R$",ListaInfo[ListaPosicao[3]],"\n")
            ListaItemAdici = [ListaInfo[ListaPosicao[0]],ListaInfo[ListaPosicao[1]],ListaInfo[ListaPosicao[2]],ListaInfo[ListaPosicao[3]],ListaInfo[ListaPosicao[4]]]

            atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo)

            # Verifica se houve promoção e a executa se houver.

            expUP = int(expUPCargo(cargoTrabalho,ListaInfo))

            if ListaInfo[ListaPosicao[4]] >= expUP:
                print("\nVocê foi promovido!!")
                promocao(cargoTrabalho)
                print("Agora vaza daqui e vai contar pra sua esposa.")
                time.sleep(5)
                break

            # Confirma se continuará trabalhando.
 
            trab = input("Deseja trabalhar mais? (Sim/Não): ")
            print("----------------------------------------\n")
        else:
            # Se a vida, fome ou sede for == 0, não executa o trabalho.
            
            print("Você tá precisando se cuidar, vai lá e depois volta pra trabalhar!!")
            trab = "Não"
            time.sleep(3)

def tarefas(cargoTrabalho):
    contador = 0
    ListaRemover = ["cargo:","\n"]
    ListaAlfabetoMi = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ó","á","ç","ú"," ",".",",","\n"]
    ListaAlfabetoMa = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ó","Á","Ç","Ú"," ",".",",","\n"]
    ListaNum = ["2","3","4","5","6","7","8","9","1","0","\n"]
    ListaTarefas = []
    
    with open('perguntas.txt','r') as f:
        texto = f.readlines()
    for linha in texto:
        for i in range(0,len(ListaRemover),1):
            linha = linha.replace(ListaRemover[i],"")
        if linha == cargoTrabalho:
            acabar = contador
            acabar += 1
            contador += 1
            break      
        else:
            contador += 1

    for linha in texto:
        if contador <= acabar:
            if texto.index(linha) == contador:
                contador += 1
                numTare = linha.replace("trabalhando:","")
                tarefas = linha.replace("trabalhando:","")
                for i in range(0,len(ListaAlfabetoMi),1):
                    numTare = numTare.replace(ListaAlfabetoMi[i],"")
                    numTare = numTare.replace(ListaAlfabetoMa[i],"")
                numTare = int(numTare[len(numTare)-1])

                comeco = 0
                for j in range(0,numTare,1):
                    final = tarefas.find(ListaNum[j])
                    tarefa = tarefas
                    tarefa = tarefa[comeco:final]
                    for k in range(0,len(ListaNum),1):
                        tarefa = tarefa.replace(ListaNum[k],"")
                    ListaTarefas.append(tarefa)
                    comeco = final

                numTare = random.randrange(0,numTare)

    return(ListaTarefas[numTare])

def perguntas(cargoTrabalho,ListaCampos):
    ListaRemover = ["cargo:","\n"]
    ListaCamposPerg = ["pergunta:","r:","frases:","boost:","\n"]
    ListaPerguntas = []
    ListaRespostas = []
    ListaFrases = []
    ListaBoosts = []
    ListaCamposBoost = []
    contador = 0

    with open('perguntas.txt','r') as f:
        texto = f.readlines()
    for linha in texto:
        for i in range(0,len(ListaRemover),1):
            linha = linha.replace(ListaRemover[i],"")
        if linha == cargoTrabalho:
            contador += 2
            break      
        else:
            contador += 1

    for linha in texto:
        comeco = 0
        if contador == 0:
            if linha.find("pergunta:") > -1:
                for i in range(0,len(ListaCamposPerg),1):
                    linha = linha.replace(ListaCamposPerg[i],"")
                ListaPerguntas.append(linha)

            elif linha.find("r:") > -1:
                for j in range(0,len(ListaCamposPerg),1):
                    linha = linha.replace(ListaCamposPerg[j],"")
                for k in range(0,2,1):
                    final = linha.find("/")
                    if final == -1:
                        final = len(linha)
                    ListaRespostas.append(linha[comeco:final])
                    linha = linha.replace(ListaRespostas[len(ListaRespostas)-1],"")
                    linha = linha.replace("/","")

            elif linha.find("frases:") > -1:
                for j in range(0,len(ListaCamposPerg),1):
                    linha = linha.replace(ListaCamposPerg[j],"")
                for k in range(0,2,1):
                    final = linha.find("/")
                    if final == -1:
                        final = len(linha)
                    ListaFrases.append(linha[comeco:final])
                    linha = linha.replace(linha[comeco:final],"")
                    linha = linha.replace("/","")

            elif linha.find("boost:") > -1:
                for j in range(0,len(ListaCamposPerg),1):
                    linha = linha.replace(ListaCamposPerg[j],"")
                for k in range(0,2,1):
                    final = linha.find("/")
                    if final == -1:
                        final = len(linha)
                    ListaBoosts.append(linha[comeco:final])
                    for l in range(0,len(ListaCampos),1):
                        if linha[comeco:final] == "0":
                            ListaCamposBoost.append("0")
                            break
                        if ListaCampos[l] in linha[comeco:final] + ":": 
                            ListaCamposBoost.append(ListaCampos[l])
                            break
                    linha = linha.replace(linha[comeco:final],"")
                    linha = linha.replace("/","")

            elif linha.find(ListaRemover[0]) > -1:
                break
        else:
            contador -= 1

    return(ListaPerguntas, ListaRespostas, ListaFrases, ListaBoosts, ListaCamposBoost)

def expUPCargo(cargoTrabalho,ListaInfo):
    ListaRemover = ["cargo:","expup:","\n"]
    ListaCargos = []
    ListaExpUp = []
    arquivo = "cargo.txt"

    with open(arquivo,'r') as f:
        texto = f.readlines()
    for linha in texto:
        if linha.find(ListaRemover[0]) > -1:
            for i in range(0,len(ListaRemover),1):
                linha = linha.replace(ListaRemover[i],"")
            ListaCargos.append(linha)
        if linha.find("expup:") > -1:
            for i in range(0,len(ListaRemover),1):
                linha = linha.replace(ListaRemover[i],"")
            ListaExpUp.append(linha)

    for i in range(0,len(ListaCargos),1):
        if cargoTrabalho == ListaCargos[i]:
            contador = i + 1
            for j in range(0,contador,1):
                del(ListaExpUp[0])
            break

    if ListaExpUp == [] or ListaExpUp[0] == "0":
        ListaExpUp.insert(0,"99999999999")

    return(ListaExpUp[0])

def promocao(cargoTrabalho):
    ListaRemover = ["cargo:","trabalhandodinheiro:","trabalhandoexp:","expup:","\n"]
    ListaDados = []
    deletar = 0
    arquivo = "cargo.txt"

    with open(arquivo,'r') as f:
        texto = f.readlines()
    for linha in texto:
        for i in range(0,len(ListaRemover),1):
            linha = linha.replace(ListaRemover[i],"")
        ListaDados.append(linha)
    for i in range(0,len(ListaDados),1):
        if cargoTrabalho == ListaDados[i]:
            for j in range(0,i+4,1):
                del(ListaDados[0])
            break
    
    for i in range(0,len(ListaRemover),1):
        with open('arq01.txt','r') as f:
            texto = f.readlines()
        if len(ListaRemover) > 2:
            with open('arq01.txt','w') as f:
                for linha in texto:
                    if linha.find(ListaRemover[0]) > -1:
                        f.write(ListaRemover[0] + ListaDados[0] + "\n")
                    else:
                        f.write(linha)
            del(ListaRemover[0])
            del(ListaDados[0])
        else:
            break

def mercado(ListaInfo):
    mercado = 1
    ListaCarrinho = []
    
    while mercado == 1:
        arquivo = "arq01.txt"
        ListaCampos = ["dinheiro:"]
        dinheiro = procurarCampo(ListaCampos,arquivo)
        dinheiro = dinheiro[0]
        print("Bem vindo(a) a Mercado Market!\n")
        print("Seu carrinho:",ListaCarrinho,"\n")
        print("Você possui: R$",ListaInfo[dinheiro],"\n")
        print("1 - Comida\n2 - Bebida\n0 - Concluir compra / Voltar\n")
        supri = input("O que deseja: ")
        supri = supri[0:2]
        supri = int(supri)

        if supri == 0:
            mercado = 0
            os.system('cls')
        elif supri > 2 or supri < 0:
            print("\nEste número não corresponde a nenhum corredor, tente novamente.")
            time.sleep(4)
            os.system('cls')
        else:
            if supri == 1:
                ListaCarac = ["comida:","\n"]
                ListaNum = ["0","1","2","3","4","5","6","7","8","9"]
                tamanho = 7
            elif supri == 2:
                ListaCarac = ["bebida:","\n"]
                ListaNum = ["0","1","2","3","4","5","6","7","8","9"]
                tamanho = 7

            ListaPrate = []
            ListaValores = []
            arquivo = open('mercado.txt','r')
            for linha in arquivo:
                linha.rstrip
                if linha[0:tamanho] == ListaCarac[0]:
                    for i in range(0,len(ListaCarac),1):
                        linha = linha.replace(ListaCarac[i],"")
                    produto = linha
                    for j in range(0,len(ListaNum),1):
                        produto = produto.replace(ListaNum[j],"")
                    ListaPrate.append(produto)
                    valor = linha.replace(produto,"")
                    ListaValores.append(valor)

            sessao = 1
            while sessao == 1:
                os.system('cls')
                contador = 0
                print("\nSeu carrinho:",ListaCarrinho,"\n")
                print("Veja o que temos na prateleira:\n")
                for i in range(0,len(ListaPrate),1):
                    contador += 1
                    print(contador,"-",ListaPrate[i].title(),"R$:",ListaValores[i],"\n")
                print("0 - Voltar\n")
                escolha = input("Digite o número do que quer levar (1 por vez): ")
                escolha = escolha[0:2]
                escolha = int(escolha)
                if escolha == 0:
                    sessao = 0
                    os.system('cls')
                elif escolha > contador or escolha < 0:
                    print("\nEste número não corresponde a nenhum produto da prateleira, tente novamente.")
                    time.sleep(4)
                else:
                    quant = input("Digite a quantidade que deseja levar: ")
                    quant = quant[0:2]
                    quant = int(quant)
                    
                    if quant > 0:
                        escolha -= 1
                        atualizado = 0
                        ListaCarac = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ã","á","é"," "]
                        for j in range(0,len(ListaCarrinho),1):
                            produto = ListaCarrinho[j].lower()
                            for k in range(0,len(ListaNum),1):
                                produto = produto.replace(ListaNum[k],"")
                            produto = produto.replace(" ","")
                            if produto == ListaPrate[escolha]:
                                atualizado = 1
                                quantCarrinho = ListaCarrinho[j].lower()
                                for l in range(0,len(ListaCarac),1):
                                    quantCarrinho = quantCarrinho.replace(ListaCarac[l],"")
                                quantCarrinho = int(quantCarrinho)
                                quant += quantCarrinho
                                quant = str(quant)
                                del(ListaCarrinho[j])

                                escolha = quant + " " + ListaPrate[escolha].title()
                                ListaCarrinho.insert(j,escolha)
                                break
  
                        if atualizado == 0:
                            quant = str(quant)
                            escolha = quant + " " + ListaPrate[escolha].title()
                            ListaCarrinho.append(escolha)
                    else:
                        print("\nQuantidade desejada incorreta, tente novamente.")
                        time.sleep(4)

    os.system('cls')
    ListaNum = ["0 ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","\n"]
    ListaCarac = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ã","á","é","ó"," "]
    ListaProdutoBolso = []
    ListaQuantBolso = []
    print("\nSeu carrinho:",ListaCarrinho,"\n")
    valor = 0
    valorSemi = 0
    total = 0
    for i in range(0,len(ListaCarrinho),1):
        linha = ListaCarrinho[i]
        produto = linha
        quant = linha.lower()
        for j in range(0,len(ListaNum),1):
            produto = produto.replace(ListaNum[j],"")
        ListaProdutoBolso.append(produto)
        ListaPrateCompleta = listaProduto()
        ListaValoresCompleta = valorProduto()
        for k in range(0,len(ListaPrateCompleta),1):
            if produto.lower() == ListaPrateCompleta[k]:
                valor = k
        for l in range(0,len(ListaCarac),1):
            quant = quant.replace(ListaCarac[l],"")
        ListaQuantBolso.append(quant)
            
        quant = int(quant)
        valorSemi = ListaValoresCompleta[valor]
        total += valorSemi * quant
    print("Total a pagar: R$",total,"\n")
    confirmar = input("Confirma o pagamento (Sim/Não - Menu Principal): ")
    confirmar = confirmar[0:3]

    if confirmar.lower() == "sim" or confirmar.lower() == "s":
        if len(ListaCarrinho) == 0:
            print("\nTa querendo comprar vento? Vaza daqui!\nPra parar de ser engraçado, me da 10 reais ai. ;)")
            time.sleep(5)

            arquivo = "arq01.txt"
            ListaCampos = ['dinheiro:']
            ListaPosicao = procurarCampo(ListaCampos,arquivo)

            dinheiroAtual = ListaInfo[ListaPosicao[0]]

            dinheiroAtual -= 10
            if dinheiroAtual < 0:
                dinheiroAtual = 0

            ListaItemAdici = [dinheiroAtual]
            arquivo = "arq01.txt"
            atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo)
        else:
            arquivo = "arq01.txt"
            ListaCampos = ['dinheiro:']
            ListaPosicao = procurarCampo(ListaCampos,arquivo)

            dinheiroAtual = ListaInfo[ListaPosicao[0]]
            if dinheiroAtual < total:
                print("\nDinheiro insuficiente, vai trabalhar!")
                time.sleep(3)
            else:
                print("\nPassando no caixa...\n")

                atualizarBolso(ListaPrateCompleta,ListaQuantBolso,ListaProdutoBolso)
                time.sleep(3)
                
                dinheiroAtual -= total
                ListaItemAdici = [dinheiroAtual]
                arquivo = "arq01.txt"
                atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo)

                print("Compras feitas!!")
                time.sleep(2)

def listaProduto():
    ListaCaracCompleta = ["comida:","bebida:","0","1","2","3","4","5","6","7","8","9","\n"]
    ListaPrateCompleta = []
    arquivo = open('mercado.txt','r')
    for linha in arquivo:
        linha.rstrip
        for i in range(0,len(ListaCaracCompleta),1):
            linha = linha.replace(ListaCaracCompleta[i],"")
        ListaPrateCompleta.append(linha)
    return(ListaPrateCompleta)

def valorProduto():
    ListaCaracCompleta= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ã","á","é","ó",":","\n"," "]
    ListaValoresCompleta = []
    arquivo = open('mercado.txt','r')
    for linha in arquivo:
        linha.rstrip
        for i in range(0,len(ListaCaracCompleta),1):
            linha = linha.replace(ListaCaracCompleta[i],"")
        ListaValoresCompleta.append(linha)
    ListaValoresCompleta = list(map(int, ListaValoresCompleta))
    return(ListaValoresCompleta)

def atualizarBolso(ListaPrateCompleta,ListaQuantBolso,ListaProdutoBolso):
    ListaNum = ["0","1","2","3","4","5","6","7","8","9","\n",":"]
    ListaCarac = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ã","á","é","ó","\n"," "]
    ListaBolso = []
    ListaQuant = []
    ListaCompleta = []
    ListaProdutoBolso = ListaProdutoBolso
    rodar = 1

    for i in range(0,len(ListaPrateCompleta),1):
        ListaCompleta.append(ListaPrateCompleta[i].lower())

    for j in range(0,len(ListaProdutoBolso),1):
        ListaBolso.append(ListaProdutoBolso[j].lower())

    arquivo = "bolso.txt"
    ListaPosicao = procurarCampo(ListaBolso,arquivo)

    for k in range(0,len(ListaBolso),1):
        with open('bolso.txt','r') as f:
            texto = f.readlines()
            for linha in texto:
                if texto.index(linha) == ListaPosicao[0]:   
                    linha.rstrip()
                    
                    produto = linha
                    quantAtual = linha

                    if rodar != 0:
                        for i in range(0,len(ListaPrateCompleta),1):
                            if i not in ListaPosicao:
                                ListaQuantBolso.insert(i,"0")
                        rodar = 0

                    remover = 0
                    for i in range(0,len(ListaPrateCompleta),1):
                        if ListaPrateCompleta[remover] not in ListaBolso:
                            ListaPrateCompleta.remove(ListaPrateCompleta[remover])
                            ListaQuantBolso.remove(ListaQuantBolso[remover])
                            remover -= 1
                        remover += 1
                        
                    quantBolso = ListaQuantBolso[ListaBolso.index(ListaPrateCompleta[0])]
                    quantBolso = int(quantBolso)

                    for j in range(0,len(ListaNum),1):
                        produto = produto.replace(ListaNum[j],"")
                    for k in range(0,len(ListaCarac),1):
                        quantAtual = quantAtual.replace(ListaCarac[k],"")
                    quantAtual = int(quantAtual)
                    quantBolso += quantAtual
                    quantBolso = str(quantBolso)

                    with open('bolso.txt','w') as f:
                        for l in texto:
                                if texto.index(l) == ListaPosicao[0]:
                                    f.write(ListaCompleta[ListaPosicao[0]]+quantBolso+'\n')
                                    del(ListaPrateCompleta[0])
                                else:
                                    f.write(l)
                        del(ListaPosicao[0])
                        break
def bolso(ListaInfo):
    ListaCarac = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ã","á","é","ó",":","\n"," "]
    ListaNum = ["0","1","2","3","4","5","6","7","8","9","\n"]
    ListaQuant = []
    ListaProduto = []
    ListaPrateCompleta = []
    continuar = 1

    while continuar == 1:
        with open('bolso.txt','r') as f:
            texto = f.readlines()
            contador = 0
            print("No bolso tem:\n")
            for linha in texto:
                produto = linha
                quant = linha

                for i in range(0,len(ListaCarac),1):
                    quant = quant.replace(ListaCarac[i],"")
                quant = int(quant)

                for j in range(0,len(ListaNum),1):
                    produto = produto.replace(ListaNum[j],"")
                ListaPrateCompleta.append(produto)

                produto = linha
                
                if quant > 0:
                    ListaQuant.append(quant)
                    for j in range(0,len(ListaNum),1):
                        produto = produto.replace(ListaNum[j],"")
                    contador += 1
                    ListaProduto.append(produto)
                    print(contador,"-",produto.title(),"Quant:",quant,"\n")
                    
            print("0 - Voltar ao Meu Principal\n")

        usar = int(input("Quer usar algo (Digite o número correspondente): "))

        if usar == 0:
            continuar = 0
        elif usar < 0 or usar > contador:
            print("\nNúmero incorreto, tente novamente.")
            time.sleep(3)
            os.system('cls')
        else:
            usar -= 1
            arquivo = "bolso.txt"
            ListaCampos = [ListaProduto[usar]]
            ListaPosicao = procurarCampo(ListaCampos,arquivo)

            quantAlte = ListaQuant[usar] - 1
            ListaItemAdici = [quantAlte]

            atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo)
            
            ListaCampos = ["vida:"]
            ListaCamposCompleta = ["vida:" + ListaProduto[usar]]
            numComida = 0
            contador = 0

            with open('boost.txt','r') as f:
                texto = f.readlines()
                for linha in texto:
                    fome = linha.find("fome:")
                    if fome != -1:
                        numComida += 1
                    sede = linha.find("sede:")
                    if sede != -1:
                        break

            for i in range(0,len(ListaPrateCompleta),1):
                contador += 1
                if ListaPrateCompleta[i] == ListaProduto[usar]:
                    if contador <= numComida:
                        ListaCamposCompleta.append("fome:" + ListaProduto[usar])
                        ListaCampos.append("fome:")
                        break
                    else:
                        ListaCamposCompleta.append("sede:" + ListaProduto[usar])
                        ListaCampos.append("sede:")
                        break

            ListaLimites = []
            for g in range(0,len(ListaCampos),1):
                ListaLimites.append("limite"+ListaCampos[g])

            ListaLimites = procurarCampo(ListaLimites,"arq01.txt")

            ListaBoost = []
            for i in range(0,len(ListaCampos),1):
                with open('boost.txt','r') as f:
                    texto = f.readlines()
                    for linha in texto:
                        produto = linha
                        boost = linha
                        for i in range(0,len(ListaNum),1):
                            produto = produto.replace(ListaNum[i],"")
                        if ListaCamposCompleta[0] == produto:
                            for i in range(0,len(ListaCarac),1):
                                boost = boost.replace(ListaCarac[i],"")
                            ListaBoost.append(boost)
                    del(ListaCamposCompleta[0])

            ListaBoost = list(map(int,ListaBoost))

            for i in range(0,len(ListaCampos),1):
                with open('arq01.txt','r') as g:
                    textoArq = g.readlines()
                with open('arq01.txt','w') as h:
                    for k in textoArq:
                        campo = k
                        quant = k
                                            
                        for i in range(0,len(ListaNum),1):
                            campo = campo.replace(ListaNum[i],"")

                        if campo == ListaCampos[0]:
                            for j in range(0,len(ListaCarac),1):
                                quant = quant.replace(ListaCarac[j],"")
                            quant = int(quant)
                            quant += ListaBoost[0]
                            if quant > ListaInfo[ListaLimites[0]]:
                                quant = 100
                            quant = str(quant)

                            h.write(ListaCampos[0]+quant+"\n")
                        else:
                            h.write(k)
                    del(ListaLimites[0])
                    del(ListaCampos[0])
                    del(ListaBoost[0])

            print("\nEnxendo a barriga...")
            time.sleep(3)
            os.system('cls')

def casa(ListaInfo):
    descansar = input("Deseja dormir? (Sim/Não - Menu Principal): ")
    if descansar.lower() == "sim" or descansar.lower() == "s":
        quantVezes = int(input("Quantas vezes quer dormir (0 - Menu Principal): "))
        if quantVezes > 0:
            os.system('cls')
            print("")
            for i in range(0,quantVezes,1):
                ListaItemAdici = []
                print("Dormindo...Zzz")
                time.sleep(60)

                ListaCampos = ["vida:","fome:","sede:"]
                arquivo = "arq01.txt"
                ListaPosicao = procurarCampo(ListaCampos,arquivo)

                for j in range(0,len(ListaCampos),1):
                    ListaInfo[ListaPosicao[j]] += 4
                    ListaItemAdici.append(ListaInfo[ListaPosicao[j]])

                atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo)

            print("\nFinalmente acordou, agora vai fazer algo da sua vida!")
            time.sleep(3)

def upgrade(ListaInfo):
    upgrade = 1

    while upgrade == 1:
        ListaCarac = ["\n"]
        ListaAlfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","I","V","Ø","(",")","/"," "]
        ListaCampos = ["vida","fome","sede","dinheiro","exp","vez"]
        ListaLimites = ["(Ø/V)","(I/V)","(II/V)","(III/V)","(IV/V)","(V/V)"]
        ListaUpgrades = []
        ListaValores = []
 
        print("Upgrades disponíveis:\n")
        contador = 0

        with open('upgrade.txt','r') as f:
            texto = f.readlines()
        for linha in texto:
            linha = linha.replace(ListaCarac[0],"")
            if linha.count("preco:") == 0:
                contador += 1
                ListaUpgrades.append(linha)
                comeco = linha.find("(")
                quant = linha[comeco:]
                print(contador,"-",linha[:comeco-1].capitalize(),quant,"\n")
            else:
                linha = linha.replace("preco:","")
                ListaValores.append(linha)
                print("Preço: R$",ListaValores[len(ListaValores)-1],"\n")
        print("0 - Voltar ao Menu Principal\n")

        usar = int(input("Digite o número correspondente ao upgrade:"))

        if usar == 0:
            upgrade = 0
        elif usar > contador or usar < 0:
            print("\nEste número não esta associado a nenhum upgrade. Tente novamente.")
            time.sleep(5)
            os.system('cls')
        else:
            usar -= 1
            preco = ListaValores[usar]
            preco = int(preco.replace("preco:",""))

            arquivo = "arq01.txt"
            CampoDinheiro = ["dinheiro:"]
            ListaPosicao = procurarCampo(CampoDinheiro,arquivo)
            dinheiro = ListaInfo[ListaPosicao[0]]

            if dinheiro < preco:
                print("\nDinheiro insuficiente, vai trabalhar vagabundo!!")
                time.sleep(5)
                upgrade = 0
            else:
                dinheiro = [str(dinheiro - preco)]
                atualizarDados(CampoDinheiro,ListaPosicao,dinheiro,arquivo)

                escolha = ListaUpgrades[usar]

                for i in range(0,len(ListaCampos),1):
                    if i <= 2:
                        campo = "limite"
                    else:
                        campo = "trabalhando"
                    if escolha.find(ListaCampos[i]) > -1:
                        ListaCampos = ListaCampos[i]
                        ListaCampos = campo + ListaCampos + ":"
                        ListaCampos = [ListaCampos]
                        break

                for j in range(0,len(ListaAlfabeto),1):
                    escolha = escolha.replace(ListaAlfabeto[j],"")
                escolha = int(escolha)

                arquivo = "arq01.txt"
                ListaPosicao = procurarCampo(ListaCampos,arquivo)

                escolha = [str(escolha + ListaInfo[ListaPosicao[0]])]

                atualizarDados(ListaCampos,ListaPosicao,escolha,arquivo)

                arquivo = "upgrade.txt"
                
                campo = ListaUpgrades[usar]

                for l in range(0,9,1):
                    campo = campo.replace(str(l),"")
                campo = campo.replace("\n","")

                ListaCampos = [campo]
               
                ListaPosicao = procurarCampo(ListaCampos,arquivo)
                ListaPosicao.append(ListaPosicao[0]+1)
                
                contador = 0
                linha = ListaUpgrades[usar]
                for l in range(0,len(ListaLimites),1):
                    if linha.find(ListaLimites[l]) > -1:
                        if quant != "(V/V)":
                            quant = quant.replace(quant,ListaLimites[l+1])
                            break
                        else:
                            quant = "(V/V)"
                            break

                campo = ListaUpgrades[usar]
                fim = campo.find("(")
                campo = ListaUpgrades[usar][:fim]

                preco = preco * 2
                
                ListaCampos = [campo,"preco:"]
                ListaItemAdici = [quant,preco]
                atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo)

                print("\n-- Upgrade obtido com sucesso! -- ")
                time.sleep(4)

        f.close()

def procurarCampo(ListaCampos,arquivo):
    ListaPosicao = []
    ListaCarac = ["0","1","2","3","4","5","6","7","8","9","\n"]
    contador = 0
    contadorDados = -1
    quantDados = 0
    arquivoQuant = open(arquivo,'r')
    arquivo = open(arquivo,'r')

    for linhaQuant in arquivoQuant:
        quantDados += 1
    
    for k in range(0,quantDados*len(ListaCampos),1):
        for linha in arquivo:
            if contador < len(ListaCampos):
                contadorDados += 1
            if len(ListaPosicao) == len(ListaCampos):
                break
            linha.rstrip()
            for i in range(0,len(ListaCarac),1):
                linha = linha.replace(ListaCarac[i],"")
        
            for j in range(0,len(ListaCampos),1):
                if linha == ListaCampos[j]:
                    ListaPosicao.append(contador)
                    break
                    break
            contador += 1

    return(ListaPosicao)

def atualizarDados(ListaCampos,ListaPosicao,ListaItemAdici,arquivo):
    ListaCaractEspeci = ["[","]",","]
    maximo = len(ListaPosicao)
    contador = 0

    adicionar = ListaItemAdici[contador]
    adicionar = str(adicionar)

    for j in range(0,3,1):
        adicionar = adicionar.replace(ListaCaractEspeci[j],"")
    with open(arquivo,'r') as f:
        texto = f.readlines()
    with open(arquivo,'w') as f:
        for k in texto:
            if contador < maximo:
                if texto.index(k) == ListaPosicao[contador]:
                    f.write(ListaCampos[contador]+adicionar+'\n')
                    contador += 1
                    if contador < maximo:
                        adicionar = ListaItemAdici[contador]
                        adicionar = str(adicionar)

                        for j in range(0,3,1):
                            adicionar = adicionar.replace(ListaCaractEspeci[j],"")
                else:
                    f.write(k)
            else:
                f.write(k)
    f.close()

def continuar(contador):
    os.system('cls')
    return(continuar)

# Começo do programa

contador = 1
ListaAlfabetoMi = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ã","á","é","ç"]
ListaAlfabetoMa = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ã","Á","É","Ç"]
ListaCaracEspe = [":","(","-",")","\n"," "]
ListaPosicoes = ["cargo:","\n"]
while contador == 1:
    arquivo = open('arq01.txt','r')
    ListaInfo = []
    for linha in arquivo:
        cargo = linha
        linha = linha.rstrip()
        if linha.count("opcoes:") == 1:
            opcoes = linha.replace("opcoes:","")
            ListaOpcoes = []
            numOpcao = 2
            comeco = 0
            for i in range(0,5,1):
                final = opcoes.find(str(numOpcao))
                ListaOpcoes.append(opcoes[comeco:final])
                comeco = final
                numOpcao += 1
            ListaInfo.append(0)
        elif cargo.count("cargo:") == 1:
            for i in range(0,len(ListaPosicoes),1):
                cargo = cargo.replace(ListaPosicoes[i],"")
            cargoTrabalho = cargo
            ListaInfo.append(0)
        else:
            for i in range(0,len(ListaAlfabetoMi),1):
                linha = linha.replace(ListaAlfabetoMi[i],"")
                linha = linha.replace(ListaAlfabetoMa[i],"")
            for j in range(0,len(ListaCaracEspe),1):
                linha = linha.replace(ListaCaracEspe[j],"")
            ListaInfo.append(linha)

    arquivo.close()
    ListaInfo = list(map(int, ListaInfo))

    status(ListaInfo,cargoTrabalho)

    for i in range(0,len(ListaOpcoes),1):
        print(ListaOpcoes[i])
    print("0 - Sair\n")

    acao = input("O que vou fazer: ")
    acao = acao[0]
    acao = int(acao)

    if acao == 1:
        print("\n")
        os.system('cls')
        trabalhar(ListaInfo,cargoTrabalho)
        os.system('cls')
    if acao == 2:
        print("\n")
        os.system('cls')
        mercado(ListaInfo)
        os.system('cls')
    if acao == 3:
        print("\n")
        os.system('cls')
        bolso(ListaInfo)
        os.system('cls')
    if acao == 4:
        print("\n")
        os.system('cls')
        casa(ListaInfo)
        os.system('cls')
    if acao == 5:
        print("\n")
        os.system('cls')
        upgrade(ListaInfo)
        os.system('cls')
    if acao == 0:
        print("\nSaindo...")
        time.sleep(3)
        contador = 0
