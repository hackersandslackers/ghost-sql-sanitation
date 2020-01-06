UPDATE
	posts,
	posts_meta
SET
	posts_meta.twitter_image = posts.feature_image
WHERE
	posts.feature_image IS NOT NULL
	AND posts.id = posts_meta.post_id;
