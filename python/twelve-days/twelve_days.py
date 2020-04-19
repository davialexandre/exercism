def recite(start_verse, end_verse):

    gifts = [
        'a Partridge in a Pear Tree',
        'two Turtle Doves',
        'three French Hens',
        'four Calling Birds',
        'five Gold Rings',
        'six Geese-a-Laying',
        'seven Swans-a-Swimming',
        'eight Maids-a-Milking',
        'nine Ladies Dancing',
        'ten Lords-a-Leaping',
        'eleven Pipers Piping',
        'twelve Drummers Drumming',
    ]
    days = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth'
    ]

    verses = []
    i = start_verse
    while i <= end_verse:
        given_gifts = ', '.join(reversed(gifts[0:i])).replace(', a P', ', and a P')
        verses.append(f'On the {days[i - 1]} day of Christmas my true love gave to me: {given_gifts}.')
        i += 1

    return verses
