from os import listdir
from os.path import isfile, join
from pybtex.database.input import bibtex
import csv


def write_to_csv(entries,filename):

    with open(filename, 'w', encoding="utf8", newline='') as csvfile:
        print(entries[0].keys())
        fieldnames = entries[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

def get_pinfobib(filename):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(filename)
    #entries = [{'title': x.title, 'author': x.author, 'year': x.year, 'doi': x.doi,'url': x.uri} for x in bib_data.entries]
    keys = list(bib_data.entries.keys())
    
    def get_field(x,field):
        try:
            return bib_data.entries[x].fields[field]
        except:
            return ""

    entries = [{'title': get_field(x,'title') , 'author': get_field(x,'author1'), 
                'year': get_field(x,'year'), 'doi': get_field(x,'doi'), 'url': get_field(x,'url') } for x in keys]

    return entries

def get_info_csv(filename):
    entries  = []
    with open(filename, encoding="utf8", mode ='r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            entries.append({'title': row[0], 'author': row[6], 'year': row[7], 'doi': row[5],'url': row[8]} )
    
    entries.pop(0)
    
    return entries

def main():
    mypath = "rawdata"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    bib = list(filter(lambda x: len(x) > 4 and x[-3:] == "bib",onlyfiles))
    csv = list(filter(lambda x: len(x) > 4 and x[-3:] == "csv",onlyfiles))

    ##print(csv)

    ##print(bib)

    all_entries = list()

    
    for b in bib: 
        all_entries.extend(get_pinfobib(f"rawdata/{b}"))
        
    for c in csv: 
        all_entries.extend(get_info_csv(f"rawdata/{c}"))

    all_entries = sorted(all_entries, key = lambda x: x['title'])

    write_to_csv(all_entries,"all_results.csv")
    print(len(all_entries))
main()