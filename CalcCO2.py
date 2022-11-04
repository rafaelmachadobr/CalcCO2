from math import ceil


def converter_consumo_em_co2(x: float, y: str, z: int) -> float:
    """
    Essa função converte do consumo anual em emissão total

    :param x: Consumo anual
    :type x: float
    :param y: Tipo de combustível
    :type y: int
    :param y: Dia
    :type y: int

    :return: A conversão do consumo anual em emissão total
    :rtype: float
    """

    alcool = z * 0.82 * 0.79 * 3.7
    diesel = z * 0.83 * 3.7
    etanol = z * 0.82 * 0.78 * 3.7
    gasolina = z * 0.82 * 0.75 * 3.7

    if y == 'alcool':
        return x * alcool
    elif y == 'diesel':
        return x * diesel
    elif y == 'etanol':
        return x * etanol
    elif y == 'gasolina':
        return x * gasolina


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
            input('\nDigite a média de quilômetro por litro (Km/L) do seu carro: '))

        dia = int(
            input('\nDigite quantos dias por semana você utiliza seu veículo: '))

        if dia < 0 or dia > 7:
            print(
                f'\nUma semana tem 7 dias e você digitou o dia "{dia}", tente novamente!')
            continue

        if taxa_consumo <= 0:
            print(f'\n"{taxa_consumo}" não pode, tente novamente!')
            continue

        consumo_diario = distancia_dia / taxa_consumo
        consumo_anual = consumo_diario * 53

        print(f'\nCom os dados adquiridos, foi concluído que em 1 dia seu carro consome {consumo_diario:.2f} Litros,\n'
              f'Já em 1 ano é consumido {consumo_anual:.2f} Litros.\n')

        tipo_combustivel = input(
            f"Das opções abaixo, digite o número que corresponde ao combustível utilizado com maior frequência em seu veículo:\n"
            "[ 1 ] - Álcool \n"
            "[ 2 ] - Diesel \n"
            "[ 3 ] - Etanol \n"
            "[ 4 ] - Gasolina \n"
            "Digite sua opção: ").replace(' ', '').lower()

        if tipo_combustivel == '1' or tipo_combustivel == 'alcool':
            combustivel = 'alcool'
        elif tipo_combustivel == '2' or tipo_combustivel == 'diesel':
            combustivel = 'diesel'
        elif tipo_combustivel == '3' or tipo_combustivel == 'etanol':
            combustivel = 'etanol'
        elif tipo_combustivel == '4' or tipo_combustivel == 'gasolina':
            combustivel = 'gasolina'
        else:
            print(f'"{tipo_combustivel}" não é um opção valida. Por favor digite apenas o NÚMERO correspondente ao combustível utilizado frequentemente (Ex: 1 = álcool ), tente novamente!')
            continue

        emissoes_totais = converter_consumo_em_co2(
            x=consumo_anual, y=combustivel, z=dia)

        print(
            f'\nCerto, o combustível que você utiliza regularmente em seu veículo é {combustivel}.')

        print(
            f"\nSua emissão total é de {emissoes_totais:.2f} kg de CO2 por ano.\n")

        numero_pessoas = int(
            input("Digite a média de passageiros que você pega por dia: "))

        emisao_pessoa = emissoes_totais / numero_pessoas

        print(
            f"\nCada passageiro emite anualmente {emisao_pessoa:.2f} kg de CO2 por ano.\n")

        plantar_arvores_atlantica = ceil(emisao_pessoa / 130)
        plantar_arvores_amazonia = ceil(emisao_pessoa / 220)

        print('De acordo com o Laboratório de Silvicultura Tropical, uma árvore na amazônia com 30 anos de crescimento.\n'
              'Assim, pode estocar em torno de 130 kg CO2-eq para as árvores na Mata Atlântica e 222 kg CO2-eq para as árvores da Floresta Amazônica. \n'
              f'Sendo assim, deverá ser plantado {plantar_arvores_atlantica} árvore(s) por ano na Mata Atlântica ou plantar {plantar_arvores_amazonia} árvore(s) na Amazônia.\n')

        plantou = input('Você plantou alguma arvore ano passado? [s/n] ')
        if plantou == 's' or plantou == 'sim':
            arvores_plantadas = int(
                input('\nQuantas árvores você plantou no ano passado: '))
            if arvores_plantadas < 0:
                print(
                    f'"{arvores_plantadas}" não é um número inteiro e positivo, tente novamente!')
                continue
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
