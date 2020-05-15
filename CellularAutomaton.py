class CellularAutomaton:
    """ Elementary Cellular Automaton written in Python. When calling the class parse a rule between 1 and 256.
        >>> c190 = CellularAutomaton(190)
        self.rule: 10111110
        >>> c190.print([1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0])
        #--#-###--#-#-#---###----##--
        >>> c30 = CellularAutomaton(30)
        self.rule: 00011110
    """

    def __init__(self, user_rule):
        self.rule = format(user_rule, '08b')
        self.old_row = [0] * 15 + [1] + [0] * 15
        self.new_row = []
        print(f'self.rule: {self.rule}')

        # The ruleset which the neighbours will be compared with to get the value in the new line
        self.rule_set = {
            "111": self.rule[0],
            "110": self.rule[1],
            "101": self.rule[2],
            "100": self.rule[3],
            "011": self.rule[4],
            "010": self.rule[5],
            "001": self.rule[6],
            "000": self.rule[7]
        }

    def __call__(self):
        # A variable which holds the number of lines to be printed
        line_count = 1
        while line_count < 20:
            # Loop through each element in the self.old_row to find the neighbours from previous line
            for (index, value) in enumerate(self.old_row):
                # If the index number is equal to 0 then we must be in the far left,
                # therefore the left neighbour should be 0
                if index == 0:
                    # print("First index")
                    left = 0
                    right = self.old_row.__getitem__(index + 1)
                # The same as above. If the index is equal to the length of the list, then we must be in the far right,
                # therefore the right neighbour should be 0
                elif index >= len(self.old_row) - 1:
                    # print("Last index")
                    left = self.old_row.__getitem__(index - 1)
                    right = 0
                # If none of the above fit then we are in the middle and we just need to find the neighbours
                else:
                    # print("Somewhere ind the middle")
                    left = self.old_row.__getitem__(index - 1)
                    right = self.old_row.__getitem__(index + 1)
                # Save the neighbours as a string variable so that we can use the variable to search in the dict.
                neighbours = str(left) + str(self.old_row[index]) + str(right)

                # Looks in the dict. for the key which matches the neighbour variable
                # and then assign the values from the dict. to the new list
                self.new_row.append(int(self.rule_set.get(neighbours)))

            # Calling the print method which converts bits to symbols
            self.print(self.old_row)

            line_count += 1
            self.old_row = self.new_row
            self.new_row = []

    def print(self, old_row):
        # Loops through the old_row and adds a "-" or "#" to a str variable which will be printed after each loop
        line = ""
        for value in old_row:
            if int(value) == 0:
                line = line + "-"
            else:
                line = line + "#"
        print(line)


c190 = CellularAutomaton(30)
c190.__call__()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

