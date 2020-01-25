
def read_file_rec():
    cook_dict = {}
    with open('recipes.txt', encoding='utf-8') as txt:
        while True:
            dishes_name = txt.readline()[1]
        for line in txt:
            key, *value = line
            cook_dict[key] = value
        print(cook_dict)

read_file_rec()