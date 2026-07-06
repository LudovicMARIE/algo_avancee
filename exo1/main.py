def compute(pieces_possibles: list[int], reste_a_rendre: int) -> tuple[int, list[int]]:
    # best[s] = (nombre_min_de_pieces, liste_des_pieces) pour rendre la somme s
    best: list[tuple[int, list[int]] | None] = [None] * (reste_a_rendre + 1)
    best[0] = (0, [])

    for s in range(1, reste_a_rendre + 1):
        for piece in pieces_possibles:
            if piece <= s and best[s - piece] is not None:
                candidat_count = best[s - piece][0] + 1
                if best[s] is None or candidat_count < best[s][0]:
                    best[s] = (candidat_count, best[s - piece][1] + [piece])

    return best[reste_a_rendre]


# pieces_possibles = [100, 50, 20, 10, 5, 2, 1]
# reste_a_rendre = 17


pieces_possibles = [4, 3, 1]
reste_a_rendre = 6


rendu = compute(pieces_possibles, reste_a_rendre)
print(rendu)
