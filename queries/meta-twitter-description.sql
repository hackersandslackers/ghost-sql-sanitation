UPDATE
	posts
SET
	twitter_description = custom_excerpt
WHERE
	twitter_description IS NULL
	AND custom_excerpt IS NOT NULL;
