## AMBIENTE PYTHON/DJANGO DISTRIBUITO SU DUE NODI VIRTUALI GENERATO TRAMITE VAGRANT

Questa repository contiene un ambiente virtuale distribuito su due nodi, in grado di gestire applicazioni web sviluppate in Python con il framework Django e con il database Postgresql. Nell'ambiente è già fornita una web app d'esempio pienamente utilizzabile, ma tale ambiente è perfettamente utilizzabile come ambiente di sviluppo.

### Prerequisiti
E' necessario avere installati nel proprio sistema Vagrant e VirtualBox.

### 1) Scaricare la repository
Scaricare l'intera repository in una qualsiasi locazione del proprio sistema.

### 2) Generare l'ambiente
Tramite terminale andare nella cartella in cui si trova la repository nel proprio sistema e digitare ```vagrant up```

Attendere la generazione dell'ambiente. Potrebbe richiedere diversi minuti per il download di tutti i software necessari.

### 3) Collegarsi al server
Una volta che la generazione dell'ambiente è completa, digitare ```vagrant ssh server``` per collegarsi al terminale del nodo server. Una volta nel terminale del nodo server far partitre il server digitando ```./server/runserver.sh```

Andare, dal proprio browser, all'indirizzo ```10.10.10.10:8080``` per utilizzare la web app d'esempio.
### NOTA PER WINDOWS
Se il proprio sistema non possiede un client ssh in %PATH%, il comando 'vagrant ssh' potrebbe non avere effetto. In tal caso è necessario scaricare un client ssh. E' consigliabile usare il software Putty collegandosi al nodo server all'indirizzo ```127.0.0.1:2211``` con ```username: vagrant``` e ```password: vagrant```

### Guida rapida
* ```vagrant up``` da terminale nella cartella della repository.
* ```vagrant ssh server``` da terminale e ```./server/runserver.sh``` da terminale del nodo server generato.
* ```10.10.10.10:8080``` dal proprio browser per utilizzare la web app d'esempio.

## API REST
La web app d'esempio fornita offre una API REST per l'ottenimento, cancellazione, creazione e aggiornamento delle sue risorse.
Per accedere a tali risorse, in formato json o xml, utilizzare un qualsiasi client REST come ad esempio Curl o Httpie sul proprio sistema.

###NB 
Se si è installato l'ambiente prima dell'introduzione al supporto delle chiamate REST è necessario creare di nuovo l'ambiente da zero (come sopra indicato), riscaricando la repository dal momento che è presente nuovo codice e nuovo software installato in fase di provision rispetto alla versione precedente.


### Alcuni esempi di utilizzo delle API REST (client REST usato negli esempi: Curl)
* Ottenere la lista dei Generi in formato json: ```curl -X GET -H "Accept: application/json" http://10.10.10.10:8080/api-rest/generi/```
* Ottenre la lista dei Film in formato xml: ```curl -X GET -H "Accept: application/xml" http://10.10.10.10:8080/api-rest/film/```
* Ottenere il Film con chiave primaria 1 in formato json: ```curl -X GET -H "Accept: application/json" http://10.10.10.10:8080/api-rest/film/1/```
* Cancellare il Genere con chiave primaria 3: ```curl -X DELETE http://10.10.10.10:8080/api-rest/generi/3/```
* Creare un nuovo Genere: ```curl -X POST -H "Content-Type: application/json" http://10.10.10.10:8080/api-rest/generi/ -d '{"nome":"HORROR"}'```
* Aggiornare un Genere con chiave primaria 5: ```curl -X PUT -H "Content-Type: application/json" http://10.10.10.10:8080/api-rest/generi/5/ -d '{"nome":"DRAMMATICO"}'```

### NOTA PER WINDOWS
Se il sistema dà errori di parsing json quando si vuole creare o aggiornare una risorsa, scrivere il json da passare in POST o PUT come segue: ```... -d "{\"nome\":\"DRAMMATICO\"}"```

