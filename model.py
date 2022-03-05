import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pickle

#Connecting to cassandra asta db
cloud_config= {
        'secure_connect_bundle': 'C:/Users/DELL/Desktop/StoreSalesProject/secure-connect-storesales.zip'
}
auth_provider = PlainTextAuthProvider('sPtdpMPgXuuZALChHGxbGuxQ','FQqvQtFwl2xg7fKMuiD9Rtxaizre1ZeAdQLfI,8m8DxviuGwcM1CId4L1insiXSmD3CD._moiuFp9Y6PL4Ays-l3bmF-hRP.pNf9.NPumZImLQ9bIXlRgM0rwY3INiiR')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect("ssp")
res = session.execute("select * from ssp.train")

dataset = pd.DataFrame(res)

#fill missing values
missing_weight_idx = np.where(dataset.Item_Weight.isnull())[0]
g = dataset.groupby(["Item_Identifier"]).mean()
for i in missing_weight_idx:
    for j in g.index:
        if dataset.Item_Identifier[i] == j:
            dataset.Item_Weight[i] = g.loc[j][3]
dataset.drop(axis=0,index=dataset[dataset.Item_Weight.isnull()].index,inplace=True)
dataset.Outlet_Size.fillna("Small",inplace=True)

dataset['Item_Visibility']=dataset.Item_Visibility**(1/2)
dataset['Item_Outlet_Sales']=dataset.Item_Outlet_Sales**(1/4)

dataset.drop(["Item_Identifier","Item_Weight","Outlet_Location_Type"],axis=1,inplace=True)

le = LabelEncoder()
dataset["Item_Fat_Content"] = le.fit_transform(dataset.Item_Fat_Content)
dataset["Outlet_Size"] = le.fit_transform(dataset.Outlet_Size)
dataset["Outlet_Identifier"] = le.fit_transform(dataset.Outlet_Identifier)
dataset["Outlet_Type"] = le.fit_transform(dataset.Outlet_Type)
dataset["Item_Type"] = le.fit_transform(dataset.Item_Type)


X = dataset.drop("Item_Outlet_Sales",axis=1)
y = dataset["Item_Outlet_Sales"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

from sklearn.ensemble import GradientBoostingRegressor
g_boosting = GradientBoostingRegressor(
     learning_rate= 0.028571428571428574, n_estimators=400, max_depth=2, random_state=0,
     )
g_boosting.fit(X_train,y_train)

pickle.dump(g_boosting,open('model.pkl','wb'))
