# b = {'1': ' ', '2': ' ', '3': ' ',
#      '4': ' ', '5': ' ', '6': ' ',
#      '7': ' ', '8': ' ', '9': ' '}

# def printBoard(board):
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])

# turn = 'X'
# for i in range(9):
#     printBoard(b)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     if move == 'q':
#         break
#     else:
#         b[move] = turn
#         if turn == 'X':
#             turn = 'O'
#         else:
#             turn = 'X'
# if  b['1'] == b['2'] == b['3'] or\
#     b['4'] == b['5'] == b['6'] or\
#     b['7'] == b['8'] == b['9'] or\
#     b['1'] == b['4'] == b['7'] or\
#     b['2'] == b['5'] == b['8'] or\
#     b['3'] == b['6'] == b['9'] or\
#     b['1'] == b['5'] == b['9'] or\
#     b['3'] == b['5'] == b['7']:
#     print('Turn wins.')
# printBoard(b)