UPDATE
	posts
SET
	meta_title = title
WHERE
	meta_title IS NULL
	AND title IS NOT NULL;
