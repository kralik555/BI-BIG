# Návod ke zprovoznění semestrální práce

Pro zprovoznění práce stačí mít datasety ve složce data/ a poté spustit soubot commands.txt. Pokud však stahujete data sami a nejsou v přiloženém adresáři, musíte datasety ještě přejmenovat na suicide.csv, happy.csv a freedom.csv. Dále přejmenujte year na Year a country na Country v datasetu suicides.csv. Poté jiý můžete spustit soubor commands.txt:
sudo sh commands.txt
Pokud by náhodou chyběla práva pro psaní do některých složek, udělte jim je. V takovém případě spusťte soubot shutdown.txt pomocí sudo sh shutdown.txt, aybste odstranili veškerou vytvořenou konfiguraci a poté opět spusťte commands.txt.

Poté otevřete kibanu na http://localhost:5601/. V záložce Management vyberte Index patterns a u Create index pattern vytvvořte index s názvem happiness.Klikněte na Next step a vyberte, že nechcete time filter. Poté klikněte na Create index pattern. 
Nyní máte vytvořený index a můžete vkládat dotazy v záložce Dev Tools.

Dotaz 1:
Tento dotaz hledá všechny záznamy, ve nich název země obsahuje slovo United a zároveň je počet sebevražd na 100 000 obyvatel vyšší než 30.
GET /happiness/_search
{
  "query": {
    "bool": {
      "filter": [
        { "match": { "Country": "United" }},
        { "range": { "suicides_per_100k": { "gt": 30 }}}
      ]
    }
  }
}

Dotaz  2:
Tento dotaz hledá všechny záznamy, v nichž je důvěra ve vládu alespoň 70 % a celkové hodnocení na žebříčku štěstí alespoň 6. Dotaz ještě omezíme na rok 2015 a na souhrn pro celé státy (obě pohlaví a všechny věkové skupiny dohromady). Výsledky jsou pak ještě setříděny podle počtu sebevražd na 100 000 obyvatel sestupně.
GET /happiness/_search
{
  "query": {
    "bool": {
      "filter": [
        {"range": { "Confidence In National Government": { "gte": 0.7 }}},
        {"range": { "Life Ladder": { "gte": 6 }}},
        {"term": { "Year": 2015 }},
        {"match": { "age": "All"}},
        {"match": {"sex": "Both"}}
      ]
    }
  },
  "sort": [
    { "suicides_per_100k": { "order": "desc" }}
  ]
}


Dotaz 3:
Třetí dotaz hledá všechny země, v jejichž názvu je písmeno x. Aby se země objevily pouze jedno, je přidáno ještě omezení na rok 2015 a na záznamy s oběmapohlavími dohromady.
GET /happiness/_search
{
  "_source": ["Country"],
  "query": {
    "bool": {
      "must": [
        {"wildcard": {
            "Country": "*x*"
          }
        },
        {"term": {"sex": "both"}},
        {"term": {"Year": 2015}}
      ]
    }
  }
}

Pokud chcete naimportovat vizualizace nebo dashboard do kibany, je tak možné učinit přes Management -> Saved Objects. Exportované vizualizace a dashboard jsou ve složkách visualizations, respektive dashboards jako json soubory.

Pro ukončení stačí spustit soubor shutdown.txt:
sudo sh shutdown.txt

