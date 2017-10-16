cook_book = { }

def cook_book_filling(file_name):
    with open(file_name) as f:
        ingridients_list = []
        for line in f:
            dish = line.strip()
            ingridient_quantity = int(f.readline().strip())
            for i in range(ingridient_quantity):
             ingridients = {}
             ingridients_name = f.readline().strip()
             temp_list = ingridients_name.split(" | ")
             ingridients["ingridient_name"] = temp_list[0]
             ingridients["quantity"] = temp_list[1]
             ingridients["measure"] = temp_list[2]
             ingridients_list.append(ingridients)
            cook_book[dish] = ingridients_list
            ingridients_list = []
            f.readline()
            
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
          new_shop_list_item = dict(ingridient)

          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)
