SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `acce`
-- ----------------------------
DROP TABLE IF EXISTS `acce`;
CREATE TABLE `acce` (
  `pid` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `x` int(1) NOT NULL,
  `y` int(1) NOT NULL,
  `item_vnum` int(11) NOT NULL,
  `item_uid` int(11) NOT NULL,
  `item_count` smallint(3) NOT NULL,
  `item_abs_chance` smallint(3) NOT NULL,
  `success` varbinary(3) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_cs ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of acce
-- ----------------------------
