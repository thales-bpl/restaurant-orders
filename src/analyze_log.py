import csv
from reader import reader


def most_ordered_by_customer(customer, data):
    pass


def burger_count_by_customer(customer, data):
    pass


def never_ordered_by_customer(customer, data):
    pass


def days_absent_by_customer(customer, data):
    working_days = set(
        ['segunda-feira', 'terça-feira', 'quarta-feira',
        'quinta-feira', 'sexta-feira', 'sabado']
        )
    days_visited = set()

    for customer, _, day in data:
        if customer == customer:
            days_visited.add(day)

    return working_days.difference(days_visited)


def analyze_log(path_to_file):
    customer_data = reader(path_to_file)

    most_ordered = most_ordered_by_customer('maria', customer_data)
    burger_count = burger_count_by_customer('arnaldo', customer_data)
    never_ordered = never_ordered_by_customer('joao', customer_data)
    days_absent = days_absent_by_customer('joao', customer_data)
