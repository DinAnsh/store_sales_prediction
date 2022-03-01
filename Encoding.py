
def Out_Identifier_encoder(id):
    l = ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049']
    if id in l:
        return l.index(id)    
    else:
        print("Identifier is Not in List!")

def Out_type_encoder(ty):
    l = ['Grocery Store','Supermarket Type1', 'Supermarket Type2','Supermarket Type3']
    if ty in l:
        return l.index(ty)
    else:
        print("Type is not in list!")

def get_features(values):
    try:
        for i in range(len(values)):
            if i==0:
                identifier = Out_Identifier_encoder(values[i])
            if i==1:
                mrp = float(values[i])
            if i==2:
                type = Out_type_encoder(values[i])
        return (identifier,mrp,type)

    except Exception as e:
        raise e 

if __name__ == "__main__":
    v = ['OUT011',52.2,'Supermarket Type1']
    # print(type(v))
    t = get_features(v)
    print(t)