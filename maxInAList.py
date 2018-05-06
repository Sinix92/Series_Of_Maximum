import time
import random


def findBestSerieInAListInTermsOfMaximum(my_list):
    my_max_value = max(my_list)
    my_max_elements = [my_max_value]

    for i in range(2, len(my_list) + 1):
        nb_elements = i

        for j in range(len(my_list) - nb_elements + 1):
            my_sum = sum(my_list[j:j + nb_elements])

            if my_sum > my_max_value:
                my_max_value = my_sum
                my_max_elements = my_list[j:j + nb_elements]

    return my_max_value, my_max_elements


def generateSerie(min_limit, max_limit, nb_elements, type_element="INTEGER"):
    random.seed(time.time())
    if type_element == "INTEGER":
        my_list = [random.randrange(min_limit, max_limit) for x in range(nb_elements)]
    elif type_element == "FLOAT":
        my_list = [random.uniform(min_limit, max_limit) for x in range(nb_elements)]
    return my_list


def mainFunction():
    my_list = generateSerie(-1001, 1000, 10, "INTEGER")
    print("My list: {}".format(my_list))
    my_max_value, my_max_elements = findBestSerieInAListInTermsOfMaximum(my_list)
    print("My best serie in terms of maxiumum: {}".format(my_max_elements))
    print("My max value: {}".format(my_max_value))


if __name__ == '__main__':
    mainFunction()
