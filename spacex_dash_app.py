"""SpaceX capstone dashboard, reconstructed from the course data and saved views."""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

records = pd.read_csv(Path(__file__).parent / "data" / "spacex_launch_dash.csv")
records["Outcome"] = records["class"].map({0: "Failed", 1: "Success"})
sites = sorted(records["Launch Site"].unique())
app = Dash(__name__)
app.layout = html.Main([
    html.H1("SpaceX Launch Records Dashboard"),
    dcc.Dropdown(id="site", options=[{"label": "All Sites", "value": "ALL"}]
                 + [{"label": site, "value": site} for site in sites],
                 value="ALL", clearable=False),
    dcc.Graph(id="outcomes"),
    html.Label("Payload range (kg)"),
    dcc.RangeSlider(id="mass", min=0, max=10000, step=100,
                    marks={n: str(n) for n in range(0, 10001, 2000)}, value=[0, 10000]),
    dcc.Graph(id="payload"),
])

@app.callback(Output("outcomes", "figure"), Input("site", "value"))
def outcome_chart(site):
    if site == "ALL":
        totals = records.groupby("Launch Site", as_index=False)["class"].sum()
        return px.pie(totals, names="Launch Site", values="class", title="Total Successful Launches by Site")
    subset = records.loc[records["Launch Site"].eq(site)]
    counts = subset["Outcome"].value_counts().rename_axis("Outcome").reset_index(name="Flights")
    return px.pie(counts, names="Outcome", values="Flights", title=f"Launch outcomes at {site}")

@app.callback(Output("payload", "figure"), Input("site", "value"), Input("mass", "value"))
def payload_chart(site, mass):
    subset = records.loc[records["Payload Mass (kg)"].between(*mass)]
    if site != "ALL":
        subset = subset.loc[subset["Launch Site"].eq(site)]
    return px.scatter(subset, x="Payload Mass (kg)", y="Outcome", color="Booster Version Category",
                      category_orders={"Outcome": ["Failed", "Success"]}, title=f"Payload and Launch Outcome: {site}")

if __name__ == "__main__":
    app.run(debug=False)
