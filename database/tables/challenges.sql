CREATE TABLE IF NOT EXISTS challenges
(
   id       SERIAL PRIMARY KEY,
   initial_task     JSON NOT NULL,
   possible_solution JSON NOT NULL,
   static_example  JSON,
   expected_static JSON
);
