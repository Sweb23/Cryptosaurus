#include <stdio.h>
#include <stdlib.h>

int main() {
    // Commande pour exécuter le script Python
    char* commande = "python main.py";

    // Exécute le script Python en utilisant la fonction système
    int resultat = system(commande);

    // Vérifie si l'exécution s'est terminée avec succès
    if (resultat == 0) {
        printf("Cryptosaurus was successfully launched.\n");
    } else {
        printf("An error occured.\n");
    }

    return 0;
}
