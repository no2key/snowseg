# -*- coding: utf-8 -*-

import codecs

import tnt

def main():
    data = []
    f = codecs.open('brown.txt', 'r', 'utf-8')
    for line in f:
        if not line.strip():
            continue
        words = map(lambda x: x.split('/'), line.split(' '))
        words = map(lambda x: (x[1], x[0]), words)
        data.append(words)
    model = tnt.TnT()
    model.train(data)
    ret = [model.tag(sent) for sent in data]
    total = 0
    error = 0
    for c1, sent in enumerate(data):
        for c2, wd in enumerate(sent):
            total += 1
            if wd[0] != ret[c1][c2][0]:
                error += 1
    print 'total: %d, error: %d, precision: %f' % (total, error, float(error).total)

if __name__ == '__main__':
    main()