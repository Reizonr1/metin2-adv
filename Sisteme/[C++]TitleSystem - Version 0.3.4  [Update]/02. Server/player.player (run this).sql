/*
Navicat MySQL Data Transfer

Source Server         : Vegas Development Database
Source Server Version : 50617
Source Host           : localhost:3306
Source Database       : player

Target Server Type    : MYSQL
Target Server Version : 50017
File Encoding         : 65005

Date: 2016-22-04 17:00:58
*/
ALTER TABLE `player`
ADD COLUMN `prestige`  smallint(4) UNSIGNED NOT NULL DEFAULT 0 AFTER `alignment`;

ALTER TABLE `player_deleted`
ADD COLUMN `prestige`  smallint(4) UNSIGNED NOT NULL DEFAULT 0 AFTER `alignment`;