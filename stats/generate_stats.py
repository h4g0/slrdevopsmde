import pandas as pd
from vega_lite import get_count_col, get_phase_domain_count, get_phase_domain_count_stacked

graph_folder = "generated_graphs"

def write_to_file(contents,filename):
  with open(filename, 'w') as file:
    file.write(contents)

def stats_column_count(col,df,max=-1):
    write_to_file(get_count_col(col,df[col],max),f"{graph_folder}/{col}.json")


def transform_phase(phase):
  
  def helper(phase):
    if phase == "all":
      return ["cd","ci","cdev","ct","co","cm","cf"]
  
    else: 
      return phase.split(",")
    
  phases = [x.upper() for x in helper(phase)]

  return phases

def transform_stats_phase(phase):
  new_phase = list()

  for p in phase:
    for i in transform_phase(p):
      new_phase.append(i) 

  return new_phase


def transform_stats_phase_domain(domain,phase):
  new_phase_domain = list()

  for p in range(len(domain)):
    for i in transform_phase(phase[p]):
      new_phase_domain.append((i,domain[p])) 

  return new_phase_domain

def combs_mde(df):
  combs = list()

  for e in range(1,len(df)):
    comb = list()
    if df["t2m"][e]:
      comb.append("T2M")
    if df["m2m"][e]:
      comb.append("M2M")
    if df["restrictions"][e]:
      comb.append("OCL") 
    if df["m2t"][e]:
      comb.append("M2T")

    combs.append(" and ".join(comb))
  
  return combs

def get_stats(df):
  cols = ["year", "domain",  "validation", "type", "goal", "m2m", "m2t", "t2m", "restrictions","year"]

  for col in cols:
    stats_column_count(col,df)

  
  
  domain = df["domain"]
  phase = df["phase"]

  transformed_phase = transform_stats_phase(phase)
  write_to_file(get_count_col("phase",transformed_phase),f"{graph_folder}/phase.json")

  print(len(domain))
  print(len(phase))

  phase_domain = transform_stats_phase_domain(domain,phase)

  write_to_file(get_phase_domain_count_stacked(phase_domain), f"{graph_folder}/phase_domain.json")

  combsmede = combs_mde(df)

  write_to_file(get_count_col("combs mde",combsmede), f"{graph_folder}/combsmde.json")

def main():

  df = pd.read_excel('analysisreegineering-extended-final.xlsx')

  
  get_stats(df)
  
  return

main()