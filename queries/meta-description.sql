UPDATE
	posts
SET
	meta_description = custom_excerpt
WHERE
	meta_description IS NULL
	AND custom_excerpt IS NOT NULL;
