
def Out_Identifier_encoder(id):
    l = ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049']
    return l.index(id)    
   

def Out_type_encoder(ty):
    l = ['Grocery Store','Supermarket Type1', 'Supermarket Type2','Supermarket Type3']
    return l.index(ty)

def Item_Type_encoder(it):
    l = ['Baking Goods', 'Breads', 'Breakfast', 'Canned', 'Dairy',
       'Frozen Foods', 'Fruits and Vegetables', 'Hard Drinks',
       'Health and Hygiene', 'Household', 'Meat', 'Others', 'Seafood',
       'Snack Foods', 'Soft Drinks', 'Starchy Foods']
    return l.index(it)

def Item_Fat_encoder(fat):
    if fat == "Low Fat":
        return 0
    else:
        return 1

def Out_size_encoder(s):
    l = ['High', 'Medium', 'Small']
    return l.index(s)

def get_features(values):    
    for i in range(len(values)):
        if i==0:    #Outlet_Identifier
            identifier = Out_Identifier_encoder(values[i])
        if i==1:  #Item_Fat_Content
            fat_content = Item_Fat_encoder(values[i])
        if i==2:  #Item_MRP
            try :
                mrp = float(values[i])
            except :
                return "please enter numeric value in Item_MRP !!"
        if i==3:    #Item_Type
            Item_type = Item_Type_encoder(values[i])
        if i==4:    #Item_Visibility
            try:
                vis = float(values[i])**(1/2)
            except :
                return "please enter numeric value in Item_visibilty !!"
        if i==5:    #Outlet_Establishment_year
            year = int(values[i])
        if i==6:    #Outlet_size
            size = Out_size_encoder(values[i])
        if i==7:    #Outlet_Type
            out_type = Out_type_encoder(values[i])
    return (identifier,fat_content,mrp,Item_type,vis,year,size,out_type)


if __name__ == "__main__":
    v = ['OUT011',52.2,'Supermarket Type1']
    # print(type(v))
    t = get_features(v)
    print(t)