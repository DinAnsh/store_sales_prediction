# store_sales_prediction
store_sales_prediction is a package which predicts how various items sell based on a provided dataset.
To accomplish this, the package uses numerous factors such product type, price and visibility. 
It can predict items sales for any shopping outlet.
![1_io2zk4HVTX8764K_fJAerw](https://user-images.githubusercontent.com/49347849/218284437-5ed0b8d2-91c0-4f03-95e9-29965970498e.png) <br />

According to the quote, "Success in sales is the sum of small efforts, repeated day in & day out".
<br />
Suppose an international shopping chain wants a realistic prediction of sales.
To assess this, various important factors should be considered,such as the different types and brands of products sold at the company.
Other important factors to consider how how well certain product types and brands sell.
This allows the sales team to come up with a reasonable prediction on which products will sell best, and act accordingly in marketing these products. 

---
### Problem Statement:
Shopping malls and chains want to predict how well their products will sell so they can market and adjust their inventories accordingly. In order to do this, they record individual item sales data. 
This data, along with consumer information and item details, is stored in data stores, which are located in a data warehouse. 
By mining the data store from the data warehouse, more anomalies and common patterns can be discovered.
Humans can make sales predictions themselves. 
However, man-made sales predictions can be unreliable due to various mistakes, such as incorrectly recording item sales, not accounting for other factors, etc.
The goal of this project is to analyze such data and build a machine learning model that can predict the sales of each item at a particular outlet. 
This model could be a useful alternative to man-made sales predictions. 
store_sales_prediction uses 12 columns and 8523 rows of data, which are retrieved from Kaggle. 

---
### Exploratory Data Analysis (EDA)
store_sales_predicition assesses the following variables, which can increase or decrease items sales for a supermarket:
-The product type: based on a given dataset, store_sales_prediction uses the"Item_Type" feature to estimate product types that have high success among customers.
- The price of the product; store_sales_prediction checks correlation between Item_MRP and "Item_Outlet_Sales"to see how prices influence sales
- The visibility of the product; store_sales_prediction uses Column "Item_Visibility" to assess this.
- The location of the store: store_sales_prediction's column "Outlet_Location_Type" records the store's location, which may influence price.

---
### Notes-Adjustments for Data Preprocessing:
Our dataset contained null values in two columns: Item_Weight and Outlet_Size. Using exploratory data analysis, the following adjustments were made to correct this issue:
- All null values in the **Item_Weight** column were from the year 1985.
- All null items in the column **Item_Weight** were replaced with mean weight values from Item_Identifier.
- A relation between Outlet_Size and Outlet_Type was discovered. This will be used to impute Outlet_Size by taking the most frequent outlet size based on outlet type.
- The data for columns **Item_Visibility** and **Item_Outlet_sales** were right skewed.As such, *exponential transformation* was applied to reduce amy skewness or outliers in the data.
- The values in the column "Item_Fat_Content" were adjusted to be more uniform.
- Categorical columns were managed with **LabelEncoder**.

---
### Instructions for Use


---
### Guidelines for Contributing

---
<<<<<<< HEAD
### WebApp Link: https://store-sales-prediction-app.herokuapp.com/
=======
### WebApp Link : https://store-sales-prediction-app.herokuapp.com/

>>>>>>> 0286e366d600dbb3646562e502858e2adfa8f199
---
### Credit:
- Dipendra Singh https://www.linkedin.com/in/dipendrahada/
- Dinansh Bhardwaj https://www.linkedin.com/in/dinansh/
#### Thank You for reading 😃<br> If you like this project, please do give the star. If you have any suggestions or issues, please drop a message.
