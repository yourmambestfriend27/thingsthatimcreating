def open_dataset(file_name, header = True):
    """Function returns data sets from file and 
    assigning header to variable and rest of data to another variable"""
    opened_file = open(file_name, encoding='utf-8')
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    return data[1:], data[0] if header else data
apps_data, header = open_dataset('AppleStore.csv')
def get_index(list,value):
    """ This gives index of value in list of lists
    my_list: main list to input
    value : (str) value to search
    """
    for i, element in enumerate(list):
        if value in element:
            return i, element.index(value)
    return None
def avg_new_list(list):
    """returns average of values from the list"""
    return round(sum(list) / len(list),2)
# Creating some list to combine ratings
games_ratings = []
non_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    genre = row[12]
    if genre == 'Games':
        games_ratings.append(rating)
    elif genre != 'Games':
        non_games_ratings.append(rating)
avg_rating_games = avg_new_list(games_ratings)
avg_rating_non_games = avg_new_list(non_games_ratings)
non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])
    if price != 0.0:
        non_free_apps_ratings.append(rating)
avg_rating_non_free = avg_new_list(non_free_apps_ratings)
print('Paid apps rates are better than free ones.' if avg_rating_non_free > 3.38 else 'Free apps are better.')
# create list for free games rating
free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])
    genre = row[12]
    if genre == 'Games' and price == 0.0:
        free_games_ratings.append(rating)
avg_rating_free_games = avg_new_list(free_games_ratings)
print()
print('The average rating of free games is:', avg_rating_free_games)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    genre = row[12]
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
avg_games_social = avg_new_list(games_social_ratings)
print('The average rate of games using social network is:', avg_games_social)

# calculate the average of non free games using social network
non_free_games_social_ratings = []
free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    genre  = row[12]
    price = float(row[5])
    if (genre == 'Social Networking' or genre == 'Games') and price != 0.0:
        non_free_games_social_ratings.append(rating)
    else:
        free_games_social_ratings.append(rating)

avg_non_free = avg_new_list(non_free_games_social_ratings)
print('The average rate of non free games using social network is:',avg_non_free)

avg_free = avg_new_list(free_games_social_ratings)
print('The average rate of free games using social network is:',avg_free)
if avg_non_free > avg_free:
    print('Paid games using social network are better than free games.  ')
else:
    print('Its better to use free games.')

ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])
    if price > 9:
        ratings.append(rating)
avg_ratings = sum(ratings) /len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings)
n_apps_more_9 = len(ratings)

# adding new colum with conditional statement if label free on non free 
for app in apps_data[1:]:
    price = float(app[5])
    if price == 0.0:
        app.append('Free')
    else:
        app.append('Non-free')
apps_data[0].append('Free_or_not')

for app in apps_data[1:]:
    price = float(app[5])
    if price == 0.0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[:6])

