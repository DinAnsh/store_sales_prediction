# store_sales_prediction
![image](https://cdn.pixabay.com/photo/2015/08/07/16/07/shopping-879498_960_720.jpg) <br />

According to the quote, "Success in sales is the sum of small efforts, repeated day in & day out"<br />
Let us consider a supermarket has several outlets or several stores around the world & they want us to predict the sales which they can expect.
We can tell the company what are all the challenges they may face
What are the brands or products which is sold the most & other such kind of things
This helps sales team to understand which product to sell & which product to promote & other such kind of things
They can also make several marketing plans(let's say that a particular product in a particular store is getting sold the most & we may find some insights from it - as of why this product is getting sold the most & this helps the company to make better marketing decisions)

---
### Problem Statement :
The main goal is to make analysis of data and to build Machine learning model to predict the sales of each of each item at a particular outlet. 
We have 12 columns and 8523 rows of data. We get this data from Kaggle. 

---
### Data Preprocessing :
As we saw it, our dataset contains null values in two columns: Item_Weight and Outlet_Size. By making exploratory we found some idea about how we can deal with NaN values in these columns.
- All the Null values in **Item_Weight** belongs to the Year 1985. 
- We replaced null values of **Item_Weight** with each Item_Identifier's mean Weight.
- For 'Outlet_Size' column, we found a relation between Outlet_Size and Outlet_Type. We will use this to impute Outlet_Size by taking most frequent Size based on Outlet type.
- As the **Item_Visibility** and **Item_Outlet_sales** were right skewed. We applied *exponential transformation* to reduce skewness or outliers.
- We made the values of the column "Item_Fat_Content" uniform.
- Manage categorical columns with **LabelEncoder**.

---
### Data Visualization
- Data visualization is the graphical representation of information and data.
- It enables decision makers to see analytics presented visually, so they can grasp difficult concepts or identify new patterns

---
### Exploratory Data Analysis (EDA)
Let's to make some hypotheses about features of data. Let's ask what element can increase or decrease items sales for a supermarket?
- The usefulness of product for the vast majority of customers. It is defined by product category or the brand of product, and so one... But here, based on our dataset, we can use "Item_Type" feature to estimate the kind of product is loved by customers.
- The price of product can influence the sales. To valid this hypothese we will check correlation between Item_MRP and "Item_Outlet_Sales"
- The visibility of product in the store: Column "Item_Visibility"
- The place where the store is established: depending on the location of the store the product's price may be different so column "Outlet_Location_Type" is important
These hypotheses are subjective. but with further exploration of the data, we will accept or reject each of these assumptions.

---
### WebApp Link :

---
### Credit :
- Dipendra Singh https://www.linkedin.com/in/dipendrahada/
- Dinansh Bhardwaj https://www.linkedin.com/in/dinansh/
#### Thank You for reading 😃<br> If you like this project, please do give the star. If you have any suggestions or issues, please drop a message.
