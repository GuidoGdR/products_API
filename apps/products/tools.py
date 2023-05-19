

def show_caregory_first(data:list[dict["category"]]) -> dict:
    
    finally_dic = {}
    for dic in data:
        
        if dic["category"] in finally_dic.keys():
            finally_dic[dic["category"]] += [dic]

        else:
            finally_dic[dic["category"]] = [dic]

    return finally_dic