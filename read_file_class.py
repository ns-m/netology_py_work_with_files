from itertools import islice

class ReadRecipesFile:
    def __init__(self):
        with open('recipes.txt', encoding='utf-8') as f:

            while True:
                cook_book = {}
                n = f.readline().rstrip()
                try:
                    c = int(f.readline().rstrip())
                except ValueError:
                    pass
                d_n = list(islice(f, c))
                f.readline()

                if not n or not d_n:
                    break

                ingrs = []
                for d in d_n:
                    value = d.split(' | ')
                    val = {'ingredient_name': value[0], 'quantity': int(value[1]),
                           'measure': value[2].replace('\n', '')}
                    ingrs.append(val)
                cook_book[n] = [*ingrs]

                print(cook_book)