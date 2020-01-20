UPDATE
    posts
SET
    status = 'draft'
WHERE
    feature_image IS NULL
    OR custom_excerpt IS NULL
    OR title IS NULL;
