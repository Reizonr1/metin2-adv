/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : player

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2016-11-12 14:26:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `offline_shop`
-- ----------------------------
DROP TABLE IF EXISTS `offline_shop`;
CREATE TABLE `offline_shop` (
  `pid` int(255) DEFAULT NULL,
  `x` int(255) DEFAULT NULL,
  `y` int(255) DEFAULT NULL,
  `map_index` int(255) DEFAULT NULL,
  `channel` int(255) DEFAULT NULL,
  `color` int(255) DEFAULT NULL,
  `size` int(2) DEFAULT NULL,
  `duration` int(255) DEFAULT NULL,
  `installtime` int(11) DEFAULT NULL,
  `gold` bigint(255) DEFAULT NULL,
  `sign` text,
  `item` text CHARACTER SET latin1 COLLATE latin1_bin,
  `price` text,
  `price2` text,
  `price3` text,
  `price4` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of offline_shop
-- ----------------------------
