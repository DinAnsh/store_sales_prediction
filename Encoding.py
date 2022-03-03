
def Out_Identifier_encoder(id):
    l = ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049']
    return l.index(id)    
   

def Out_type_encoder(ty):
    l = ['Grocery Store','Supermarket Type1', 'Supermarket Type2','Supermarket Type3']
    return l.index(ty)

def get_features(values):   
    for i in range(len(values)):
        if i==2:
            identifier = Out_Identifier_encoder(values[i])
        if i==1:
            try :
                mrp = float(values[i])
            except :
                return "please enter numeric value in Item_MRP !!"
        if i==0:
            out_type = Out_type_encoder(values[i])
    return (identifier,mrp,out_type)


if __name__ == "__main__":
    v = ['OUT011',52.2,'Supermarket Type1']
    # print(type(v))
    t = get_features(v)
    print(t)