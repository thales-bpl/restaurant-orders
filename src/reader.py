import csv


def reader(path):
    if ".csv" in path:
        try:
            with open(path, "r") as file:
                return list(csv.reader(file))
                # return [entry for entry in csv.reader(file)]
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")

    raise FileNotFoundError(f"Extensão inválida: {path}")