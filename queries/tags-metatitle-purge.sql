UPDATE
	tags
SET
	meta_title = REPLACE(meta_title, ' - Hackers and Slackers', '')
WHERE
	meta_title IS NOT NULL;
