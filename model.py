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
dataset.drop(["Item_Identifier","Item_Fat_Content","Item_Weight","Item_Visibility","Item_Type","Outlet_Location_Type","Outlet_Size","Outlet_Establishment_Year"],axis=1,inplace=True)

le = LabelEncoder()
dataset["Outlet_Identifier"] = le.fit_transform(dataset.Outlet_Identifier)
dataset["Outlet_Type"] = le.fit_transform(dataset.Outlet_Type)

dataset['Item_Outlet_Sales']=dataset.Item_Outlet_Sales**(1/4)

X = dataset.drop("Item_Outlet_Sales",axis=1)
y = dataset["Item_Outlet_Sales"]

from sklearn.ensemble import GradientBoostingRegressor
g_boosting = GradientBoostingRegressor(
     learning_rate= 0.028571428571428574, n_estimators=400, max_depth=2, random_state=0,
     )
g_boosting.fit(X,y)

pickle.dump(g_boosting,open('model.pkl','wb'))
