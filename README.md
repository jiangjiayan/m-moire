## TP2.6.3 Mise en oeuvre simplexe
Mettez en oeuvre l'algorithme du simplexe d'ecrit dans ce chapitre 2. En particulier, programmez les fonctions suivantes.

##### Le code sur python  
``` python

from fractions import Fraction

def initial_tableau(c, A, b):
    m, n = len(A), len(A[0])
    tableau = [[Fraction(0) for j in range(n+1)] for i in range(m+1)]
    for j in range(n):
        tableau[0][j] = -c[j]
    for i in range(m):
        for j in range(n):
            tableau[i+1][j] = A[i][j]
        tableau[i+1][-1] = b[i]
    return tableau

def pivot_col(tableau):
    m, n = len(tableau), len(tableau[0])
    j = 0
    for i in range(1, n):
        if tableau[0][i] < tableau[0][j]:
            j = i
    if tableau[0][j] >= 0:
        return -1
    return j

def pivot_row(tableau, col):
    m, n = len(tableau), len(tableau[0])
    ratios = []
    for i in range(1, m):
        if tableau[i][col] > 0:
            ratios.append((tableau[i][-1] / tableau[i][col], i))
    if not ratios:
        return -1
    return min(ratios)[1]

def pivot(tableau, row, col):
    pivot_value = tableau[row][col]
    m, n = len(tableau), len(tableau[0])
    for j in range(n):
        tableau[row][j] /= pivot_value
    for i in range(m):
        if i != row:
            factor = tableau[i][col]
            for j in range(n):
                tableau[i][j] -= factor * tableau[row][j]

def simplex(c, A, b):
    tableau = initial_tableau(c, A, b)
    while True:
        col = pivot_col(tableau)
        if col < 0:
            return tableau
        row = pivot_row(tableau, col)
        if row < 0:
            return "Problème non borné"
        pivot(tableau, row, col)
c = [3, 1, 2]
A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
b = [30, 24, 36]

tableau = simplex(c, A, b)

if isinstance(tableau, str):
    print(tableau)
else:
    print("Solution optimale: ", [row[-1] for row in tableau])
    print("Valeur de la fonction objectif: ", -tableau[0][-1])
    print("Tableau final:")
    for row in tableau:
        print([float(f) for f in row])

```
    
### Fonctions  
#### initial_tableau(c, A, b)  
Cette fonction construit le tableau 
initial à partir de la forme canonique 
d'un problème de programmation linéaire et renvoie 
le tableau initial qui sera utilisé pour l'algorithme du
simplexe. La fonction crée un tableau de dimensions 
(m+1) x (n+1) où m est le nombre de contraintes, 
n est le nombre de variables, et la dernière 
colonne est réservée pour les termes constants. 
La première ligne du tableau est remplie avec les 
coefficients négatifs de la fonction objectif. Les 
lignes suivantes correspondent aux contraintes du problème,
où chaque coefficient de la matrice A est copié dans 
le tableau et chaque terme constant est copié dans 
la dernière colonne.  

#### pivot_col(tableau)  
Cette fonction calcule la variable entrante pour le pivot.
Elle cherche la colonne avec le coefficient le plus négatif 
dans la première ligne du tableau, à l'exception de la dernière 
colonne qui correspond aux termes constants. Si tous les 
coefficients sont positifs ou nuls, cela signifie que la 
solution optimale a été atteinte et la fonction renvoie -1 pour 
signaler la fin de l'algorithme.

#### pivot_row(tableau, col)  
Cette fonction calcule la variable 
sortante pour le pivot. Elle calcule le rapport 
entre le terme constant de chaque contrainte et le coefficient 
de la variable entrante pour chaque ligne où le coefficient est 
strictement positif. Elle renvoie l'indice de la ligne 
correspondant au rapport le plus petit, qui sera la variable 
sortante pour le pivot. Si tous les coefficients sont nuls ou 
négatifs, cela signifie que le problème est non borné et la 
fonction renvoie -1.

#### pivot(tableau, row, col)  
Cette fonction effectue les opérations 
de mise à jour du tableau par rapport au pivot désigné. 
Elle divise la ligne du pivot par le coefficient de la 
variable entrante pour que le coefficient soit égal à 1. 
Ensuite, pour chaque ligne différente de celle du pivot, 
elle soustrait un multiple approprié de la ligne du pivot 
pour que le coefficient de la variable entrante soit nul. 
Ces opérations garantissent que la nouvelle solution satisfait 
toutes les contraintes du problème.
#### simplex(c, A, b)  
  
Cette fonction coordonne l'exécution des fonctions 
précédentes jusqu'à ce que la solution optimale 
soit atteinte ou que le problème soit déclaré non borné. 
Elle commence par construire le tableau initial en appelant 
initial_tableau. Ensuite, elle exécute une boucle 
infinie qui cherche la variable entrante et la 
variable sortante en appelant respectivement pivot_col et 
pivot_row. Si les deux fonctions renvoient des indices valides, 
elle appelle pivot pour effectuer les opérations de mise à 
jour du tableau. Si pivot_col renvoie -1, cela signifie que la 
solution optimale a été atteinte et la fonction renvoie le 
tableau final. Si pivot_row renvoie -1, cela signifie que 
le problème est non borné et la fonction renvoie une 
chaîne de caractères signalant ce fait.
### Utilisation  
Le programme principal est dans le fichier TP2.py. 
Vous pouvez l'exécuter avec les arguments suivants :
```python
c = [3, 1, 2]
A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
b = [30, 24, 36]

tableau = simplex(c, A, b)
```  
où c, A, et b sont les vecteurs et matrices correspondant à la 
forme canonique d'un problème de programmation linéaire. 
Les éléments de c, A, et b doivent être séparés par des espaces.  

### Résultat
```
Solution optimale:  [28.0, 18.0, 4.0, 8.0]
Valeur de la fonction objectif:  -28.0
Tableau final:
[0.0, 0.0, 0.16666666666666666, 28.0]
[0.0, 0.0, 0.5, 18.0]
[0.0, 1.0, 2.6666666666666665, 4.0]
[1.0, 0.0, -0.16666666666666666, 8.0]
```
Car la Valeur -28 est le première qui est moins 0,donc son maximum est 28. 
