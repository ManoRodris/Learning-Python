# Import packages
from dash import Dash, html, dash_table, dcc
from main import total_fsa, total_bjl, total_ii, total_j, total_vc
import pandas as pd
import plotly.express as px
import os
print(os.getcwd())

# Incorporate data
inscriptions_embarcatech = pd.read_csv("C:/Users/Rodrigo/Documents/Learning_Python/Embarcatech_data_analysis/Advanced_analysis/subscribers_embarcatech.csv")
inscriptions_embarcatech = inscriptions_embarcatech.drop(columns=["Unnamed: 0"], errors="ignore")

amount_of_subscribers = {
    "Polos": ["Feira de Santana","Bom Jesus da Lapa","Ilhéus/Itabuna","Juazeiro","Vitória da Conquista"],
    "Amount_Polos": [total_fsa, total_bjl, total_ii, total_j, total_vc]
}

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='EmbarcaTech Data Analysis'),
    dash_table.DataTable(data=inscriptions_embarcatech.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(amount_of_subscribers, x="Polos", y="Amount_Polos", histfunc='avg'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
