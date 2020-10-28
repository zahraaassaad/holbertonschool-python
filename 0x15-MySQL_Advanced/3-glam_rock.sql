-- lists all bands with Glam as their main style
SELECT DISTINCT 'brand_name', 
       		IFNULL ('split', 2020) - 'formed' as 'lifespan'
       FROM 'metal_bands' WHERE FIND_IN_SET('Glam rock', style)
       ORDER BY 'lifespan' DESC;
