# Návod ke zprovoznění semestrální práce

Spusťte soubot commands.txt (pokud nemá práva, přidělte u je pomocí chmod +x commands.txt):
sudo sh commands.txt

Spusťte mongo shell:
sudo docker exec -it technologie-mongos01-1 mongosh

Pro přidání záznamů zkopírujte obsah souboru content.JSON a poté  se připojte k databázi a vložte jej do ní:
use cms
db.content.insertMany(\<zkopírovaný obsah content.json\>)

Pro spuštění příkazů zkopírujte dotazy do mongo shell. 

Pro ukončení spusťe soubor shutdown.txt:
sudo sh shutdown.txt


