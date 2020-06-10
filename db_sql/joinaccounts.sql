-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 09, 2020 at 10:28 AM
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
-- Table structure for table `joinaccounts`
--

CREATE TABLE `joinaccounts` (
  `user_id` int(11) NOT NULL,
  `accno` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `joinaccounts`
--

INSERT INTO `joinaccounts` (`user_id`, `accno`) VALUES
(3, '123456789'),
(2, '456123789'),
(1, '987654321'),
(4, '8956231245');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `joinaccounts`
--
ALTER TABLE `joinaccounts`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `accno` (`accno`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `joinaccounts`
--
ALTER TABLE `joinaccounts`
  ADD CONSTRAINT `joinaccounts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `joinaccounts_ibfk_2` FOREIGN KEY (`accno`) REFERENCES `accountdet` (`accno`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
