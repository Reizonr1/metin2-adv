
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for offline_shop_item
-- ----------------------------
DROP TABLE IF EXISTS `offline_shop_item`;
CREATE TABLE `offline_shop_item` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) unsigned NOT NULL DEFAULT '0',
  `pos` smallint(5) unsigned NOT NULL DEFAULT '0',
  `count` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `vnum` int(11) unsigned NOT NULL DEFAULT '0',
  `socket0` int(10) unsigned NOT NULL DEFAULT '0',
  `socket1` int(10) unsigned NOT NULL DEFAULT '0',
  `socket2` int(10) unsigned NOT NULL DEFAULT '0',
  `socket3` int(10) unsigned NOT NULL DEFAULT '0',
  `socket4` int(10) unsigned NOT NULL DEFAULT '0',
  `socket5` int(10) unsigned NOT NULL DEFAULT '0',
  `attrtype0` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue0` smallint(6) NOT NULL DEFAULT '0',
  `attrtype1` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue1` smallint(6) NOT NULL DEFAULT '0',
  `attrtype2` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue2` smallint(6) NOT NULL DEFAULT '0',
  `attrtype3` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue3` smallint(6) NOT NULL DEFAULT '0',
  `attrtype4` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue4` smallint(6) NOT NULL DEFAULT '0',
  `attrtype5` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue5` smallint(6) NOT NULL DEFAULT '0',
  `attrtype6` tinyint(4) NOT NULL DEFAULT '0',
  `attrvalue6` smallint(6) NOT NULL DEFAULT '0',
  `applytype0` tinyint(4) NOT NULL DEFAULT '0',
  `applyvalue0` smallint(6) NOT NULL DEFAULT '0',
  `applytype1` tinyint(4) NOT NULL DEFAULT '0',
  `applyvalue1` smallint(6) NOT NULL DEFAULT '0',
  `applytype2` tinyint(4) NOT NULL DEFAULT '0',
  `applyvalue2` smallint(6) NOT NULL DEFAULT '0',
  `applytype3` int(11) NOT NULL DEFAULT '0',
  `applyvalue3` int(11) NOT NULL DEFAULT '0',
  `applytype4` int(11) NOT NULL DEFAULT '0',
  `applyvalue4` int(11) NOT NULL DEFAULT '0',
  `applytype5` int(11) NOT NULL DEFAULT '0',
  `applyvalue5` int(11) NOT NULL DEFAULT '0',
  `applytype6` int(11) NOT NULL DEFAULT '0',
  `applyvalue6` int(11) NOT NULL DEFAULT '0',
  `applytype7` int(11) NOT NULL DEFAULT '0',
  `applyvalue7` int(11) NOT NULL DEFAULT '0',
  `price` int(11) NOT NULL DEFAULT '0',
  `status` smallint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `owner_id_idx` (`owner_id`),
  KEY `item_vnum_index` (`vnum`)
) ENGINE=MyISAM AUTO_INCREMENT=2430000326 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of offline_shop_item
-- ----------------------------

-- ----------------------------
-- Table structure for offline_shop_npc
-- ----------------------------
DROP TABLE IF EXISTS `offline_shop_npc`;
CREATE TABLE `offline_shop_npc` (
  `owner_id` int(11) NOT NULL DEFAULT '0',
  `sign` varchar(32) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `x` int(11) DEFAULT NULL,
  `y` int(11) DEFAULT NULL,
  `z` int(11) DEFAULT NULL,
  `mapIndex` int(11) DEFAULT NULL,
  `channel` int(2) DEFAULT NULL,
  PRIMARY KEY (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of offline_shop_npc
-- ----------------------------
