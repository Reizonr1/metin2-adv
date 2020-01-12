ALTER TABLE `player`
ADD COLUMN `t_choosed`  int(11) NOT NULL DEFAULT 0 AFTER `language`,
ADD COLUMN `t_available`  varbinary(201) NOT NULL DEFAULT "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0," AFTER `t_choosed`;
