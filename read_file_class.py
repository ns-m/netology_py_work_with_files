from itertools import islice


class ReadRecipesFile:

    def __init__(self):
        with open('recipes.txt', encoding='utf-8') as f:
            cook_book = {}
            while True:
                dish_name = f.readline().rstrip()
                try:
                    amount_of_ingrs = int(f.readline().rstrip())
                except ValueError:
                    pass
                name_of_ingrs = list(islice(f, amount_of_ingrs))
                f.readline()

                if not dish_name or not name_of_ingrs:
                    break

                ingrs = []
                for name in name_of_ingrs:
                    value = name.split(' | ')
                    val = {'ingredient_name': value[0], 'quantity': int(value[1]),
                           'measure': value[2].replace('\n', '')}
                    ingrs.append(val)
                    cook_book[dish_name] = [*ingrs]

                self.cook_book = cook_book