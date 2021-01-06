import os

W, H = os.get_terminal_size()

WELCOME = ["", "Bienvenue dans l'apprentisseur de poèmes", "", "Choisissez votre poème", ""]
HELP = ["", "Appuyez sur \"x\" lorsque vous avez oublié le vers suivant", "", "Appuyer sur n'importe quelle autre touche dévoilera la prochaine ligne", ""]

KEYWORDS = ["<start>", "<titre>", "<auteur>", "<end>"]



def read():
    with open("poemes.txt") as f:
        data = [datum.strip() for datum in f.readlines()]
        for n, i in enumerate(data):
            if i == "" and data[n - 1] == "":
                data.pop(n)
                data.insert(n, "...")
        data = [datum for datum in data if datum]

    return data



def poem_selector(data):
    
    #get relevant indexes
    n_poeme = 0
    index_cache = []
    d_n_poem = {}
    
    for n, i in enumerate(data):
        if i in KEYWORDS:
            index_cache.append(n)
        if len(index_cache) == 4:
            d_n_poem[n_poeme] = index_cache[:]
            n_poeme += 1
            index_cache = []
    
    #choose poem
    print("")
    
    for n, indexes in d_n_poem.items():
        autor = data[indexes[1] + 1]
        name = data[indexes[2] + 1]
        print(str(n).rjust(3), "->", autor, "par", name)
    
    while True:
        try:
            print("")
            user_input = int(input("Poème numéro : "))
            start_index = d_n_poem[user_input][0]
            end_index = d_n_poem[user_input][3]
            return data[start_index : end_index]
            
        except (ValueError, KeyError):
            print("Mauvais numéro...")
    
    print(d_n_poem)
    
    
            
            
def cacher(poem):
    while poem:
        new_line = poem.pop(0)
        if new_line not in KEYWORDS:
            fake_input = input()
            print(new_line)
            

def main():
    data = read()
    
    for msg in WELCOME:
        print(msg.center(W, "."))
        
    poem = poem_selector(data)
    
    print("")
    
    for msg in HELP:
        print(msg.center(W, "-"))
    
    cacher(poem)



if __name__ == "__main__":
    main()