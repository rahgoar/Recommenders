import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#df = pd.read_csv('u.data', sep='\t', names=['user_id','item_id','rating','titmestamp'])

df = pd.read_csv('ratings.csv', sep=',', header = 0)
#-------------------------------------------------
'''
userId - the ID of the user who rated the movie.
movieId - the ID of the movie.
rating - The rating the user gave the movie, between 1 and 5.
timestamp - The time the movie was rated.
title - The title of the movie.
genres - The genres of the movie '''
#-------------------------------------------------

print(df.head())
movie_titles = pd.read_csv('movies.csv', sep=',', header=0)
print(movie_titles.head())

df = pd.merge(df, movie_titles, on='movieId')
print(df.head())

print(df.describe())
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
print(ratings.head())
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
print(ratings.head())


movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')


print(ratings.sort_values('number_of_ratings', ascending=False).head(10))

# Collect the rate Similarities:
AFO_user_rating = movie_matrix['Air Force One (1997)']
contact_user_rating = movie_matrix['Contact (1997)']
print(AFO_user_rating.head(50))
print(contact_user_rating.head(50))

similar_to_air_force_one=movie_matrix.corrwith(AFO_user_rating)
#print(similar_to_air_force_one.head(40))
similar_to_air_force_one.to_csv('test.csv')
similar_to_contact = movie_matrix.corrwith(contact_user_rating)
#print(similar_to_contact.head(40))

'''
# Get the correlations:
corr_contact = pd.DataFrame(similar_to_contact, columns=['Correlation'])
corr_contact.dropna(inplace=True)
print(corr_contact.head())
'''
'''
corr_AFO = pd.DataFrame(similar_to_air_force_one, columns=['correlation'])
corr_AFO.dropna(inplace=True)
print(corr_AFO.head())
corr_AFO = corr_AFO.join(ratings['number_of_ratings'])
corr_contact = corr_contact.join(ratings['number_of_ratings'])
print(corr_AFO .head())
print(corr_contact.head())

# Increase the threshold criterion:
corr_AFO[corr_AFO['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10)
corr_contact[corr_contact['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(10)
'''


