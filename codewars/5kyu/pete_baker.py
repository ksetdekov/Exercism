def cakes(recipe, available):
    portions = []
    for ingredient, count in recipe.items():
        have = available.get(ingredient, 0)
        portions.append(have // count)
    return min(portions)
