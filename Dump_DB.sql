-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: owners_mysql
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `feedbacks`
--

DROP TABLE IF EXISTS `feedbacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedbacks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `tel` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedbacks`
--

LOCK TABLES `feedbacks` WRITE;
/*!40000 ALTER TABLE `feedbacks` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedbacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `houses`
--

DROP TABLE IF EXISTS `houses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `houses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model` varchar(20) NOT NULL,
  `stead` int DEFAULT NULL,
  `square` float DEFAULT NULL,
  `price` int DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `houses`
--

LOCK TABLES `houses` WRITE;
/*!40000 ALTER TABLE `houses` DISABLE KEYS */;
INSERT INTO `houses` VALUES (1,'zx83',10,100.1,38000000,'Подойдет семейной паре с двумя детьми. В доме есть 3 спальни, 2 санузла, гостиная с кухней. Дом полностью меблирован. На участке также имеется навес под 1 автомобиль.'),(2,'zx149',12,128.3,45000000,'Подойдет семейной паре с двумя детьми. В доме есть 3 спальни, 2 санузла, гостиная с кухней. Дом полностью меблирован. На участке также имеется навес под 2 автомобиля.'),(3,'zx153',15,149.6,52000000,'Подойдет семейной паре с тремя детьми. В доме есть 4 спальни, 3 санузла, гостиная с кухней. Дом полностью меблирован. На участке также имеется навес под 2 автомобиля.'),(4,'zx101',20,159.3,60000000,'Подойдет семейной паре с тремя детьми. В доме есть 4 спальни, 4 санузла, гостиная с кухней. Дом полностью меблирован. На участке также имеется навес под 2 автомобиля.');
/*!40000 ALTER TABLE `houses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `content` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'2020-01-08 09:00:50','В поселке началось строительство первой очереди.'),(2,'2020-04-20 10:00:50','Закончены работы по подъездным путям и электрификации.'),(3,'2020-10-17 09:00:50','Закончены работы по газификации поселка.'),(4,'2021-02-12 12:00:50','Введены в эксплуатацию первые дома.'),(5,'2021-04-07 14:00:50','Первые жильцы получили ключи от своих домов. Поздравляем новосёлов!'),(6,'2021-10-01 09:40:50','Проводятся работы по озеленению поселка. Начата вторая очередь строительства.'),(7,'2022-03-10 09:30:50','Проводятся работы по прокладке оптоволоконного кабеля для высокоскоростной сети интернета.'),(8,'2022-05-01 08:00:50','01.06.2022г. состоится день открытых дверей. Все желающие смогут посетить поселок и получить ответы на все интересующие вопросы.'),(9,'2022-06-02 17:00:50','Состоялся день открытых дверей. Более 100 человек посетили поселок.  Многие из них скоро станут нашими соседями.'),(10,'2022-08-12 13:00:50','Открылся магазин на ул. Лесная.'),(11,'2022-09-01 16:53:50','Проводятся ремонтные работы на линии электропередачи. Свет в домах будет восстановлен в ближайшие часы.'),(12,'2022-12-07 10:00:50','Начата третья очередь строительства.');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `payment_id` varchar(100) DEFAULT NULL,
  `payment_summ` varchar(100) DEFAULT NULL,
  `status` tinyint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `payments_idx` (`user_id`),
  CONSTRAINT `payments` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,'2023-01-27 09:51:50','2c31334a-000f-5000-9000-12558db12f5d','200000',1,4),(2,'2023-03-27 09:57:02','2c2f854e-000f-5000-9000-17c18ee6743b','268400',1,4),(3,'2023-04-27 11:58:57','2c2f85c1-000f-5000-9000-156578374a1b','600085',1,4),(4,'2023-04-27 12:02:06','2c2f867e-000f-5000-a000-1a77e328f156','290000',1,4);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profiles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `tel` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `balance` int DEFAULT NULL,
  `account` varchar(45) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `profiles_idx` (`user_id`),
  CONSTRAINT `profiles` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
INSERT INTO `profiles` VALUES (2,'Иван Иванов','+7-901-000-0000','ivanov@riviera.ru','36',-225572,'4',4);
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service` (
  `id` int NOT NULL AUTO_INCREMENT,
  `service` varchar(50) DEFAULT NULL,
  `tariff` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
INSERT INTO `service` VALUES (1,'electro',420),(2,'gas',687),(3,'water',520),(4,'garbage',100000);
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texts`
--

DROP TABLE IF EXISTS `texts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `texts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(50) DEFAULT NULL,
  `label_content` varchar(50) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texts`
--

LOCK TABLES `texts` WRITE;
/*!40000 ALTER TABLE `texts` DISABLE KEYS */;
INSERT INTO `texts` VALUES (1,'houses','main','В поселке \"Ривьера\" Вы можете выбрать один из четырех проектов домов от архитектурной студии Z500. Каким он будет, небольшим (110,6 кв.м), уютным (128,3 кв.м), комфортным (149,6 кв.м) или же просторным (159,3 кв.м) - решать только Вам. На участке и в доме имеются все необходимые коммуникации для комфортного проживания. \nЕсли Вы хотите проживать в КП \"Ривьера\", то Вы можете оставить заявку и наш менеджер обязательно с Вами свяжется и ответит на интересующие вопросы. Вы сможете съездить в коттеджный поселок пообщаться с архитектором, посмотреть инфраструктуру, узнать о жизни в поселке, что позволит определиться и принять окончательное решение. На все дома уже подготовлены документы, поэтому процесс оформления не займёт много времени и будет выполнен специалистами быстро и грамотно.'),(2,'index','description','Поселок коттеджного типа \"Ривьера\" создан в едином архитектурном стиле \"минимализм\". На территории поселка, относящейся к землям ИЖС, расположились 220 домовладений от 110 до 160 кв. м, построенных из монолитного бетона с утеплением в 200 мм и оборудованных проточно-вытяжной вентиляцией, что позволяет комфортно себя чувствовать жильцам в любое время года. Площадь участков составляет от 10 до 20 соток. Ведется третья заключительная очередь строительства.'),(3,'index','location','Поселок находится в престижном Слободском районе, в 20 км от МКАД по Рижскому шоссе у берега реки Ивушка, в окружении соснового бора. Добраться до поселка можно как на личном транспорте, так и на маршрутных такси.'),(4,'index','infrastructure','В поселке имеются игровые площадки для детей, две спортивные площадки, сеть дорог для автомобилей и пешеходов, зоны отдыха, велодорожки, зоны выгула собак и магазин. Территория поселка полностью благоустроена и озеленена. Поселок круглосуточно находится под охраной. \"Ривьера\" идеально подойдет для семей с детьми, так как в 3 км от поселка находятся муниципальные детский сад и школа, а в 12 км - районная больница. Посёлок расположен в экологически чистом районе, поэтому Вы сможете постоянно дышать чистым и свежим воздухом, а также наслаждаться окружающей природной красотой.'),(5,'index','utility','Поселок обеспечен всеми коммуникациями городского типа: электроснабжение 15 кВт, магистральное газоснабжение 7 м3/ч, централизованное водоснабжение, ливневая и бытовая канализации, заведен в дома оптоволоконный кабель для скоростного интернета до 1 Гбит/с. Возле каждого домовладения установлен контейнер для бытовых отходов, вывоз мусора осуществляется на регулярной основе.');
/*!40000 ALTER TABLE `texts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(45) NOT NULL,
  `password` varchar(500) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_UNIQUE` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (4,'first','pbkdf2:sha256:600000$nZTJ8Ju64qV534Xf$c4e880730b5d07e07e81586970f7efb1883e71dc18f20cb83c5d2dac00926bed','2023-06-30 15:25:46');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilities`
--

DROP TABLE IF EXISTS `utilities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `value_electro` int DEFAULT NULL,
  `value_gas` int DEFAULT NULL,
  `value_water` int DEFAULT NULL,
  `summ` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `utilities_idx` (`user_id`),
  CONSTRAINT `utilities` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilities`
--

LOCK TABLES `utilities` WRITE;
/*!40000 ALTER TABLE `utilities` DISABLE KEYS */;
INSERT INTO `utilities` VALUES (1,'2022-11-27 11:09:45',0,0,0,0,4),(2,'2022-12-27 11:09:45',200,100,10,257900,4),(3,'2023-01-27 11:20:56',250,200,50,210500,4),(4,'2023-02-27 11:24:50',400,300,130,273300,4),(5,'2023-03-27 11:25:41',450,350,200,191750,4),(6,'2023-04-27 11:27:09',539,395,217,177135,4),(7,'2023-05-27 11:28:03',673,467,284,240584,4),(8,'2023-06-27 11:28:57',754,511,416,232888,4);
/*!40000 ALTER TABLE `utilities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-01 13:18:47
