UPDATE
	posts
SET
	twitter_title = title
WHERE
	twitter_title IS NULL
	AND title IS NOT NULL;
