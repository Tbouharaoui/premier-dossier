"""import pandas as pd

df=pd.read_csv('/home/simplon/Téléchargements/netflix_titles.csv',index_col=0)
print(df.head())

## 2. Afficher les dimensions du dataframe
df.shape

## 3. Compter les films et les séries
resultat = df["type"].value_counts()
print(resultat)


## 4. Générer le résumé statistique du dataframe
print(df.describe(include="all"))


## 5. Compter les valeurs manquantes
dfvaleur = df.isna()
dfvaleur.sum()

## 6. Explorer les valeurs manquantes

## A.

df1 = df.loc[df['director'].isna()==True]
print(df1['type'].value_counts())

## B.

df2 = df.loc[df['cast'].isna()==True]
print(df2['listed_in'].value_counts().head(10))

## 7. Supprimer les lignes dupliquées
data = df.duplicated()
print(data)
data2 = df.drop_duplicates()
print(data2)

#8.Compter les films/séries produits par les États-Unis et par la France

df[(df["title"]=="country")].shape

# 9. Afficher le contenu le plus vieux disponible sur Netflix

OldestFilm = df[(df["release_year"]==df["release_year"].min())]
print(OldestFilm['title'])

# 10. Afficher le film avec la durée la plus longue sur Netflix
# a. Nouvelle notion : les méthodes str
# b. Énoncé

data_movies = df.loc[df.type == ['Movie']
duree = pd.Series(data_movies['duration']).str.replace(" min", "").astype('int').sort_values(ascending=False).head(5)
print(duree)


#12

import pandas as pd
df=pd.read_csv("/home/simplon/Téléchargements/netflix_titles (1).csv",
index_col=[0])
categories=pd.Series(", ".join(donnees["director"].dropna()).split(", "))
categories.value_counts().head(10)
#13. Voir si Jan Suter travaille souvent avec les mêmes acteurs




df2 = df.dropna()
janSuter = df2.loc[df2['director'].str.contains(pat = "Jan Suter")]
actor = pd.Series(", ".join(janSuter["cast"]).split(", "))
print(actor)
print(actor.value_counts().head(5))

#14. Représenter les dix pays qui ont produit le plus de conte-
#nus disponibles sur Netflix, avec le nombre de contenus par
#pays

import seaborn as sns

pays = df['country'].value_counts().head(10)
print(pays)
defpays= df.loc[df['country'].isin(pays.index)]
print(defpays)
sns.countplot(y= 'country', data=defpays)

#15Tracer un graphe à barres du nombre de films/séries par
#classement de contenu (rating)
sns.countplot(y= 'rating',data=df,palette = 'dark')

#16

import matplotlib.pyplot as plt
#16
data2 = df
#16.1
data2["date_added"] = pd.to_datetime(data2["date_added"]) 
#16.2 
data2["year_added"] = pd.to_datetime(data2["date_added"]).dt.year 
#16.3 
data_date_movie = data2.groupby(["year_added", "type"]).size().reset_index(name='Count')


sns.pointplot(x='year_added',y='Count', hue='type', data=data_date_movie)
plt.xticks(rotation=90)
print(data_date_movie)

#17 Afficher la distribution de la durée des films disponibles
#sur Netflix

movie = df[(df["type"]=="Movie")]
duree = pd.Series(movie["duration"]).str.replace("min","").astype("int").sort_values(ascending=False)
sns.distplot(duree)

#18Tracer un graphique représentant le nombre de séries par
#modalité de nombre de saisons


data_series = df.loc[df.type == 'TV Show']
plt.figure(figsize=[15,6])
sns.countplot(x ='duration', data = data_series)
plt.title("Nombre de Séries & de Saisons")
plt.ylabel("Nombre de Series")
plt.xlabel("Nombre de Saisons")
plt.show()

"""

import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://simplon:Tarek7997@localhost:3306/netflix')

df = pd.read_csv("/home/simplon/Téléchargements/netflix_titles(1).csv")
print(df)

#df=id/categorie
cat_name = pd.DataFrame(data = df,columns = ["ca_id", "cat_name"])
cat_name.dropna(inplace=True)
print(cat_name)

#df=id/cast
cast = pd.DataFrame(data = df,columns = ["ca_id", "cast_name"])
cast.dropna(inplace=True)

#df=id/director
directors = pd.DataFrame(data = df,columns = ["ca_id", "dir_name"])
directors.dropna(inplace=True)

#df=id/country
country = pd.DataFrame(data = df,columns = ["ca_id", "co_name"])
country.dropna(inplace=True)

#fonction split 
def separator(id, column, column_name):
    c = 0
    liste_id = []
    liste_col = []
    for i in column:
        x = i.split(", ")
        for z in x:
            liste_col.append(z)
            liste_id.append(id[c])
        
        c+=1
    dataframe = pd.DataFrame({'ca_id':liste_id, column_name: liste_col}, columns = ['ca_id', column_name])
    return dataframe 



#dataframe id/catégories
cat_id=separator(cat_name['ca_id'], cat_name['cat_name'], 'cat_name')
print(cat_id)
#dataframe id/cast
cast_id=separator(cat_name['ca_id'], cast['cast_name'], 'cast_name')
#dataframe id/directors
dir_id=separator(cat_name['ca_id'], directors['dir_name'], 'dir_name')
#dataframe id/country
country_id=separator(cat_name['ca_id'], country['co_name'], 'co_name')
print(cast_id)

#table categorie catalogue
categories = cat_id.drop_duplicates(subset=['cat_name']).reset_index().rename(columns={"index": "cat_id"})
cat_categories= cat_id.merge(categories, left_on="cat_name", right_on= 'cat_name')
del categories['ca_id']
cat_categories = cat_categories.rename(columns={"ca_id_x": "ca_id"})
del cat_categories['cat_name']
del cat_categories['ca_id_y']
print(categories)
#table country catalogue
country = country_id.drop_duplicates(subset=['co_name']).reset_index().rename(columns={"index": "co_id"})
cat_country = country_id.merge(country, left_on="co_name", right_on="co_name")
del country['ca_id']
del cat_country['co_name']
del cat_country['ca_id_y']
cat_country = cat_country.rename(columns={"ca_id_x": "ca_id"})

#table cast catalogue
cast= cast_id.drop_duplicates(subset=['cast_name']).reset_index().rename(columns={"index": "cast_id"})
cat_cast = cast_id.merge(cast, left_on="cast_name", right_on = "cast_name")
del cast["ca_id"]
del cat_cast['cast_name']
del cat_cast['ca_id_y']
cat_cast = cat_cast.rename(columns={"ca_id_x": "ca_id"})

#table dir catalogue
dir = dir_id.drop_duplicates(subset=['dir_name']).reset_index().rename(columns={"index": "dir_id"})
cat_dir = dir_id.merge(dir, left_on = "dir_name", right_on = "dir_name")
del dir["ca_id"]
del cat_dir['dir_name']
del cat_dir['ca_id_y']
cat_dir = cat_dir.rename(columns={"ca_id_x": "ca_id"})



#table catalogue
del df['cat_name']
del df['dir_name']
del df['cast_name']
del df['co_name']
del df['Unnamed: 12']



#changement type durée et date ajout

df['ca_duration'] = df['ca_duration'].str.replace(" min", "").str.replace(" Season", "").str.replace(" season", "").str.replace("s", "").astype(int)
df['ca_date']=pd.to_datetime(df['ca_date'])

#insertion tables

df.to_sql('catalogue', con=engine, if_exists='append', index=False)
country.to_sql('country', con=engine, if_exists='append', index=False)
cast.to_sql('cast', con=engine, if_exists='append', index=False)
dir.to_sql('directors', con=engine, if_exists='append', index=False)



#insertion tables d'association

cat_country.to_sql('catalogue_country', con=engine, if_exists='append', index=False)
cat_cast.to_sql('catalogue_cast', con=engine, if_exists='append', index=False)
cat_dir.to_sql('catalogue_directors', con=engine, if_exists='append', index=False)
cat_categories.to_sql('catalogue_category', con=engine, if_exists='append', index=False)
