from read_file_class import ReadRecipesFile
import sys
cooking = ReadRecipesFile()

def get_shop_list_by_dishes():
    count_dishes = int(input('Input the quantity of dishes : '))
    count = 0
    ing_dishes = []
    while count < count_dishes:
        dishes = input(f'Input the name of dishes №{count+1} : ')
        count += 1
        try:
            ing_dishes.append(cooking.cook_book[dishes])
        except:
            print('No such dish!')
            sys.exit()
    person_count = int(input('Enter the number of people : '))
    ing_menu = {ing_dishes[0]:{ing_dishes[1],ing_dishes[2]}}
    print(ing_menu)

get_shop_list_by_dishes()