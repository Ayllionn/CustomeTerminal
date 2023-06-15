from CustomTerm import CustomTerminal

"""dans la même idée vous pouvée directement initié le terminal avec toute les commandes sans passer par la méthode add_commande"""

def test1():
    """test d'une fonction"""
    print('ça fonctionne bien')

term = CustomTerminal(terminal_name="test", print=test1) #cela peut fonctionné aussi avec des disctionnaires **{cmd:fonction, cmd:fonction, etc...}

term.start()