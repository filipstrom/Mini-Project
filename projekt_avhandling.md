**Mini-project report**
Medlemmar: Filip Ström, Isabel Silva Henriksson, Joakim Forsberg, Miliam Eliasson

Program: Civilingenjörsprogrammet i Teknisk Matematik

Kurs: 1DV501

Inlämningsdatum: 

**Introduktion**
Projektet är uppdelat i fem delar som alla utgår ifrån egengjorda hashing och binary search tree program. Projektet börjar med uppgiften "Count unique words 1" som går ut på att, med hjälp av pythons set-klass, hitta antalet unika ord i två olika filer med ord. Man ska också, med hjälp av dictionary-klassen, ta fram de tio mest frekventa orden som har fyra eller mer bokstäver i samma filer. 

I del två skulle man man bygga ett hashing-set och en binary search tree-map från ett givet skelett. 
Skeletten innehöll de olika funktionerna man skulle ändra för att få en fungerande klass. Man fick också ett output-exempel för att se hur outputen skulle se ut när man körde klasserna i ett program.

I del tre skulle man använda sitt hash-set och sin bst-map förr att göra samma sak som i del ett. Man skulle räkna antalet unika ord i de två textfilerna med sitt hash-set. Sedan skulle man printa de tio vanligaste orden i filerna som var fyra tecken eller längre med sin binary search tree-map. Sedan skulle man göra två nya saker, man skulle printa den maximala storleken på "buckets" efter man fört in orden i hash-settet, och man skulle printa det absoluta djupet i sitt binary search tree efter orden förts in.

I del fyra skulle man importera mathplotlib, som används för att rita grafer, för att rita två olika grafer, varav två av varje (en för varje fil). Den första grafen är ett histogram som visar hur många ord det finns i filerna för olika längder på orden där antalet ord är y-axeln och längderna är x-axeln.
Den andra grafen är ett linjediagram som visar hur många ord som lagts till i ens hash-set och hur många av orden som är unika där antalet ord är x-axeln och unika ord är y-axeln.

I den sista delen, den femte, mäter man tiden på mätningar i klasserna. Först i binära sökträdet, där tar man tre olika storlekar på trädet och söker igenom trädet lika många gånger i varje storlek på trädet för att se hur tiden påverkas (Linjärt? logaritmiskt? exponentiellt? m.m).
Med information man fått gör man två olika grafer, en som visar söktiden per storlek på träd, och en som visar djupet på trädet mot trädets storlek.
Den andra delen av del fem för uppgiften är att kolla hur lång tid det tar att lägga till nya element i sitt hash-set och hur rehashing påverkar denna tid. Sedan ska man även kolla "bucket"-djupet. 
Man ska använda informationen för att rita grafer på tiden det tar att lägga in en viss mängd element (en större mängd) och hur set-storlekar påverkar detta genom rehashing. Man ska även rita en graf som visar hur "bucket"-djupet påverkas av setstorlekar.



