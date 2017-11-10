def  isAnagram(str1, str2):
    if str1 == None and str2 == None:
        return 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1.replace(" ","")
    str2.replace(" ", "")
    str1 = ''.join(val for val in str1 if val.isalnum())
    str2 = ''.join(val for val in str2 if val.isalnum())
    if str1 == str2:
        return 1
    else:
        dict1 = {}
        dict2 = {}
        
        
        for i in str1:
            if i in dict1:
                dict1[i] = dict1[i] +1
            else:
                dict1[i] = 1
        for i in str2:
            if i in dict2:
                dict2[i] = dict2[i] +1
            else:
                dict2[i] = 1
        if len(dict1) != len(dict2):
            return 0
        for k,v in dict1.items():
            if k not in dict2:
                return 0
            if k in dict2.keys() and v!=dict2[k]:
                return 0 
        for k,v in dict2.items():
            if k not in dict1:
                return 0
            if k in dict1.keys() and v!=dict1[k]:
                return 0 
                
        return 1 
