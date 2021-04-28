from bs4 import BeautifulSoup as bs
import pandas as pd
import os


#Making the directories
files = os.listdir()
os.mkdir("Cleaned_Patents")
for i in range(2000, 2021):
    os.mkdir("Cleaned_Patents/{}".format(str(i)))
to_fill_dir = "Cleaned_Patents"


#Logging the files that we cannot parse for whatever reason
open("ExceptionLog.txt", "w")

#Each filing is split by that xml encoding line
for file in files:
    if file[:3] == "ipg":
        year = file[3:][:2]
        month = file[3:][2:4]
        day = file[3:][4:6]
    if file[:2] == "pg":
        year = file[2:][:2]
        month = file[2:][2:4]
        day = file[2:][4:6]
    write_directory = "20{}/{}_{}.csv".format(year, month, day)
    try:
        with open(file, "r") as f:
            content = "".join(f.readlines())
        content = content.split('<?xml version="1.0" encoding="UTF-8"?>')
        for i in range(len(content)):
            content[i] += '<?xml version="1.0" encoding="UTF-8"?>'

        data = []
        for x in content:
            #Use beautifulsoup to grab content, convert to csv
            bs_content = bs(x, "lxml")
            description = bs_content.find_all("description")
            claims = bs_content.find_all("claims")
            term_grant = bs_content.find_all("us-term-of-grant")
            title = bs_content.find_all("invention-title")
            date = bs_content.find_all("date")
            kind = bs_content.find_all("kind")
            data.append([description, claims, term_grant, title, date, kind])


        data = pd.DataFrame(data, columns=["description", "claims", "term_grant", "title", "date", "kind"])
        data.to_csv("Cleaned_Patents/{}".format(write_directory))
    except:
        with open("ExceptionLog.txt", "a") as f:
            f.write(file + "\n")
        pass
        