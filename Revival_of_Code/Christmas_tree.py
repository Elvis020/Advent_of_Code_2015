def draw_christmas_tree(number_of_trees):
    for index, element in enumerate(range(number_of_trees + 1)):
        sides = '*' * index
        spaces = (number_of_trees - index) * ' '
        print(spaces+sides+'*'+sides+spaces)


draw_christmas_tree(7)
