UPDATE
	posts
SET
	feature_image = REPLACE(feature_image, '%402x', '@2x')
WHERE feature_image LIKE '%402x%';
