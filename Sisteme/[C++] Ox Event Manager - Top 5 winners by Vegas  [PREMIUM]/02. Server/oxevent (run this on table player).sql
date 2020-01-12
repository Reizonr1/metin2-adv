SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `oxevent`
-- ----------------------------
DROP TABLE IF EXISTS `oxevent`;
CREATE TABLE `oxevent` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(24) COLLATE latin1_german1_ci NOT NULL,
  `level` int(11) unsigned NOT NULL,
  `guild` varchar(16) COLLATE latin1_german1_ci DEFAULT NULL,
  `empire` int(11) NOT NULL,
  `job` tinyint(2) NOT NULL,
  `date` datetime NOT NULL,
  `correct_answers` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_german1_ci;

-- ----------------------------
-- Records of oxevent
-- ----------------------------
