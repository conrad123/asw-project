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
