SELECT name as results
FROM (
    SELECT u.name,
           COUNT(mr.movie_id) AS cnt_movie
    FROM MovieRating mr 
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.name
    ORDER BY cnt_movie DESC, u.name
) t
WHERE ROWNUM = 1
union all
select TITLE as result
from (
        select m.title, avg(mr.rating) as avg_rating
    from MovieRating mr 
    join Movies m on m.movie_id=mr.movie_id
    where to_char(mr.created_at, 'yyyy-mm')='2020-02'
    group by m.title
    order by avg_rating desc , m.title asc)
where rownum=1
