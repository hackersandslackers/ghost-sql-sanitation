UPDATE
	posts
SET
	meta_title = CONCAT(title, " - Hackers and Slackers")
WHERE
	meta_title IS NULL
	AND title IS NOT NULL;
