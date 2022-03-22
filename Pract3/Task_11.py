import matplotlib.pyplot as plt
import csv


with open('GAMES.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    for row in reader:
        data += row[0].split(';')

    csv_file.close()

years = []
for i in range(3, len(data), 4):
    if data[i] != '"не издана"':
        data[i] = int(data[i].replace('"', ''))
        years.append(data[i])

years_counter = dict.fromkeys(years, 0)
for i in years:
    years_counter[i] += 1

genres = []
for i in range(1, len(data), 4):
    if data[i+2] != '"не издана"':
        genres.append(data[i])
print(len(genres))


def genre_counter(genre, border, start=1981):
    counter = dict.fromkeys(years, 0)
    for j in range(len(years)):
        if start <= years[j] < border:
            if genres[j] == genre:
                counter[years[j]] += 1
    return counter


x1 = range(1981, 2009)
y = []
for i in x1:
    if i in years_counter:
        y.append(years_counter[i])
    else:
        y.append(0)
fig = plt.figure()
popular_years_bar = fig.add_subplot(221)
popular_years_bar.title.set_text('Количество выпущенных игр по годам')
popular_years_bar.bar(x1, y)


top_genres = ['"Arcade"', '"Action"', '"Simulation"', '"Sports"', '"Strategy"', '"RPG"', '"Adventure"',
              '"Tabletop"', '"Racing"', '"Educational"', '"Interactive Fiction"', '"Quest"', '"Puzzle"']
top_genres_counters_80s = []
top_genres_counters_90s = []
top_genres_counters_00s = []
for i in range(len(top_genres)):
    top_genres_counters_80s.append(genre_counter(top_genres[i], 1990))
    top_genres_counters_90s.append(genre_counter(top_genres[i], 2000, 1990))
    top_genres_counters_00s.append(genre_counter(top_genres[i], 2009, 2000))

def genre_summ(genre_counter):
    res = 0
    for i in genre_counter:
        res += genre_counter[i]
    return res

genre_80s = fig.add_subplot(222)
genre_80s.title.set_text('Жанры игр в 80-х')
genre_80s.pie([genre_summ(top_genres_counters_80s[i]) for i in range(len(top_genres))], labels=top_genres, autopct='%1.1f%%')

genre_90s = fig.add_subplot(223)
genre_90s.title.set_text('Жанры игр в 90-х')
genre_90s.pie([genre_summ(top_genres_counters_90s[i]) for i in range(len(top_genres))], labels=top_genres, autopct='%1.1f%%')

genre_00s = fig.add_subplot(224)
genre_00s.title.set_text('Жанры игр в нулевых')
genre_00s.pie([genre_summ(top_genres_counters_00s[i]) for i in range(len(top_genres))], labels=top_genres, autopct='%1.1f%%')

plt.show()

print(genre_counter(top_genres[0], 2009, 2000))
