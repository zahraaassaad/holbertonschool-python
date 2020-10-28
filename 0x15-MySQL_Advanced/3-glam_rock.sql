-- Ranks longevity of Glam bands
-- Column names must be: band_name and lifespan (in years)

SELECT
band_name, ifnull(split, 2020)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
