*Autors: Antoni Dalmau Diéguez i Oriol Balagué Chorto*
# Practica1SD

En aquest projecte hem implementat un MapReduce en el qual a partir d’un fitxer amb un tamany considerable executem dues funcions la CountWords i la WordCount.

-La funció CountWords s’encarrega de contar el nombre de vegades que apareix una paraula en un string que rep per paràmetre i retorna un diccionari amb clau “paraula” i valor “# vegades que apareix”.

-La funció WordCount s’encarrega de contar el nombre de paraules que conté un string que rep per paràmetre i retorna aquest valor. 

# Utilitzacio versió Distribuida
Per utilitzar el projecte (en la versió distribuida) s'ha d'executar la seguent comanda:

$python HTTPServer.py [numMapers]

Si es volgues afegir un nombre major (o reduir) el nombre de mapers, s'haura de modificar la variable global numMapers dels fitxers: HTTPServer.py i server.py.

Un cop executats els fitxers el projecte realitzara les seguents operacions:
1. HTTPServer particiona el fitxer i el penja en un simple HTTP server local.

2. Registra els mapers al registry

3. El servidor fa un spawn de tos els mapers del registry, i els hi envia l’orde de començar a executar.

4. Els mapers descarreguen el seu fitxer corresponent del simple HTTP server que hem creat prèviament.

5. Un cop descarregat executen la funció corresponents (CountWords o WordCount) i envien el resultat al servidor.

6. El servidor executa l’actor reducer i mostra per pantalla el resultat final.

# Utilització versió sequencial
Per executar la versió sequencial simplement s'haura d'executar la seguent comanda:

$python SequencialDiccionari.py [numMapers]
o
$python SequencialParaules.py [numMapers]

Un cop executat el fitxer el projecte realitzara les seguents operacions:
1. Executem l'unic maper que tenim.

2. El maper llegeix el contingut del fitxer i un cop ha acabat d'executar la funció corresponent li pasa la sortida al reducer.

3. El reducer redueix i mostra el resultat final per pantalla.
