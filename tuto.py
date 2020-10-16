import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import sqlite3
import seaborn as sns

app = dash.Dash()
# df = pd.read_csv('carData.csv')

# fig = px.scatter(df, x="Year", y="Selling_Price")
# id_fig = "prix_en_fct_de_lannee"

connexion = sqlite3.connect("C:/sqlite/Cars.sq3")
connexion.execute('''CREATE TABLE CAR(Car_Name, Year, Selling_Price, Present_Price,
Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)  ''')

sql = "SELECT * FROM CAR"
df = pd.read_sql(sql, connexion)

sns.set_theme(style="ticks")
sns.catplot(data=df, x="Car_Name", y="Selling_Price")
#id_fig = "Catplot carname"

#app.layout = html.Div([
#    dcc.Graph(
#        id=id_fig,
#       figure=fig
#                )
#            ]
#        )

# Les catplots sont utiles pour tracer des graphes avec des données qui peuvent être catégorisées dans
# des groupes distincs comme par exemple ici les categories "Diesel" et "Petrol" ou "Manuel" et "Automatic"

# if __name__ == '__main__':
#     app.run_server(debug=True)
