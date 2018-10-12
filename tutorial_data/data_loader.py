import os

installpath = os.path.dirname(os.path.realpath(__file__))


def get_lalaland_comments(n_limit=-1):

    fname = '%s/lalaland_comments.txt' % installpath

    with open(fname, encoding='utf-8') as f:
        scores = []
        texts = []

        for i, doc in enumerate(f):
            if n_limit > 0 and i >= n_limit:
                break

            try:
                text, score = doc.strip().split('\t')
                texts.append(text)
                scores.append(int(score))
            except Exception as e:
                print(e)
                continue

    return texts, scores