/* Write your PL/SQL query statement below */
with tmp as (
    select 
        book_id,
        count(*) current_borrowers 
    from borrowing_records
    where return_date is null
    group by book_id
)
select 
    b.book_id,
    title,
    author,
    genre, 
    publication_year,
    current_borrowers
from library_books b
join tmp t
on b.book_id=t.book_id
where current_borrowers=total_copies
order by current_borrowers desc,title asc