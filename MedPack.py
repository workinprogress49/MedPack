def update():
    import wget
    from requests import get
    from io import BytesIO
    from zipfile import ZipFile
    import requests, zipfile, io
    from tqdm import tqdm
    import urllib.request, json
    
    data_files = []
    import urllib.request, json 
    with urllib.request.urlopen("https://api.fda.gov/download.json") as url:
        data = json.loads(url.read().decode())
    for i in data['results']['drug']['label']['partitions']:
        data_files.append(i['file'])
    
    FDA = []
    for i in tqdm(data_files, desc = 'Pulling From Open FDA'):
        try:
            r = requests.get(i)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall()
            FDA.append(i.split('/')[-1].replace('.zip',''))
            
        except:
            break

    print('Created zips: ' + str(FDA))
    
    import requests
    import json

    FDAdrugs = {} #Initialize dictionary as blank dictionary

    def archive(): #archive fuction created to loop through json files and pull out data to dictionary.
        for i in range(len(data['results'])):
            try:
                druginfo = {"indications_and_usage" : data['results'][i]["indications_and_usage"][0]}
            except:
                continue
            for item in ['product_type', 'rxcui', 'product_ndc', 'route', 'substance_name', 'pharm_class_pe', 'pharm_class_epc', 'pharm_class_moa']:
                try:
                    druginfo.update({item:data['results'][i]["openfda"][item]})
                except:
                    continue
            try:
                FDAdrugs.update({data['results'][i]['openfda']['generic_name'][0]:druginfo})
            except:
                continue

            try:
                FDAdrugs.update({data['results'][i]['openfda']['brand_name'][0]:druginfo})
            except:
                continue
        
    for i in tqdm(FDA, desc = 'Creating FDA Dictionary'):
        data = json.load(open(i))
        archive()

    print('Writing JSON...')

    # write to json
    json = json.dumps(FDAdrugs, indent=4, sort_keys=True)
    f = open("FDAdrugs.json","w")
    f.write(json)
    f.close()
    
    print('JSON file successfully created.')
    import pandas as pd

    pharm_class_epc = []
    pharm_class_pe = []
    product_ndc  = []
    product_type = []
    route = []
    rxcui = []
    substance_name = []
    pharm_class_moa = []

    text_list = ['pharm_class_epc','pharm_class_pe','product_ndc','product_type','route','rxcui','substance_name','pharm_class_moa']
    reg_list = [pharm_class_epc,pharm_class_pe,product_ndc,product_type,route,rxcui,substance_name,pharm_class_moa]

    for i in FDAdrugs:
        for x in range(len(text_list)):
            try:
                for item in FDAdrugs[i][text_list[x]]:
                    reg_list[x].append(item)
            except:
                pass

    pharm_class_epc = list(set(pharm_class_epc))
    pharm_class_pe = list(set(pharm_class_pe))
    product_ndc  = list(set(product_ndc))
    product_type = list(set(product_type))
    route = list(set(route))
    rxcui = list(set(rxcui))
    substance_name = list(set(substance_name))
    pharm_class_moa = list(set(pharm_class_moa))

    to_text_string = ['product_ndc','rxcui','substance_name']
    to_text = [product_ndc,route,substance_name]

    for i in range(len(to_text_string)):
        with open((to_text_string[i] + '.txt'), 'w') as thefile:
            for item in to_text[i]:
                thefile.write(str(item) + '\n')

    to_csv = [pharm_class_epc,pharm_class_pe,pharm_class_moa,route,product_type]

    df = pd.DataFrame(to_csv, ['pharm_class_epc', 'pharm_class_pe','pharm_class_moa','route', 'product_type']).T
    df.to_csv('pharm_classes product_types routes.csv', index=False)
    print('Supporting Files Created.')
    
    import os
    for i in tqdm(FDA, desc = 'Cleaning up Folder'):
        os.remove(i)
    print('Clean up Complete!')
    
    
def search_drugs(name = 'no_name',
indications_and_usage = None,
pharm_class_epc = None,
pharm_class_pe = None,
product_ndc  = None,
product_type = None,
route = None,
rxcui = None,
substance_name = None,
pharm_class_moa = None,
JSON = False,
CSV = False,
pretty_list = False): 
    
    from tqdm import tqdm
    import json
    import re
    from fuzzywuzzy import fuzz

    FDAdrugs = json.load(open('FDAdrugs.json'))

    result = {}

    for i in tqdm(FDAdrugs, desc = 'Searching Medications'):
        if indications_and_usage != None:
            if re.search(indications_and_usage.upper(),FDAdrugs[i]['indications_and_usage'].upper()):
                pass
            else:
                continue     
        try:
            epc = None
            if pharm_class_epc != None:
                for x in FDAdrugs[i]['pharm_class_epc']:
                    if fuzz.partial_ratio(pharm_class_epc.upper(), x.upper()) > 98:
                        epc = True
                        break
                    else:
                        epc = False
                        pass
            if epc == True:
                pass
            if epc == None:
                pass
            if epc == False:
                continue
        except:
            continue

        try:
            pe = None
            if pharm_class_pe != None:
                for x in FDAdrugs[i]['pharm_class_pe']:
                    if fuzz.partial_ratio(pharm_class_pe.upper(), x.upper()) > 98:
                        pe = True
                        break
                    else:
                        pe = False
                        pass
            if pe == True:
                pass
            if pe == None:
                pass
            if pe == False:
                continue
        except:
            continue
        
        try:
            ndc = None
            if product_ndc != None:
                for x in FDAdrugs[i]['product_ndc']:
                    if fuzz.partial_ratio(product_ndc.upper(), x.upper()) > 98:
                        ndc = True
                        break
                    else:
                        ndc = False
                        pass
            if ndc == True:
                pass
            if ndc == None:
                pass
            if ndc == False:
                continue
        except:
            continue
                
        try:
            pt = None
            if product_type != None:
                for x in FDAdrugs[i]['product_type']:
                    if fuzz.partial_ratio(product_type.upper(), x.upper()) > 98:
                        pt = True
                        break
                    else:
                        pt = False
                        pass
            if pt == True:
                pass
            if pt == None:
                pass
            if pt == False:
                continue
        except:
            continue        
        
        try:
            rt = None
            if route != None:
                for x in FDAdrugs[i]['route']:
                    if fuzz.partial_ratio(route.upper(), x.upper()) > 98:
                        rt = True
                        break
                    else:
                        rt = False
                        pass
            if rt == True:
                pass
            if rt == None:
                pass
            if rt == False:
                continue
        except:
            continue 
        
        try:
            rx = None
            if rxcui != None:
                for x in FDAdrugs[i]['rxcui']:
                    if fuzz.partial_ratio(rxcui.upper(), x.upper()) > 98:
                        rx = True
                        break
                    else:
                        rx = False
                        pass
            if rx == True:
                pass
            if rx == None:
                pass
            if rx == False:
                continue
        except:
            continue         

        try:
            sn = None
            if substance_name != None:
                for x in FDAdrugs[i]['substance_name']:
                    if fuzz.partial_ratio(substance_name.upper(), x.upper()) > 98:
                        sn = True
                        break
                    else:
                        sn = False
                        pass
            if sn == True:
                pass
            if sn == None:
                pass
            if sn == False:
                continue
        except:
            continue       

        try:
            pc = None
            if pharm_class_moa != None:
                for x in FDAdrugs[i]['pharm_class_moa']:
                    if fuzz.partial_ratio(pharm_class_moa.upper(), x.upper()) > 98:
                    #if pharm_class_moa.upper() == x.upper():
                        pc = True
                        break
                    else:
                        pc = False
                        pass
            if pc == True:
                pass
            if pc == None:
                pass
            if pc == False:
                continue
        except:
            continue         
    
        result.update({i:FDAdrugs[i]})
        

    
    if pretty_list == True:
        pretty = list(result.keys())
        pretty = map(lambda x:x.lower(),pretty)
        pretty = list(set(pretty))
        print('Total Results found:')
        print(len(pretty))
        return pretty

    if JSON == True:
        json = json.dumps(result, indent=4, sort_keys=True)
        f = open((name + '.json'),"w")
        f.write(json)
        f.close()
        
    if CSV == True:
        import csv
        pretty = list(result.keys())
        pretty = map(lambda x:x.lower(),pretty)
        pretty = list(set(pretty))
        with open((name+'.csv'), 'wb') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(pretty)

        
        
    
def search_drugs_widget(
#name = 'no_name',
indications_and_usage = '',
pharm_class_epc = '',
pharm_class_pe = '',
product_ndc  = '',
product_type = '',
route = '',
rxcui = '',
substance_name = '',
pharm_class_moa = ''
#JSON = '',
#CSV = '',
#pretty_list = ''
): 
    
    from tqdm import tqdm
    import json
    import re
    from fuzzywuzzy import fuzz

    FDAdrugs = json.load(open('FDAdrugs.json'))

    result = {}

    for i in tqdm(FDAdrugs, desc = 'Searching Medications'):
        if indications_and_usage != '':
            if re.search(indications_and_usage.upper(),FDAdrugs[i]['indications_and_usage'].upper()):
                pass
            else:
                continue     
        try:
            epc = None
            if pharm_class_epc != '':
                for x in FDAdrugs[i]['pharm_class_epc']:
                    if fuzz.partial_ratio(pharm_class_epc.upper(), x.upper()) > 95:
                        epc = True
                        break
                    else:
                        epc = False
                        pass
            if epc == True:
                pass
            if epc == None:
                pass
            if epc == False:
                continue
        except:
            continue

        try:
            pe = None
            if pharm_class_pe != '':
                for x in FDAdrugs[i]['pharm_class_pe']:
                    if fuzz.partial_ratio(pharm_class_pe.upper(), x.upper()) > 95:
                        pe = True
                        break
                    else:
                        pe = False
                        pass
            if pe == True:
                pass
            if pe == None:
                pass
            if pe == False:
                continue
        except:
            continue
        
        try:
            ndc = None
            if product_ndc != '':
                for x in FDAdrugs[i]['product_ndc']:
                    if fuzz.partial_ratio(product_ndc.upper(), x.upper()) > 95:
                        ndc = True
                        break
                    else:
                        ndc = False
                        pass
            if ndc == True:
                pass
            if ndc == None:
                pass
            if ndc == False:
                continue
        except:
            continue
                
        try:
            pt = None
            if product_type != '':
                for x in FDAdrugs[i]['product_type']:
                    if fuzz.partial_ratio(product_type.upper(), x.upper()) > 95:
                        pt = True
                        break
                    else:
                        pt = False
                        pass
            if pt == True:
                pass
            if pt == None:
                pass
            if pt == False:
                continue
        except:
            continue        
        
        try:
            rt = None
            if route != '':
                for x in FDAdrugs[i]['route']:
                    if fuzz.partial_ratio(route.upper(), x.upper()) > 95:
                        rt = True
                        break
                    else:
                        rt = False
                        pass
            if rt == True:
                pass
            if rt == None:
                pass
            if rt == False:
                continue
        except:
            continue 
        
        try:
            rx = None
            if rxcui != '':
                for x in FDAdrugs[i]['rxcui']:
                    if fuzz.partial_ratio(rxcui.upper(), x.upper()) > 95:
                        rx = True
                        break
                    else:
                        rx = False
                        pass
            if rx == True:
                pass
            if rx == None:
                pass
            if rx == False:
                continue
        except:
            continue         

        try:
            sn = None
            if substance_name != '':
                for x in FDAdrugs[i]['substance_name']:
                    if fuzz.partial_ratio(substance_name.upper(), x.upper()) > 95:
                        sn = True
                        break
                    else:
                        sn = False
                        pass
            if sn == True:
                pass
            if sn == None:
                pass
            if sn == False:
                continue
        except:
            continue       

        try:
            pc = None
            if pharm_class_moa != '':
                for x in FDAdrugs[i]['pharm_class_moa']:
                    if fuzz.partial_ratio(pharm_class_moa.upper(), x.upper()) > 95:
                    #if pharm_class_moa.upper() == x.upper():
                        pc = True
                        break
                    else:
                        pc = False
                        pass
            if pc == True:
                pass
            if pc == None:
                pass
            if pc == False:
                continue
        except:
            continue         
    
        
        if indications_and_usage == pharm_class_epc == pharm_class_pe == product_ndc == product_type == route == rxcui == substance_name == pharm_class_moa:
            result = {}
        else:
            result.update({i:FDAdrugs[i]})
            
    pretty = list(result.keys())
    pretty = map(lambda x:x.lower(),pretty)
    pretty = list(set(pretty))
    print('Total Results found:')
    print(len(pretty))
    print(pretty)
    
def pharm_class_epc():
    import pandas as pd
    df = pd.read_csv('pharm_classes product_types routes.csv')
    return [x for x in list(df['pharm_class_epc']) if str(x) != 'nan']

def pharm_class_pe():
    import pandas as pd
    df = pd.read_csv('pharm_classes product_types routes.csv')
    return [x for x in list(df['pharm_class_pe']) if str(x) != 'nan']

def pharm_class_moa():
    import pandas as pd
    df = pd.read_csv('pharm_classes product_types routes.csv')
    return [x for x in list(df['pharm_class_moa']) if str(x) != 'nan']

def route():
    import pandas as pd
    df = pd.read_csv('pharm_classes product_types routes.csv')
    return [x for x in list(df['route']) if str(x) != 'nan']

def product_type():
    import pandas as pd
    df = pd.read_csv('pharm_classes product_types routes.csv')
    return [x for x in list(df['product_type']) if str(x) != 'nan']

def show_me(variable):
    import pandas as pd
    df = pd.read_csv('pharm_classes product_types routes.csv')
    return [x for x in list(df[variable]) if str(x) != 'nan']