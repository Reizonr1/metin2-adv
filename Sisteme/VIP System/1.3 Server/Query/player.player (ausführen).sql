ALTER TABLE `player`
ADD COLUMN `vip`  int(11) UNSIGNED NOT NULL DEFAULT 0 AFTER `alignment`;
ALTER TABLE `player_deleted`
ADD COLUMN `vip`  int(11) UNSIGNED NOT NULL DEFAULT 0 AFTER `alignment`;
