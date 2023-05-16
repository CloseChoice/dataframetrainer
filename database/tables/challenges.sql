 create table challenges
(
   id       integer primary key, 
   initial_task     json not null,
   possible_solution json not null
);