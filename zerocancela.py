#INICIANDO VARIAVEIS
ultimo = 0
penultimo = 0
antepenultimo = 0
atual = 0
soma = 0
contador_zeros = 0
contador_validos = 0
contador_invalidos = 0

atual = int(input("Digite o numero:  "))

while (atual >= 0):
    soma += atual

    if (atual == 0):
        contador_zeros += 1
        contador_invalidos += 1
        contador_validos -= 1
        if (ultimo == 0 and contador_zeros > 3):
            print("Somente 3 zeros seguidos podem ser inseridos.")
            contador_validos += 1
            contador_invalidos -= 1
        elif (soma == 0) or (ultimo == 0 and penultimo == 0 and antepenultimo == 0):
            contador_invalidos -= 1
            contador_validos += 1
        else:
            soma -= ultimo
            ultimo = penultimo
            penultimo = antepenultimo
            antepenultimo = 0
    else:
        if (contador_zeros > 0):
            contador_zeros = 0
        antepenultimo = penultimo
        penultimo = ultimo
        ultimo = atual
        contador_validos += 1
    '''print("zeros contabilizados", contador_zeros, "CONSIDERADOS", contador_validos, "Nao considerados", contador_invalidos)
    print("\n atual " ,atual, "ultimo " ,ultimo, "penultimo " ,penultimo, "antepenultimo", antepenultimo)'''
    atual = int(input("Digite o numero:  "))

#SAIDA
print("\nRESULTADOS")
print("\nSoma:", soma)
print("\nNúmeros Considerados:", contador_validos)
print("\nNúmeros Desconsiderados:", contador_invalidos)