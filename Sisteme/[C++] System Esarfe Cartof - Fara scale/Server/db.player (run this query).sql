ALTER TABLE `player`
ADD COLUMN `part_acce`  smallint(4) UNSIGNED NOT NULL DEFAULT 0 AFTER `part_hair`;

ALTER TABLE `player_deleted`
ADD COLUMN `part_acce`  smallint(4) UNSIGNED NOT NULL DEFAULT 0 AFTER `part_hair`;

ALTER TABLE `item`
ADD COLUMN `applytype0`  tinyint(4) NOT NULL DEFAULT 0 AFTER `attrvalue6`,
ADD COLUMN `applyvalue0`  smallint(6) NOT NULL DEFAULT 0 AFTER `applytype0`,
ADD COLUMN `applytype1`  tinyint(4) NOT NULL DEFAULT 0 AFTER `applyvalue0`,
ADD COLUMN `applyvalue1`  smallint(6) NOT NULL DEFAULT 0 AFTER `applytype1`,
ADD COLUMN `applytype2`  tinyint(4) NOT NULL DEFAULT 0 AFTER `applyvalue1`,
ADD COLUMN `applyvalue2`  smallint(6) NOT NULL DEFAULT 0 AFTER `applytype2`,
ADD COLUMN `applytype3`  int(11) NOT NULL DEFAULT 0 AFTER `applyvalue2`,
ADD COLUMN `applyvalue3`  int(11) NOT NULL DEFAULT 0 AFTER `applytype3`,
ADD COLUMN `applytype4`  int(11) NOT NULL DEFAULT 0 AFTER `applyvalue3`,
ADD COLUMN `applyvalue4`  int(11) NOT NULL DEFAULT 0 AFTER `applytype4`,
ADD COLUMN `applytype5`  int(11) NOT NULL DEFAULT 0 AFTER `applyvalue4`,
ADD COLUMN `applyvalue5`  int(11) NOT NULL DEFAULT 0 AFTER `applytype5`,
ADD COLUMN `applytype6`  int(11) NOT NULL DEFAULT 0 AFTER `applyvalue5`,
ADD COLUMN `applyvalue6`  int(11) NOT NULL DEFAULT 0 AFTER `applytype6`,
ADD COLUMN `applytype7`  int(11) NOT NULL DEFAULT 0 AFTER `applyvalue6`,
ADD COLUMN `applyvalue7`  int(11) NOT NULL DEFAULT 0 AFTER `applytype7`;