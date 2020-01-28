from read_file_class import ReadRecipesFile
import sys

cooking = ReadRecipesFile()

def get_shop_list_by_dishes():
    count_dishes = int(input('Input the quantity of dishes : '))
    count = 0
    ing_dishes = []
    menu = {}
    while count < count_dishes:
        dishes = input(f'Input the name of dishes №{count+1} : ')
        count += 1
        try:
            # ing_dishes.append(cooking.cook_book[dishes])
            menu.update(cooking.cook_book[dishes])
        except:
            print('No such dish!')
            sys.exit()
    person_count = int(input('Enter the number of people : '))
    count2 = 0
    # for ing in ing_dishes:
    #     print(ing)
    for x in ing_dishes[0]:
        for k, v in x.items():
            print(k, v)
        # k = ing[count2]['ingredient_name']
        # v = ing[count2].items()


    print(menu)

get_shop_list_by_dishes()