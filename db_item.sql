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
-- Table structure for table `olxproperty`
--

CREATE TABLE `bk_item_iter` (
  `id` int(11) NOT NULL,
  `idd` varchar(64) DEFAULT NULL,
  `sku_id` INT(64) DEFAULT NULL,
  `shop_id` varchar(64) DEFAULT NULL,
  `item_name` varchar(200) DEFAULT NULL,
  `category`varchar(64) DEFAULT NULL,
  `subCategory`varchar(64) DEFAULT NULL,
  `subSubCategory`varchar(64) DEFAULT NULL,
  `id_category` int(11) DEFAULT NULL,
  `url_category` varchar(500) DEFAULT NULL,
  `couriers` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `deal_applied_date` datetime DEFAULT NULL,
  `deal_discount_price` int(64) DEFAULT NULL, 
  `deal_expired_date` datetime DEFAULT NULL,
  `deal_original_price` int(64) DEFAULT NULL,
  `deal_percentage` int(11) DEFAULT NULL,
  `description` varchar(100000) DEFAULT NULL,
  `is_digital_product` boolean DEFAULT NULL,
  `is_for_sale` boolean DEFAULT NULL,
  `max_quantity` int(64) DEFAULT NULL,
  `merchant_return_insurance` boolean DEFAULT NULL,
  `min_quantity` int(11) DEFAULT NULL,
  `rating` FLOAT DEFAULT NULL,
  `rating_user_count`  INT(64) DEFAULT NULL,
  `rating_relisted_at` DATETIME DEFAULT NULL,
  `rating_is_rush_delivery`  BOOLEAN DEFAULT NULL,
  `shipping_force_insurance`  BOOLEAN DEFAULT NULL,
  `stats_interest_count`  INT(64) DEFAULT NULL,
  `stats_sold_count`  INT(64) DEFAULT NULL,
  `stats_view_count`  INT(64) DEFAULT NULL,
  `stats_waiting_payment_count`  INT(64) DEFAULT NULL,
  `stock`  INT(64) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `url_product` varchar(200) DEFAULT NULL,
  `warranty_cheapest`  BOOLEAN DEFAULT NULL,
  `product_weight`  INT(64) DEFAULT NULL,
  `without_shipping` BOOLEAN DEFAULT NULL,
  `scraper_datetime` datetime DEFAULT NULL
  
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `olxproperty`
--
ALTER TABLE `bk_item_iter`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `olxproperty`
--
ALTER TABLE `bk_item_iter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
