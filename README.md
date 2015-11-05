# cq-formation-spark
Introduction à l'analyse de données avec Spark sur une grappe de calcul

## Prérequis

Les notes de cours et les exercices de cette formation sont prévues
pour être exécutés soit sur une grapppe de calcul ou encore directement
sur votre ordinateur.

### Exécution sur une grappe de calcul

1. Installez sur votre ordinateur [X2Go](http://wiki.x2go.org/doku.php).
2. Configurez une session vers la grappe de calcul sur lequel se donne la formation. Consultez la vidéo [Créer une [Créer une session interactive avec X2Go](https://www.youtube.com/watch?v=8CwtbgQsrFg) pour savoir comment faire.

### Exécution sur votre ordinateur personnel

Vous aurez besoin d'installer sur votre ordinateur :  
* [Python 2.7.x](https://www.python.org/downloads/)
* [R 3.x](https://www.r-project.org/)
* [Java JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* [Apache Spark 1.5.1](http://spark.apache.org/)

#### Environnement Python

Nous vous recommandons d'installer les modules Python à l'intérieur d'un [environnement virtuel](https://pypi.python.org/pypi/virtualenv). Vous aurez besoin d'installer les modules suivants:  
* [jupyter](https://pypi.python.org/pypi/jupyter)
* [Pillow](https://pypi.python.org/pypi/Pillow)

### Jeux de données

Exécutez le contenu du notebook 0 - Configuration.

## Exécution sur une grappe de calcul

1. Lancez une session interactive X2Go sur la grappe de calcul.
2. À partir d'un terminal, réservez une session interactives à l'aide de Moab. Ajustez le temps d'exécution (`-l walltime`), le nombre de noeuds (`-l nodes`) et le compte (`-A`) en fonction du système et des paramètres fournies par la formation.  
	```
	msub -I -l walltime=02:00:00 -l nodes=1:ppn=8 -A cluster-users
	```
3. Procédez à l'extraction du contenu de l'archive du cours qui est dans votre compte:  
	```
	tar xvf cours_spark.tar.gz
	```
4. Lancez le script `cours_spark.sh` dans la session interactive Moab.  
	```
	source cours_spark.sh
	```
5. Cliquez sur le lien suivant le message `The IPython Notebook is running at`, par exemple:  

	```
	starting org.apache.spark.deploy.master.Master, logging to /tmp/spark-user2-org.apache.spark.deploy.master.Master-1-r109-n18.out
	starting org.apache.spark.deploy.worker.Worker, logging to /tmp/spark-user2-org.apache.spark.deploy.worker.Worker-1-r109-n18.out
	[I 16:08:18.406 NotebookApp] Serving notebooks from local directory: /home/user2/cours_spark
	[I 16:08:18.406 NotebookApp] 0 active kernels 
	[I 16:08:18.406 NotebookApp] The IPython Notebook is running at: http://10.225.109.18:8888/
	[I 16:08:18.406 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
	```

## Exécution locale

