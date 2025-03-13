SELECT * FROM uae_cars;


-- GET ALL AVAILABLE BRANDS
/*

Toyota
Kia
Mini
Nissan
Chevrolet
Cadillac
Mercedes-Benz
Infiniti
Mazda
Jeep
Ferrari
Bmw
Porsche
Bentley
Land-Rover
Honda
Dodge
Rolls-Royce
Ford
Hyundai
Lamborghini
Mitsubishi
Aston-Martin
Gmc
Renault
Volkswagen
Lexus
Suzuki
Lincoln
Audi
Maybach
Peugeot
Jaguar
Citroen
Maserati
Tesla
Volvo
Lotus
Mclaren
Alfa-Romeo
Fiat
Chrysler
Opel
Mercedes-Maybach
Geely
Acura
Subaru
Genesis
Isuzu
Westfield-Sportscars

*/
SELECT 
    DISTINCT MAKE
FROM uae_cars;




-- MOST EXPENSIVE BRANDS (AVERAGE PRICES)
/* 

1- Mclaren                 2145859.51 AED
2- Rolls-Royce             1827529.65 AED
3- Lamborghini             1608101.19 AED 
4- Ferrari                 1225834.09 AED
5- Mercedes-Maybach        1203588.13 AED

*/ 
SELECT 
    Make, 
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Make
ORDER BY Average_Price DESC
LIMIT 5;



-- CHEAPEST BRANDS ON AVERAGE
/* 

1- Mercury          24124.0 AED
2- Daihatsu         22694.67 AED
3- Saab             22091.0 AED
4- Gac              20899.0 AED
5- Geely            20065.5 AED

*/
SELECT 
    Make, 
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) ASC) as Rank
FROM uae_cars
GROUP BY Make
ORDER BY Average_Price ASC
LIMIT 5;





-- MOST EXPENSIVE CAR IN EACH CITY
/* 

Abu Dhabi         Mercedes-Benz G-Class 2009            1094820 AED
Ajman             Land-Rover Range-Rover 2020           460904 AED
Al Ain            Land-Rover Range-Rover 2013           1302640 AED
Dubai             Mclaren P1 2020                       14686975 AED
Fujeirah          Nissan Patrol 2016                    100647 AED
Ras Al Khaimah    Lexus Es-Series 2013                  126636 AED
Sharjah           Rolls-Royce Cullinan 2017             2220808 AED
Umm Al Qawain     Mercedes-Benz E-Class 2014            104610 AED


*/
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




-- MOST EXPENSIVE CARS SINCE 2020
/* 

1- Mclaren P1 2020 (Yellow)                 4197282 AED
2- Ferrari 599 2024  (Blue)                 2766551 AED
3- Rolls-Royce Cullinan 2023 (Grey)         2656394 AED
4- Rolls-Royce Cullinan 2023 (White)        1655646 AED
5- Rolls-Royce Phantom 2021 (Black)         1655206 AED

*/
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



-- CHEAPEST CARS SINCE 2020
/* 

1- Nissan Altima 2024              10704 AED 
2- Nissan Sunny 2023               10609 AED
3- Nissan Murano 2022              9353 AED
4- Nissan Sunny 2023 Silver        9321 AED
5- Nissan Altima 2024 Black        7183 AED

*/
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



-- NUMBER OF AUTOMATIC VEHICLES VS. MANUALS
/* 

Automatic          9626
MANUAL             374

*/
SELECT 
    Transmission, 
    COUNT(*) as Transmission_Type_Count
FROM uae_cars
GROUP BY Transmission;



-- AVERAGE PRICE BY TRANSMISSION
/* 

1- Automatic   250236.78 AED
2- Manual      116486.15 AED

*/
SELECT 
    Transmission,
    ROUND(AVG(Price), 2) AS Average_Price
FROM uae_cars
GROUP BY Transmission;




-- NUMBER OF CARS BY COLOUR
/* 

1- White    3355
2- Black    2126
3- Grey     1307
4- Silver   866
5- Blue     686

*/
SELECT 
    Color, 
    COUNT(*) as Colour_Count, 
    RANK() OVER (ORDER BY COUNT(*) DESC) as Rank
FROM uae_cars
GROUP BY Color
ORDER BY Colour_Count DESC;


-- AVERAGE PRICE OF CARS BY CITY
/* 

Dubai                 277990.01 AED
Al Ain                216607.62 AED
Abu Dhabi             128155.28 AED
Ajman                 103642.56 AED
Sharjah               101190.1 AED
Umm Al Qawain         66941.7 AED
Ras Al Khaimah        61424.83 AED
Fujeirah              53236.22 AED

*/
SELECT 
    Location,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Location
ORDER BY Average_Price DESC;


-- AVERAGE PRICE BY YEAR
/*

2005	269206.56
2006	249170.68
2007	243777.98
2008	222341.79
2009	202267.07
2010	231788.5
2011	247443.36
2012	240902.42
2013	301705.42
2014	243610.67
2015	257518.77
2016	248035.98
2017	261488.21
2018	239740.49
2019	227927.0
2020	250423.64
2021	244529.98
2022	213130.48
2023	277636.46
2024	235450.53

*/

SELECT 
    YEAR,
    ROUND(AVG(Price), 2) AS Average_Price
FROM uae_cars
GROUP BY Year;




-- MOST EXPENSIVE COLOURS
/* 

1- Yellow   1257843.16 AED
2- Green    562504.2 AED
3- Purple   545639.69 AED
4- Orange   536212.16 AED
5- Blue     304107.45 AED

*/
SELECT 
    Color,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Color
ORDER BY Average_Price DESC
LIMIT 5;


-- AVERAGE PRICE BY BODY TYPE
/* 

Sports Car               706251.14 AED
Hard Top Convertible     660750.19 AED
Soft Top Convertible     569321.74 AED
Coupe                    369481.44 AED
5-Wagon                  308644.93 AED

*/
SELECT 
    Body_Type,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Body_type
ORDER BY Average_Price DESC
LIMIT 5;


-- AVERAGE PRICE BY FUEL TYPE
/* 

1- Hybrid          1455045.22 AED
2- Gasoline        243544.9 AED
3- Electric        215576.67 AED
4- Diesel          191963.51 AED

*/
SELECT 
    Fuel_Type,
    ROUND(AVG(Price), 2) AS Average_Price,
    RANK() OVER (ORDER BY ROUND(AVG(Price), 2) DESC) as Rank
FROM uae_cars
GROUP BY Fuel_Type
ORDER BY Average_Price DESC;



-- MOST COMMON COLORS IN EACH CITY 

/* 

1- calculate the count of each color by location
2- rank the colors by their counts within each location 
(this is how you find the mode of qualitative values)
*/

/* 

Dubai               White
Al Ain              White
Abu Dhabi           White
Ajman               White
Sharjah             White
Umm Al Qawain       White
Ras Al Khaimah      Grey + Silver
Fujeirah            White

*/
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



-- LEAST COMMON COLOR IN EACH CITY 
/* 

Dubai               Tan
Al Ain              Beige
Abu Dhabi           Teal
Ajman               Brown + Burgundy
Sharjah             Yellow
Umm Al Qawain       Green + Grey + 	Other Color
Ras Al Khaimah      Green + Yellow
Fujeirah            Red

*/
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





-- MOST ECO-FRIENDLY BRANDS
/*
1- calculate the count of fuel type for each make
2- rank the fuel_type by their counts within each make 
*/


/*
 
THESE ARE THE ONLY BRANDS THAT MANUFACTURE THE MOST ECO-FRIENDLY VEHICLES (BOTH HYPRID AND ELECTRIC)

1- Tesla            102
2- Volkswagen	    84
3- Audi             16
4- Ford             8
5- Lexus	        8
6- Porsche          6
7- Renault          6
8- Mclaren          4
9- Mercedes-Benz    4
10- Ferrari         2

*/

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



-- Least ECO-FRIENDLY BRANDS
/* ICE STANDS FOR internal combustion engine  */
/*
1- calculate the count of fuel type for each make
2- rank the fuel_type by their counts within each make 
*/

/* 
THESE ARE THE ONLY BRANDS THAT HAPPEN TO MANUFACTURE THE MOST ICE VEHICLES
BOTH GASOLINE AND DIESEL

1- Porsche	    894
2- Audi     	778
3- Jeep     	690
4- Lexus	    670
5- Volkswagen	384
*/


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


