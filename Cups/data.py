logo = '''

                                                             
  ,ad8888ba,     88        88    88888888ba      ad88888ba   
 d8"'    `"8b    88        88    88      "8b    d8"     "8b  
d8'              88        88    88      ,8P    Y8,          
88               88        88    88aaaaaa8P'    `Y8aaaaa,    
88               88        88    88""""""'        `"""""8b,  
Y8,              88        88    88                     `8b  
 Y8a.    .a8P    Y8a.    .a8P    88             Y8a     a8P  
  `"Y8888Y"'      `"Y8888Y"'     88              "Y88888P"   
                                                             
                                                             
'''





suits = [
    'Clubs',
    'Diamonds',
    'Hearts',
    'Spades',
]

cards = [
    'Ace',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'Jack',
    'Queen',
    'King',
]

deck_one = [

    {'number': 1, 'card_name': 'Ace', 'card_type': 'Clubs', 'value': 0},
    {'number': 2, 'card_name': 'Ace', 'card_type': 'Diamonds', 'value': 0},
    {'number': 3, 'card_name': 'Ace', 'card_type': 'Hearts', 'value': 0},
    {'number': 4, 'card_name': 'Ace', 'card_type': 'Spades', 'value': 0},
    {'number': 5, 'card_name': '2', 'card_type': 'Clubs', 'value': 12},
    {'number': 6, 'card_name': '2', 'card_type': 'Diamonds', 'value': 12},
    {'number': 7, 'card_name': '2', 'card_type': 'Hearts', 'value': 12},
    {'number': 8, 'card_name': '2', 'card_type': 'Spades', 'value': 12},
    {'number': 9, 'card_name': '3', 'card_type': 'Clubs', 'value': 11},
    {'number': 10, 'card_name': '3', 'card_type': 'Diamonds', 'value': 11},
    {'number': 11, 'card_name': '3', 'card_type': 'Hearts', 'value': 11},
    {'number': 12, 'card_name': '3', 'card_type': 'Spades', 'value': 11},
    {'number': 13, 'card_name': '4', 'card_type': 'Clubs', 'value': 10},
    {'number': 14, 'card_name': '4', 'card_type': 'Diamonds', 'value': 10},
    {'number': 15, 'card_name': '4', 'card_type': 'Hearts', 'value': 10},
    {'number': 16, 'card_name': '4', 'card_type': 'Spades', 'value': 10},
    {'number': 17, 'card_name': '5', 'card_type': 'Clubs', 'value': 9},
    {'number': 18, 'card_name': '5', 'card_type': 'Diamonds', 'value': 9},
    {'number': 19, 'card_name': '5', 'card_type': 'Hearts', 'value': 9},
    {'number': 20, 'card_name': '5', 'card_type': 'Spades', 'value': 9},
    {'number': 21, 'card_name': '6', 'card_type': 'Clubs', 'value': 8},
    {'number': 22, 'card_name': '6', 'card_type': 'Diamonds', 'value': 8},
    {'number': 23, 'card_name': '6', 'card_type': 'Hearts', 'value': 8},
    {'number': 24, 'card_name': '6', 'card_type': 'Spades', 'value': 8},
    {'number': 25, 'card_name': '7', 'card_type': 'Clubs', 'value': 7},
    {'number': 26, 'card_name': '7', 'card_type': 'Diamonds', 'value': 7},
    {'number': 27, 'card_name': '7', 'card_type': 'Hearts', 'value': 7},
    {'number': 28, 'card_name': '7', 'card_type': 'Spades', 'value': 7},
    {'number': 29, 'card_name': '8', 'card_type': 'Clubs', 'value': 6},
    {'number': 30, 'card_name': '8', 'card_type': 'Diamonds', 'value': 6},
    {'number': 31, 'card_name': '8', 'card_type': 'Hearts', 'value': 6},
    {'number': 32, 'card_name': '8', 'card_type': 'Spades', 'value': 6},
    {'number': 33, 'card_name': '9', 'card_type': 'Clubs', 'value': 5},
    {'number': 34, 'card_name': '9', 'card_type': 'Diamonds', 'value': 5},
    {'number': 35, 'card_name': '9', 'card_type': 'Hearts', 'value': 5},
    {'number': 36, 'card_name': '9', 'card_type': 'Spades', 'value': 5},
    {'number': 37, 'card_name': '10', 'card_type': 'Clubs', 'value': 4},
    {'number': 38, 'card_name': '10', 'card_type': 'Diamonds', 'value': 4},
    {'number': 39, 'card_name': '10', 'card_type': 'Hearts', 'value': 4},
    {'number': 40, 'card_name': '10', 'card_type': 'Spades', 'value': 4},
    {'number': 41, 'card_name': 'Jack', 'card_type': 'Clubs', 'value': 3},
    {'number': 42, 'card_name': 'Jack', 'card_type': 'Diamonds', 'value': 3},
    {'number': 43, 'card_name': 'Jack', 'card_type': 'Hearts', 'value': 3},
    {'number': 44, 'card_name': 'Jack', 'card_type': 'Spades', 'value': 3},
    {'number': 45, 'card_name': 'Queen', 'card_type': 'Clubs', 'value': 2},
    {'number': 46, 'card_name': 'Queen', 'card_type': 'Diamonds', 'value': 2},
    {'number': 47, 'card_name': 'Queen', 'card_type': 'Hearts', 'value': 2},
    {'number': 48, 'card_name': 'Queen', 'card_type': 'Spades', 'value': 2},
    {'number': 49, 'card_name': 'King', 'card_type': 'Clubs', 'value': 1},
    {'number': 50, 'card_name': 'King', 'card_type': 'Diamonds', 'value': 1},
    {'number': 51, 'card_name': 'King', 'card_type': 'Hearts', 'value': 1},
    {'number': 52, 'card_name': 'King', 'card_type': 'Spades', 'value': 1}
]

deck_two = [

    {'number': 53, 'card_name': 'Ace', 'card_type': 'Clubs', 'value': 0},
    {'number': 54, 'card_name': 'Ace', 'card_type': 'Diamonds', 'value': 0},
    {'number': 55, 'card_name': 'Ace', 'card_type': 'Hearts', 'value': 0},
    {'number': 56, 'card_name': 'Ace', 'card_type': 'Spades', 'value': 0},
    {'number': 57, 'card_name': '2', 'card_type': 'Clubs', 'value': 12},
    {'number': 58, 'card_name': '2', 'card_type': 'Diamonds', 'value': 12},
    {'number': 59, 'card_name': '2', 'card_type': 'Hearts', 'value': 12},
    {'number': 60, 'card_name': '2', 'card_type': 'Spades', 'value': 12},
    {'number': 61, 'card_name': '3', 'card_type': 'Clubs', 'value': 11},
    {'number': 62, 'card_name': '3', 'card_type': 'Diamonds', 'value': 11},
    {'number': 63, 'card_name': '3', 'card_type': 'Hearts', 'value': 11},
    {'number': 64, 'card_name': '3', 'card_type': 'Spades', 'value': 11},
    {'number': 65, 'card_name': '4', 'card_type': 'Clubs', 'value': 10},
    {'number': 66, 'card_name': '4', 'card_type': 'Diamonds', 'value': 10},
    {'number': 67, 'card_name': '4', 'card_type': 'Hearts', 'value': 10},
    {'number': 68, 'card_name': '4', 'card_type': 'Spades', 'value': 10},
    {'number': 69, 'card_name': '5', 'card_type': 'Clubs', 'value': 9},
    {'number': 70, 'card_name': '5', 'card_type': 'Diamonds', 'value': 9},
    {'number': 71, 'card_name': '5', 'card_type': 'Hearts', 'value': 9},
    {'number': 72, 'card_name': '5', 'card_type': 'Spades', 'value': 9},
    {'number': 73, 'card_name': '6', 'card_type': 'Clubs', 'value': 8},
    {'number': 74, 'card_name': '6', 'card_type': 'Diamonds', 'value': 8},
    {'number': 75, 'card_name': '6', 'card_type': 'Hearts', 'value': 8},
    {'number': 76, 'card_name': '6', 'card_type': 'Spades', 'value': 8},
    {'number': 77, 'card_name': '7', 'card_type': 'Clubs', 'value': 7},
    {'number': 78, 'card_name': '7', 'card_type': 'Diamonds', 'value': 7},
    {'number': 79, 'card_name': '7', 'card_type': 'Hearts', 'value': 7},
    {'number': 80, 'card_name': '7', 'card_type': 'Spades', 'value': 7},
    {'number': 81, 'card_name': '8', 'card_type': 'Clubs', 'value': 6},
    {'number': 82, 'card_name': '8', 'card_type': 'Diamonds', 'value': 6},
    {'number': 83, 'card_name': '8', 'card_type': 'Hearts', 'value': 6},
    {'number': 84, 'card_name': '8', 'card_type': 'Spades', 'value': 6},
    {'number': 85, 'card_name': '9', 'card_type': 'Clubs', 'value': 5},
    {'number': 86, 'card_name': '9', 'card_type': 'Diamonds', 'value': 5},
    {'number': 87, 'card_name': '9', 'card_type': 'Hearts', 'value': 5},
    {'number': 88, 'card_name': '9', 'card_type': 'Spades', 'value': 5},
    {'number': 89, 'card_name': '10', 'card_type': 'Clubs', 'value': 4},
    {'number': 90, 'card_name': '10', 'card_type': 'Diamonds', 'value': 4},
    {'number': 91, 'card_name': '10', 'card_type': 'Hearts', 'value': 4},
    {'number': 92, 'card_name': '10', 'card_type': 'Spades', 'value': 4},
    {'number': 93, 'card_name': 'Jack', 'card_type': 'Clubs', 'value': 3},
    {'number': 94, 'card_name': 'Jack', 'card_type': 'Diamonds', 'value': 3},
    {'number': 95, 'card_name': 'Jack', 'card_type': 'Hearts', 'value': 3},
    {'number': 96, 'card_name': 'Jack', 'card_type': 'Spades', 'value': 3},
    {'number': 97, 'card_name': 'Queen', 'card_type': 'Clubs', 'value': 2},
    {'number': 98, 'card_name': 'Queen', 'card_type': 'Diamonds', 'value': 2},
    {'number': 99, 'card_name': 'Queen', 'card_type': 'Hearts', 'value': 2},
    {'number': 100, 'card_name': 'Queen', 'card_type': 'Spades', 'value': 2},
    {'number': 101, 'card_name': 'King', 'card_type': 'Clubs', 'value': 1},
    {'number': 102, 'card_name': 'King', 'card_type': 'Diamonds', 'value': 1},
    {'number': 103, 'card_name': 'King', 'card_type': 'Hearts', 'value': 1},
    {'number': 104, 'card_name': 'King', 'card_type': 'Spades', 'value': 1}
]
