SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `hwid_list`;
CREATE TABLE `hwid_list` (
  `login` varchar(30) DEFAULT NULL,
  `hwid` varchar(255) NOT NULL DEFAULT '',
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`hwid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
