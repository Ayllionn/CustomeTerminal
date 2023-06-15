from CustomTerm import CustomTerminal

"""1er utilisation basique du terminal faites vos fonctions avec vos agruments"""
def test1():
    """sert a affiché un message""" #ajouté une doc a votre commande pour que cela s'affiche dans la commande help du terminal
    print('Oui je fonctionne bien')

def calc_cmd(operateur, a, b): #mettez les différent argument que votre fonction nécéssite comme d'habitude par contre les argument serrons forcément du type 'str' alors si vous voulez du int par exemple il faudra faire de la conversion et de la gestion d erreur
    """permet de faire une opération avec 2 nombre
    :arg 3
    operateur : + ou - ou / ou * ou * etc...
    a : 1er nombre
    b : 2eme nombre""" #il est important de mettre exactement le nom de vos argument ici pour que l'utilisateur puisse utilisé le terminal de façons plus poussé
    print(f"{a}{operateur}{b}" + " = " + calc(f"{a}{operateur}{b}"))

term = CustomTerminal() #création d'une instance du terminal
# option dispo 'terminal_name permet de donné un nom a votre terminal, search soit 'o' ou 'n' pour oui ou non. cette option permet de savoir que si une commande est
#pas reconnue alors elle serra demande ou non au système d'éxploitation, panel True ou False permet de retiré ou laissé le pannel et le blaze du dev dans le terminal'

term.add_command(fonction=test1) #permet d'ajouté une fonction comme commande au terminal seulement l'argument fonction est obligatoir
term.add_command(calc_cmd, "calc")

term.start() #lance le terminal

"""
commande a tester dans le terminal de l'application :

help
help print
help calc

print
calc - 5 1
calc / --b 0 --a 5
"""