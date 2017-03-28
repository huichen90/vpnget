# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class GetvpnPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='testdb')
        cur = conn.cursor()
        insert_sql = (
                "insert into vpn_info (vpn_ip, vpn_tcp_port, vpn_udp_port) "
            "values (%s,%s,%s);"
        )
        values = (item['ip'], item['tcp'], item['udp'])

        try:
            cur.execute(insert_sql, values)
        except Exception, e:
            print("insert faild: ", e)
            conn.rollback()
        else:
            conn.commit()
        cur.close()
        conn.close()

