import os
import glob

author_filter=[{
            "tag": "100", #author
            "ind1": "1",
            "ind2": " ",
            }]
title_filter=[{
            "tag": "245", #title
            "ind1": "1",
            "ind2": "0",
            }]

lastcopies_filter=[{
            "tag":"583", #bwlastcopies
            "ind1":"1",
            "ind2":" ",
}]

issue_filter=[#issue_filter,
    { 
        "tag":"250",
        "ind1":" ",
        "ind2":" ",
}
]

namespaces={  # Manually extracted from the XML file, but there could be code written to automatically do that.
            "zs": "http://www.loc.gov/zing/srw/",
            "": "http://www.loc.gov/MARC21/slim",
                }



ReiheA='./Reihe A/'
extractReiheA='./extract/Reihe A/'
filelist_1=glob.glob('./Reihe A/Reihe*.csv',recursive=True)
isbnlist='./extract/isbnlist/'
filelist_2=glob.glob('./extract/Reihe A/Reihe*-extract.csv',recursive=True)
dnbresult='./extract/DNB/'
filelist2_5=glob.glob('./extract/isbnlist/Reihe*.csv',recursive=True)
filelist_3=glob.glob('./extract/isbnlist/Reihe*-urllist.csv',recursive=True)
filelist_4=glob.glob('./extract/DNB/Reihe-*-additdata.csv',recursive=True)

namespace={  # Manually extracted from the XML file, but there could be code written to automatically do that.
            "zs": "http://www.loc.gov/zing/srw/",
            "": "http://www.loc.gov/MARC21/slim",
                }
url_template_k10plus = "https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{author}+and+pica.per%3D{title}+and+pica.bib%3D20735&maximumRecords=10&recordSchema=marcxml"

paths=['./extract/Reihe A/','./extract/isbnlist/','./extract/DNB/','Reihe A/']
test=glob.glob('./extract/DNB/Reihe-21*.csv',recursive=True)