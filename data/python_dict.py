PYTHON_DICT = [
    {
        "name": "print()",
        "description": "Affiche un message dans la console.",
        "details": "C'est la première fonction que tout le monde apprend. Tu peux lui donner autant de valeurs que tu veux, séparées par des virgules. Par défaut, elles s'affichent avec un espace entre elles et un saut de ligne à la fin — mais tu peux changer ça avec sep= et end=.",
        "example": 'print("Bonjour", "Alice")     # -> Bonjour Alice\nprint("Chargement", end="...")  # -> Chargement...',
        "doc": "https://docs.python.org/3/library/functions.html#print"
    },
    {
        "name": "len()",
        "description": "Donne le nombre d'éléments dans une collection.",
        "details": "Fonctionne sur tout ce qui contient des éléments : une liste, une chaîne de caractères, un dictionnaire... C'est l'équivalent de demander 'combien y a-t-il de choses ici ?'",
        "example": 'len("Bonjour")    # -> 7 (lettres)\nlen([10, 20, 30]) # -> 3 (éléments)',
        "doc": "https://docs.python.org/3/library/functions.html#len"
    },
    {
        "name": "range()",
        "description": "Génère une suite de nombres pour faire des boucles.",
        "details": "Imagine que tu veux répéter quelque chose 5 fois, ou compter de 1 à 10 : c'est range() qu'il te faut. Tu peux lui donner un début, une fin et un pas (intervalle entre chaque nombre).",
        "example": 'for i in range(3):          # 0, 1, 2\nfor i in range(1, 6):       # 1, 2, 3, 4, 5\nfor i in range(0, 10, 2):   # 0, 2, 4, 6, 8',
        "doc": "https://docs.python.org/3/library/functions.html#func-range"
    },
    {
        "name": "type()",
        "description": "Indique de quel type est une valeur.",
        "details": "Très utile quand tu débogues et que tu ne sais plus ce que contient une variable. Python te répond avec le type exact : int, str, list, etc.",
        "example": 'type(42)        # -> <class "int">\ntype("bonjour") # -> <class "str">\ntype([1, 2])    # -> <class "list">',
        "doc": "https://docs.python.org/3/library/functions.html#type"
    },
    {
        "name": "int()",
        "description": "Convertit une valeur en nombre entier.",
        "details": "Utile notamment pour convertir ce que l'utilisateur tape au clavier (toujours une chaîne) en nombre. Attention : int(3.9) donne 3, pas 4 — il coupe, il n'arrondit pas.",
        "example": 'int("42")    # -> 42\nint(3.9)     # -> 3  (pas d\'arrondi)\nint("0", 2)  # -> 0  (binaire vers entier)',
        "doc": "https://docs.python.org/3/library/functions.html#int"
    },
    {
        "name": "float()",
        "description": "Convertit une valeur en nombre décimal.",
        "details": "Transforme un entier ou une chaîne de caractères en nombre à virgule. Attention aux imprécisions courantes : 0.1 + 0.2 ne donne pas exactement 0.3 en Python (c'est une limite des ordinateurs, pas de Python).",
        "example": 'float("3.14")  # -> 3.14\nfloat(5)       # -> 5.0\nfloat("1e3")   # -> 1000.0',
        "doc": "https://docs.python.org/3/library/functions.html#float"
    },
    {
        "name": "str()",
        "description": "Convertit une valeur en texte.",
        "details": "Indispensable pour assembler du texte avec des nombres. En Python, on ne peut pas directement écrire 'Tu as ' + 25 + ' ans' — il faut d'abord convertir 25 en chaîne avec str(25).",
        "example": 'str(100)    # -> "100"\nstr(True)   # -> "True"\n"Tu as " + str(25) + " ans"  # -> "Tu as 25 ans"',
        "doc": "https://docs.python.org/3/library/functions.html#func-str"
    },
    {
        "name": "bool()",
        "description": "Convertit une valeur en True ou False.",
        "details": "En Python, presque tout peut être évalué comme vrai ou faux. Sont considérés comme False : 0, une liste vide [], une chaîne vide '', et None. Tout le reste est True.",
        "example": 'bool(1)     # -> True\nbool(0)     # -> False\nbool([])    # -> False  (liste vide)\nbool("hi")  # -> True',
        "doc": "https://docs.python.org/3/library/functions.html#bool"
    },
    {
        "name": "list()",
        "description": "Crée une liste à partir d'une autre collection.",
        "details": "Permet de transformer n'importe quelle suite d'éléments en liste modifiable. Très pratique pour convertir le résultat de range() ou pour copier une liste existante.",
        "example": 'list(range(5))   # -> [0, 1, 2, 3, 4]\nlist("abc")      # -> ["a", "b", "c"]',
        "doc": "https://docs.python.org/3/library/functions.html#func-list"
    },
    {
        "name": "dict()",
        "description": "Crée un dictionnaire (collection clé → valeur).",
        "details": "Un dictionnaire, c'est comme un annuaire : à chaque nom (clé) correspond une information (valeur). Tu peux le créer avec des arguments nommés ou depuis une liste de paires.",
        "example": 'dict(nom="Alice", age=25)       # -> {"nom": "Alice", "age": 25}\ndict([("a", 1), ("b", 2)])      # -> {"a": 1, "b": 2}',
        "doc": "https://docs.python.org/3/library/functions.html#func-dict"
    },
    {
        "name": "tuple()",
        "description": "Crée un tuple : une liste qu'on ne peut pas modifier.",
        "details": "Un tuple ressemble à une liste, mais une fois créé, on ne peut plus le changer. Utile pour stocker des données fixes, comme les coordonnées GPS ou les couleurs RGB.",
        "example": 'tuple([1, 2, 3])  # -> (1, 2, 3)\ncoordonnees = (48.8566, 2.3522)  # Paris, immuable\ntuple([42]) # -> (42,)',
        "doc": "https://docs.python.org/3/library/functions.html#func-tuple"
    },
    {
        "name": "set()",
        "description": "Crée un ensemble qui supprime automatiquement les doublons.",
        "details": "Si tu as une liste avec des répétitions et que tu veux juste les valeurs uniques, set() fait ça en une ligne. C'est aussi très rapide pour vérifier si un élément est présent.",
        "example": 'set([1, 2, 2, 3, 3])  # -> {1, 2, 3}\n"a" in set(["a","b"]) # -> True  (vérification rapide)',
        "doc": "https://docs.python.org/3/library/functions.html#func-set"
    },
    {
        "name": "input()",
        "description": "Demande à l'utilisateur de saisir quelque chose au clavier.",
        "details": "Le programme se met en pause et attend que l'utilisateur tape quelque chose puis appuie sur Entrée. Important : le résultat est toujours du texte, même si l'utilisateur tape un nombre — pense à le convertir !",
        "example": 'prenom = input("Comment tu t\'appelles ? ")\nage = int(input("Quel est ton âge ? "))  # convertir en nombre !',
        "doc": "https://docs.python.org/3/library/functions.html#input"
    },
    {
        "name": "enumerate()",
        "description": "Parcourt une liste en donnant à la fois l'index et la valeur.",
        "details": "Quand tu veux savoir 'à quelle position se trouve cet élément' pendant une boucle, enumerate() est la solution propre. Tu évites ainsi de gérer un compteur manuellement.",
        "example": 'fruits = ["pomme", "banane", "cerise"]\nfor i, fruit in enumerate(fruits):\n    print(i, fruit)\n# 0 pomme / 1 banane / 2 cerise',
        "doc": "https://docs.python.org/3/library/functions.html#enumerate"
    },
    {
        "name": "zip()",
        "description": "Associe les éléments de deux listes côte à côte.",
        "details": "Imagine deux colonnes dans un tableau : zip() les relie ligne par ligne. Si les listes n'ont pas la même longueur, il s'arrête à la plus courte.",
        "example": 'noms = ["Alice", "Bob"]\nnotes = [18, 14]\nfor nom, note in zip(noms, notes):\n    print(nom, "->", note)\n# Alice -> 18 / Bob -> 14',
        "doc": "https://docs.python.org/3/library/functions.html#zip"
    },
    {
        "name": "map()",
        "description": "Applique une même fonction à chaque élément d'une liste.",
        "details": "C'est comme dire 'fais cette opération sur chaque élément, sans écrire de boucle'. Pratique pour transformer une liste entière en une ligne.",
        "example": 'list(map(int, ["1", "2", "3"]))    # -> [1, 2, 3]\nlist(map(str.upper, ["a", "b"]))   # -> ["A", "B"]',
        "doc": "https://docs.python.org/3/library/functions.html#map"
    },
    {
        "name": "filter()",
        "description": "Garde uniquement les éléments qui satisfont une condition.",
        "details": "Comme un tamis : tu lui donnes une liste et une condition, il ne garde que les éléments pour lesquels la condition est vraie.",
        "example": 'nombres = [1, 2, 3, 4, 5, 6]\npairs = list(filter(lambda x: x % 2 == 0, nombres))\n# -> [2, 4, 6]',
        "doc": "https://docs.python.org/3/library/functions.html#filter"
    },
    {
        "name": "sorted()",
        "description": "Retourne une nouvelle liste triée, sans modifier l'originale.",
        "details": "Contrairement à .sort() qui modifie la liste en place, sorted() crée une nouvelle liste. Tu peux trier dans l'ordre inverse avec reverse=True, ou selon un critère personnalisé avec key=.",
        "example": 'sorted([3, 1, 4, 1, 5])              # -> [1, 1, 3, 4, 5]\nsorted(["banane","kiwi","abricot"])   # -> alphabétique\nsorted(mots, key=len)                # -> du plus court au plus long',
        "doc": "https://docs.python.org/3/library/functions.html#sorted"
    },
    {
        "name": "reversed()",
        "description": "Parcourt une liste dans le sens inverse.",
        "details": "Retourne les éléments à l'envers, sans modifier la liste originale. Utile quand tu veux afficher ou traiter une liste en sens inverse.",
        "example": 'list(reversed([1, 2, 3]))  # -> [3, 2, 1]\nfor lettre in reversed("abc"):\n    print(lettre)  # c, b, a',
        "doc": "https://docs.python.org/3/library/functions.html#reversed"
    },
    {
        "name": "sum()",
        "description": "Calcule la somme de tous les éléments d'une liste.",
        "details": "Additionne tous les nombres d'un itérable. Tu peux aussi lui donner une valeur de départ à ajouter au total.",
        "example": 'sum([10, 20, 30])      # -> 60\nsum([1, 2, 3], 100)    # -> 106  (commence à 100)',
        "doc": "https://docs.python.org/3/library/functions.html#sum"
    },
    {
        "name": "max()",
        "description": "Trouve la valeur la plus grande dans une liste.",
        "details": "Fonctionne avec des nombres, mais aussi avec des chaînes (ordre alphabétique). Avec key=, tu peux définir ce que 'le plus grand' signifie.",
        "example": 'max([5, 2, 9, 1])           # -> 9\nmax("abc", "xyz", "mno")    # -> "xyz"\nmax(prenoms, key=len)       # -> le prénom le plus long',
        "doc": "https://docs.python.org/3/library/functions.html#max"
    },
    {
        "name": "min()",
        "description": "Trouve la valeur la plus petite dans une liste.",
        "details": "L'exact opposé de max(). Même fonctionnement, même options. Très pratique pour trouver le minimum d'un ensemble de données.",
        "example": 'min([5, 2, 9, 1])           # -> 1\nmin(prenoms, key=len)       # -> le prénom le plus court',
        "doc": "https://docs.python.org/3/library/functions.html#min"
    },
    {
        "name": "abs()",
        "description": "Retourne la valeur absolue (toujours positive) d'un nombre.",
        "details": "Utile quand tu veux la 'distance' entre deux valeurs peu importe le sens. abs(-5) et abs(5) donnent tous les deux 5.",
        "example": 'abs(-42)    # -> 42\nabs(3.14)   # -> 3.14\nabs(-8)     # -> 8',
        "doc": "https://docs.python.org/3/library/functions.html#abs"
    },
    {
        "name": "round()",
        "description": "Arrondit un nombre décimal au nombre de chiffres souhaité.",
        "details": "Par défaut, arrondit à l'entier le plus proche. Tu peux préciser combien de décimales tu veux garder. Pratique pour afficher des prix ou des résultats propres.",
        "example": 'round(3.14159)      # -> 3\nround(3.14159, 2)   # -> 3.14\nround(9.876, 1)     # -> 9.9',
        "doc": "https://docs.python.org/3/library/functions.html#round"
    },
    {
        "name": "pow()",
        "description": "Calcule la puissance d'un nombre (x exposant y).",
        "details": "pow(2, 10) calcule 2 à la puissance 10, comme 2**10. Avec un troisième argument, il calcule le résultat modulo ce nombre — utile en mathématiques et en cryptographie.",
        "example": 'pow(2, 8)        # -> 256  (2 puissance 8)\npow(3, 3)        # -> 27   (3 au cube)',
        "doc": "https://docs.python.org/3/library/functions.html#pow"
    },
]