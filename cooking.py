from read_file_class import ReadRecipesFile
import sys
from pprint import pprint

cooking = ReadRecipesFile()


def get_shop_list_by_dishes():
    count_dishes = int(input('Input the quantity of dishes : '))
    count, count2, count3 = 0, 0, 0
    ing_dishes, menu2, menu3 = [], [], []
    menu_dict = {}
    while count < count_dishes:
        dishes = input(f'Input the name of dishes №{count+1} : ')
        count += 1
        try:
            ing_dishes.append(cooking.cook_book[dishes])
        except:
            print('No such dish!')
            sys.exit()
    person_count = int(input('Enter the number of people : '))
    while count2 < len(ing_dishes):
        for x in ing_dishes[count2]:
            for k, v in x.items():
                menu2.append(k)
                menu3.append(v)
        count2 += 1
    while count3 <= len(menu3)-1:
        menu4 = {menu3[count3]:{'measure': menu3[count3+2], 'quantity':menu3[(count3+1)]*person_count}}
        count3 += 3
        menu_dict.update(menu4.copy())
    pprint(menu_dict)


get_shop_list_by_dishes()
