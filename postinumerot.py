import http_request


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat

postinumerot = http_request.hae_postinumerot()
toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

def main():
    toimipaikka = input('Anna postitoimipaikka: ').strip().upper()

    if toimipaikka in toimipaikat:
        toimipaikat[toimipaikka].sort()

        loytyy_str = ', '.join(toimipaikat[toimipaikka])
        print('Postinumerot: ' + loytyy_str)

    else:
        print('Postitoimipaikka ei löytynyt')

if __name__ == '__main__':
    main()