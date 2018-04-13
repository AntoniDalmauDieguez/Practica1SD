*Autors: Antoni Dalmau Diéguez i Oriol Balagué Chorto*
# Practica1SD

En aquest projecte hem implementat un MapReduce en el qual a partir d'un fitxer amb un tamany considerable executem dues funcions la CountWords i la WordCount.

-La funció CountWords s'encarrega de contar el nombre de vegades que apareix una paraula en un string que rep per paràmetre i retorna un diccionari amb clau "paraula" i valor "# vegades que apareix".

-La funció WordCount s'encarrega de contar el nombre de paraules que conté un string que rep per paràmetre i retorna aquest valor.

# Utilització versió Distribuïda
Per utilitzar el projecte (en la versió distribuïda) s'han d'executar els seguents fitxers en ordre esperant que acabi l'execució del fitxer anterior:
1. HTTPServer.py
2. registry.py
3. maper1.py
4. maper2.py
5. maper3.py
6. maper4.py
7. server.py

Per augmentar el tamany del fitxer, s'ha d'executar el fitxer multiplicador.py i a continuació modificar el nom del path on es troba el nou fitxer.

Per afegir un nombre major (o reduir) el nombre de mapers, s'haurà de modificar la variable global numMapers dels fitxers: HTTPServer.py i server.py.

Un cop executats els fitxers el projecte realitzarà les següents operacions:
1. HTTPServer particiona el fitxer i el penja en un simple HTTP server local.

2. Registra els mapers al registry.

3. El servidor fa un spawn de tos els mapers del registry, i els hi envia l'orde de començar a executar.

4. Els mapers descarreguen el seu fitxer corresponent del simple HTTP server que hem creat prèviament.

5. Un cop descarregat executen la funció corresponent (CountWords o WordCount) i envien el resultat al servidor.

6. El servidor executa l'actor reducer i mostra per pantalla el resultat final.

# Utilització versió Seqüencial
Per executar la versió seqüencial simplement s'haurà d'executar la comanda:

$python SequencialDiccionari.py
o
$python SequencialParaules.py

Un cop executat el fitxer el projecte realitzarà les següents operacions:
1. Executem l'únic maper que tenim.

2. El maper llegeix el contingut del fitxer i un cop ha acabat d'executar la funció corresponent li passa la sortida al reducer.

3. El reducer redueix i mostra el resultat final per pantalla.
