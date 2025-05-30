-- Active: 1744916696249@@localhost@5432@uae_cars_analysis
SELECT * FROM uae_cars_analysis;


SELECT 
    DISTINCT MAKE
FROM uae_cars;




SELECT 
    Make, 
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Make
ORDER BY Average_Price DESC
LIMIT 5;



SELECT 
    Make, 
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) ASC) as Rank
FROM uae_cars
GROUP BY Make
ORDER BY Average_Price ASC
LIMIT 5;




SELECT
    Location,
    CONCAT(Make, ' ', Model, ' ', Year) AS Car,
    Price AS Max_Price
FROM
    uae_cars
WHERE
    (Location, Price) IN (
        SELECT
            Location,
            MAX(Price)
        FROM
            uae_cars
        GROUP BY
            Location
    )
ORDER BY
    Max_Price DESC;





WITH CarPrices AS (
    SELECT 
        CONCAT(Make, ' ', Model, ' ', Year, ' ', Color) AS Car, 
        Price
    FROM uae_cars
    WHERE Year >= 2020
)
SELECT 
    Car, 
    Price,
    RANK() OVER (ORDER BY Price DESC) AS Rank
FROM CarPrices
ORDER BY Price DESC
LIMIT 5;




WITH CarPrices AS (
    SELECT 
        CONCAT(Make, ' ', Model, ' ', Year, ' ', Color) AS Car, 
        Price
    FROM uae_cars
    WHERE Year >= 2020
)
SELECT 
    Car, 
    Price,
    RANK() OVER (ORDER BY Price ASC) AS Rank
FROM CarPrices
ORDER BY Price ASC
LIMIT 5;



SELECT 
    Transmission, 
    COUNT(*) as Transmission_Type_Count
FROM uae_cars
GROUP BY Transmission;



 
SELECT 
    Transmission,
    ROUND(AVG(Price), 2) AS Average_Price
FROM uae_cars
GROUP BY Transmission;





SELECT 
    Color, 
    COUNT(*) as Colour_Count, 
    RANK() OVER (ORDER BY COUNT(*) DESC) as Rank
FROM uae_cars
GROUP BY Color
ORDER BY Colour_Count DESC;



SELECT 
    Location,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Location
ORDER BY Average_Price DESC;



SELECT 
    YEAR,
    ROUND(AVG(Price), 2) AS Average_Price
FROM uae_cars
GROUP BY Year;





SELECT 
    Color,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Color
ORDER BY Average_Price DESC
LIMIT 5;


SELECT 
    Body_Type,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Body_type
ORDER BY Average_Price DESC
LIMIT 5;


 
SELECT 
    Fuel_Type,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Fuel_Type
ORDER BY Average_Price DESC;





WITH Color_Counts AS (
    SELECT 
        Location,
        Color,
        COUNT(*) AS Colour_Count
    FROM uae_cars
    GROUP BY Location, Color
),

Max_Color AS (
    SELECT
        Location,
        Color,
        Colour_Count,
        RANK() OVER (PARTITION BY Location ORDER BY Colour_Count DESC) AS Rank
    FROM Color_Counts
)
SELECT
    Location,
    Color AS Mode_Color
FROM Max_Color
WHERE Rank = 1;






WITH Color_Counts AS (
    SELECT 
        Location,
        Color,
        COUNT(*) AS Colour_Count
    FROM uae_cars
    GROUP BY Location, Color
),

Max_Color AS (
    SELECT
        Location,
        Color,
        Colour_Count,
        RANK() OVER (PARTITION BY Location ORDER BY Colour_Count ASC) AS Rank
    FROM Color_Counts
)
SELECT
    Location,
    Color AS Mode_Color
FROM Max_Color
WHERE Rank = 1;









WITH ECO_TYPE_COUNT AS (
    SELECT 
        Make,
        Fuel_Type,
        COUNT(*) AS ECO_TYPE_COUNT
    FROM uae_cars
    WHERE Fuel_Type = 'Electric' OR Fuel_Type = 'Hybrid'
    GROUP BY Make, Fuel_Type
),
ECO_COUNT AS (
    SELECT 
        Make,
        Fuel_Type,
        COUNT(*) AS ECO_TYPE_COUNT,
        RANK() OVER (PARTITION BY Make ORDER BY COUNT(*) ASC) AS Rank
    FROM uae_cars
    WHERE Fuel_Type = 'Electric' OR Fuel_Type = 'Hybrid'
    GROUP BY Make, Fuel_Type
)
SELECT 
    DISTINCT Make, 
    ECO_TYPE_COUNT
FROM ECO_COUNT
WHERE Rank = 1
ORDER BY ECO_TYPE_COUNT DESC
LIMIT 10;









WITH ICE_TYPE_COUNT AS (
    SELECT 
        CONCAT(Make, ' ', Model, ' ', Year) as Car,
        Fuel_Type,
        COUNT(*) AS ICE_TYPE_COUNT
    FROM uae_cars
    WHERE Fuel_Type = 'Gasoline' OR Fuel_Type = 'Diesel'
    GROUP BY Car, Fuel_Type
),
ICE_COUNT AS (
    SELECT 
        CONCAT(Make, ' ', Model, ' ', Year) as Car,
        Fuel_Type,
        COUNT(*) AS ICE_TYPE_COUNT,
        RANK() OVER (PARTITION BY Make ORDER BY COUNT(*) ASC) AS Rank
    FROM uae_cars
    WHERE Fuel_Type = 'Gasoline' OR Fuel_Type = 'Diesel'
    GROUP BY Car, Fuel_Type
)
SELECT 
    CONCAT(Make, ' ', Model, ' ', Year) as Car, 
    ECO_TYPE_COUNT
FROM ICE_COUNT
WHERE Rank = 1 
GROUP BY Car
ORDER BY ECO_TYPE_COUNT DESC
LIMIT 5;


