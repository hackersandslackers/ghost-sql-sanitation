UPDATE
	posts_meta
SET
	meta_title = REPLACE(meta_title, ' | Hackers and Slackers', ' - Hackers and Slackers')
WHERE meta_title LIKE '%% | Hackers and Slackers%%';
