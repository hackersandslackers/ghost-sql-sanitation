UPDATE
	posts
SET
	og_title = title
WHERE
	og_title IS NULL
	AND title IS NOT NULL;
