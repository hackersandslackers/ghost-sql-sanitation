UPDATE
	posts_meta
SET
	posts_meta.twitter_title = posts.title
WHERE
	posts_meta.twitter_title IS NULL
	AND posts.title IS NOT NULL
	AND posts.id = posts_meta.post_id;
