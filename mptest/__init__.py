def noop(input):
    return input

def print_n(id, n):
    for i in range(n):
        print(f"{id}: {i}")

def crash(input):
    raise Exception(f"{input}")