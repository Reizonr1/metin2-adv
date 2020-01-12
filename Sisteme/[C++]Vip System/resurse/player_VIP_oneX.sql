/*
Navicat MySQL Data Transfer

Source Server         : Metin2WF
Source Server Version : 50630
Source Host           : 188.212.103.158:3306
Source Database       : player

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-09-06 19:16:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `player_VIP_oneX`
-- ----------------------------
DROP TABLE IF EXISTS `player_VIP_oneX`;
CREATE TABLE `player_VIP_oneX` (
  `PID_VIP` int(11) NOT NULL DEFAULT '0',
  `TIMP` int(20) NOT NULL DEFAULT '0',
  `FARA_TIMP` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`PID_VIP`),
  KEY `TIMP` (`TIMP`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of player_VIP_oneX
-- ----------------------------
