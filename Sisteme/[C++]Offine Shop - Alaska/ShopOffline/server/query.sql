
DROP TABLE IF EXISTS `player_shop`;
CREATE TABLE `player_shop` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `player_id` int(255) NOT NULL,
  `shop_vid` int(255) NOT NULL,
  `item_count` int(3) NOT NULL DEFAULT '0',
  `name` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  `status` enum('OK','CLOSED') COLLATE utf8_polish_ci NOT NULL DEFAULT 'OK',
  `map_index` int(20) NOT NULL DEFAULT '0',
  `x` int(30) NOT NULL DEFAULT '0',
  `y` int(30) NOT NULL DEFAULT '0',
  `z` int(30) NOT NULL,
  `date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `date_close` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ip` varchar(255) COLLATE utf8_polish_ci NOT NULL DEFAULT '0.0.0.0',
  `gold` varchar(255) COLLATE utf8_polish_ci NOT NULL DEFAULT '0',
  `cash` int(255) NOT NULL DEFAULT '0',
  `channel` int(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`,`shop_vid`)
) ENGINE=MyISAM;

DROP TABLE IF EXISTS `shop_cost`;
CREATE TABLE `shop_cost` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `time` int(255) NOT NULL DEFAULT '0',
  `time_type` enum('day','hour','normal_shop') NOT NULL DEFAULT 'day',
  `cost` int(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12;

-- ----------------------------
-- Records of shop_cost
-- ----------------------------
INSERT INTO `shop_cost` VALUES ('5', '0', 'normal_shop', '5000000');
INSERT INTO `shop_cost` VALUES ('6', '1', 'hour', '100000');
INSERT INTO `shop_cost` VALUES ('7', '2', 'hour', '500000');
INSERT INTO `shop_cost` VALUES ('8', '3', 'hour', '1000000');
INSERT INTO `shop_cost` VALUES ('9', '1', 'day', '1500000');
INSERT INTO `shop_cost` VALUES ('10', '2', 'day', '2000000');
INSERT INTO `shop_cost` VALUES ('11', '3', 'day', '2500000');


DROP TABLE IF EXISTS `shop_limit`;
CREATE TABLE `shop_limit` (
  `channel` int(2) DEFAULT NULL,
  `map_index` int(11) DEFAULT NULL,
  `shop_limit` varchar(255) DEFAULT NULL
) ENGINE=MyISAM;

DROP TABLE IF EXISTS `player_gift`;
CREATE TABLE `player_gift` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `owner_id` int(255) NOT NULL,
  `date_add` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `date_get` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `status` enum('WAIT','OK') COLLATE utf8_polish_ci NOT NULL DEFAULT 'WAIT',
  `from` varchar(255) COLLATE utf8_polish_ci NOT NULL DEFAULT '0',
  `reason` text COLLATE utf8_polish_ci NOT NULL,
  `vnum` int(255) NOT NULL DEFAULT '0',
  `count` bigint(255) NOT NULL DEFAULT '1',
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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM;
ALTER TABLE `player_gift` ADD UNIQUE `id` (`id`);

-- ----------------------------
-- Table structure for player_shop_items
-- ----------------------------
DROP TABLE IF EXISTS `player_shop_items`;
CREATE TABLE `player_shop_items` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `shop_id` int(255) NOT NULL,
  `player_id` int(255) NOT NULL DEFAULT '0',
  `vnum` int(255) NOT NULL DEFAULT '0',
  `count` int(20) NOT NULL DEFAULT '1',
  `pos` int(20) NOT NULL DEFAULT '0',
  `display_pos` int(20) NOT NULL DEFAULT '0',
  `price` bigint(255) NOT NULL DEFAULT '0',
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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM;
