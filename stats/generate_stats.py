import pandas as pd
from vega_lite import get_count_col

graph_folder = "generated_graphs"

def write_to_file(contents,filename):
  with open(filename, 'w') as file:
    file.write(contents)

def stats_column_count(col,df,max=-1):
    write_to_file(get_count_col(col,df[col],max),f"{graph_folder}/{col}.json")

def get_stats(df):
  cols = ["year", "domain", "phase", "validation", "type", "goal", "m2m", "m2t", "t2m", "restrictions","year"]

  for col in cols:
    stats_column_count(col,df)

  domain = df["domain"]
  phase = df["phase"]

  print(len(domain))
  print(len(phase))

  phase_domain = [f"{domain[i]}, {phase[i]}" for i in range(len(domain))]

  write_to_file(get_count_col("phase_domain",phase_domain,5),f"{graph_folder}/phase_domain.json")

def main():

  df = pd.read_excel('analysisreegineering-extended-final.xlsx')

  
  get_stats(df)
  
  return

main()