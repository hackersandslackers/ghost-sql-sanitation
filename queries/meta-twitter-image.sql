UPDATE
	posts
SET
	twitter_image = feature_image
WHERE
	feature_image IS NOT NULL;
