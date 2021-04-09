import json
import re

if __name__ == "__main__":
    with open("database.json", 'r') as fRead:                    # open file database.json and load to perf_db
        perf_db = json.load(fRead)

    perf_db_clear = []
    perf_comp_set = []
    for perf in perf_db:                                         # loop through each components list of product
        perf_data = perf["comp"]
        for i in range(0, len(perf_data)):
            perf_data[i] = perf_data[i].strip().lower().title()  # remove whitespace, change to lowercase and title
            if perf_data[i] == 'Bht':                            # change Bht to uppercase
                perf_data[i] = 'BHT'
            if re.search("Alcohol Denat", perf_data[i]):                 # rename alcohol, water and perfume from components
                perf_data[i] = "Alcohol"
            if re.search("Aqua", perf_data[i]) or re.search("Water", perf_data[i]) or re.search("Eau", perf_data[i]):
                perf_data[i] = "Water"
            if re.search("Parfum", perf_data[i]) or re.search("Fragrance", perf_data[i]):
                perf_data[i] = "Parfum"
            if re.search("[Ii]somethyl", perf_data[i]):
                perf_data[i] = "Alpha-Isomethyl Ionone"
            if re.search("[Zz]oylmethane", perf_data[i]):
                perf_data[i] = "Butyl Methoxydibenzoylmethane"
            if re.search("[Mm]ethylpropional", perf_data[i]):
                perf_data[i] = "Butylphenyl Methylpropional"
            if re.search("Diethylamino", perf_data[i]):
                perf_data[i] = "Diethylamino hydroxybenzoyl hexyl benzoate"
            if re.search("\d{5}", perf_data[i]):
                temp = re.search("\d{5}", perf_data[i])[0]
                perf_data[i] = "CI " + temp
            if perf_data[i] not in perf_comp_set:
                perf_comp_set.append(perf_data[i])
        perf_db_clear.append({"name": perf["name"][0], "comp": perf_data})

    with open("set.txt", "w") as sWrite:
        perf_comp_set.sort()
        for each in perf_comp_set:
            sWrite.write(each + "\n")

    with open("database_clear.json", "w") as fWrite:
        json.dump(perf_db_clear, fWrite, indent=4)