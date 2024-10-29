-- Data Analysis Queries

-- Average Price by Grade
SELECT grade, AVG(price) AS AvgPrice
FROM HouseDetails
GROUP BY grade;

-- Average Price by Bedrooms
SELECT bedrooms, AVG(price) AS AvgPrice
FROM HouseDetails
GROUP BY bedrooms;

-- Impact of Renovation and View on Price
SELECT renovated, nice_view, AVG(price) AS AvgPrice
FROM HouseDetails
GROUP BY renovated, nice_view;
