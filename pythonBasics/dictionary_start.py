# dictionary is like a telephone book,retrieve the value using
population = {"chaina": 143,
              "india": 136,
              "USA": 32,
              "Pakistan": 21}


def add():
    country = input("Enter country name to add:")
    country = country.lower()
    if country in population:
        print("country already exist in the dataset")
        return
    p = input(f"enter population for {country}")
    p = float(p)
    population[country] = p
    print_all()


def remove():
    country = input("Enter country name  to remove")
    country = country.lower()
    if country not in population:
        print("country doesn't exist in our dataset")
        return
    del population[country]
    print_all()


def query():
    country = input("Enter country  name to query")
    country = country.lower()
    if country not in population:
        print("country doesnot exist in our dataset")
        return
    print(f"popoulation of {country} is {population[country]} crore")


def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")


def main():
    op = input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()


if __name__ == '__main__':
    main()
