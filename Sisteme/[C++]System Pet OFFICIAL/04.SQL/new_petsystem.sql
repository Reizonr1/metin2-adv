/*
Navicat MySQL Data Transfer

Source Server         : Server
Source Server Version : 50538
Source Host           : 188.212.103.152:3306
Source Database       : player

Target Server Type    : MYSQL
Target Server Version : 50538
File Encoding         : 65001

Date: 2016-03-04 19:28:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for new_petsystem
-- ----------------------------
DROP TABLE IF EXISTS `new_petsystem`;
CREATE TABLE `new_petsystem` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL DEFAULT '1',
  `evolution` int(11) NOT NULL DEFAULT '1',
  `exp` int(11) NOT NULL DEFAULT '0',
  `expi` int(11) NOT NULL DEFAULT '0',
  `bonus0` int(11) NOT NULL DEFAULT '0',
  `bonus1` int(11) NOT NULL DEFAULT '0',
  `bonus2` int(11) NOT NULL DEFAULT '0',
  `skill0` int(11) NOT NULL DEFAULT '-1',
  `skill0lv` int(11) NOT NULL DEFAULT '0',
  `skill1` int(11) NOT NULL DEFAULT '-1',
  `skill1lv` int(11) NOT NULL DEFAULT '0',
  `skill2` int(11) NOT NULL DEFAULT '-1',
  `skill2lv` int(11) NOT NULL DEFAULT '0',
  `duration` int(11) NOT NULL DEFAULT '0',
  `tduration` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of new_petsystem
-- ----------------------------
