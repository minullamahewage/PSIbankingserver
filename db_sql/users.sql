-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 09, 2020 at 10:29 AM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `IlYy99NiBs`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `email` text COLLATE utf8_unicode_ci NOT NULL,
  `first_name` text COLLATE utf8_unicode_ci NOT NULL,
  `last_name` text COLLATE utf8_unicode_ci NOT NULL,
  `password_salt` text COLLATE utf8_unicode_ci NOT NULL,
  `password_hash` text COLLATE utf8_unicode_ci NOT NULL,
  `created` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `email`, `first_name`, `last_name`, `password_salt`, `password_hash`, `created`) VALUES
(1, 'test@gmail.com', 'Test', 'User 1', '75b6e8243d6774daaea278f67fc2e9b7', 'e107271df14eeda28efe529996408353dbf381962a7405feda7424b185dc5102', '2020-05-11 11:50:15'),
(2, 'minullamahewage@gmail.com', 'Minul', 'Lamahewage', 'e73f301fd27168a9d5d3bdad489d6fbc', '333ad56eacf67af4b3eae42c47ad00dd54b905be2f554e646bc8679b52563155', '2020-05-15 07:50:30'),
(3, 'rashnanayakkara.17@cse.mrt.ac.lk', 'rashmika', 'lakshan', 'ea85579c8e0365ed459e50aae5895927', 'eeaa79c6b74fd7b2185b69d8c271ab6e5d3a66092a67a6fd37ef266565e3cfc0', '2020-05-15 21:01:50'),
(4, 'testuser2@gmail.com', 'Test', 'User 2', '0597d17925d35784638206bb4d7252a1', 'bf17f5ad58994fcb49ffed40a97d65840593f1ad716e078fa2bf6878be7eea08', '2020-05-18 21:07:16'),
(5, 'rash123@gmail.com', 'rash', 'mika', '41ab77b4a401312ba3f2167ed29582ce', '54a107df113b828c4f2dc07afae2aa7866f9b3e3f6eb97c88a0037b5cb623a04', '2020-05-21 06:52:07'),
(6, 's@h.co', 'lam', 'kk', 'eba6ef87b497ceed7018427944dacaad', '97a138e78af1eb195b471d1be4aae5d0be171a845fa1f7b6c5d66d5f2daec490', '2020-05-31 06:22:08'),
(7, 'davidbilla@gmail.com', 'david', 'billa', '1b39bf99ee22b02dccae076c578d7567', '329e168bbb3afa356658b31fd5ab0c80bf6291f1276f3625dc87777c2f8559f1', '2020-05-31 06:27:15'),
(8, 'bruce@gmail.com', 'bruce', 'wayne', 'd6529d0281bd84377c2f586d087cbebb', 'a7e4fb19f5535f367feffa4180a0612222b28972698e0579d170881888cbeb53', '2020-06-01 04:01:13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
