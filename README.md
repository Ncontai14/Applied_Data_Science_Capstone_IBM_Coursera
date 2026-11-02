# Predicting Falcon 9 first-stage landing outcomes

Nishith Maity · IBM Applied Data Science Capstone

The modeling sample contains 90 historical flights, including 60 positive landing outcomes under the course definition. Logistic regression, SVM, decision tree and K-nearest neighbors each classified 15 of the 18 held-out flights correctly. This is a historical benchmark. The positive class includes controlled ocean landings, and the negative class includes flights without a confirmed landing.

## Run locally

Use Python 3.12. Open a terminal in this directory and run:

```sh
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open each notebook and run all cells in numerical order. Keep the notebooks beside the `data` folder. Each notebook includes its saved outputs. The wrangling, feature-engineering and modeling notebooks prefer the preceding notebook’s CSV export and otherwise read the bundled course snapshot. To use only the bundled files, remove the generated CSVs beside the notebooks. Basemap tiles and Leaflet assets require internet access when viewing Folium outputs.

| Notebook | Analysis |
| --- | --- |
| 01 | Read the archived SpaceX launch response, filter single-core/single-payload Falcon 9 flights, and join the archived lookup fields |
| 02 | Parse the pinned Wikipedia tables and export 121 numbered flight rows |
| 03 | Assign landing classes from the outcome strings |
| 04 | Run ten SQLite queries on 101 mission records |
| 05 | Plot site, orbit, payload and year patterns and reproduce the 83-column feature matrix |
| 06 | Map 56 flight records, expand site clusters and measure distances to selected reference points |
| 07 | Tune four classifiers with 10-fold cross-validation and evaluate on a common 18-flight test set |

Run `python spacex_dash_app.py` and open the local address printed by Dash. The dashboard script was reconstructed from the course dataset and saved dashboard views. Select a site to compare its successful and unsuccessful outcomes, or select all sites to see the distribution of successful flights. The slider filters the payload scatter plot.

## Reading the results

- SQL has 101 mission records, EDA and classification use 90 flights, and the interactive labs use 56 records. Their outcome fields and denominators differ.
- The original EDA export contained 80 columns. Encoding both values of GridFins, Reused, and Legs reproduces the 83 columns in the IBM model input. The notebook compares the full matrix to that input.
- The verification run fits the scaler inside each training fold, uses valid tree settings, and fixes the tree seed. The original lab’s best cross-validation scores and the corrected scores are distinguished in the presentation. Both runs produced the same four-way test tie.
- The coastline distance of 0.51 km is to the coordinate selected in the course lab. Supplemental road, rail and city distances refer to mapped points, rather than nearest boundaries.
- The scraper retains the first payload entry on each numbered Falcon 9 row. Payload-mass strings retain source qualifications. Unknown masses stay missing.

## Sources and attribution

The original lab instructions and author credits are retained in the notebooks. The course datasets are historical extracts.

- [IBM course datasets](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/) — archived launch JSON, datasets 1–3 and the two interactive-lab extracts. The bundled file `launches.json` corresponds to `API_call_spacex_api.json`.
- [IBM SQL extract](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv).
- [Wikipedia launch list, revision 1027686922](https://en.wikipedia.org/w/index.php?oldid=1027686922) — the bundled HTML contains the numbered launch tables extracted from this revision. Text by Wikipedia contributors, [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
- [OpenStreetMap contributors](https://www.openstreetmap.org/copyright) — [Centaur Road point](https://www.openstreetmap.org/node/1116487179) and [rail spur point](https://www.openstreetmap.org/node/1116487198). [GeoNames city reference point](https://www.geonames.org/4175437/titusville.html).
