aantalLeeftijd = eval(input('Hoe oud ben je?: '))
bezitPaspoort = input('Ben je in bezit van een Nederlands paspoort?: ')

if aantalLeeftijd >= 18 and bezitPaspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Helaas, je mag niet stemmen')