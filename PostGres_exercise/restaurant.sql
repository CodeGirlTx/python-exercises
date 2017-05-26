CREATE TABLE restaurant (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR,
  distance INTEGER,
  stars INTEGER DEFAULT 0 CHECK (stars >= 0 AND stars <=5),
  category VARCHAR,
  favorite_dish VARCHAR,
  takeout BOOLEAN,
  last_visited DATE
);

-- ********
-- #queries
-- ********

INSERT INTO restaurant (name, stars, category, takeout) VALUES ('Piada', '5', 'Italian', TRUE)

restaurant=# SELECT * FROM restaurant ORDER BY stars;

SELECT * FROM restaurant WHERE stars = 5;

SELECT favorite_dish FROM restaurant WHERE stars = 5;

SELECT * FROM restaurant WHERE category = 'BBQ';

SELECT * FROM restaurant WHERE distance <= 2;

restaurant=# SELECT * FROM restaurant WHERE name = 'Moon Tower';

SELECT * FROM restaurant WHERE last_visited < '2017-05-01';

SELECT * FROM restaurant WHERE last_visited < '2017-05-01' and stars = 5;

-- *********************************
-- Aggregation and Sorting Exercises:
-- *********************************

SELECT * FROM restaurant ORDER BY distance;
SELECT * FROM restaurant ORDER BY distance limit 2;
SELECT * FROM restaurant ORDER BY stars desc limit 2;

--by stars and less than 2 miles away:
SELECT * FROM restaurant WHERE distance <= 2 ORDER BY stars desc limit 2;

-- Counts number of rows:
SELECT count(*) FROM restaurant;
SELECT category, count(*) FROM restaurant GROUP BY category;
SELECT category, AVG(stars) FROM restaurant GROUP BY category;
SELECT category, MAX(stars) FROM restaurant GROUP BY category;

SELECT category, AVG(stars) AS average_points FROM restaurant GROUP BY category;
