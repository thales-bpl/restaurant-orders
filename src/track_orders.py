class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append(customer, order, day)

    def get_most_ordered_dish_per_customer(self, customer):
        order_count_dict = {}
        most_frequent = self._data[0][1]

        for name, dish, _ in self._data:
            if name == customer:
                if dish not in order_count_dict:
                    order_count_dict[dish] = 1
                else:
                    order_count_dict[dish] += 1
            
                if order_count_dict[dish] > order_count_dict[most_frequent]:
                    most_frequent = dish

        return most_frequent

    def get_never_ordered_per_customer(self, customer):
        menu = set(
            ['pizza', 'hamburguer', 'coxinha', 'misto-quente']
            )
        dishes_tried = set()

        for name, dish, _ in self._data:
            if name == customer:
                dishes_tried.add(dish)

        return menu.difference(dishes_tried)

    def get_days_never_visited_per_customer(self, customer):
        working_days_set = set(
            ['segunda-feira', 'terça-feira', 'quarta-feira',
            'quinta-feira', 'sexta-feira', 'sabado']
            )
        days_visited_set = set()

        for name, _, day in self._data:
            if name == customer:
                days_visited_set.add(day)

        return working_days_set.difference(days_visited_set)

    def get_busiest_day(self):
        day_count_dict = {}
        busiest_day = self._data[0][2]

        for _, _, day in self._data:
            if day not in day_count_dict:
                day_count_dict[day] = 1
            else:
                day_count_dict[day] += 1
        
            if day_count_dict[day] > day_count_dict[busiest_day]:
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        day_count_dict = {}
        least_busy_day = self._data[0][2]

        for _, _, day in self._data:
            if day not in day_count_dict:
                day_count_dict[day] = 1
            else:
                day_count_dict[day] += 1
        
            if day_count_dict[day] < day_count_dict[least_busy_day]:
                least_busy_day = day

        return least_busy_day

    def get_dish_count_by_customer(self, customer, order):
        dish_count = 0

        for name, dish, _ in self._data:
            if name == customer and dish == order:
                dish_count += 1
        
        return dish_count
