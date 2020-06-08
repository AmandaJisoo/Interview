1.
SELECT e.name AS city
  FROM geo.world as w, w.mondial.country as c, c.province as p,
       CASE WHEN is_array(p.city)
             THEN p.city
             ELSE [p.city] END as e
 WHERE c.name = 'Peru'
 ORDER BY e.name;

 2.
SELECT C.name AS name, C.population AS population, sum(religions) as num_religions
  FROM geo.world AS W, W.mondial.country AS C
   LET religions = (CASE WHEN C.religions IS MISSING
                      THEN 0
                      WHEN is_array(C.religions)
                      THEN ARRAY_COUNT(C.religions)
                      ELSE 1 END)
 GROUP BY C.name, C.population
 ORDER BY C.name ASC;

3.
SELECT res.`#text` AS religion, COUNT(c.name) AS num_countries
FROM geo.world AS w, w.mondial.country AS c,
        (CASE WHEN is_array(c.religions)
                       THEN c.religions
                       ELSE [c.religions] END) AS res
WHERE res.`#text`IS NOT NULL
GROUP BY res.`#text`
ORDER BY COUNT(c.name) DESC;

4.
SELECT name as ethnic_group, count(*) as num_countries,
SUM(float(e.`-percentage`) /100.0 * float(c.population)) as total_population
FROM geo.world w,  w.mondial.country c,
(CASE WHEN is_array(c.ethnicgroups) THEN c.ethnicgroups
WHEN is_missing(c.ethnicgroups) THEN [] ELSE [c.ethnicgroups] END) e
GROUP BY e.`#text` as name;

5.
SELECT mountain.name AS mountain, mountain.height AS height, s AS country_code, C.name AS country_name
FROM geo.world w, w.mondial.mountain mountain, w.mondial.country C, split(mountain.`-country`,  ' ') s
WHERE s = C.`-car_code`
ORDER BY int(mountain.height) DESC;


6.
SELECT c.`-car_code` AS country_code, c.name AS country_name, R AS mountains
FROM geo.world w, w.mondial.country c
LET R = 
    (SELECT m.name AS mountain, m.height AS height 
    FROM geo.world w, w.mondial.mountain m, split(m.`-country`,  ' ') s
    WHERE s = c.`-car_code`)
ORDER BY array_count(R) DESC;

7.

SELECT *
FROM geo.world AS w, w.mondial.country AS c,
	  (SELECT VALUE S.name
	  FROM w.mondial.sea AS S
	  WHERE c.`-car_code` in SPLIT(S.`-country`, " ")) AS cd
GROUP BY c.name AS country_name, c.`-car_code` AS country_code GROUP AS seas(cd AS sea)
HAVING ARRAY_COUNT(seas) >= 2
order by ARRAY_COUNT(seas) ASC;

8.
SELECT ct.`-car_code` AS country_code, ct.name AS country_name, ct.`-area` AS area
FROM geo.world w, w.mondial.country ct
LET  res = 
    (SELECT s.name AS sea
    FROM geo.world w, w.mondial.sea s, split(s.`-country`,  ' ') spc
    WHERE spc = ct.`-car_code`)
WHERE array_count(res) = 0
ORDER BY  float(ct.`-area`) DESC;

9. 