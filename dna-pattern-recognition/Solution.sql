/* Write your PL/SQL query statement below */
select 
    s.*,
    case when substr(dna_sequence,1,3)='ATG' 
    then 1 else 0 end has_start,
    case when substr(dna_sequence,-3,3) in ('TAA','TAG','TGA')
    then 1 else 0 end has_stop,
    case when instr(dna_sequence,'ATAT')!=0
    then 1 else 0 end has_atat,
    case when instr(dna_sequence,'GGG')!=0
    then 1 else 0 end has_ggg
from samples s
order by sample_id;