select * from users;
select * from friendships;

insert into friendships(user_id, friend_id, create_at)
values (2, 1, now());

select users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_first_name from users
left join friendships on users.id = friendships.user_id
left join users as user2 on friendships.friend_id = user2.id;
