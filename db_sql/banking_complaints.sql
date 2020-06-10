-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 09, 2020 at 10:25 AM
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
-- Table structure for table `banking_complaints`
--

CREATE TABLE `banking_complaints` (
  `brid` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `complain_behaviour` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `complain_management` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `complain_facility` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `complain_wasting` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `banking_complaints`
--

INSERT INTO `banking_complaints` (`brid`, `complain_behaviour`, `complain_management`, `complain_facility`, `complain_wasting`) VALUES
('b1', 'inappropriate manager behaviour', NULL, NULL, NULL),
('b2', NULL, 'account transactions not updated', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `banking_complaints`
--
ALTER TABLE `banking_complaints`
  ADD KEY `brid` (`brid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `banking_complaints`
--
ALTER TABLE `banking_complaints`
  ADD CONSTRAINT `banking_complaints_ibfk_1` FOREIGN KEY (`brid`) REFERENCES `branches` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
