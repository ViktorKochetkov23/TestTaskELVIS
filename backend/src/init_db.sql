--Заполнение пользователей
insert into users (user_name, language)
values
('Пользователь 1', 'ru'),
('Пользователь 2', 'ru'),
('User 1', 'en'),
('User 2', 'en'),
('NewUser', 'en'),
('ОхотникЗаДостижениями132','ru'),
('LazyGuy451','en'),
('HighwayKing371', 'en');

--Заполнение достижений
insert into achievements (achievement_name, achievement_value, achievement_desc)
values
('Добро пожаловать!', 10, 'Вы зарегистрировались в системе'),
('Тут есть достижения?', 20, 'Вы посмотрели свою статистику'),
('Соскучились?)', 20, 'Вы заходили 3 дня подряд'),
('Вперед, к вершинам!', 10, 'Вы посмотрели статистику других участников'),
('Around the world', 10, 'Вы сменили свой язык в настройках'),
('Первые шаги!', 20, 'Вы заработали 5 достижений'),
('100!', 20, 'Вы заработали 100 очков'),
('Топ-10', 30, 'Вы оказались в топ-10 участников по очкам'),
('Топ-3', 50, 'Вы оказались в топ-3 участникво по очкам'),
('Топ-1', 100, 'Вы стали лучшим участником в ситеме'),
('Secret...', 60, 'А что у нас здесь?');

--Присвоение достижений пользователям
insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2020-04-01'
from users, achievements
where achievements.achievement_name in ('Добро пожаловать!', 'Тут есть достижения?', 'Соскучились?)');

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2020-04-10'
from users, achievements
where achievements.achievement_name in ('Вперед, к вершинам!')
and users.user_name in ('User 1', 'User 2', 'ОхотникЗаДостижениями132', 'HighwayKing371');

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-09'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = 'Around the world';

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-10'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = 'Первые шаги!';

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-11'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = '100!';

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-12'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = 'Топ-10';

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-13'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = 'Топ-3';

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-14'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = 'Топ-1';

insert into users_achievements (user_id, achievement_id, date)
select users.id, achievements.id, '2023-05-15'
from users, achievements
where users.user_name = 'ОхотникЗаДостижениями132'
and achievements.achievement_name = 'Secret...';
