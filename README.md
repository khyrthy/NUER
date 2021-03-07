# Nao's Universe : Endless Run

[Logo du jeu](https://github.com/khyrthy/NUER/raw/master/Assets/GUI/Title.png "Logo du jeu")

(FR) Un jeu où il faut sauter par-dessus des boites et ramasser des pièces.  
(EN) A game about jumping around crates and collecting coins.

# Français (France)

## Téléchargements
Les téléchargements sont disponnibles directement dans l'onglet [*Releases*](https://github.com/khyrthy/NUER/releases) ou bien sur [la page du site](http://khyrthy.fr.nf/nuer/)

## Construire depuis la source
Il est également possible de construire depuis la source.

### Pré-requis
Voici ce dont vous aurez besoin pour construire Nao's Universe : Endless Run :
* Python (3.6+)
* Pip
* Pygame
* Cx_Freeze
* Git (Windows et MacOS)

#### Python 3.x (3.6+)

##### Sous Linux :
python3 est préinstallé sur la grande majorité des distributions récentes (Ubuntu 16+, etc.)
S'il n'est pas installé, installez les paquets `python3` et `python3-pip`:
```bash
sudo apt install python3 python3-pip
sudo yum install python3 python3-pip
```
##### Sous Windows (7+) et MacOS (10.11+) :
Téléchargez et installez Python depuis [le site officiel de Python](https://www.python.org/downloads/release/python-392/)
N'oubliez pas de cocher les options *Pip* et *Add to PATH* dans la fenêtre de l'installeur

#### Pygame (1.9.2+)

##### Sous Windows et MacOS :
Dans une fenêtre CMD, installez pygame grâce à Pip :
```bat
python -m pip install pygame--user
```
##### Sous Linux :
Vous pouvez installer le paquet `python3-pygame` avec votre gestionnaire de paquets
```bash
sudo apt install python3-pygame
sudo yum install python3-pygame
```

#### cx_Freeze
Installez `cx_freeze` grâce à pip (erreurs possibles)
##### Windows et MacOS :
```bash
python -m pip install cx_freeze
```
##### Linux :
```bash
pip3 install cx_freeze
```
#### Git (Windows et MacOS)
##### Windows et MacOS (Git-Scm) :
Téléchargez et installez l'installeur de [Git](https://git-scm.com/downloads)

##### MacOS (Homebrew)
Installez `git` avec Homebrew :
```bash
brew install git
```
### Construire
Maintenant que nous avons tous les pré-requis, passons à l'installation

#### Cloner le repo :
Rien de plus simple, ouvrez une fenêtre de terminal (ou une fenêtre Git-bash si vous disposez de Git-SCM)
```bash
git clone https://github.com/khyrthy/NUER
```
Ceci clonera le repo dans un dossier, que nous allons nommer *folder*

#### Fichier Setup.py:
C'est le fichier qui nous intéressera pour la construction.  
**Si vous êtes sous Windows, remplacez `base = None` par `base = "Win32GUI"`***

#### Construire
Pour construire, rien de plus simple, éxécutez cette commande dans le dossier du code :
##### Windows et MacOS
```bash
python ./setup.py build
```
##### Linux
```bash
python3 ./setup.py build
```
