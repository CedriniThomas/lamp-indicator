# lamp-indicator
## English
This indicator for Ubuntu Unity will help you !
It displays a traffic light changing on apache2 status. You can now start, stop and restart your apache2 and mysql services with a simple click and watch their status on your screen.

To add this indicator works on login, just type Startup Applications on the dash and choose the application with this name. Then, click "Add" on the right side of the little window just opened and fill the form in : 
  - Name : (whatever you want) Lamp-Indicator
  - Command : python pathToYourPyFile/lamp-indicator.py
  - Comment : (whatever you want again) Shortcut to lamp informations

## French
Ceci est un indicateur pour le bureau Unity d'Ubuntu. Il ira se placer en haut à droite de votre bureau à côté de l'heure au démarrage de votre session (si vous le lui demandez gentiment).
Il affiche un feu tricolore représentant l'état dans lequel se trouvent apache et mysql. Vous pourrez alors voir d'un coup d'oeil si votre serveur local est en route et le lancer d'un clic (vous pourrez aussi l'arrêter et le relancer au besoin).

Pour lancer le script python rien de plus simple, aller dans la console dans le dossier de votre script (<code>cd le_chemin_du_dossier</code>) et lancer la commande suivante :
<pre><code>python lamp-indicator.py &</code></pre>

Pour l'ajouter en démarrage automatique, entrez dans le Dash "Applications au démarrage" et choisissez l'application portant ce nom, une petite fenêtre s'ouvre dans laquelle 3 boutons sont disponibles sur la droite, choisissez "Ajouter" et remplissez le petit formulaire qui s'affiche :
  - Nom : (ce que vous voulez) Lamp-Indicator
  - Commande : python cheminVersVotreFichierPython/lamp-indicator.py
  - Commentaire : (ce que vous voulez) Raccourcis vers lamp-indicator
