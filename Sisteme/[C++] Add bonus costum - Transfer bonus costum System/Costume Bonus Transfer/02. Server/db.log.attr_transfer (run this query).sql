SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `attr_transfer`
-- ----------------------------
DROP TABLE IF EXISTS `attr_transfer`;
CREATE TABLE `attr_transfer` (
  `pid` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `x` int(1) NOT NULL,
  `y` int(1) NOT NULL,
  `item_vnum` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_cs ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of attr_transfer
-- ----------------------------
