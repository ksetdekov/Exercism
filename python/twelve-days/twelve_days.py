def day(count):
    return ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
            "twelfth"][count - 1]


def recite(start_verse, end_verse):
    final = list()
    things = ["twelve Drummers Drumming, ",
              "eleven Pipers Piping, ",
              "ten Lords-a-Leaping, ",
              "nine Ladies Dancing, ",
              "eight Maids-a-Milking, ",
              "seven Swans-a-Swimming, ",
              "six Geese-a-Laying, ",
              "five Gold Rings, ",
              "four Calling Birds, ",
              "three French Hens, ",
              "two Turtle Doves, and ",
              "a Partridge in a Pear Tree."]
    for v in range(start_verse, end_verse + 1):
        final.append(f'On the {day(v)} day of Christmas my true love gave to me: '+''.join(things[(12 - v):12]))
    return final
