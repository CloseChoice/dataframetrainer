insert into users ("id", "name") 
  values ('d037ce8d-0381-471f-bfa5-98467685a335'::uuid, 'admin'),
  ('user_elo_id', 'user_elo_name') ON CONFLICT DO NOTHING;

insert into sessions (id, user_id, active_expires, idle_expires) values ('session_id_user_elo', 'user_elo_id', 4102444800000, 4102444800000) ON CONFLICT DO NOTHING;

insert into users_groups ("group_id", "user_id") values (1, 'd037ce8d-0381-471f-bfa5-98467685a335'::uuid) ON CONFLICT DO NOTHING;

insert into users_elo ("elo", "user_id") values (900, 'd037ce8d-0381-471f-bfa5-98467685a335'::uuid) ON CONFLICT DO NOTHING;

update challenges_elo set "elo" = 900 where "challenge_id" = 'GroupTerms';