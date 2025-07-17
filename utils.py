import pandas as pd
import numpy as np



def make_for_bus(df, type_):
    if type_ not in ['forward', 'backward']:
        raise Exception #('Key error') 
        # type = 'forward' 
    fio_pass = [ 'fio_transfer', 'passport' ] 
    # n_forward int
    sub_column = ['phone_number'] + [v + '_' + type_  for v in fio_pass]
    # pass_seria fio 
    pre_final = df[sub_column]
    
    # check here 
    
    
    final_one = pd.merge(pd.merge(pre_final.pass_seria.apply(pd.Series).iloc[:, :1], 
         pre_final.fio.apply(pd.Series).iloc[:, :1] ,
         left_index=True, 
         right_index=True), 
         pre_final.phone_number, 
         left_index=True, 
         right_index=True)

    ttt = final_one.rename(columns={'0_x': 'seria_number', '0_y': 'fio'})
    ttt.sort_values(by='fio', inplace=True)
    ttt.reset_index(inplace=True)
    ttt.drop(columns='index', inplace=True)
    return ttt[['fio', 'phone_number', 'seria_number']]  



def find_inert(a, num):  
    # arrays
    bus_num = [0 for i in range(len(a))]
    used_element = [False for i in range(len(a))]
     
    # vars 
    temp_sum = 0 
    r = 0 
    target_bus = 1 
    
    while r < len(a):
        if not used_element[r]:
            temp_v = temp_sum + a[r] 
            # накопленная сумма + текущий элемент 
            
            if temp_v == num:
                bus_num[r] = target_bus 
                target_bus += 1
                temp_sum = 0 
                
            elif temp_v < num: 
                bus_num[r] = target_bus
                #used_element[l] = True
                temp_sum = temp_v
                
            elif temp_v > num:
                # adding of current element increacse sum greaser than needed
                l = r + 1
                
                while l < len(a) and temp_sum != 0:
                    if not used_element[l]:
                        temp_v = temp_sum + a[l] 
                        if temp_v == num:
                            bus_num[l] = target_bus 
                            used_element[l] = True
                            target_bus += 1
                            temp_sum = 0 
                            r -= 1
                            #print('11', r, l, temp_sum, target_bus)
                        
                        if temp_v < num: 
                            bus_num[l] = target_bus
                            used_element[l] = True
                            temp_sum = temp_v  
                            #print('12', r, l, temp_sum, target_bus)
                    l += 1
                    
                #print('22', r, l, temp_sum, target_bus)
                # краевое решение когда не нашли !
                if temp_sum != 0 : 
                    # не нашли  
                    target_bus += 1
                    temp_sum = 0 
                    r -= 1
                
        r += 1
        
    # if bus_num[-1] == 0 and not used_element[-1]:
    #     bus_num[
    return (bus_num, used_element)  



def make_inter(dff, transfer_clmn, people, target_col, n):
    df = dff.copy()

    target_indx = list(df.columns).index(target_col) 
    
    date = df[(df[people] > 0) & (df.fraud == False)][transfer_clmn].unique() 
    for d in date: 
        # print(d)
        v = part[(df[transfer_clmn] == d) & (df.fraud == False)][people] 
        ind = list(v.index)
        bus_no, _ = find_inert(v.values, n)
        df.iloc[ind[:], target_indx] = np.array(bus_no)
    return df
