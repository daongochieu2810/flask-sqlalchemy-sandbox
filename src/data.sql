insert into student (email) values ('kellcock0@trellian.com');
insert into student (email) values ('eburchett1@mozilla.com');
insert into student (email) values ('kmathieu2@miibeian.gov.cn');
insert into student (email) values ('aoven3@163.com');
insert into student (email) values ('kblankau4@indiegogo.com');
insert into student (email) values ('asandyfirth5@livejournal.com');
insert into student (email) values ('fshirer6@state.tx.us');
insert into student (email) values ('kshalloo7@usda.gov');
insert into student (email) values ('maustins8@wikimedia.org');
insert into student (email) values ('vmacilraith9@rediff.com');

insert into book (isbn, title, author) values ('718229515-6', 'Riverworld', 'Danie Osmond');
insert into book (isbn, title, author) values ('994203207-X', 'NATO''s Secret Armies (Gladio: L''esercito segreto della Nato)', 'Shellie Snazle');
insert into book (isbn, title, author) values ('597971252-6', 'Pretty/Handsome', 'Evyn Thirlwell');
insert into book (isbn, title, author) values ('081175910-5', 'Lake City', 'Wolf Nyssen');
insert into book (isbn, title, author) values ('276030421-3', 'Calendar Girl', 'Hermann Shegog');
insert into book (isbn, title, author) values ('066093023-4', 'Sam Peckinpah''s West: Legacy of a Hollywood Renegade', 'Lionel Cansdall');
insert into book (isbn, title, author) values ('166106603-8', 'Charlie''s Country', 'Henrie Heinzler');
insert into book (isbn, title, author) values ('032728936-8', 'Goldene Zeiten', 'Cortney Wennam');
insert into book (isbn, title, author) values ('693974864-4', 'Kummelin jackpot', 'Rafaelia Bollini');
insert into book (isbn, title, author) values ('823819572-1', 'You Can Count on Me', 'Reube Heyns');

delete from assignment;
insert into assignment (isbn, email) (select isbn, email from student, book where random() < 0.1);