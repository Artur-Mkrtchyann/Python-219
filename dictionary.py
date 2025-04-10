dictionary = {}
def add_word():
    word = input("Գրեք նոր բառը: ")
    meaning = input(f"Գրեք '{word}' բառի նշանակությունը: ")
    dictionary[word] = meaning
    print(f"{word} բառը հաջողությամբ ավելացված է մեր բառարանում.")

def update_word():
    word = input("Որ բառի նշանակությունն եք ցանկանում փոխել? ")
    if word in dictionary:
        new_meaning = input(f"Գրեք '{word}' բառի նոր նշանակությունը: ")
        dictionary[word] = new_meaning
        print(f"{word} բառի նշանակությունը հաջողությամբ փոխված է.")
    else:
        print(f"{word} բառը չկա բառարանում։")

def query_word():
    query = input("\n Ինչ բառի նշանակությունն եք ուզում իմանալ (կամ 'exit' դուրս գալու համար): ")
    
    if query.lower() == 'exit':
        return False 
    elif query in dictionary:
        print(f"{query} բառը նշանակում է: {dictionary[query]}")
    else:
        print(f"{query} բառը չի գտնվել մեր բառարանում.")
    
    return True
  
def show_all_words():
    if dictionary:
        print("\n Բառարանը պարունակում է հետևյալ բառերը:")
        for word, meaning in dictionary.items():
            print(f"{word}: {meaning}")
    else:
        print("Բառարանը դատարկ է!")

def exit_program():
    print("Ծրագիրը փակվում է.")
    exit()

def main_menu():
    while True:
        print("\n Բառարան՝ ընտրեք գործողություն:")
        print("1. Ավելացնել նոր բառ")
        print("2. Փոփոխել բառի նշանակությունը")
        print("3. Հարցնել բառի նշանակությունը")
        print("4. Ցուցադրել բոլոր բառերը")
        print("5. Փակել ծրագիրը")
        
        choice = input("Ընտրեք գործողությունը (1-5): ")
        
        if choice == '1':
            add_word()
        elif choice == '2':
            update_word()
        elif choice == '3':
            if not query_word():
                break
        elif choice == '4':
            show_all_words()
        elif choice == '5':
            exit_program()
        else:
            print("Սխալ ընտրություն, կրկնեք:")
            
main_menu()
