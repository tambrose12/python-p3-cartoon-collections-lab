def roll_call_dwarves(names):
    for index, name in enumerate(names):
        print(f"{index + 1}. {name}")
    # or
    # count = 1
    # for name in names:
    #     print(f"{count}. {name}")
    #     count += 1


def summon_captain_planet(calls):
    new_list = []
    for call in calls:
        new_list.append(f"{call.capitalize()}!")
    return new_list
    # or
    # return [call.capitalize() + "!" for call in calls]


def long_planeteer_calls(words_list):
    for word in words_list:
        if len(word) > 4:
            return True
    return False


def find_the_cheese(snack_list):
    the_cheeses = ["cheddar", "gouda", "camembert"]
    for the_snack in snack_list:
        if the_snack in the_cheeses:
            return the_snack
    return None
