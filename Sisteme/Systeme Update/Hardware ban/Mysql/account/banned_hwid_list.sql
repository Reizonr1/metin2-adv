SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `banned_hwid_list`;
CREATE TABLE `banned_hwid_list` (
  `hwid` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
