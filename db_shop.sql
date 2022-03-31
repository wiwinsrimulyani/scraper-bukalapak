-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2022 at 04:48 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scrapy`
--

-- --------------------------------------------------------

--
-- Table structure for table `bk_shop_iter`
--

CREATE TABLE `bk_shop_iter` (
   `id` int(11) NOT NULL,
  `city` varchar(64) DEFAULT NULL,
  `province` varchar(64) DEFAULT NULL,
  `is_brand_seller` BOOLEAN DEFAULT NULL,
  `is_shop_closed` BOOLEAN DEFAULT NULL,
  `delivery_time` DATETIME DEFAULT NULL,

  `first_upload_product_at` DATETIME DEFAULT NULL,
  `is_shop_inactive` BOOLEAN DEFAULT NULL,
  `last_appear_at` DATETIME DEFAULT NULL,
  `last_order_schedule` DATETIME DEFAULT NULL, 
  `shop_level` varchar(64) DEFAULT NULL,
  `shop_name` varchar(64) DEFAULT NULL,
  `shop_premium_level` varchar(64) DEFAULT NULL,
  `is_shop_premium_top_seller` BOOLEAN DEFAULT NULL,
  `recent_rejection_transaction` INT(64) DEFAULT NULL,
  `rejected_count` INT(64) DEFAULT NULL,
  `negative_reviews` INT(64) DEFAULT NULL,
  `positive_reviews` INT(64) DEFAULT NULL,
  `sla_type` INT(64) DEFAULT NULL, 
  `sla_value` INT(11) DEFAULT NULL,
  `subscribers_amount` INT(64) DEFAULT NULL,
  `shop_url` varchar(200) DEFAULT NULL,
  `scraper_datetime` DATETIME DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `olxproperty`
--
ALTER TABLE `bk_shop_iter`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `olxproperty`
--
ALTER TABLE `bk_shop_iter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
