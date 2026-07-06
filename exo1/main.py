
# VAR
# pieces_possibles = [100, 50, 20, 10, 5, 2, 1]

# reste_a_rendre = 17

# # FUNC
# def compute(pieces_possibles, reste_a_rendre) -> tuple[int, list[int]]:
#     sorted(pieces_possibles, reverse=True)

#     nb_pieces_compt = 0
#     pieces_details = []

#     for piece in pieces_possibles:
#         if piece <= reste_a_rendre:
#             if reste_a_rendre > 0 :
#                 reste_a_rendre = reste_a_rendre - piece
#                 pieces_details.append(piece)
#                 nb_pieces_compt = nb_pieces_compt + 1


#     return (nb_pieces_compt, pieces_details)


# print(compute(pieces_possibles, reste_a_rendre))

# __________________________________________________________________________________________________

# VAR
pieces_possibles = [4, 3, 1]

reste_a_rendre = 6

# FUNC
def compute(pieces_possibles, reste_a_rendre) -> tuple[int, list[int]]:
    sorted(pieces_possibles, reverse=True)

    nb_pieces_compt = 0
    pieces_details = []

    for piece in pieces_possibles:
        if piece <= reste_a_rendre:
            if reste_a_rendre > 0 :
                reste_a_rendre = reste_a_rendre - piece
                pieces_details.append(piece)
                nb_pieces_compt = nb_pieces_compt + 1


    return (nb_pieces_compt, pieces_details)


print(compute(pieces_possibles, reste_a_rendre))

    
