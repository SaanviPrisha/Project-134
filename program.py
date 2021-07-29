import pandas as pd
import csv
import plotly.express as px

rows = []

with open("stars.csv","r") as f:
  csvreader = csv.reader(f)
  
  for row in csvreader:
    rows.append(row)

headers = rows[0]
stars_data = rows[1:]

dataframe = pd.read_csv("final.csv")

stars_mass = dataframe["solar_mass"].tolist()
stars_radius = dataframe["solar_radius"].tolist()
star_names = dataframe["star_names"].tolist()

stars_mass.pop(0)
stars_radius.pop(0)
star_names.pop(0)

solar_mass = []

for row in solar_mass:
    si_unit = float(row)*1.989e+30
    solar_mass.append(si_unit)

solar_radius = []

for data in solar_radius:
    si_unit = float(row)* 6.957e+8
    solar_radius.append(si_unit)


star_mass = solar_mass
star_radius = solar_radius

star_gravities = []
for index,data in enumerate(star_names):
    gravity = (float(star_mass[index])*5.972e+24) / (float(star_radius[index])*float(star_radius[index])*6371000*6371000) * 6.674e-11
    star_gravities.append(gravity)

for index, data in enumerate(stars_data):
    stars_data.append(stars_data[index] + star_gravities[index])

graph = px.scatter(stars_data, x=stars_data["Distance"] , y=stars_data["Gravity"])
graph.show()

suitable_gravity = []

for i in stars_data:
  if float(i[2]) >= 100:
    suitable_gravity.append(i)

ideal_stars = []

for i in suitable_gravity:
  if float(i[5]) < 1.5:
    ideal_stars.append(i)

temp = []
for i in ideal_stars:
  if float(i[5]) < 3.5:
    temp.append(i)

line = px.line(x=stars_data[2] , y=stars_data[3])
line.show()

with open("final.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)