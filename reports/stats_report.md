# **E-Commerce Sales Data Insights Report**

This report presents key insights generated from the data warehouse for e-commerce analytics. The insights are derived from SQL queries executed on the PostgreSQL database and visualized using Python.

---

## **1. Top 5 Products by Total Sales Revenue**

The following products generated the highest revenue:

| **Product Name**                                      | **Description**                                                                                   | **Total Revenue ($)** |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------|
| Fjallraven - Foldsack No. 1 Backpack                  | Your perfect pack for everyday use and walks in the forest.                                        | 2199.00               |
| John Hardy Women's Legends Naga Gold & Silver Bracelet| Inspired by the mythical water dragon, symbolizing love and protection.                           | 1390.00               |
| WD 4TB Gaming Drive Works with Playstation 4 Portable | Expand your PS4 gaming experience, Play anywhere.                                                 | 342.00                |
| Men's Cotton Jacket                                   | Great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions.                    | 335.94                |
| SanDisk SSD PLUS 1TB Internal SSD                     | Easy upgrade for faster boot up, shutdown, application load, and response.                        | 218.00                |

---

## **2. Top Customers by Total Spending**

The customers with the highest spending:

| **Customer Name**     | **Email**               | **Total Spent ($)** |
|-----------------------|-------------------------|---------------------|
| John Doe              | john@gmail.com          | 10130.22            |
| Don Romer             | don@gmail.com           | 1120.00             |
| David Morrison        | morrison@gmail.com      | 567.80              |
| Kevin Ryan            | kevin@gmail.com         | 481.76              |
| William Hopkins       | william@gmail.com       | 9.85                |

---

## **3. Total Sales Revenue by Product Category**

Revenue distribution across product categories:

| **Category Name**     | **Total Revenue ($)**   |
|-----------------------|-------------------------|
| Men's Clothing        | 2646.44                 |
| Jewelry               | 1410.98                 |
| Electronics           | 624.00                  |
| Women's Clothing      | 9.85                    |

---

### **Conclusion**

The insights generated from the data warehouse have provided a clear view of the top-performing products, valuable customers, and revenue distribution across categories. This information is crucial for making informed business decisions and identifying potential growth areas in the e-commerce domain.

For detailed SQL queries and methodologies, refer to the **[queries.sql](../sql/queries.sql)** file.