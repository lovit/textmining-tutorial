def get_lalaland_comments(n_limit=-1):

    fname = './lalaland_comments.txt'

    with open(fname, encoding='utf-8') as f:
        idxs = []
        scores = []
        texts = []

        for i, doc in enumerate(f):
            if n_limit > 0 and i >= n_limit:
                break

            try:
                idx, text, score = doc.strip().split('\t')
                idxs.append(idx)
                texts.append(text)
                scores.append(int(score))

            except Exception as e:
                print(e)
                continue

    return idxs, texts, scores