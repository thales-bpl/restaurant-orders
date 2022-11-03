class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append(customer, order, day)

    def get_most_ordered_dish_per_customer(self, customer):
        pass

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
        pass

    def get_least_busy_day(self):
        pass

    def get_dish_count_by_customer(self):
        pass