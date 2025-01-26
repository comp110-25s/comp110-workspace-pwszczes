"""This program helps one plan a tea party!"""

__author__: str = "730643202"


def main_planner(guests: int) -> None:
    """This function is the entrypoint to the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """This function calculates the number of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """This function calculates the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function calculates total cost of the tea party"""
    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are at the tea party?")))
