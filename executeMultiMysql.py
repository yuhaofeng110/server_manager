#!/usr/bin/python3.6

import pymysql
import yaml
import multiprocessing


class execMysql:
	def __init__(self):
		f = open('./mysql.yaml',encoding = 'utf-8')
		self.config = yaml.load(f)
	
	def executeOne(self, config, project):
		db = pymysql.connect(project[1], project[2], project[3], project[2], charset='utf8')
		cursor = db.cursor(pymysql.cursors.DictCursor)
		sql = """
		
DROP TABLE IF EXISTS `t_deny_list`;
CREATE TABLE `t_deny_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(512) NOT NULL DEFAULT '',
  `title` varchar(512) NOT NULL DEFAULT '',
  `desc` varchar(512) NOT NULL DEFAULT '',
  `is_active` int(11) NOT NULL DEFAULT '1' COMMENT 'default 1 active 0 inactive',
  `sweet_reason` varchar(512) NOT NULL DEFAULT '',
  `deny_type` int(11) NOT NULL DEFAULT '1' COMMENT 'default 0    1 mobile 2 id 3 cs',
  `insert_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `update_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

INSERT INTO `t_deny_list` VALUES ('1', 'Duplicate registration of ID card', 'Duplicate registration of ID card', 'Duplicate registration of ID card', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('2', 'User is deny because not E-KTP', 'The ID Card is not E-KTP', 'User is deny because not E-KTP', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('3', 'Address book is less than 20', 'Address book is less than 20', 'Address book is less than 20', '1', 'Sorry, your data does not comply with our terms', '1', '2018-01-31 13:57:47', '2018-02-01 15:13:16');
INSERT INTO `t_deny_list` VALUES ('4', 'Deafult Reason(old user)', 'Deafult Reason', 'Deafult Reason(old user)', '1', 'Sorry, your data does not comply with our terms', '0', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('5', 'User is deny because the id card is not on listed location', 'ID card not in listed location', 'User is deny because the id card is not on listed location', '1', 'We are not available on your area sorry for the incovenance', '2', '2018-01-31 13:57:35', '2018-01-31 13:57:39');
INSERT INTO `t_deny_list` VALUES ('6', 'User is deny because the SMS contents bill more than 7 days either from bank, other financial applications, etc. Personal conflicts related to user\'s finance', 'SMS data refused', 'User is deny because the SMS contents bill more than 7 days either from bank, other financial applications, etc. Personal conflicts related to user\'s finance', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:42', '2018-01-31 13:57:45');
INSERT INTO `t_deny_list` VALUES ('7', 'User is deny because the SMS, APP, Customer Phone call data empty', 'SMS, APP, Customer phone call refused', 'User is deny because the SMS, APP, Customer Phone call data empty', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('8', 'User is deny because someone else on the third photo', 'Auto Collection failed', 'User is deny because someone else on the third photo', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('9', 'User is deny because the photo in ID card is different with people who hold the ID card', 'Face recognize failed', 'User is deny because the photo in ID card is different with people who hold the ID card', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('10', 'User is deny because photo in the ID card can not be recognize', 'ID Card recognize failed', 'User is deny because photo in the ID card can not be recognize', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('11', 'User is deny because the age below 21 year old', 'Age rule refused', 'User is deny because the age below 21 year old', '0', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-02-01 02:47:35');
INSERT INTO `t_deny_list` VALUES ('12', 'User is deny because loan app installed more than 10 app', 'Loan app installed too much', 'User is deny because loan app installed more than 10 app', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-02-01 15:12:24');
INSERT INTO `t_deny_list` VALUES ('13', 'User is deny because the emergency contacs are invalid numbers', 'Emergency contact denied', 'User is deny because the emergency contacs are invalid numbers', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-02-01 15:12:33');
INSERT INTO `t_deny_list` VALUES ('14', 'User\'s contact denied because number in the contact has bad loan', 'Contact relation denied', 'User\'s contact denied because number in the contact has bad loan', '1', 'Sorry, your data does not comply with our terms', '2', '2018-01-31 13:57:47', '2018-02-01 15:35:15');
INSERT INTO `t_deny_list` VALUES ('15', 'User don\'t wear shirt: Let the user resubmit', 'Photos are not compliant', 'User don\'t wear shirt: Let the user resubmit', '1', 'Photos are not compliant, please resubmit', '2', '2018-01-31 13:57:47', '2018-02-01 15:34:40');
INSERT INTO `t_deny_list` VALUES ('16', 'User is deny because the user fail to answer the phone', 'Phone cannot connect', 'User is deny because the user fail to answer the phone', '1', 'Sorry we are unable to confirm your informations', '3', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('17', 'User is denied because the money use is not on list', 'Money usage for play', 'User is denied because the money use is not on list', '1', 'Sorry, you are not eligible to make loan on our platform', '3', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('18', 'User is denied because she is a housewife and have no stable income', 'If the applicant is housewife', 'User is denied because she is a housewife and have no stable income', '1', 'Sorry, you are not eligible to make loan on our platform', '3', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('19', 'User is denied because he/she no longer have work and have no certain occupation', 'If the applicant have no work or already resign from the office', 'User is denied because he/she no longer have work and have no certain occupation', '1', 'Sorry, you are not eligible to make loan on our platform', '3', '2018-01-31 13:57:47', '2018-01-31 13:57:47');
INSERT INTO `t_deny_list` VALUES ('20', 'Point too low', 'Point too low', 'Point too low', '1', 'Sorry, your data does not comply with our terms', '4', '2018-01-31 13:57:47', '2018-01-31 13:57:47');


ALTER TABLE `t_customer_certify`
MODIFY COLUMN `audit_remark`  varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '审核失败备注' ;
		
"""
		res = cursor.execute(sql)
		result = cursor.fetchall()
		db.commit()
		cursor.close()
		db.close()
		print("<<< %s 影响行数: %s " %(project[0], res) )
		print(result)
		print("\n")
	
	def execute(self):
		for project in self.config['projects']:
			my_process = multiprocessing.Process(target=self.executeOne, args=(self.config, project,))
			my_process.start()
			my_process.join()
		print("\n*************  all cmd finished ***************")


if __name__ == '__main__':
	exec = execMysql()
	exec.execute()
