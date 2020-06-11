-- creating tables-----------------------------------

-- user table-----------
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `email` text COLLATE utf8_unicode_ci NOT NULL,
  `first_name` text COLLATE utf8_unicode_ci NOT NULL,
  `last_name` text COLLATE utf8_unicode_ci NOT NULL,
  `password_salt` text COLLATE utf8_unicode_ci NOT NULL,
  `password_hash` text COLLATE utf8_unicode_ci NOT NULL,
  `created` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;


-- accountdet table ------------
CREATE TABLE `accountdet` (
  `accno` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nic` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `branch` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `accountdet`
  ADD PRIMARY KEY (`accno`);


-- branches -------------------
CREATE TABLE `branches` (
  `id` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `branchname` varchar(10) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `branches`
  ADD PRIMARY KEY (`id`);


-- consumers table --------------
CREATE TABLE `consumers` (
  `nic` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `address` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `postalno` int(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `consumers`
  ADD PRIMARY KEY (`nic`);


-- fields table ------------------
CREATE TABLE `fields` (
  `accno` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `fieldname` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `fields`
  ADD PRIMARY KEY (`accno`);


-- banking complaints table----------
CREATE TABLE `banking_complaints` (
  `brid` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `complain_behaviour` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `complain_management` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `complain_facility` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `complain_wasting` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `banking_complaints`
  ADD KEY `brid` (`brid`);

ALTER TABLE `banking_complaints`
  ADD CONSTRAINT `banking_complaints_ibfk_1` FOREIGN KEY (`brid`) REFERENCES `branches` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- bill transactions table ------------
CREATE TABLE `billpaymenttransactions` (
  `accno` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nic` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `debit` float(20,2) NOT NULL DEFAULT '0.00',
  `credit` float(20,2) NOT NULL DEFAULT '0.00',
  `balance` float(20,2) NOT NULL DEFAULT '0.00',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `billpaymenttransactions`
  ADD KEY `accno` (`accno`),
  ADD KEY `nic` (`nic`);

ALTER TABLE `billpaymenttransactions`
  ADD CONSTRAINT `billpaymenttransactions_ibfk_1` FOREIGN KEY (`accno`) REFERENCES `fields` (`accno`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `billpaymenttransactions_ibfk_2` FOREIGN KEY (`nic`) REFERENCES `consumers` (`nic`) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- joinaccounts table ----------------
CREATE TABLE `joinaccounts` (
  `user_id` int(11) NOT NULL,
  `accno` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `joinaccounts`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `accno` (`accno`);

ALTER TABLE `joinaccounts`
  ADD CONSTRAINT `joinaccounts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `joinaccounts_ibfk_2` FOREIGN KEY (`accno`) REFERENCES `accountdet` (`accno`) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- transactions table ----------------
CREATE TABLE `transactions` (
  `accno` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `description` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `debit` float(20,2) NOT NULL DEFAULT '0.00',
  `credit` float(20,2) NOT NULL DEFAULT '0.00',
  `balance` float(20,2) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

ALTER TABLE `transactions`
  ADD KEY `accno` (`accno`);

ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`accno`) REFERENCES `accountdet` (`accno`) ON DELETE RESTRICT ON UPDATE RESTRICT;







-- insert queries-----------------------------------
INSERT INTO `users` (`user_id`, `email`, `first_name`, `last_name`, `password_salt`, `password_hash`, `created`) VALUES
(1, 'test@gmail.com', 'Test', 'User 1', '75b6e8243d6774daaea278f67fc2e9b7', 'e107271df14eeda28efe529996408353dbf381962a7405feda7424b185dc5102', '2020-05-11 11:50:15'),
(2, 'minullamahewage@gmail.com', 'Minul', 'Lamahewage', 'e73f301fd27168a9d5d3bdad489d6fbc', '333ad56eacf67af4b3eae42c47ad00dd54b905be2f554e646bc8679b52563155', '2020-05-15 07:50:30'),
(3, 'rashnanayakkara.17@cse.mrt.ac.lk', 'rashmika', 'lakshan', 'ea85579c8e0365ed459e50aae5895927', 'eeaa79c6b74fd7b2185b69d8c271ab6e5d3a66092a67a6fd37ef266565e3cfc0', '2020-05-15 21:01:50'),
(4, 'testuser2@gmail.com', 'Test', 'User 2', '0597d17925d35784638206bb4d7252a1', 'bf17f5ad58994fcb49ffed40a97d65840593f1ad716e078fa2bf6878be7eea08', '2020-05-18 21:07:16'),
(5, 'rash123@gmail.com', 'rash', 'mika', '41ab77b4a401312ba3f2167ed29582ce', '54a107df113b828c4f2dc07afae2aa7866f9b3e3f6eb97c88a0037b5cb623a04', '2020-05-21 06:52:07'),
(6, 's@h.co', 'lam', 'kk', 'eba6ef87b497ceed7018427944dacaad', '97a138e78af1eb195b471d1be4aae5d0be171a845fa1f7b6c5d66d5f2daec490', '2020-05-31 06:22:08'),
(7, 'davidbilla@gmail.com', 'david', 'billa', '1b39bf99ee22b02dccae076c578d7567', '329e168bbb3afa356658b31fd5ab0c80bf6291f1276f3625dc87777c2f8559f1', '2020-05-31 06:27:15'),
(8, 'bruce@gmail.com', 'bruce', 'wayne', 'd6529d0281bd84377c2f586d087cbebb', 'a7e4fb19f5535f367feffa4180a0612222b28972698e0579d170881888cbeb53', '2020-06-01 04:01:13');

INSERT INTO `accountdet` (`accno`, `name`, `nic`, `branch`) VALUES
('123456789', 'N.G.L.R.Lakshan', '364512785V', 'Galle'),
('4556128978', 'Albert Ainstain', '962378554V', 'Seegiriya'),
('456123789', 'Jorge Washinton', '789632145V', 'Kalutara'),
('8956231245', 'S.C.Dhavinchi', '5588124722V', 'Matara'),
('987654321', 'K.G.Siriwardhana', '784512963V', 'Colombo');

INSERT INTO `branches` (`id`, `branchname`) VALUES
('b1', 'galle'),
('b2', 'colombo'),
('b3', 'matara'),
('b4', 'jaffna'),
('b5', 'moratuwa');

INSERT INTO `consumers` (`nic`, `name`, `address`, `postalno`) VALUES
('4578632195V', 'Charlie Swane ', 'esthima, aluth wanguwa, australia', 78),
('555879996V', 'K.W.Saranga', '170/A, dobagahawatta, norway', 8080);

INSERT INTO `fields` (`accno`, `fieldname`) VALUES
('11111', 'Electricity'),
('22222', 'Insuarance'),
('33333', 'Telephone'),
('44444', 'Television'),
('55555', 'Water');

INSERT INTO `banking_complaints` (`brid`, `complain_behaviour`, `complain_management`, `complain_facility`, `complain_wasting`) VALUES
('b1', 'inappropriate manager behaviour', NULL, NULL, NULL),
('b2', NULL, 'account transactions not updated', NULL, NULL);

INSERT INTO `billpaymenttransactions` (`accno`, `nic`, `debit`, `credit`, `balance`) VALUES
('44444', '555879996V', 3000.00, 0.00, 3000.00),
('44444', '555879996V', 0.00, 750.00, 2250.00),
('44444', '555879996V', 0.00, 200.00, 2050.00);

INSERT INTO `joinaccounts` (`user_id`, `accno`) VALUES
(3, '123456789'),
(2, '456123789'),
(1, '987654321'),
(4, '8956231245');

INSERT INTO `transactions` (`accno`, `description`, `debit`, `credit`, `balance`) VALUES
('123456789', 'started', 5000.00, 0.00, 5000.00),
('123456789', 'paid water bill', 0.00, 1500.00, 3500.00),
('456123789', 'started', 12000.00, 0.00, 12000.00),
('456123789', 'deposited', 3000.00, 0.00, 15000.00),
('456123789', 'retrieved', 0.00, 5500.00, 9500.00),
('987654321', 'started', 6500.00, 0.00, 6500.00),
('987654321', 'paid sltbill', 0.00, 1200.00, 5300.00),
('987654321', 'bought from ebay', 0.00, 1300.00, 4000.00),
('456123789', 'transfered from K.G.Siriwardhana', 1000.00, 0.00, 10500.00),
('987654321', 'transfered to Test', 0.00, 1000.00, 3000.00),
('456123789', 'K.W.Saranga\'s Televisionbill paid ', 0.00, 750.00, 9750.00),
('123456789', 'K.W.Saranga\'s Televisionbill paid ', 0.00, 200.00, 3300.00),
('987654321', 'transfered from N.G.L.R.Lakshan', 300.00, 0.00, 3300.00),
('123456789', 'transfered to K.G.Siriwardhana', 0.00, 300.00, 3000.00),
('4556128978', 'started', 50000.00, 0.00, 50000.00);