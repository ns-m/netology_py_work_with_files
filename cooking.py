from read_file_class import ReadRecipesFile
cooking = ReadRecipesFile()

# cook_dict = {cooking.__dict__}
# for cook in cook_dict:
#     print(cook.keys())

def get_shop_list_by_dishes(dishes, person_count):
    count_dishes = int(input('Input dishes count : '))
    count = 0
    ing_dishes = []
    while count < count_dishes:
        dishes = input('Input dishes : ')
        count += 1
        ing_dishes.append(cooking.__dict__[dishes])
    person_count = int(input('Input person count : '))
    print(ing_dishes, person_count)

get_shop_list_by_dishes(0, 2)