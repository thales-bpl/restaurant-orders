from src.reader import reader
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    customer_data = reader(path_to_file)
    data_list = TrackOrders()

    for name, order, day in customer_data:
        data_list.add_new_order(name, order, day)

    idx_1 = data_list.get_most_ordered_dish_per_customer('maria')
    idx_2 = data_list.get_dish_count_by_customer(
        'arnaldo', 'hamburguer'
        )
    idx_3 = data_list.get_never_ordered_per_customer('joao')
    idx_4 = data_list.get_days_never_visited_per_customer('joao')

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{idx_1}\n{idx_2}\n{idx_3}\n{idx_4}")
