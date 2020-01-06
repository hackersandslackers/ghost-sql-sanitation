UPDATE
	posts_meta
SET
	meta_title = CONCAT(meta_title, ' - Hackers and Slackers')
WHERE
	meta_title IS NOT NULL
	AND meta_title NOT LIKE '%%Hackers and Slackers%%';
