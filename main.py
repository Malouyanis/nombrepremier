"""Module pour vérifier si un nombre est premier."""

def isprime(p):
    """Vérifie si un nombre entier p est un nombre premier."""
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(p**0.5) + 1, 2):
        if p % i == 0:
            return False
    return True

def main():
    """Affiche les nombres premiers de 0 à 99."""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()  # Pour terminer la ligne après la liste des nombres premiers

if __name__ == "__main__":
    main()
