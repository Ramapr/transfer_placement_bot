import re 


def filter_surname_name(x) -> list:
    return re.findall(r'\w*', x.lower())

def filter_null_elements(x:list ): 
    return list(filter(lambda x: len(x) > 0 and not x.isdigit() , x)) 


def find_serparator(s): 
    for sep in ['\n', ',', ';', ',']: 
        return sep if sep in s else '-1' 

def parse_fio(x):
    seps = [',', ';', '\n']
    if any([s in x for s in seps]): 
        for sep in seps:
            if sep in x: 
                return len(x.split(sep))
        # sep not found 
    return -1 
    # it is fraud  

def get_fio(x):
    # fio > 1
    seps = [',', ';', '\n']
    if any([s in x for s in seps]): 
        for sep in seps:
            if sep in x: 
                return x.split(sep)
        # sep not found 
    return [x]
    
def find_pass(x):
    """seria and number"""
    return re.findall(r'\d{10}', x) 


def parse_phone(x):
    """seria and number"""
    return re.findall(r'\d{10}', x) 

def find_fios(v):
    return list(map(lambda x: get_fio(x), v))
    
def find_pass_data(x): 
    """
    find_pass_data(slice.passport_forward)
    """
    return list(map(lambda x: find_pass(x), x.str.replace(' ' , '').values))
