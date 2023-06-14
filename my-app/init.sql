INSERT INTO ACCOUNT 
(ID, Email, Password, Name, Gender, Create_time) 
VALUES 
("418ad16f-859d-4939-bc4b-2c43f020c56a","Apple@gmail.com","18cbeb8fbe922de28c0b1cf620cdac60e68b52322b6d259176d156dd4ce6df2d","Apple","female",NOW()),
("ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2","Pig@gmail.com","fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3", "Pig", "male", NOW()), 
("c1c9f9c8-7747-4f74-b934-47e53434fc3a","Fish@gmail.com","62dcbf5586c4c7c3fbeef075770cdd1d3750c9fb60dca5a194d231eebc2a7e8f", "Fish", "female", NOW()),
("4ba6c72b-9600-4e8b-a105-dd4cf069c670","Cow@gmail.com","18cbeb8fbe922de28c0b1cf620cdac60e68b52322b6d259176d156dd4ce6df2d", "Cow", null, NOW()), 
("bb910b70-c07a-4b59-a38f-3515d526fe92","Dog@gmail.com","dbff5341acad5e2a58db4efd5e72e2d9a0a843a28e02b1183c68162d0a3a3de6", "Dog", "female", NOW()),
("ad867f51-892c-45a0-a243-bb84f7b0ab07","Windy@gmail.com","dbff5341acad5e2a58db4efd5e72e2d9a0a843a28e02b1183c68162d0a3a3de6", "Windy", "female", NOW());


INSERT INTO POST 
(ID, Account_id, Type, Title, Content, Location, Limit_member, Create_time, Start_time, End_time) 
VALUES 
<<<<<<< Updated upstream
("17316a7c-0751-4e37-bdca-a514cb46d9eb", "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2", "揪團好康", "游泳課三人同行一人免費", "政大游泳系開課啦～凡是政大學生揪團報名課程，三人同行一人免費，一個人只要999!", "政大池塘", 3, NOW(), "2023-04-10 08:00:00", "2023-04-16 18:00:00"),
("1caca70c-287b-4918-b711-9f34c8c3c9a2", "4ba6c72b-9600-4e8b-a105-dd4cf069c670", "Free Hug", "雨後的擁抱", "政大愛心社將於明日下午舉辦Free Hug活動，將在愛心社前廣場，歡迎大家踴躍參加呦～", "愛心社前廣場", 99, NOW(), "2023-04-12 14:00:00", "2023-04-12 18:00:00"),
("2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3", "bb910b70-c07a-4b59-a38f-3515d526fe92", '禮物贈送', '五月天演唱會門票免費贈送', '目前有多出4張五月天門票，想贈送給大家~歡迎索取', '四維堂', 4, NOW(), "2023-04-20 14:00:00", "2023-05-12 18:00:00"),
("3d82ee37-dd4f-4569-9ba5-a0d2acc86e33", "418ad16f-859d-4939-bc4b-2c43f020c56a", 'Free Hug', '散場的擁抱', '政大愛心社將於明日下午舉辦Free Hug活動，將在愛心社前廣場，歡迎大家踴躍參加呦～', '政大正門口', 100, NOW(), "2023-05-15 14:00:00", "2023-05-30 18:00:00"),
("799991aa-12f8-4c7c-aa13-a80e4cdda3e8", "c1c9f9c8-7747-4f74-b934-47e53434fc3a", '揪團好康', '星巴克買一送一', '星巴克買一送一! 一同來分享!', '星巴克政大門市', 1, NOW(), "2023-05-20 08:00:00", "2023-05-21 20:00:00"),
("e77c261f-71ad-45e2-8f42-f1a8a3d425d1", "418ad16f-859d-4939-bc4b-2c43f020c56a", '揪團好康', '7-11拿鐵第二杯半價', '7-11拿鐵第二杯半價，想揪人一起買~', '7-11政大門市', 1, NOW(), "2023-05-02 14:00:00", "2023-05-30 18:00:00");
=======
("17316a7c-0751-4e37-bdca-a514cb46d9eb", "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2", "揪團好康", "游泳課三人同行一人免費", "政大游泳系開課啦～凡是政大學生揪團報名課程，三人同行一人免費，一個人只要999!", "政大池塘", 3,"2023-04-15 12:00:00", "2023-04-30 12:00:00", "2023-05-15 16:00:00", "2023-04-25 12:00:00"),
("1caca70c-287b-4918-b711-9f34c8c3c9a2", "4ba6c72b-9600-4e8b-a105-dd4cf069c670", "Free Hug", "雨後的擁抱", "政大愛心社將於明日下午舉辦Free Hug活動，將在愛心社前廣場，歡迎大家踴躍參加呦～", "愛心社前廣場", 99, NOW(), NOW(), NOW() + INTERVAL 20 DAY, NOW() + INTERVAL 15 DAY),
("2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3", "bb910b70-c07a-4b59-a38f-3515d526fe92", '禮物贈送', '五月天演唱會門票免費贈送', '目前有多出4張五月天門票，想贈送給大家~歡迎索取', '四維堂', 4, NOW(),  "2023-06-25 14:31:27", "2023-07-11 14:31:27", "2023-06-20 14:31:27"),
("3d82ee37-dd4f-4569-9ba5-a0d2acc86e33", "418ad16f-859d-4939-bc4b-2c43f020c56a", 'Free Hug', '散場的擁抱', '政大愛心社將於明日下午舉辦Free Hug活動，將在愛心社前廣場，歡迎大家踴躍參加呦～', '政大正門口', 100, NOW(), NOW(), NOW() + INTERVAL 30 DAY, NOW() + INTERVAL 20 DAY),
("799991aa-12f8-4c7c-aa13-a80e4cdda3e8", "c1c9f9c8-7747-4f74-b934-47e53434fc3a", '揪團好康', '星巴克買一送一', '星巴克買一送一! 一同來分享!', '星巴克政大門市', 1, NOW(), NOW(), NOW() + INTERVAL 2 DAY, NOW() + INTERVAL 1 DAY),
("e77c261f-71ad-45e2-8f42-f1a8a3d425d1", "418ad16f-859d-4939-bc4b-2c43f020c56a", '揪團好康', '7-11拿鐵第二杯半價', '7-11拿鐵第二杯半價，想揪人一起買~', '7-11政大門市', 1, NOW(), NOW(), NOW() + INTERVAL 5 DAY, NOW() + INTERVAL 2 DAY),
("228787f1-9b63-4fb2-a42d-40d8c0813193", "418ad16f-859d-4939-bc4b-2c43f020c56a", 'Free Hug', 'Free Hug活動招募', '快來一起響應Free Hug~', '政大行政大樓前', 1, NOW(), NOW(), NOW() + INTERVAL 5 DAY, NOW() + INTERVAL 2 DAY);
>>>>>>> Stashed changes


INSERT INTO POST_PARTICIPANT
(Post_id, Account_id) 
VALUES
("2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3", "418ad16f-859d-4939-bc4b-2c43f020c56a"), 
("2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3", "c1c9f9c8-7747-4f74-b934-47e53434fc3a"), 
("17316a7c-0751-4e37-bdca-a514cb46d9eb", "418ad16f-859d-4939-bc4b-2c43f020c56a"), 
("1caca70c-287b-4918-b711-9f34c8c3c9a2", "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2"), 
("e77c261f-71ad-45e2-8f42-f1a8a3d425d1", "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2"),
("1caca70c-287b-4918-b711-9f34c8c3c9a2", "4ba6c72b-9600-4e8b-a105-dd4cf069c670");

INSERT INTO MEDICAL_ARTICLES
(Title, Author, Article, Url)
VALUES
('test','test','test',NULL),
('yoyo','yoyo','yoyo',NULL),
('inner','inner','inner',NULL),
('4','4','4',NULL),
('5','5','5',NULL),
('6','6','6',NULL);



-- INSERT INTO WEATHER 
-- (Temperature, Description, Time) 
-- VALUES
-- (24, "午後可能降雨", NOW());