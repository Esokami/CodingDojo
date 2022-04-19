-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: product-schema
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories_products`
--

DROP TABLE IF EXISTS `categories_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories_products` (
  `product_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  KEY `FK2a3u5mbtmtq3d4s5abajhhksf` (`category_id`),
  KEY `FK2tnk948b1lgpg3uggwyi2kwfq` (`product_id`),
  CONSTRAINT `FK2a3u5mbtmtq3d4s5abajhhksf` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `FK2tnk948b1lgpg3uggwyi2kwfq` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories_products`
--

LOCK TABLES `categories_products` WRITE;
/*!40000 ALTER TABLE `categories_products` DISABLE KEYS */;
INSERT INTO `categories_products` VALUES (1,2),(1,1),(3,1),(2,3),(4,1),(4,2);
/*!40000 ALTER TABLE `categories_products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-18 16:24:15
