def covert_to_tag(positivo, negativo):
    if (.45 < positivo < .55) and (.45 < negativo < .55):
        return "NEU"
    if positivo > .55:
        return "POS"
    if negativo > .55:
        return "NEG"

    return "UNK"
