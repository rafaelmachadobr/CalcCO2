total_carbono = 0

print('-' * 45)
print('Descubra se você taxista ou motorista de aplicativo possui crédito de CO²')
print('-' * 45)
print("Primeiramente, vamos precisar de alguns dados!\n")

gasto_combustivel = -1

while gasto_combustivel <= -1:
    try:
        gasto_combustivel = float(
            input('Digite a média mensal de gasto seu com combustível: R$').replace(',', '.'))
        if gasto_combustivel < 0:
            print('-' * 45)
            print('Não pode ser numero negativo!')
            print('-' * 45)
    except ValueError:
        print('-' * 45)
        print('Isso não é um número válido. Tente novamente')
        print('-' * 45)

tipo_combustivel = ''

while not tipo_combustivel == '1' and not tipo_combustivel == '2' and not tipo_combustivel == '3':
    tipo_combustivel = input(
        f"Escolha o tipo de combustível que você utiliza:\n"
        "[ 1 ] - Gasolina \n"
        "[ 2 ] - Etanol \n"
        "[ 3 ] - Diesel \n"
        "Digite sua opção: ").replace(' ', '')

    if tipo_combustivel == '1':
        combustivel = 0.0035
    elif tipo_combustivel == '2':
        combustivel = 0.0039
    elif tipo_combustivel == '3':
        combustivel = 0.0042
    else:
        print('-' * 45)
        print(f'"{tipo_combustivel}" não é um opção valida, tente novamente!')
        print('-' * 45)

total_combustivel = gasto_combustivel * combustivel
total_carbono += total_combustivel

print(
    f"\nVocê está utilização de combustiveis {total_combustivel:.2f} toneladas de CO² por ano, \n"
    f"Até o momento você polui {total_carbono:.2f} toneladas de CO² por ano!\n")

conta_luz = -1

while conta_luz < 0:
    try:
        conta_luz = float(
            input("Digite o valor médio da conta de luz da sua empresa: R$"))

        if conta_luz < 0:
            print('-' * 45)
            print('Não pode ser numero negativo!')
            print('-' * 45)
        else:
            luz = conta_luz * 0.002136
            total_carbono += luz

            print(f"Sua empresa emite {luz:.2f} toneladas de CO² por ano,\ntotalizando até agora "
                  f"{total_carbono:.2f} toneladas de CO² por ano!\n")

    except ValueError:
        print('-' * 45)
        print('Isso não é um número válido. Tente novamente')
        print('-' * 45)

frete_mes = -1

while frete_mes < 0:
    try:
        frete_mes = int(
            input('Digite a quantidade de viagens que você faz ao mês: '))

        if frete_mes < 0:
            print('-' * 45)
            print('Não pode ser numero negativo! Tente novamente')
            print('-' * 45)
            continue

    except ValueError:
        print('-' * 45)
        print('Isso não é um número válido. Tente novamente')
        print('-' * 45)

distancia = ''

while not distancia == '1' and not distancia == '2' and not distancia == '3':
    distancia = input(f"Escolha a localização da maioria das viagens:\n"
                      "[ 1 ] - 1 km até 100 km \n"
                      "[ 2 ] - 100 km a 600 km \n"
                      "[ 3 ] - 600 km até 2000 km \n"
                      "Digite sua opção: ").replace(' ', '')

    if distancia == '1':
        media_frete = frete_mes * 0.00213
    elif distancia == '2':
        media_frete = frete_mes * 0.00381
    elif distancia == '3':
        media_frete = frete_mes * 0.00416
    else:
        print('-' * 45)
        print(f'"{distancia}" não é um opção valida, tente novamente!')
        print('-' * 45)

    total_carbono += media_frete


print(f"Você emite por meio de utilização de viagens {media_frete:.2f} toneladas de CO² por ano,\ntotalizando até agora "
    f"{total_carbono:.2f} toneladas de CO² por ano!\n")

arvores_plantadas = int(input('Quantas árvores sua empresa planta por ano?: '))
meta_arvores = round(total_carbono * 7)
credito = 0

if arvores_plantadas > meta_arvores:
    for i in range(meta_arvores, arvores_plantadas):
        credito += 1
    print(f"Você plantou {arvores_plantadas} arvores e precisava plantar {meta_arvores} arvores para compensar o carbono emitido pela sua empresa, então recebe {credito} créditos de carbono por isso!")

    vender_credito = ''

    while not vender_credito == '1' and not vender_credito == '2': 
        vender_credito = input(f"Deseja converter o(s) {credito} crédito(s) de carbono em R$:\n"
                                "[ 1 ] - Sim\n"
                                "[ 2 ] - Não\n" 
                                "Digite sua opção: ").replace(' ', '')
        if vender_credito == '1':
            credito_convertido = f'R${credito * 365:_.2f}'
            credito_convertido = credito_convertido.replace('.', ',').replace('_', '.')
            print(f'Convertendo para real você terá: {credito_convertido} disponíveis.')
        elif vender_credito == '2':
            pass
        else:
            print(f'"{vender_credito}" não é um opção valida, tente novamente!')

elif arvores_plantadas == meta_arvores:
    print(
        f'Você consiguiu chegar a meta de {meta_arvores} arvores da sua meta para compensar o carbono emitido pela empresa.')
else:
    print(
        f'Você não consiguiu bater a meta de {meta_arvores} arvores para compensar o carbono emitido pela empresa.\n'
        f'Você prescisa comprar {meta_arvores - arvores_plantadas} credito(s) de carbono')

print('Fim do Programa!')
