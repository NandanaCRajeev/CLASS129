import csv
data=[]
with open("PS_2022.02.08_04.44.36.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planets_data=data[1:]
for data_point in planets_data:
    data_point[2]=data_point[2].lower()
planets_data.sort(key=lambda planets_data:planets_data[2])
with open("dataset_2_sorted.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planets_data)