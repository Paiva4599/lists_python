l_numeros = list()

def Menu():
    menu = input("Digite: \n"
                "[a] para acrescentar um número na lista\n"
                "[b] para ver a lista\n"
                "[c] para somar os valores da lista\n"
                "[d] para ver o maior e o menor número da lista\n"
                "[e] para verificar se número está na lista\n"
                "[f] para colocar a lista em ordem crescente\n"
                "[g] para adicionar o número 33 na posição 1 da lista\n"
                "[h] para colocar a lista em ordem decrescente\n"
                "[i] para calcular a média dos valores da lista\n"
                "[j] para calcular a porcentagem dos números acima de 10 da lista\n"
                "[k] para remover um número da lista\n"
                "[l] para sair\n")
    menu = menu.lower()
    return menu

while True:
    aux = Menu()
    if aux == 'a':
        a = int(input("Digite um número para acrescentar na lista:\n"))
        l_numeros.append(a)
    if aux == 'b':
        print(l_numeros)
        print(len(l_numeros))
    if aux == 'c':
        print("Soma dos Valores da Lista:\n",sum(l_numeros))
    if aux == 'd':
        print("Maior Valor:", max(l_numeros), "\nMenor Valor:", min(l_numeros), "\n")
    if aux == 'e':
        v = int(input("Digite um valor:\n"))
        if v in l_numeros:
            print("O valor está na posição", l_numeros.index(v), "da lista\n")
        else:
            print("O valor não está na lista. Adicionar?\n"
                  "Pressione 'Y' para adicionar e 'N' para não adicionar\n")
            add = input()
            add = add.lower()
            if add == 'y':
                l_numeros.append(v)
            elif add == 'n':
                pass
            else:
                pass
    if aux == 'f':
        l_numeros.sort()
        print("Lista em Ordem Crescente: \n", l_numeros)
    if aux == 'g':
        l_numeros.insert(1, 33)
        print(l_numeros)
    if aux == 'h':
        l_numeros.sort(reverse=True)
        print(l_numeros)
    if aux == 'i':
        media = sum(l_numeros)/len(l_numeros)
        print("Média dos termos da lista: \n", media)
    if aux == 'j':
        total = len(l_numeros)
        counter = 0
        for i in l_numeros:
            if i > 10:
                counter += 1
        print("Porcentagem dos números maiores que dez na lista:", (counter/total)*100, "%\n")
    if aux == 'k':
        a = int(input("Digite o valor da lista que você deseja remover:\n"))
        l_numeros.remove(a)
        print(l_numeros)
    if aux == 'l':
        break
