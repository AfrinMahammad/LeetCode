# Write your MySQL query statement below
select w1.id from Weather w1, Weather w2 where subdate(w1.recordDate,1)=w2.recordDate and w1.temperature>w2.temperature 