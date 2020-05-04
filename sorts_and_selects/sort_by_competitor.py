import collections

def topNCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    word_count = collections.defaultdict(int)
    for review in reviews:
        words = review.split()
        words = set(words)
        for w in words:
            word_count[w.lower()] += 1

    to_sort = []
    for c in competitors:
        to_sort.append((-word_count[c.lower()], c))
    to_sort.sort()
    return [item[1] for item in to_sort[:topNCompetitors]]

assert topNCompetitors(6, 2, ['newshop', 'shopnow', 'afshion', 'fashionbeats', 'mymarket', 'tcellular'], 6, [
    'Newshop Newshop blah blah blah',
    'newshop blah blah',
    'fashionbeats blah blah blah',
    'fashionbeats afsdf asdfasdf asdfasdf asdfasdf',
    'asdfasdf mymarket asdfasdf asdf asdf asdf sdf',
    'newshop asdf Newshop asd fasdf asd fasd f'
]) == ['newshop', 'fashionbeats']
