# Návod ke zprovoznění semestrální práce

Pro zprovoznění práce stačí mít datasety ve složce data/ a poté spustit soubot commands.txt. Pokud však stahujete data sami a nejsou v přiloženém adresáři, musíte datasety ještě přejmenovat na suicide.csv, happy.csv a freedom.csv. Dále přejmenujte year na Year a country na Country v datasetu suicides.csv. Poté jiý můžete spustit soubor commands.txt:
sudo sh commands.txt
Pokud by náhodou chyběla práva pro psaní do některých složek, udělte jim je. V takovém případě spusťte soubot shutdown.txt pomocí sudo sh shutdown.txt, aybste odstranili veškerou vytvořenou konfiguraci a poté opět spusťte commands.txt.

Poté otevřete kibanu na http://localhost:5601/. V záložce Management vyberte Index patterns a u Create index pattern vytvvořte index s názvem happiness.Klikněte na Next step a vyberte, že nechcete time filter. Poté klikněte na Create index pattern. 
Nyní máte vytvořený index a můžete vkládat dotazy v záložce Dev Tools.

Import vizualizací.
