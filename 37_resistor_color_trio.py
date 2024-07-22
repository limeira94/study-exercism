COLORS = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }


def label(colors):
    result = int(str(COLORS[colors[0]]) + str(COLORS[colors[1]]) + "0" * COLORS[colors[2]])
    if result < 1000:
        return f"{result} ohms"
    elif result < 1000000:
        return f"{result // 1000} kiloohms"
    elif result < 1000000000:
        return f"{result // 1000000} megaohms"
    else:
        return f"{result // 1000000000} gigaohms"