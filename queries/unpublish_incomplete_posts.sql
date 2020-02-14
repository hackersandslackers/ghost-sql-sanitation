UPDATE
    posts
SET
    status = 'draft'
WHERE
    status = 'published'
    AND feature_image IS NULL
    OR custom_excerpt IS NULL
    OR title IS NULL;
