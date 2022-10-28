from math import ceil


alcool = 5 * 0.82 * 0.79 * 3.7
diesel = 5 * 0.83 * 3.7
etanol = 5 * 0.82 * 0.78 * 3.7
gasolina = 5 * 0.82 * 0.75 * 3.7
continuar = 's'

print('-' * 80)
print('Descubra se você taxista ou motorista de aplicativo possui ou deve crédito de CO²')
print('-' * 80)
print("Primeiramente, vamos precisar de alguns dados!")

while continuar != 'n':
    try:
        distancia_dia = int(
            input('\nDigite a média de quilômetro (Km) que seu carro roda por dia: '))

        taxa_consumo = int(
            input('Digite a média de quilômetro por litro (Km/L) do seu carro: '))

        if taxa_consumo <= 0:
            print(f'\n"{taxa_consumo}" não pode, tente novamente!')
            continue

        consumo_diario = distancia_dia / taxa_consumo
        consumo_anual = consumo_diario * 53

        print(f"\nSeu consumo diário é de {consumo_diario:.2f} Litros,\n"
              f"Já o seu consumo anual é de {consumo_anual:.2f} Litros\n")

        tipo_combustivel = input(
            f"Escolha o tipo de combustível que você utiliza:\n"
            "[ 1 ] - Álcool \n"
            "[ 2 ] - Diesel \n"
            "[ 3 ] - Etanol \n"
            "[ 4 ] - Gasolina \n"
            "Digite sua opção: ").replace(' ', '').lower()

        if tipo_combustivel == '1' or tipo_combustivel == 'alcool':
            emissoes_totais = consumo_anual * alcool
        elif tipo_combustivel == '2' or tipo_combustivel == 'diesel':
            emissoes_totais = consumo_anual * diesel
        elif tipo_combustivel == '3' or tipo_combustivel == 'etanol':
            emissoes_totais = consumo_anual * etanol
        elif tipo_combustivel == '4' or tipo_combustivel == 'gasolina':
            emissoes_totais = consumo_anual * gasolina
        else:
            print(f'"{tipo_combustivel}" não é um opção valida, tente novamente!\n')
            continue

        print(
            f"\nSua emissão total é de {emissoes_totais:.2f} kg de CO2 por ano.\n")

        numero_pessoas = int(
            input("Digite a média de passageiros que você pega por dia: "))

        emisao_pessoa = emissoes_totais / numero_pessoas

        print(
            f"\nA emissão por pessoa fica assim {emisao_pessoa:.2f} kg de CO2 por ano.\n")

        plantar_arvores_atlantica = ceil(emisao_pessoa / 130)
        plantar_arvores_amazonia = ceil(emisao_pessoa / 220)

        plantou = input('Você plantou alguma arvore ano passado? [s/n] ')
        if plantou == 's' or plantou == 'sim':
            arvores_plantadas = int(
                input('Quantas árvores você plantou no ano passado: '))
        else:
            arvores_plantadas = 0

        credito = (arvores_plantadas - plantar_arvores_atlantica) / 7
        if arvores_plantadas > plantar_arvores_amazonia and arvores_plantadas > plantar_arvores_atlantica:
            print(
                f'\nParabéns você passou da meta que era de {plantar_arvores_atlantica} arvores,\n'
                f'Por isso você ganha {credito:.2f} credito(s) de carbono.\n')

            vender_credito = input(f"Deseja converter o(s) {credito:.2f} crédito(s) de carbono em R$:\n"
                                   "[ 1 ] - Sim\n"
                                   "[ 2 ] - Não\n"
                                   "Digite sua opção: ").replace(' ', '')
            if vender_credito == '1':
                credito_convertido = f'R${credito * 365:_.2f}'
                credito_convertido = credito_convertido.replace(
                    '.', ',').replace('_', '.')
                print(
                    f'\nConvertendo para real você terá: {credito_convertido} disponíveis.\n')
            elif vender_credito == '2':
                pass
            else:
                print(
                    f'"{vender_credito}" não é um opção valida, tente novamente!')
                continue
        elif arvores_plantadas == plantar_arvores_atlantica:
            print(
                '\nVocê está equilibrado não prescisa comprar credito de carbono ou arvore\n')
        else:
            if arvores_plantadas > plantar_arvores_amazonia:
                print(
                    f'\nPara compensar a taxa de emissão de CO², será necessário plantar mais {plantar_arvores_atlantica - arvores_plantadas} árvore(s) na Mata Atlântica.\n')
            else:
                credito = (plantar_arvores_atlantica) / 7
                print(
                    f'\nPara compensar a taxa de emissão de CO², será necessário plantar mais {plantar_arvores_atlantica - arvores_plantadas} árvore(s) na Mata Atlântica,\n'
                    f'ou plantar mais {plantar_arvores_amazonia - arvores_plantadas} árvores na Amazônia.')
                credito_convertido = f'R${credito * 365:_.2f}'
                credito_convertido = credito_convertido.replace(
                    '.', ',').replace('_', '.')
                print(
                    f'Ou comprar {credito:.2f} credito(s) de carbono, que convertendo em real fica {credito_convertido}.\n')

        continuar = input(
            'Deseja fazer outro calculo no programa: [s/n] ').lower()
    except ValueError:
        print()
        print('-' * 40)
        print('Ops! aconteceu um erro, tente novamente!')
        print('-' * 40)


print('\nFim do Programa!')
