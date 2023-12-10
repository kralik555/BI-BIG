# Postup vytvoření vizualizací

(obsah viz 2. část, podčást B)

## Vizualizace 1
První vizualizace pracuje s daty o počtu sebevražd na 100 000 obyvatel. Vytváří jednoduchý koláčový graf ze všech dat.

## Vizualizace 2

Druhá vizualizace je sloupcový graf. Jako metrika je vybrán počet a na ose x jsou hodnoty počtu sebevraž na 100 000 obyvatel. Toto pole bylo rozděleno na intervaly po jedné. Každý sloupec byl zároveň rozdělen podle pole Life Ladder opět s intervalem rozdělení 1.

## Vizualizace 3

Třetí vizualizace pracuje s daty z atributu Life Ladder, který udává celkové štěstí. Graf byl votvořen jako line graph, přičemž metrika byla použita count a nebyl použit žádný filtr, jsou v něm tedy veškeré záznamy. Data byla rozdělena do 8 skupin vždy po jedné.

## Vizualizace 4

Tato vizualizace byla vytvořena jako horizontální sloupcový graf. Jako celková metrika bylo vybráno Count. Jako osa x byla vybrána data z pole suicides\_per\_100k rozdělená do histogramů s minimální šířkou 5. Poté byla ještě přidána možnost split series, kde jsem rozdělil grafy podle Total freedom na histogramy šíčky alespoň 15.

## Vizualizace 5

Pátá vizualizace byla vytvořena jako heat mapa. Metrika byla použita Count. Na ose x je Confidence in national goverment rozdělena podle histogramu s šířkou 0,1. Na ose y je Perceptions of Corruptions rozdělená na úseky také dlouhé 0,1. 

## Vizualizace 6

Dalším grafem je Are graph, který zobrazuje PR Rating. PR rating je na ose x rozdělen jako histogram na intervaly dlouhé 1 a jako filtr bylo použito pole "sex" s hodnotou "both", aby byly brány pouze záznamy celých států.

## Vizualizace 7

Jako předposlední vizualizace byla vytvořena tabulka s hodnotami. Hodnoty jsou  z pole population na 5 úseků: 0 - 1 000 000, 1 000 000 - 10 000 000, 10 000 000 - 100 000 000, 100 000 000 - 1 000 000 000 a na všechny zbylé hodnoty. Byl použit filtr "sex" na "both", aby opět byly brány pouze celé státy.

## Vizualizace 8

Poslední vizualizace je typu Metric. Agregace byla vybrána jako maximum z pole suicides\_no. Hodnoty byly dále rozděleny podle zemí a seřazeny podle počtu sebevražd sestupně.

