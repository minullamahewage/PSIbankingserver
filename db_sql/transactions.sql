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
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `accno` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `description` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `debit` float(20,2) NOT NULL DEFAULT '0.00',
  `credit` float(20,2) NOT NULL DEFAULT '0.00',
  `balance` float(20,2) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `transactions`
--

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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD KEY `accno` (`accno`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`accno`) REFERENCES `accountdet` (`accno`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
