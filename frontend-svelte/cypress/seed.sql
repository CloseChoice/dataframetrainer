DELETE FROM users;
SELECT register_user_with_credentials('Bob', '$2a$12$cYhFn8kddol1aEfEhFtT/.l81gZ31LfaYDg.WvdJNHHPxJpHIVReS');
-- Bobs password is 1234
-- Passwords are hashed using bcrypt.