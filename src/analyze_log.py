from reader import reader
from track_orders import TrackOrders


def analyze_log(path_to_file):
    customer_data = reader(path_to_file)
    data_list = TrackOrders()

    for name, order, day in customer_data:
        data_list.add_new_order(name, order, day)

    # most_ordered = data_list.get_most_ordered_dish_per_customer('maria')
    # burger_count = data_list.get_dish_count_by_customer(
    #     'arnaldo', 'hamburguer'
    #     )
    # never_ordered = data_list.get_never_ordered_per_customer('joao')
    # days_absent = data_list.get_days_never_visited_per_customer('joao')
