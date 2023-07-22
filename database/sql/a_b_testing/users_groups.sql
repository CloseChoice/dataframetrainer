CREATE TABLE IF NOT EXISTS users_groups(
    group_id INT NOT NULL,
    user_id TEXT NOT NULL,
  CONSTRAINT "users_groups_userid_fkey" FOREIGN KEY (user_id) REFERENCES users (id),
  CONSTRAINT "users_groups_groupid_fkey" FOREIGN KEY (group_id) REFERENCES groups (id),
  UNIQUE CONSTRAINT "users_groups" (user_id, group_id)
) TABLESPACE pg_default;
