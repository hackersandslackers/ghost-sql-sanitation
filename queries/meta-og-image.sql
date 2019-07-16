UPDATE
	posts
SET
	og_image = feature_image
WHERE
	feature_image IS NOT NULL;
