/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : player

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2016-11-14 17:55:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `item`
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) unsigned NOT NULL DEFAULT '0',
  `window` enum('INVENTORY','EQUIPMENT','SAFEBOX','MALL','DRAGON_SOUL_INVENTORY','PRIVATE_SHOP','SAFEBOX_EXTRA','BELT_INVENTORY') NOT NULL DEFAULT 'INVENTORY',
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
  PRIMARY KEY (`id`),
  KEY `owner_id_idx` (`owner_id`),
  KEY `item_vnum_index` (`vnum`)
) ENGINE=MyISAM AUTO_INCREMENT=30000705 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of item
-- ----------------------------