insert into users ("id", "name", "email") 
  values ('d037ce8d-0381-471f-bfa5-98467685a335'::uuid, 'admin', 'admin@dummy.org') ON CONFLICT DO NOTHING;

insert into groups ("id", "description") values (1, 'elo_group') ON CONFLICT DO NOTHING;

insert into users_groups ("group_id", "user_id") values (1, 'd037ce8d-0381-471f-bfa5-98467685a335'::uuid) ON CONFLICT DO NOTHING;

insert into users_elo ("elo", "user_id", "time") values (900, 'd037ce8d-0381-471f-bfa5-98467685a335'::uuid, '2023-07-21 07:34:00') ON CONFLICT DO NOTHING;

update challenges_elo set "elo" = 900 where "challenge_id" = 'GroupTerms';