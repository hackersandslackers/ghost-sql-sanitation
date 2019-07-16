UPDATE
	posts
SET
	og_description = custom_excerpt
WHERE
	og_description IS NULL
	AND custom_excerpt IS NOT NULL;
