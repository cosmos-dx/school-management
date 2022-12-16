-- MySQL dump 10.13  Distrib 5.5.46, for Win32 (x86)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	5.5.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `calender`
--

DROP TABLE IF EXISTS `calender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calender` (
  `fyear` int(11) NOT NULL AUTO_INCREMENT,
  `year` date NOT NULL DEFAULT '0000-00-00',
  PRIMARY KEY (`fyear`),
  KEY `calenderindex` (`fyear`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calender`
--

LOCK TABLES `calender` WRITE;
/*!40000 ALTER TABLE `calender` DISABLE KEYS */;
INSERT INTO `calender` VALUES (1,'2016-04-01');
/*!40000 ALTER TABLE `calender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cash`
--

DROP TABLE IF EXISTS `cash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cash` (
  `cashID` int(11) NOT NULL AUTO_INCREMENT,
  `transactionID` int(11) NOT NULL DEFAULT '0',
  `ac_type` smallint(2) NOT NULL DEFAULT '0',
  `debit` decimal(8,2) NOT NULL DEFAULT '0.00',
  `credit` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fyear` smallint(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cashID`,`fyear`),
  KEY `cashindex` (`transactionID`,`ac_type`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1
/*!50500 PARTITION BY RANGE  COLUMNS(fyear)
(PARTITION fy1 VALUES LESS THAN (1) ENGINE = InnoDB) */;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cash`
--

LOCK TABLES `cash` WRITE;
/*!40000 ALTER TABLE `cash` DISABLE KEYS */;
INSERT INTO `cash` VALUES (1,1,0,1100.00,0.00,0),(2,2,0,1000.00,0.00,0),(3,3,0,800.00,0.00,0),(4,4,0,1800.00,0.00,0),(5,5,0,800.00,0.00,0),(6,6,0,1350.00,0.00,-1),(7,7,0,9205.00,0.00,-1);
/*!40000 ALTER TABLE `cash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `classID` smallint(2) NOT NULL,
  `sectionID` smallint(2) NOT NULL DEFAULT '0',
  `fee0` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee1` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee2` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee3` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee4` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee5` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee6` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee7` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee8` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee9` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee10` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee11` decimal(8,2) NOT NULL DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(2,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(3,0,5500.00,1000.00,500.00,100.00,0.00,0.00,400.00,0.00,0.00,0.00,0.00,0.00),(4,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(5,0,8000.00,200.00,50.00,5.00,0.00,0.00,350.00,0.00,0.00,0.00,0.00,0.00),(6,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(7,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(8,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(9,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(10,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(11,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(12,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(51,0,5500.00,700.00,0.00,100.00,0.00,500.00,400.00,0.00,0.00,0.00,0.00,0.00),(52,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00),(53,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employeeID` int(11) NOT NULL AUTO_INCREMENT,
  `ledgerID` int(11) NOT NULL DEFAULT '0',
  `designation` varchar(25) NOT NULL DEFAULT 'T',
  `employee_name` varchar(25) NOT NULL DEFAULT '',
  `guardian_name` varchar(25) NOT NULL DEFAULT '',
  `add1` varchar(25) NOT NULL DEFAULT '',
  `add2` varchar(25) NOT NULL DEFAULT '',
  `email` varchar(50) NOT NULL DEFAULT '',
  `phone` varchar(11) NOT NULL DEFAULT '',
  `off_phone` varchar(11) NOT NULL DEFAULT '',
  `status` tinyint(1) NOT NULL DEFAULT '0',
  `conv_mode` tinyint(2) NOT NULL DEFAULT '0',
  `distance` smallint(3) NOT NULL DEFAULT '0',
  `conv_bool` tinyint(1) NOT NULL DEFAULT '0',
  `dob` date NOT NULL DEFAULT '0000-00-00',
  `doa` date NOT NULL DEFAULT '0000-00-00',
  `dot` date NOT NULL DEFAULT '0000-00-00',
  `comment` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`employeeID`),
  KEY `employeeindex` (`employeeID`,`ledgerID`,`employee_name`,`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,4,'T','AAAAA','KKK','LL','PP','','88888888888','77777777777',0,0,0,0,'2016-06-16','2016-06-16','0000-00-00',''),(2,48,'T','JAYANTI SRIVASTVA','JAI PRAKASH SRIVASTVA','INDRA NAGAR','DEORIA','','11111111111','33333333333',0,0,0,0,'1989-10-25','2012-10-01','0000-00-00',''),(3,52,'T','SUNITI JAISWAL ','GJGJG','ASDF','ASDF','','383383','',0,0,0,0,'2017-01-15','2017-01-15','0000-00-00',''),(4,57,'T','PRITI GUPTA','BABU ROA SINGH','DEORIA','DEORIA','','92828282828','',0,0,0,2,'1999-01-12','2017-01-27','0000-00-00','');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empreg`
--

DROP TABLE IF EXISTS `empreg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empreg` (
  `empregID` int(11) NOT NULL AUTO_INCREMENT,
  `employeeID` int(11) NOT NULL DEFAULT '0',
  `ap` varchar(1) NOT NULL DEFAULT 'A',
  `daytime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `iddate` varchar(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`empregID`),
  UNIQUE KEY `iddate` (`iddate`),
  KEY `sturegindex` (`employeeID`,`daytime`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empreg`
--

LOCK TABLES `empreg` WRITE;
/*!40000 ALTER TABLE `empreg` DISABLE KEYS */;
INSERT INTO `empreg` VALUES (4,2,'A','2017-01-25 06:15:13','220170125'),(5,1,'P','2017-01-25 06:15:13','120170125'),(6,3,'P','2017-01-25 06:15:13','320170125'),(9,3,'P','2017-01-26 07:05:04','320170126'),(10,1,'A','2017-01-26 07:05:09','120170126'),(11,2,'A','2017-01-26 07:05:09','220170126'),(18,2,'P','2017-01-27 13:01:07','220170127'),(19,4,'P','2017-01-27 13:01:07','420170127'),(20,1,'A','2017-01-27 13:01:10','120170127'),(21,3,'A','2017-01-27 13:01:10','320170127');
/*!40000 ALTER TABLE `empreg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ledger`
--

DROP TABLE IF EXISTS `ledger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ledger` (
  `ledgerID` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ledgerID`),
  KEY `ledgerindex` (`ledgerID`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ledger`
--

LOCK TABLES `ledger` WRITE;
/*!40000 ALTER TABLE `ledger` DISABLE KEYS */;
INSERT INTO `ledger` VALUES (3,2),(4,1),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),(12,2),(13,2),(14,2),(15,2),(16,2),(17,2),(18,2),(19,2),(20,2),(21,2),(22,2),(23,2),(24,2),(25,2),(26,2),(27,2),(28,2),(29,2),(30,2),(31,2),(32,2),(33,2),(34,2),(35,2),(36,2),(37,2),(38,2),(39,2),(40,2),(41,2),(42,2),(43,2),(44,2),(45,2),(46,2),(47,2),(48,1),(49,2),(50,2),(51,2),(52,1),(53,2),(54,2),(55,1),(56,2),(57,1);
/*!40000 ALTER TABLE `ledger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owner_det`
--

DROP TABLE IF EXISTS `owner_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `owner_det` (
  `owner_det_id` smallint(2) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `add1` varchar(25) NOT NULL DEFAULT '',
  `add2` varchar(25) NOT NULL DEFAULT '',
  `phone` varchar(11) NOT NULL DEFAULT '',
  `licence` varchar(25) NOT NULL DEFAULT '',
  `tin` varchar(25) NOT NULL DEFAULT '',
  `user_id` varchar(25) NOT NULL DEFAULT '',
  `user_pass` varchar(25) NOT NULL DEFAULT '',
  `statutory1` varchar(50) NOT NULL DEFAULT '',
  `statutory2` varchar(50) NOT NULL DEFAULT '',
  `statutory3` varchar(50) NOT NULL DEFAULT '',
  `statutory4` varchar(50) NOT NULL DEFAULT '',
  `pport` varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (`owner_det_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner_det`
--

LOCK TABLES `owner_det` WRITE;
/*!40000 ALTER TABLE `owner_det` DISABLE KEYS */;
INSERT INTO `owner_det` VALUES (1,'MY SCHOOL','TEST ADD 1','TEST ADD 2','9935188831','abcd','12345678900','123','123','Subject to DEORIA jurisdiction only on the','assurance of the party that they have their','LICENCE we are executing the indent ','.','LPT1');
/*!40000 ALTER TABLE `owner_det` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `section` (
  `sectionID` smallint(2) NOT NULL AUTO_INCREMENT,
  `section` varchar(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`sectionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
/*!40000 ALTER TABLE `section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sheet`
--

DROP TABLE IF EXISTS `sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sheet` (
  `sheetID` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` int(11) NOT NULL DEFAULT '0',
  `employeeID` int(11) NOT NULL DEFAULT '0',
  `classID` smallint(2) NOT NULL DEFAULT '0',
  `category` smallint(2) NOT NULL DEFAULT '0',
  `sheet_date` date NOT NULL DEFAULT '0000-00-00',
  `hindi` decimal(8,2) NOT NULL DEFAULT '0.00',
  `english` decimal(8,2) NOT NULL DEFAULT '0.00',
  `science` decimal(8,2) NOT NULL DEFAULT '0.00',
  `math` decimal(8,2) NOT NULL DEFAULT '0.00',
  `sstd` decimal(8,2) NOT NULL DEFAULT '0.00',
  `comp` decimal(8,2) NOT NULL DEFAULT '0.00',
  `bio` decimal(8,2) NOT NULL DEFAULT '0.00',
  `chem` decimal(8,2) NOT NULL DEFAULT '0.00',
  `phys` decimal(8,2) NOT NULL DEFAULT '0.00',
  `sans` decimal(8,2) NOT NULL DEFAULT '0.00',
  `civic` decimal(8,2) NOT NULL DEFAULT '0.00',
  `hist` decimal(8,2) NOT NULL DEFAULT '0.00',
  `geog` decimal(8,2) NOT NULL DEFAULT '0.00',
  `comm` decimal(8,2) NOT NULL DEFAULT '0.00',
  `sact` decimal(8,2) NOT NULL DEFAULT '0.00',
  `sport` decimal(8,2) NOT NULL DEFAULT '0.00',
  `other` decimal(8,2) NOT NULL DEFAULT '0.00',
  `attend` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fyear` smallint(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sheetID`,`fyear`),
  KEY `sheetindex` (`sheetID`,`studentID`,`classID`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1
/*!50500 PARTITION BY RANGE  COLUMNS(fyear)
(PARTITION fy1 VALUES LESS THAN (1) ENGINE = InnoDB) */;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheet`
--

LOCK TABLES `sheet` WRITE;
/*!40000 ALTER TABLE `sheet` DISABLE KEYS */;
INSERT INTO `sheet` VALUES (13,2,1,3,0,'2016-06-16',99.00,77.00,66.00,66.00,77.00,66.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(14,8,1,2,0,'2016-10-25',40.00,88.00,99.00,0.00,77.00,77.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,79.00,0),(15,30,2,1,0,'2016-08-25',33.00,33.00,33.00,44.00,55.00,66.00,66.00,99.00,0.00,0.00,88.00,99.00,0.00,88.00,0.00,88.00,88.00,88.00,0),(16,32,2,2,0,'2016-04-29',22.00,20.00,22.00,22.00,22.00,33.00,22.00,12.00,23.00,44.00,55.00,66.00,22.00,22.00,22.00,33.00,22.00,65.00,0),(17,32,2,2,0,'2016-10-21',22.00,20.00,22.00,22.00,22.00,33.00,22.00,12.00,23.00,44.00,55.00,66.00,22.00,22.00,22.00,33.00,22.00,65.00,0),(18,32,2,2,0,'2016-06-21',22.00,20.00,22.00,22.00,22.00,33.00,22.00,12.00,23.00,44.00,55.00,66.00,22.00,22.00,22.00,33.00,22.00,65.00,0),(19,32,2,2,0,'2016-07-21',22.00,20.00,22.00,22.00,22.00,33.00,22.00,12.00,23.00,44.00,55.00,66.00,22.00,22.00,22.00,33.00,22.00,65.00,0),(20,32,2,2,0,'2016-08-21',22.00,20.00,22.00,22.00,22.00,33.00,22.00,12.00,23.00,44.00,55.00,66.00,22.00,22.00,22.00,33.00,22.00,65.00,0),(21,32,2,2,0,'2016-05-22',22.00,20.00,22.00,22.00,22.00,33.00,22.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(22,32,2,2,0,'2016-05-25',0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(23,42,2,2,0,'2016-04-08',4.00,4.00,4.00,4.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(24,42,2,2,0,'2016-05-08',5.00,5.00,5.00,5.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(25,42,2,2,0,'2016-06-08',5.00,6.00,6.00,6.00,6.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(26,42,2,2,0,'2016-07-08',7.00,7.00,7.00,6.00,6.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(27,42,2,2,0,'2016-08-08',8.00,7.00,7.00,6.00,6.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(28,42,2,2,0,'2016-09-08',9.00,7.00,9.00,6.00,6.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(29,42,2,2,0,'2016-10-08',10.00,7.00,9.00,6.00,6.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4.00,0),(30,42,2,2,0,'2016-04-01',0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(31,43,2,1,0,'2017-01-12',77.00,88.00,66.00,55.00,44.00,66.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(32,24,2,52,0,'2017-01-14',56.00,76.00,88.00,100.00,76.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(33,24,2,52,0,'2016-10-14',44.00,44.00,44.00,44.00,44.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(34,24,2,52,0,'2016-11-14',11.00,11.00,11.00,11.00,11.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(35,24,2,52,0,'2016-12-14',12.00,12.00,12.00,12.00,12.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(36,24,2,52,0,'2016-04-14',4.00,4.00,4.00,4.00,4.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(37,24,2,52,0,'2016-05-14',5.00,5.00,5.00,5.00,5.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(38,24,2,52,0,'2016-06-14',6.00,6.00,6.00,6.00,6.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(39,24,2,52,0,'2016-07-14',7.00,7.00,7.00,7.00,7.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(40,24,2,52,0,'2016-08-14',8.00,8.00,8.00,8.00,8.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(41,24,2,52,0,'2016-09-14',9.00,9.00,9.00,9.00,9.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(42,43,2,1,0,'2016-11-15',11.00,11.00,11.00,11.00,11.00,100.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(43,44,3,5,0,'2017-01-15',47.00,50.00,50.00,45.00,50.00,50.00,50.00,50.00,50.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0),(44,45,3,5,0,'2017-01-15',1.00,2.00,3.00,1.00,23.00,12.00,1.00,4.00,3.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0);
/*!40000 ALTER TABLE `sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `studentID` int(11) NOT NULL AUTO_INCREMENT,
  `ledgerID` int(11) NOT NULL DEFAULT '0',
  `classID` smallint(2) NOT NULL DEFAULT '0',
  `student_name` varchar(25) NOT NULL DEFAULT '',
  `guardian_name` varchar(25) NOT NULL DEFAULT '',
  `add1` varchar(25) NOT NULL DEFAULT '',
  `add2` varchar(25) NOT NULL DEFAULT '',
  `email` varchar(50) NOT NULL DEFAULT '',
  `phone` varchar(11) NOT NULL DEFAULT '',
  `section` varchar(1) NOT NULL DEFAULT 'A',
  `off_phone` varchar(11) NOT NULL DEFAULT '',
  `status` tinyint(1) NOT NULL DEFAULT '0',
  `conv_mode` tinyint(2) NOT NULL DEFAULT '0',
  `distance` smallint(3) NOT NULL DEFAULT '0',
  `conv_bool` tinyint(1) NOT NULL DEFAULT '0',
  `dob` date NOT NULL DEFAULT '0000-00-00',
  `doa` date NOT NULL DEFAULT '0000-00-00',
  `dot` date NOT NULL DEFAULT '0000-00-00',
  `comment` varchar(30) NOT NULL DEFAULT '0000-00-00',
  PRIMARY KEY (`studentID`),
  KEY `studentindex` (`studentID`,`ledgerID`,`classID`,`student_name`,`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (2,3,3,'PRINCY MISHRA','HG MISHRA','ABCD','ABCD','','8090780057','A','9044440703',0,0,0,0,'2002-06-16','2016-06-16','0000-00-00',''),(3,5,3,'PRINCY MISHRA','K N MISHRA','C C ROAD','DEORIA','akm979@gmail.com','9889486081','A','9999999999',0,0,0,0,'1999-07-01','2016-04-08','0000-00-00',''),(4,6,1,'AAA','BBB','MMMM','NNNN','','11111111111','A','22222222222',0,0,0,0,'2006-01-05','2016-04-05','0000-00-00',''),(5,7,53,'ESHANT SINGH ','RAJESH KUMAR SINGH ','INDRA NAGER ','DEORIA ','','9450681117','A','9473620727',0,0,0,0,'2009-11-18','2016-04-11','0000-00-00',''),(6,8,2,'PRINCE KUMAR YADAV','LATE SHESHNATH YADAV','KAILASHPURI LANE 3 ','DEORIA','','9125195538','A','',0,0,0,0,'2009-05-05','2016-04-06','0000-00-00',''),(7,9,51,'ARADHYA YADAV ','SRIKESH RAWAT ','ARCS NAGER ','DEORIA','','9889769267','A','',0,0,0,0,'2012-12-12','2016-04-12','0000-00-00',''),(8,10,2,'PRINCY MISHRA','SRI BALWANT MISHTRA','INDRA NAGHER','DEORIA','','9532312105','A','8600949256',0,0,0,0,'2008-03-15','2016-04-05','0000-00-00',''),(9,11,53,'SHRUTI CHAUHAN','SANHEEV CHAUHAN','UMA NAGAR WARD 15','DEORIA','','8808180755','A','8858041037',0,0,0,0,'2008-03-15','2016-04-05','0000-00-00',''),(10,12,53,'SHWETA CHAUHAN','SANJEEV KUMAR','UMA NAGER ','DEORIA','','8808180755','A','',0,0,0,0,'2011-04-20','2011-11-14','0000-00-00',''),(11,13,52,'SACHIN MADDESHIYA','MR RAKESH MADDESHIYA',' KAILASH PURI LANE 3','','','8931876660','A','7068390606',0,0,0,0,'2009-09-15','2016-04-06','0000-00-00',''),(12,14,51,'SACHIN MADDESIA','SHRI RAKESH MADDESIA','KAILASHPURI LANE 3','DEORIA','','7068390606','A','8931876660',0,0,0,0,'2009-09-15','2016-04-07','0000-00-00','NURSERY'),(13,15,51,'MRITUNJAY SINGH','SHRI UPENDRA KUMAR SINGH','KAILASH PURI LANE 2','CC ROAD DEORIA','','7388837505','A','8127848859',0,0,0,0,'2013-03-08','2016-04-01','0000-00-00',''),(14,17,51,'DIBYANSH GUPTA','SHRI RANJAN KUMAR GUPTA','PLOT-589 BHUJOULI','CALONY DEORIA','','9792434345','A','9792434345',0,0,0,0,'2012-12-16','2016-04-01','0000-00-00',''),(15,18,51,'MOHD.ASIF ALI KHAN','SHRI KAMARUZZAMA KHAN','ABUBAKAR NAGAR','GKP ROAD DEORIA','','8416980042','A','8416980042',0,0,0,0,'2013-02-24','2016-04-01','0000-00-00',''),(16,19,51,'ANANYA PANDEY','SHRI AJAY KUMAR PANDEY','BHUJOULI RD WARD NO',' 13/410 DEORIA ','','9415359890','A','8562959926',0,0,0,0,'2012-04-06','2016-04-01','0000-00-00','NURSERY'),(17,20,51,'ARADHYA MANI','SHRI AJAY MANI','INDRANAGAR','DEORIA','','9532697103','A','8005302729',0,0,0,0,'2012-08-28','2015-07-06','0000-00-00','NURSERY'),(18,21,51,'NAMAN KUMAR YADAVA','SHRI SANTOSH KUMAR YADAVA','INDRANAGAR SUGARMILL','DEORIA','','9125216992','A','8381913570',0,0,0,0,'2012-08-28','2015-07-01','0000-00-00','NURSERY'),(19,22,51,'ATHRAV KUMAR SHAH','SHRI VISHAL KUMAR SHAH','MP  BHULOULI CLNY','DEORIA','','8004788451','A','8765074442',0,0,0,0,'2012-12-12','2015-07-01','0000-00-00','NURSERY'),(20,23,53,'ALEEZA','MOHD.ARIF','ALINAGAR,NR KARBLA','DEORIA','','8858677218','A','9793727516',0,0,0,0,'2011-06-22','2015-07-06','0000-00-00',''),(21,24,51,'ANKUR MAURYA','SHRI PRADEEP MAURYA','KAILASHPURI LANE 3','DEORIA','','9455074642','A','8004639027',0,0,0,0,'2013-01-16','2015-04-01','0000-00-00','NURSERY'),(22,25,51,'ANUP KUMAR RAI','SHRI ARVIND KUMAR RAI','KAILASHPURI LANE 4','DEORIA','','8382806705','A','8382806705',0,0,0,0,'2012-03-23','2015-04-01','0000-00-00','NURSERY'),(23,29,52,'SHREYA CHAURASIA ','SHRI SANTOSH KUMAR','8/549 INDRANAGAR','DEORIA','','9453452859','A','9125476761',0,0,0,0,'2011-01-23','2014-04-01','0000-00-00',''),(24,30,52,'SIDDHI YADAV','SHRI SANDEEP YADAV','INDRANAGAR','DEORIA','','9648318084','A','9648318084',0,0,0,0,'2012-09-15','2014-04-01','0000-00-00',''),(25,31,53,'MUDDASIR KAMRUZZMA KHAN','SHRI KAMARUZZMA KHAN','25/369 ABUBAKAR NGR','DEORIA','','9838576920','A','8416980042',0,0,0,0,'2012-09-15','2013-04-01','0000-00-00','DOB CHEK'),(26,32,51,'KABYA TRIPATHI','AJAY RAJ TRIPATHI','UMANAGAR','DEORIA','','8948844694','A','9450672489',0,0,0,0,'2016-10-25','2016-10-20','0000-00-00',''),(27,33,51,'AARADHYA SINGH','AMIT SINGH','KAILASHPURI LANE NO ','CC ROAD','','8115997869','A','9452303820',0,0,0,0,'2012-04-02','2016-08-01','0000-00-00',''),(28,34,51,'REDHIMA RAO','RAM SINGH RAO','INDRANAGAR','DEORIA','','7081253554','A','9554827393',0,0,0,0,'2013-05-04','2016-08-01','0000-00-00',''),(29,35,51,'MAHI MISHRA','PANKAJ MISHRA','KAILASHPURI LANE 3','CC ROAD DEORIA','','9169536004','A','9169536007',0,0,0,0,'2013-07-13','2016-07-13','0000-00-00',''),(30,36,1,'ESHANT SINGH','RAJESH KUMAR SINGH','5/446 INDRANAGAR','DEORIA','','9450681117','A','9473620727',0,0,0,0,'2009-11-18','2016-07-30','0000-00-00',''),(31,37,3,'PRINCE KUMAR YADAV','LATE SHESH NATH YADAV','KAILASHPURI LANE 3','CC ROAD DEORIA','','9559488372','A','8127083874',0,0,0,0,'2007-11-18','2016-04-26','0000-00-00',''),(32,38,2,'PRINCY MISHRA','SRI BALWANT MISHRA','INDRANAGAR','DEORIA','','9532312105','A','8600949256',0,0,0,0,'2008-03-15','2016-04-07','0000-00-00',''),(33,39,53,'SHRUTI CHAUHAN','SANJEEV CHAUHAN','15/234UMANAGAR','NR SSM DEORIA','','8808180755','A','',0,0,0,0,'2011-01-14','2016-04-05','0000-00-00','8858041037'),(34,40,53,'SHEWTA CHAUHAN','SANJEEV CHAUHAN','15/234UMANAGAR','SSM DEORIA','','8808180755','A','',0,0,0,0,'2011-01-14','2016-04-05','0000-00-00','8858041037'),(35,41,52,'SACHIN MADDESHIA','RAKESH MADDESHIA','KAILASHPURI LANE 3','DEORIA','','9451416022','A','7068390606',0,0,0,0,'2009-09-15','2016-04-05','0000-00-00',''),(36,42,51,'MRITUNJAY SINGH','UPENDRA KUMAR SINGH','INDRANAGAR','DEORIA','','8127848859','A','7388837505',0,0,0,0,'2013-03-08','2016-04-02','0000-00-00',''),(37,43,51,'ANSH KUMAR MADHESIA','PANKAJ KUMAR MADHESIA','INDRANAGAR','DEORIA','','9026435304','A','7786945410',0,0,0,0,'2012-10-23','2016-04-03','0000-00-00',''),(38,44,51,'DIBYANSH GUPTA','RANJAN KUMAR GUPTA','PLOT NO 589','BHUJOULI DEORIA','','9792434345','A','9792434345',0,0,0,0,'2012-12-16','2016-04-01','0000-00-00',''),(39,45,51,'MD.ASIF ALI KHAN','KAMRUZZAMA KHAN','ABUBAKAR NAGAR','DEORIA','','8416980042','A','9838576920',0,0,0,0,'2013-02-24','2016-04-01','0000-00-00',''),(40,46,51,'ANANYA PANDEY','AJAY KUMAR PANDEY','13/410BHUJOULI RD','DEORIA','','9415359890','A','8562959926',0,0,0,0,'2013-02-24','2015-04-07','0000-00-00','NURSERY'),(41,47,51,'AARADHYA MANI','AJAY MANI','INDIRA NAGAR','DEORIA','','9532697103','A','8005302729',0,0,0,0,'2012-08-28','2015-04-07','0000-00-00','NURSERY'),(42,49,2,'PARTH TIWARI','ALOK TIWARI','INDRANAGAR','DEORIA','','9455078800','A','',0,0,0,0,'2008-10-09','2012-04-02','0000-00-00',''),(43,50,1,'TEST STUDENT 1ST CLASS','TEST FATHER 1ST CLASS','TTT','TTT','','33333333333','A','44444444444',0,3,10,1,'2017-01-12','2017-01-12','0000-00-00',''),(44,51,5,'ANTRA GUPTA ','SUNIL  GUPTA','RAM GULAM TOLA','DEORIA','me.abhi.deo.18@gmail.com','13344456455','A','95843958439',0,0,0,0,'2006-07-08','2017-01-15','0000-00-00',''),(45,53,5,'KOMAL CHAND ','JGHJGIJHIYHI','JGJHHK','JHH','','77657686589','A','',0,0,0,0,'2017-01-15','2017-01-15','0000-00-00',''),(46,54,1,'TEST STU 2','TEST FAT2','TT22','TT222','','22222222222','A','22222222222',0,1,5,1,'2017-01-17','2017-01-17','0000-00-00',''),(47,56,5,'NAITIK SRIVASTAV ','MAYANK SRIVASTAV','DEORIA','DEORIA ','','12345890888','A','1234567890',0,3,20,1,'2006-01-17','2017-01-27','0000-00-00','');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stureg`
--

DROP TABLE IF EXISTS `stureg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stureg` (
  `sturegID` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` int(11) NOT NULL DEFAULT '0',
  `daytime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `iddate` varchar(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sturegID`),
  UNIQUE KEY `iddate` (`iddate`),
  KEY `sturegindex` (`studentID`,`daytime`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stureg`
--

LOCK TABLES `stureg` WRITE;
/*!40000 ALTER TABLE `stureg` DISABLE KEYS */;
INSERT INTO `stureg` VALUES (1,46,'2017-01-25 04:43:01','4620170125'),(2,30,'2017-01-25 04:43:01','3020170125'),(3,4,'2017-01-25 04:43:01','420170125'),(4,43,'2017-01-25 04:43:01','4320170125'),(5,46,'2017-01-26 06:23:29','4620170126'),(6,32,'2017-01-26 06:23:29','3220170126'),(7,43,'2017-01-26 06:23:29','4320170126'),(9,42,'2017-01-26 15:07:14','4220170126'),(10,4,'2017-01-27 13:04:18','420170127'),(11,47,'2017-01-27 13:06:48','4720170127'),(12,45,'2017-01-27 13:06:48','4520170127');
/*!40000 ALTER TABLE `stureg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `transactionID` int(11) NOT NULL AUTO_INCREMENT,
  `ledgerID` int(11) NOT NULL DEFAULT '0',
  `classID` smallint(2) NOT NULL DEFAULT '0',
  `fee0` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee1` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee2` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee3` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee4` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee5` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee6` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee7` decimal(8,2) NOT NULL DEFAULT '0.00',
  `fee8` decimal(8,2) NOT NULL DEFAULT '0.00',
  `date` date NOT NULL DEFAULT '0000-00-00',
  `fyear` smallint(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`transactionID`,`fyear`),
  KEY `transactionID` (`transactionID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1
/*!50500 PARTITION BY RANGE  COLUMNS(fyear)
(PARTITION fy1 VALUES LESS THAN (1) ENGINE = InnoDB) */;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,3,3,0.00,1000.00,0.00,100.00,0.00,0.00,0.00,0.00,0.00,'2016-06-16',0),(2,7,53,0.00,700.00,0.00,0.00,0.00,300.00,0.00,0.00,0.00,'2016-07-06',0),(3,38,2,0.00,800.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,'2016-10-27',0),(4,50,1,1000.00,200.00,0.00,0.00,0.00,600.00,0.00,0.00,0.00,'2016-09-12',0),(5,50,1,0.00,800.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,'2017-01-19',0),(6,54,1,0.00,800.00,0.00,100.00,0.00,450.00,0.00,0.00,0.00,'2017-01-27',0),(7,56,5,8000.00,200.00,0.00,5.00,0.00,1000.00,0.00,0.00,0.00,'2017-01-27',0);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-27 19:21:54