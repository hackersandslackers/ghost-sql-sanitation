UPDATE
	posts
SET
	feature_image = REPLACE(feature_image, '.jpg', '@2x.jpg')
WHERE feature_image NOT LIKE '%@2x.jpg%';
