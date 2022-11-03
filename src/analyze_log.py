import csv
from reader import reader
from track_orders import TrackOrders


def most_ordered_by_customer(customer, data):
    pass


def dish_count_by_customer(customer, data):
    pass


# def never_ordered_by_customer(customer, data):
#     menu = set(
#         ['pizza', 'hamburguer', 'coxinha', 'misto-quente']
#         )
#     dishes_tried = set()

#     for name, dish, _ in data:
#         if name == customer:
#             dishes_tried.add(dish)

#     return menu.difference(dishes_tried)


# def days_absent_by_customer(customer, data):
#     working_days = set(
#         ['segunda-feira', 'terça-feira', 'quarta-feira',
#         'quinta-feira', 'sexta-feira', 'sabado']
#         )
#     days_visited = set()

#     for name, _, day in data:
#         if name == customer:
#             days_visited.add(day)

#     return working_days.difference(days_visited)


def analyze_log(path_to_file):
    customer_data = reader(path_to_file)
    data_list = TrackOrders()

    for name, order, day in customer_data:
        data_list.add_new_order(name, order, day)

    most_ordered = data_list.get_most_ordered_dish_per_customer('maria')
    burger_count = data_list.get_dish_count_by_customer('arnaldo', 'hamburguer')
    never_ordered = data_list.get_never_ordered_per_customer('joao')
    days_absent = data_list.get_days_never_visited_per_customer('joao')
