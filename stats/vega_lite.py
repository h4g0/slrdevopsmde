def get_count_col(col_name,cols,max=-1):
    

    count_list = dict()


    for col in cols:
        
        count_t = count_list.get(col,0) + 1
        
        count_list.update({col: count_t })



    count_list = [(k,v) for k, v in count_list.items()]

    ##filtered_list = filter(lambda x: x[1] > 1000, count_list)

    ##sorted_list = sorted(filtered_list, key=lambda x: x[1],reverse=True)

    if max > -1:
        count_list = sorted(count_list, key = lambda x: x[1],reverse=True)[0:max]

    values = ",".join(["{" + '"' + col_name + '": "' + str(x[0]) + '" , '  + '"count": ' + str(x[1]) + "}" for x in count_list])


    template =  '''{
  
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A bar chart with highlighting on hover and selecting on click. (Inspired by Tableau's interaction style.)",
  "data": {
    "values": [
          (values)
        ]
  },
  "mark":  {"type": "bar", "size": 20},
  "encoding": {
    "x": {"field": "(col_name)", "type": "ordinal","scale": {"padding": 5}, "sort": "-y"},
    "y": {"field": "count", "type": "quantitative", "stack": false}
  }
  
}

'''

    template = template.replace("(values)",values)
    template = template.replace("(col_name)",col_name)

    return template