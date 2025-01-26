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



def get_phase_domain_count(phase_domain):
    
    values = list()
    count = dict()

    for pd in phase_domain:
      new_count = count.get(pd,0) + 1
      count.update({pd: new_count})


    for item in count.items():
        pd, count_item = item
        p,d = pd
        
        values.append(f"{{\"domain\":\"{d}\", \"phase\":\"{p}\", \"value\":{count_item}}}")

    values = ",\n".join(values)
    

    template = '''{
      "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
      "data": {
        "values": [
          (values)
        ]
      },
      "mark": "bar",
      "encoding": {
        "x": {"field": "domain"},
        "y": {"field": "value", "type": "quantitative"},
        "xOffset": {"field": "phase"},
        "color": {"field": "phase"}
      }
    }'''
    
    template = template.replace("(values)",values)
    
    return template


def get_phase_domain_count_stacked(phase_domain):
    
    values = list()
    count = dict()

    for pd in phase_domain:
      new_count = count.get(pd,0) + 1
      count.update({pd: new_count})


    for item in count.items():
        pd, count_item = item
        p,d = pd
        
        values.append(f"{{\"domain\":\"{d}\", \"phase\":\"{p}\", \"value\":{count_item}}}")

    values = ",\n".join(values)
    
    template = '''{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {
      "values": [
        {"domain":"Cloud", "phase":"CD", "value":13},
        {"domain":"Cloud", "phase":"CI", "value":8},
        {"domain":"Generic", "phase":"CI", "value":5},
        {"domain":"Generic", "phase":"CD", "value":5},
        {"domain":"Safety-Crytical Systems", "phase":"CT", "value":1},
        {"domain":"Safety-Crytical Systems", "phase":"CI", "value":1},
        {"domain":"Safety-Crytical Systems", "phase":"CD", "value":1},
        {"domain":"IoT", "phase":"CI", "value":2},
        {"domain":"IoT", "phase":"CD", "value":4},
        {"domain":"Generic", "phase":"CDEV", "value":3},
        {"domain":"Generic", "phase":"CT", "value":3},
        {"domain":"Generic", "phase":"CO", "value":4},
        {"domain":"Generic", "phase":"CM", "value":3},
        {"domain":"Generic", "phase":"CF", "value":3},
        {"domain":"Data Science", "phase":"CD", "value":1},
        {"domain":"Data Science", "phase":"CI", "value":1},
        {"domain":"Data Science", "phase":"CDEV", "value":1},
        {"domain":"Data Science", "phase":"CT", "value":1},
        {"domain":"Data Science", "phase":"CO", "value":1},
        {"domain":"Data Science", "phase":"CM", "value":1},
        {"domain":"Data Science", "phase":"CF", "value":1},
        {"domain":"Security", "phase":"CD", "value":2},
        {"domain":"Security", "phase":"CI", "value":2},
        {"domain":"Security", "phase":"CDEV", "value":2},
        {"domain":"Security", "phase":"CT", "value":2},
        {"domain":"Security", "phase":"CO", "value":2},
        {"domain":"Security", "phase":"CM", "value":2},
        {"domain":"Security", "phase":"CF", "value":2},
        {"domain":"Cyber-Physical Systems", "phase":"CDEV", "value":1},
        {"domain":"Cyber-Physical Systems", "phase":"CT", "value":1},
        {"domain":"Cyber-Physical Systems", "phase":"CM", "value":1}
      ]
    },
    "transform": [
      {"filter": "datum.value > 0"}
    ],
    "mark": "bar",
    "encoding": {
      "x": {"field": "phase", "type": "nominal", "axis": {"title": "phase"}},
      "y": {"field": "value", "type": "quantitative", "axis": {"title": "value"}},
      "color": {"field": "domain", "type": "nominal", "legend": {"title": "domain"}}
    }
    }'''
    
    template = template.replace("(values)",values)
    
    return template