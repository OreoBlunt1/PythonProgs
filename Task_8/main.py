def main(x):
    x = x.replace('\\begin', ' ')\
        .replace('.\\end', ' ')\
        .replace('. \\end', ' ')\
        .replace('#', ' ')\
        .replace('variable', ' ')\
        .replace('(', ' ')\
        .replace(')', ' ')\
        .replace(';', ' ')\
        .replace('\n', ' ')
    x_parts = x.split('.')
    x_parts1 = [i.split('<==') for i in x_parts]
    dict1 = {}
    for i in range(len(x_parts1)):
        suka = x_parts1[i][1].split()
        for j in range(len(suka)):
            suka[j] = int(suka[j])
        blyat = x_parts1[i][0].replace(' ', '')
        dict1[blyat] = suka
    return dict1
