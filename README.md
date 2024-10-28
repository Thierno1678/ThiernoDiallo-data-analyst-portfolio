# ThiernoDiallo-data-analyst-portfolio
"My Data Analyst Portfolio showcasing various projects"
# House Sales Analysis

This repository contains the data, SQL queries, visualizations, and analysis of house sales data. The purpose of this project is to explore the impact of various features like renovations, number of bedrooms, and area on house prices and provide predictions based on trends observed in the data.

## Project Overview
The **House Sales Analysis** project analyzes a dataset of house sales to identify trends and generate insights. We use Power BI for visualizations and SQL for data cleaning and manipulation.

Key insights from the project:
- **Renovations**: Renovated properties tend to have higher prices than non-renovated properties.
- **Bedrooms**: Properties with more bedrooms show a direct increase in price.
- **Quartile Zones**: Wealthier zones have more stable or increasing property values compared to others.

## Technologies Used
- **Power BI**: For creating visualizations and dashboards.
- **SQL (SQL Server Management Studio)**: For data cleaning, manipulation, and querying.
- **GitHub**: Version control and collaboration.

## File Structure



## Steps to Run the Analysis

1. **Data Cleaning**:
   - We cleaned and manipulated the dataset using SQL.
   - See `SQL_Scripts/cleaning.sql` for the exact queries used to prepare the dataset.

2. **Data Analysis**:
   - Key metrics such as price, area, renovations, and bedrooms were analyzed using SQL.
   - Check `SQL_Scripts/analysis.sql` for the analysis steps.

3. **Visualizations**:
   - We created interactive dashboards using Power BI. The visualizations highlight the trends we found, such as price differences based on grades, bedroom counts, and area.
   - You can find the visualizations in the `Visualizations/` folder as images or a PDF export.

## Key Insights
- **Price vs Grade**: Higher-graded properties are more expensive on average.
- **Bedrooms and Price**: Homes with more bedrooms consistently sell for higher prices.
- **Renovation Impact**: Renovated homes have a clear price advantage over non-renovated ones.
- **Seasonality of Sales**: First quarter tends to have the highest sales activity.

## Predictions
Based on the data, we can predict:
- **Renovated homes** will continue to see an increase in value, especially in high-demand zones.
- **Larger homes** (4+ bedrooms) will maintain their price growth due to demand for more space.
- **Wealthier zones** will have stable or increasing property values, while lower zones might see slower growth.
  
## Conclusion
This analysis provides insights into key factors affecting house prices. By focusing on renovations, property size, and quartile zones, sellers and buyers can make more informed decisions.

## How to Use the Files
- **SQL Scripts**: Use the SQL scripts in your preferred SQL environment to clean and analyze the data.
- **Power BI Files**: Open the visualizations folder to review the visualizations created during the analysis.

HouseSalesAnalysis/
├── Data/
│   ├── house_data.csv            # Original dataset used for analysis
├── SQL_Scripts/
│   ├── cleaning_queries.sql      # SQL queries for data cleaning
│   ├── analysis_queries.sql      # SQL queries for data analysis
├── Visualizations/
│   ├── price_by_grade.png        # Power BI visualizations (Exported PNGs)
│   ├── bedrooms_vs_price.png     # Power BI visualizations
│   ├── full_dashboard.pdf        # Full Power BI dashboard as PDF
├── Documentation/
│   ├── House_Sales_Report.pdf    # Final project report (PDF)
├── README.md                     # Overview of the project

# House Sales Analysis

This repository contains SQL queries, visualizations, and analysis of house sales data. The purpose of this project is to explore the impact of various factors like renovations, number of bedrooms, and house grade on house prices.

## Project Overview
The **House Sales Analysis** project analyzes a dataset of house sales to identify trends and generate insights. We use SQL for data cleaning and analysis, and Power BI for visualizations.

Key insights from the project:
- **Renovations**: Renovated homes have higher average prices compared to non-renovated homes.
- **Bedrooms**: Properties with more bedrooms have a direct increase in price.
- **Grade**: Higher grade properties are priced higher on average.

## Technologies Used
- **Power BI**: For creating visualizations and dashboards.
- **SQL**: For data cleaning, querying, and analysis.
- **GitHub**: For version control and collaboration.

## File Structure


## Steps to Run the Analysis

1. **Data Cleaning**:  
   We cleaned and prepared the dataset using SQL. You can find the SQL queries used for cleaning in the [SQL_Scripts/cleaning_queries.sql](SQL_Scripts/cleaning_queries.sql) file.
   - **Duplicate Detection**: Identified duplicates using:
     ```sql
     SELECT sale_date, price, bedrooms, grade, COUNT(*)
     FROM HouseDetails
     GROUP BY sale_date, price, bedrooms, grade
     HAVING COUNT(*) > 1;
     ```

2. **Data Analysis**:  
   We performed various analyses on the dataset. The SQL queries used for analysis can be found in the [SQL_Scripts/analysis_queries.sql](SQL_Scripts/analysis_queries.sql) file.
   - Example: Average price by grade:
     ```sql
     SELECT grade, AVG(price) AS AvgPrice
     FROM HouseDetails
     GROUP BY grade;
     ```

3. **Visualizations**:  
   We created interactive visualizations using Power BI, which highlight trends in house prices, bedrooms, and renovations. The visualizations are stored in the [Visualizations/](Visualizations/) folder as PNGs and PDFs.  
   - Example of visualizations: [price_by_grade.png](Visualizations/price_by_grade.png) and [bedrooms_vs_price.png](Visualizations/bedrooms_vs_price.png).

## Key Insights
- **Grade vs Price**: Higher-graded properties tend to have higher prices.
- **Bedrooms vs Price**: Homes with more bedrooms consistently sell for higher prices.
- **Renovation Impact**: Renovated homes tend to have higher sale prices.

## Conclusion
This project provides key insights into factors affecting house prices, and the results can help homeowners or investors make data-driven decisions.

