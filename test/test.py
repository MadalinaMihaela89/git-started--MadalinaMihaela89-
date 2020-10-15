def init_board():
    lista_finala = []
    for i in range(3):
        lista_temporara = []
        for j in range(3):
            lista_temporara.append('.')
        lista_finala.append(lista_temporara)
    return lista_finala

x = init_board()
for i in x:
    print(i)


# def get_move():
#     x = init_board()
#     coordonata = input('please enter coordinates')
#     if coordonata not in ['A1', 'A2']:
#         print("input wrong")
#         get_move()


# def get_move():
#     tabla = init_board()
#     lista_coordonate = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
#     coordonata = input("Please enter coordinates")
#     if coordonata not in lista_coordonate:
#         print("Input is wrong")
#         get_move()
#     else:
#         dictionar_coordonate = {'A': 0, 'B': 1, 'C': 2, '1': 0, '2': 1, '3': 2}
#         x = dictionar_coordonate[coordonata[0]]
#         y = dictionar_coordonate[coordonata[1]]
#         if tabla[x][y] != '.':
#             print("Location is taken")
#             get_move()
#         else:
#             return (x, y)
