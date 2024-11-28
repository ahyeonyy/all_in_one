-- member
insert into member (member_id, email, pw, type, image, nickname, is_admin, is_withdraw, created_at)
overriding system value VALUES
(0, 'admin@naver.com', '$2a$10$lvh8zmXKD/DdiBteWTdmS.fsn6MYIxym/rqqlgdO57NNkN/ZhAnP6', 'LIKE_IT', '/', '어드민', TRUE, FALSE, now()),
(1, 'user@naver.com', '$2a$10$lvh8zmXKD/DdiBteWTdmS.fsn6MYIxym/rqqlgdO57NNkN/ZhAnP6', 'LIKE_IT', '/', '일반회원', FALSE, FALSE, now()),
(2, 'likeit@naver.com', '$2a$10$lvh8zmXKD/DdiBteWTdmS.fsn6MYIxym/rqqlgdO57NNkN/ZhAnP6', 'LIKE_IT', '/', '라이킷', FALSE, FALSE, now());

-- category
insert into category (category_id, image, name, info, option, created_at)
overriding system value VALUES
(0, 'category/etc.png', '전체', NULL, 'BALANCE', now()),
(1, 'category/daily.png', '일상', '작은 일상이 모인 큰 행복', 'BALANCE', now()),
(2, 'category/food.png', '음식', '마음을 나눌 수 있는 가장 맛있는 방법', 'BALANCE', now()),
(3, 'category/love.png', '연애/관계', '서로의 마음을 이해하는 가장 아름다운 단어', 'BALANCE', now()),
(4, 'category/social.png', '사회', '변화, 함께 만들어가는 작은 행동에서 시작', 'BALANCE', now()),
(5, 'category/ability.png', '능력', '노력의 결실, 가능성의 끝은 없다', 'BALANCE', now()),
(6, 'category/thing.png', '물건', '우리의 삶을 풍요롭게 하는 소중한 동반자', 'BALANCE', now()),
(7, 'category/situation.png', '상황', '긍정의 씨앗은 놀라운 꽃을 피운다', 'BALANCE', now()),
(8, 'category/etc.png', '자유', '마음 가는대로', 'BALANCE', now()),
(9, '', '공지사항', NULL, 'BOARD', now()),
(10, '', 'FAQ', NULL, 'BOARD', now()),
(11, '', '이벤트', NULL, 'EVENT', now());

-- balance
insert into balance (balance_id, category_id, member_id, title, image, share_count, created_at)
overriding system value VALUES
(0, 1, 0, '이재용 VS 카리나', 'balance/default_1.png', 0, now()),
(1, 1, 0, '걸어서 30분 VS 택시타고 5분', 'balance/default_2.png', 0, now()),
(2, 1, 1, '누워서 24시간 VS 서서 24시간', 'balance/default_3.png', 0, now()),
(3, 1, 2, '넌 뭘 위해 살고있니?', 'balance/default_4.png', 0, now()),
(4, 2, 0, '희대의 난제', 'balance/default_5.png', 0, now()),
(5, 3, 0, '전여친 VS 전짝사랑녀', 'balance/default_1.png', 0, now()),
(6, 4, 0, '무단횡단은 진짜 나쁠까?', 'balance/default_2.png', 0, now()),
(7, 5, 0, '평생 물 소환 VS 평생 콜라 소환', 'balance/default_3.png', 0, now()),
(8, 6, 0, '벤츠 VS BMW', 'balance/default_4.png', 0, now()),
(9, 7, 0, '몰래 외박했는데', 'balance/default_5.png', 0, now()),
(10, 8, 0, '너 뭐좀 되니?', 'balance/default_1.png', 0, now());

-- balance_content
insert into balance_content (balance_content_id, balance_id, image, content, created_at)
overriding system value values
-- 이재용 VS 카리나 (0)
(0, 0, '/', '이재용', now()),
(1, 0, '/', '카리나', now()),
-- 걸어서 30분 VS 택시타고 5분 (1)
(2, 1, '/', '걸어서 30분', now()),
(3, 1, '/', '택시타고 5분', now()),
-- 누워서 24시간 VS 서서 24시간 (2)
(4, 2, '/', '누워서 24시간', now()),
(5, 2, '/', '서서 24시간', now()),
-- 넌 뭘 위해 살고있니? (3)
(6, 3, '/', '죽지못해 사는 중', now()),
(7, 3, '/', '죽기위해 사는 중', now()),
-- 희대의 난제 (4)
(8, 4, '/', '치킨', now()),
(9, 4, '/', '피자', now()),
-- 전여친 VS 전짝사랑녀 (5)
(10, 5, '/', '전여친', now()),
(11, 5, '/', '전짝사랑녀', now()),
-- 무단횡단은 진짜 나쁠까? (6)
(12, 6, '/', '나쁘다', now()),
(13, 6, '/', '할 수도 있지', now()),
-- 평생 물 소환 VS 평생 콜라 소환 (7)
(14, 7, '/', '평생 물 소환', now()),
(15, 7, '/', '평생 콜라 소환', now()),
-- 벤츠 VS BMW (8)
(16, 8, '/', '벤츠', now()),
(17, 8, '/', 'BMW', now()),
-- 몰래 외박했는데 (9)
(18, 9, '/', '아빠한테 전화 옴', now()),
(19, 9, '/', '엄마한테 전화 옴', now()),
-- 너 뭐좀 되니? (10)
(20, 10, '/', '어 나 뭐 되지', now()),
(21, 10, '/', '미안 ㅜㅠ', now());

-- debate
insert into debate (debate_id, balance_content_id, member_id, title, content, image, created_at)
overriding system value values
(0, 0, 0, '이걸 왜 카리나를 가?', '이거 카리나 가는 애들은 진짜 경제 공부 다시 해라 ㅋㅋ', '/', now()),
(1, 1, 1, '카리나는 신이야', '이재용 고르면 누가 돈주냐?', '/', now()),
(2, 0, 2, '재드래곤 렛츠 고', '재드래곤 렛츠 고 기릿 맨', '/', now()),
(3, 2, 0, '작은 돈부터 아끼는게 재테크의 시작이야', '너네 복리의 마법이라고 모르냐?', '/', now()),
(4, 3, 1, '시간은 돈이다', '시간은 돈이다를 이해하지 못했으면 넌 나가라', '/', now()),
(5, 2, 2, '나는 그냥 걷는게 좋아', '그냥 걷는게 좋아서 눌러봄', '/', now()),
(6, 4, 0, '누워있는것이 곧 삶의 낙', '너넨 한번이라도 누워본적이 있어?', '/', now()),
(7, 5, 1, '걷는게 건강이여 젊은이들', '나때는 말이지 천리행군도 마다했어, 그냥 걸어', '/', now()),
(8, 5, 2, '침대', '이미 나와 한 몸이 된채로 오래지', '/', now());

-- debate_reply
insert into debate_reply (reply_id, debate_id, member_id, content, reply_member_id, created_at)
overriding system value values
(0, 0, 0, '카리나 무시함?', null, now()),
(1, 0, 1, 'ㅋㅋ 무시하긴 해', 0, now()),
(2, 2, 2, '재드래곤 맛있긴하지', null, now()),
(3, 3, 0, '나는 그렇게 생각안해', null, now()),
(4, 4, 1, '돈은 시간이다 이자식아',null, now()),
(5, 5, 2, '저도 걷는게 좋아요 ㅎ', null, now()),
(6, 5, 0, '근데 안물어본거 알지', 2, now()),
(7, 7, 1, '아재요.. 들어가소', null, now()),
(8, 8, 2, '굉장히 인정하는 부분입니다.', null, now());

-- achieve
insert into achieve (achieve_id, name, image, type, achieve_info, goal_count, created_at)
overriding system value values
(0, '전설의 시작', '/', 'FIRST_CREATE_BALANCE', '첫 밸런스 게임 생성을 진행한 사람', null, now()),
(1, '용감한 선택', '/', 'FIRST_VOTE_BALANCE', '첫 밸런스 게임 투표를 진행한 사람', null, now()),
(2, '제너럴 리스트', '/', 'GENERALIST', '모든 카테고리 종류의 밸런스 게임 생성을 진행한 사람', null, now()),
(3, '스페셜 리스트 ', '/', 'SPECIALIST', '한개의 카테고리 기준 30개 이상 밸런스 게임 생성을 진행한 사람', null, now()),
(4, '좋아요? 좋아요!', '/', 'LIKE_LIKE', '밸런스 게임 좋아요 10000개 달성 시, 업적 획득', null, now()),
(5, '뭉치면 ㅇㅇ 흩어지면 ㅇㅇ', '/', 'BALANCE_SHARE', '밸런스 게임 공유 100회 이상 진행한 사람', null, now()),
(6, '뛰어난 언변가', '/', 'GREAT_DEBATER', '토론장 생성 글 좋아요 10000개 달성 시, 업적 획득', null, now()),
(7, '이 구역 인싸', '/', 'IN_SSA', '토론장 내 닉네임 언급 100회 이상 당할 시, 업적 획득', null, now()),
(8, '선택의 달인', '/', 'MASTER_OF_CHOICE', '100회 이상의 밸런스 게임에 참여한 사람', null, now());

-- member_achieve
insert into member_achieve (member_achieve_id, achieve_id, member_id, progress_count, achieve_at, is_point, created_at)
overriding system value values
(0, 0, 0, 0, null, FALSE, now()),
(1, 1, 0, 0, null, FALSE, now()),
(2, 2, 0, 0, null, FALSE, now()),
(3, 3, 0, 0, null, FALSE, now()),
(4, 4, 0, 0, null, FALSE, now()),
(5, 5, 0, 0, null, FALSE, now()),
(6, 6, 0, 0, null, FALSE, now()),
(7, 7, 0, 0, null, FALSE, now()),
(8, 8, 0, 0, null, FALSE, now()),

(9, 0, 1, 0, null, FALSE, now()),
(10, 1, 1, 0, null, FALSE, now()),
(11, 2, 1, 0, null, FALSE, now()),
(12, 3, 1, 0, null, FALSE, now()),
(13, 4, 1, 0, null, FALSE, now()),
(14, 5, 1, 0, null, FALSE, now()),
(15, 6, 1, 0, null, FALSE, now()),
(16, 7, 1, 0, null, FALSE, now()),
(17, 8, 1, 0, null, FALSE, now()),

(18, 0, 2, 0, null, FALSE, now()),
(19, 1, 2, 0, null, FALSE, now()),
(20, 2, 2, 0, null, FALSE, now()),
(21, 3, 2, 0, null, FALSE, now()),
(22, 4, 2, 0, null, FALSE, now()),
(23, 5, 2, 0, null, FALSE, now()),
(24, 6, 2, 0, null, FALSE, now()),
(25, 7, 2, 0, null, FALSE, now()),
(26, 8, 2, 0, null, FALSE, now());

-- board
insert into board (board_id, category_id, title, info, content, thumbnail, status, created_at)
overriding system value values
-- event
(0, 11, '쿠폰 프로모션', '쿠폰 프로모션 간략 설명', '세 부 내 용 ', '/', '/', now()),
(1, 11, '출석 이벤트', '출석 이벤트 간략 설명', '/', '/', '/', now()),
(2, 11, '이벤트 테스트 제목', '이벤트 테스트 간략 설명', '/', '/', '/', now()),
(7, 11, '포인트 안내', '포인트 적립해보시덩가~', '/', '/', '/', now()),
-- notice
(3, 9, '공지사항입니다', '공지사항 간략 설명', '/', '/', '/', now()),
(4, 9, '공지사항이라니깐요', '간략설명이라니깐요', '/', '/', '/', now()),
-- faq
(5, 10, 'FAQ랍니다', 'FAQ 간략 설명', '/', '/', '/', now()),
(6, 10, 'FAQ라니깐요', '간략설명이라니깐요', '/', '/', '/', now());






