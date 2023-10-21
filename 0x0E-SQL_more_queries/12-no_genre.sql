-- This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Using JOIN, we can do this
-- Showing only what don't have genres_id (only NULL)
SELECT title, genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, genre_id;

