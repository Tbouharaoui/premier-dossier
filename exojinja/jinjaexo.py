#%%
from jinja2 import Environment, FileSystemLoader
import datetime
import pandas as pd 
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns


#%%

engine = create_engine('mysql+pymysql://simplon:Tarek7997@localhost:3306/netflix')
connection = engine.connect()

TMPL_DIR = "template"
fichier = 'rapport.jinja'

legend = connection.engine.execute("SELECT country.co_name, count(catalogue.ca_id) FROM catalogue JOIN catalogue_country using(ca_id) JOIN netflix.country using(co_id) GROUP by country.co_name ORDER BY count(catalogue.ca_id) DESC LIMIT 5")
graph = connection.engine.execute("SELECT country.co_name FROM catalogue JOIN catalogue_country using(ca_id) JOIN netflix.country using(co_id)")
graph2 = connection.engine.execute("SELECT country.co_name, catalogue.ca_date, count(catalogue.ca_id) FROM catalogue JOIN catalogue_country USING (ca_id) JOIN country USING(co_id) GROUP BY country.co_name,catalogue.ca_date ORDER BY catalogue.ca_date")
nombidon = ("select distinct tmpa.country, tmpa.category, tmpa.compte from "   
"(SELECT o.country, o.category, o.compte FROM "
	"(SELECT country.co_name as country, category.cat_name as category, count(catalogue.ca_id) as compte FROM catalogue "
	"JOIN catalogue_country USING(ca_id) "
	"JOIN country USING(co_id) "
	"JOIN catalogue_category USING(ca_id) "
	"JOIN category USING(cat_id) GROUP BY country, category) as o) as tmpa "
"left join "
"(SELECT b.country, b.category, b.compte FROM "
	"(SELECT country.co_name as country, category.cat_name as category, count(catalogue.ca_id) as compte FROM catalogue "
	"JOIN catalogue_country USING (ca_id) "
	"JOIN country USING(co_id) "
	"JOIN catalogue_category USING(ca_id) "
	"JOIN category USING(cat_id) GROUP BY country, category) as b) as tmpb "
"on tmpa.country = tmpb.country AND tmpa.compte < tmpb.compte "
"WHERE tmpb.compte is NULL")
graph3 = connection.engine.execute(nombidon)


templateLoader = FileSystemLoader(searchpath=TMPL_DIR)
templateEnv = Environment(loader=templateLoader)
template = templateEnv.get_template(fichier)

pays = input("veuillez choisir des pays séparé par une virgule :")
pays = pays.split(", ")

df = pd.DataFrame(legend.fetchall(), columns=["pays", "nombre"])
query_graph = pd.DataFrame(graph.fetchall(), columns=["pays"])
query_graph2 = pd.DataFrame(graph2.fetchall(), columns=["pays", "année", "nombre"])
query_graph3 = pd.DataFrame(graph3.fetchall(), columns=["pays", "categories", "nombre"])

qu = "pays == {}".format(pays)
query_graph.query(qu, inplace=True)
query_graph2.query(qu, inplace=True)
query_graph3.query(qu, inplace=True)



first_graph = plt.title("Nombre de films par pays")
first_graph = sns.countplot(x='pays',data=query_graph) 
first_graph = plt.savefig("country.png")

plt.figure()

second_graph = plt.title("evolution des sorties films par pays")
second_graph = sns.lineplot(x = "année", y="nombre" ,data=query_graph2, hue="pays", palette="tab10", linewidth=2.5)
second_graph = plt.savefig("year.png")




data={
    'time_stamp':datetime.datetime.now().strftime("%X %x"),
    "df" : df,
    "query_graph3" : query_graph3
}


outputText = template.render(data)

html_file = open('index.html', "w")
html_file.write(outputText)
html_file.close()

print(query_graph3)

# %%
