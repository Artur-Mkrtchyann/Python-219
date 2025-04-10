dictionary = {}
num_entries = int(input("Որքան բառ կցանկանաք ավելացնել dictionary-ում "))
for _ in range(num_entries):
    word = input("Գրեք բառը: ")
    meaning = input(f"Գրեք '{word}' բառի նշանակությունը: ")
    dictionary[word] = meaning
while True:
    query = input("\n Որ բառի նշանակությունն եք ուզում իմանալ (կամ 'exit' դուրս գալու համար): ")
    if query.lower() == 'exit':
        print("Ծրագիրը փակվում է.")
        break
    if query in dictionary:
        print(f"{query} բառը նշանակում է: {dictionary[query]}")
    else:
        print(f"{query} բառը չի գտնվել բառարանում.")
