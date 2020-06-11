-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 09, 2020 at 10:26 AM
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
-- Table structure for table `billpaymenttransactions`
--

CREATE TABLE `billpaymenttransactions` (
  `accno` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nic` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `debit` float(20,2) NOT NULL DEFAULT '0.00',
  `credit` float(20,2) NOT NULL DEFAULT '0.00',
  `balance` float(20,2) NOT NULL DEFAULT '0.00',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `billpaymenttransactions`
--

INSERT INTO `billpaymenttransactions` (`accno`, `nic`, `debit`, `credit`, `balance`) VALUES
('44444', '555879996V', 3000.00, 0.00, 3000.00),
('44444', '555879996V', 0.00, 750.00, 2250.00),
('44444', '555879996V', 0.00, 200.00, 2050.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billpaymenttransactions`
--
ALTER TABLE `billpaymenttransactions`
  ADD KEY `accno` (`accno`),
  ADD KEY `nic` (`nic`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `billpaymenttransactions`
--
ALTER TABLE `billpaymenttransactions`
  ADD CONSTRAINT `billpaymenttransactions_ibfk_1` FOREIGN KEY (`accno`) REFERENCES `fields` (`accno`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `billpaymenttransactions_ibfk_2` FOREIGN KEY (`nic`) REFERENCES `consumers` (`nic`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
