from utils import multiplier


def get_42():
    result = multiplier()
    if result != 42:
        raise ValueError


if __name__ == '__main__':
    get_42()
