-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 09, 2020 at 10:20 AM
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
-- Table structure for table `accountdet`
--

CREATE TABLE `accountdet` (
  `accno` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nic` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `branch` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `accountdet`
--

INSERT INTO `accountdet` (`accno`, `name`, `nic`, `branch`) VALUES
('123456789', 'N.G.L.R.Lakshan', '364512785V', 'Galle'),
('4556128978', 'Albert Ainstain', '962378554V', 'Seegiriya'),
('456123789', 'Jorge Washinton', '789632145V', 'Kalutara'),
('8956231245', 'S.C.Dhavinchi', '5588124722V', 'Matara'),
('987654321', 'K.G.Siriwardhana', '784512963V', 'Colombo');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accountdet`
--
ALTER TABLE `accountdet`
  ADD PRIMARY KEY (`accno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
