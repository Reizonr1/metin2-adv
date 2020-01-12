SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for achievementshop_items
-- ----------------------------
DROP TABLE IF EXISTS `achievementshop_items`;
CREATE TABLE `achievementshop_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` int(11) NOT NULL,
  `vnum` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
