-- Data Cleaning Queries

-- Duplicate Detection
SELECT sale_date, price, bedrooms, grade, COUNT(*)
FROM HouseDetails
GROUP BY sale_date, price, bedrooms, grade
HAVING COUNT(*) > 1;

-- Duplicate Removal
DELETE FROM HouseDetails
WHERE sale_id IN (SELECT sale_id
                  FROM HouseDetails
                  GROUP BY sale_date, price, bedrooms, grade
                  HAVING COUNT(*) > 1);
