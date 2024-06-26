#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_member_dictionary = social_graph.get(from_member)
    to_member_dictionary = social_graph.get(to_member)
    
    if (from_member in to_member_dictionary["following"] and to_member in from_member_dictionary["following"]) == True:
        return("friends")
    elif (to_member in from_member_dictionary["following"]) == True:
        return("follower")
    elif (from_member in to_member_dictionary["following"]) == True:
        return("followed by")
    else:
        return("no relationship")


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    row_in_board = 0
    column_in_board = 0
    position = []

    if len(board) == 3:
        for i in board:
            for j in board[row_in_board]:
                position.append(j)
                column_in_board +=1
            row_in_board+=1

        def find_all_indices(lst, value):
                return [i for i, x in enumerate(lst) if x == value]

        position_X = find_all_indices(position, "X")
        position_X = {item for item in position_X}
        

        position_O = find_all_indices(position, "O")
        position_O = {item for item in position_O}

        win_combo1 = {0,1,2}
        win_combo2 = {3,4,5}
        win_combo3 = {6,7,8}
        win_combo4 = {0,3,6}
        win_combo5 = {1,4,7}
        win_combo6 = {2,5,8}
        win_combo7 = {0,4,8}
        win_combo8 = {2,4,6}

        if position_X.issuperset(win_combo1) or position_X.issuperset(win_combo2) or position_X.issuperset(win_combo3) or position_X.issuperset(win_combo4) or position_X.issuperset(win_combo5) or position_X.issuperset(win_combo6) or position_X.issuperset(win_combo7) or position_X.issuperset(win_combo8) == True:
            return ("X")

        elif position_O.issuperset(win_combo1) or position_O.issuperset(win_combo2) or position_O.issuperset(win_combo3) or position_O.issuperset(win_combo4) or position_O.issuperset(win_combo5) or position_O.issuperset(win_combo6) or position_O.issuperset(win_combo7) or position_O.issuperset(win_combo8) == True:
            return ("O")

        else:
            return ("NO WINNER")

        return

    elif len(board) == 4:
        for i in board:
            for j in board[row_in_board]:
                position.append(j)
                column_in_board +=1
            row_in_board+=1

        def find_all_indices(lst, value):
                return [i for i, x in enumerate(lst) if x == value]

        position_X = find_all_indices(position, "X")
        position_X = {item for item in position_X}

        position_O = find_all_indices(position, "O")
        position_O = {item for item in position_O}

        ## combinations = 012,345,678,036,147,258,048,246
        win_combo1 = {0,1,2,3}
        win_combo2 = {4,5,6,7}
        win_combo3 = {8,9,10,11}
        win_combo4 = {12,13,14,15}
        win_combo5 = {0,4,8,12}
        win_combo6 = {1,5,9,13}
        win_combo7 = {2,6,10,14}
        win_combo8 = {3,7,11,15}
        win_combo9 = {0,5,10,15}
        win_combo10 = {3,6,9,12}

        if position_X.issuperset(win_combo1) or position_X.issuperset(win_combo2) or position_X.issuperset(win_combo3) or position_X.issuperset(win_combo4) or position_X.issuperset(win_combo5) or position_X.issuperset(win_combo6) or position_X.issuperset(win_combo7) or position_X.issuperset(win_combo8) or position_X.issuperset(win_combo9) or position_X.issuperset(win_combo10) == True:
            return ("X")

        elif position_O.issuperset(win_combo1) or position_O.issuperset(win_combo2) or position_O.issuperset(win_combo3) or position_O.issuperset(win_combo4) or position_O.issuperset(win_combo5) or position_O.issuperset(win_combo6) or position_O.issuperset(win_combo7) or position_O.issuperset(win_combo8) or position_O.issuperset(win_combo9) or position_O.issuperset(win_combo10) == True:
            return ("O")

        else:
            return ("NO WINNER")

        return

    elif len(board) == 5:
        for i in board:
            for j in board[row_in_board]:
                position.append(j)
                column_in_board +=1
            row_in_board+=1

        def find_all_indices(lst, value):
                return [i for i, x in enumerate(lst) if x == value]

        position_X = find_all_indices(position, "X")
        position_X = {item for item in position_X}

        position_O = find_all_indices(position, "O")
        position_O = {item for item in position_O}

        win_combo1 = {0,1,2,3,4}
        win_combo2 = {5,6,7,8,9}
        win_combo3 = {10,11,12,13,14}
        win_combo4 = {15,16,17,18,19}
        win_combo5 = {20,21,22,23,24}
        win_combo6 = {0,5,19,15,20}
        win_combo7 = {1,6,11,16,21}
        win_combo8 = {2,7,12,17,22}
        win_combo9 = {3,8,13,18,23}
        win_combo10 = {4,9,14,19,24}
        win_combo11 = {0,6,12,18,24}
        win_combo12 = {4,8,12,16,20}

        if position_X.issuperset(win_combo1) or position_X.issuperset(win_combo2) or position_X.issuperset(win_combo3) or position_X.issuperset(win_combo4) or position_X.issuperset(win_combo5) or position_X.issuperset(win_combo6) or position_X.issuperset(win_combo7) or position_X.issuperset(win_combo8) or position_X.issuperset(win_combo9) or position_X.issuperset(win_combo10) or position_X.issuperset(win_combo11) or position_X.issuperset(win_combo12) == True:
            return ("X")

        elif position_O.issuperset(win_combo1) or position_O.issuperset(win_combo2) or position_O.issuperset(win_combo3) or position_O.issuperset(win_combo4) or position_O.issuperset(win_combo5) or position_O.issuperset(win_combo6) or position_O.issuperset(win_combo7) or position_O.issuperset(win_combo8) or position_O.issuperset(win_combo9) or position_O.issuperset(win_combo10) or position_O.issuperset(win_combo11) or position_O.issuperset(win_combo12) == True:
            return ("O")

        else:
            return ("NO WINNER")

        return

    elif len(board) == 6:
        for i in board:
            for j in board[row_in_board]:
                position.append(j)
                column_in_board +=1
            row_in_board+=1

        def find_all_indices(lst, value):
                return [i for i, x in enumerate(lst) if x == value]

        position_X = find_all_indices(position, "X")
        position_X = {item for item in position_X}

        position_O = find_all_indices(position, "O")
        position_O = {item for item in position_O}

        win_combo1 = {0,1,2,3,4,5}
        win_combo2 = {6,7,8,9,10,11}
        win_combo3 = {12,13,14,15,16,17}
        win_combo4 = {18,19,20,21,22,23}
        win_combo5 = {24,25,26,27,28,29}
        win_combo6 = {30,31,32,33,34,35}
        win_combo7 = {0,6,12,18,24,30}
        win_combo8 = {1,7,13,19,25,31}
        win_combo9 = {2,8,14,20,26,32}
        win_combo10 = {3,9,15,21,27,33}
        win_combo11 = {4,10,16,22,28,34}
        win_combo12 = {5,11,17,23,29,35}
        win_combo13 = {0,7,14,21,28,35}
        win_combo14 = {5,10,15,20,25,30}

        if position_X.issuperset(win_combo1) or position_X.issuperset(win_combo2) or position_X.issuperset(win_combo3) or position_X.issuperset(win_combo4) or position_X.issuperset(win_combo5) or position_X.issuperset(win_combo6) or position_X.issuperset(win_combo7) or position_X.issuperset(win_combo8) or position_X.issuperset(win_combo9) or position_X.issuperset(win_combo10) or position_X.issuperset(win_combo11) or position_X.issuperset(win_combo12) or position_X.issuperset(win_combo13) or position_X.issuperset(win_combo14) == True:
            return ("X")

        elif position_O.issuperset(win_combo1) or position_O.issuperset(win_combo2) or position_O.issuperset(win_combo3) or position_O.issuperset(win_combo4) or position_O.issuperset(win_combo5) or position_O.issuperset(win_combo6) or position_O.issuperset(win_combo7) or position_O.issuperset(win_combo8) or position_O.issuperset(win_combo9) or position_O.issuperset(win_combo10) or position_O.issuperset(win_combo11) or position_O.issuperset(win_combo12) or position_O.issuperset(win_combo13) or position_O.issuperset(win_combo14) == True:
            return ("O")

        else:
            return ("NO WINNER")

        return

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    eta = 0
    key_in_order = []
    current_stop = first_stop
    
    for i in route_map.keys():
        key_in_order.append(i)
    
    if first_stop == second_stop:
        eta = 0
        return(eta)
    elif (first_stop, second_stop) in route_map.keys():
        eta += route_map.get((first_stop, second_stop)).get("travel_time_mins")
    else:
        while current_stop != second_stop:
            for j in range(0, len(key_in_order)):
                if key_in_order[j][0] == current_stop:
                    eta += route_map[key_in_order[j]]['travel_time_mins']
                    current_stop = key_in_order[j][1]
                    break
                else:
                    continue
 
    return(eta)

