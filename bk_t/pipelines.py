# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bk_t import settings
import pymysql

class BkTPipeline:

    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.save_item(item)
        self.save_shop(item)
        return item


    def save_shop(self, item):

        self.cursor.execute(
            "insert into bk_shop_iter (shop_id, city, province, is_brand_seller, is_shop_closed, delivery_time, first_upload_product_at, is_shop_inactive, last_appear_at, last_order_schedule, shop_level, shop_name, shop_premium_level, is_shop_premium_top_seller, recent_rejection_transaction, rejected_count, negative_reviews, positive_reviews, sla_type, sla_value, subscribers_amount, shop_url, scraper_datetime) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (   item['shop_id'],
                item['city'],
                item['province'],
                item['is_brand_seller'],
                item['is_shop_closed'],
                item['delivery_time'],
                #item['shop_description'],
                item['first_upload_product_at'],
                item['is_shop_inactive'],
                item['last_appear_at'],
                item['last_order_schedule'],
                item['shop_level'],
                item['shop_name'],
                item['shop_premium_level'],
                item['is_shop_premium_top_seller'],
                item['recent_rejection_transaction'],
                item['rejected_count'],
                item['negative_reviews'],
                item['positive_reviews'],
                item['sla_type'],
                item['sla_value'],
                item['subscribers_amount'],
                #item['term_and_condition'],
                item['shop_url'],
                item['scraper_datetime'],

                 ))
        self.connect.commit()


    def save_item(self, item):
        self.cursor.execute(
            "insert into bk_item_iter (idd, sku_id, shop_id, item_name, category, subCategory, subSubCategory, id_category, url_category, couriers, created_at, deal_applied_date, deal_discount_price, deal_expired_date, deal_original_price, deal_percentage, description, is_digital_product, is_for_sale, max_quantity, merchant_return_insurance, min_quantity, rating, rating_user_count, rating_relisted_at, rating_is_rush_delivery, shipping_force_insurance, stats_interest_count, stats_sold_count, stats_view_count, stats_waiting_payment_count, stock, updated_at, url_product, warranty_cheapest, product_weight, without_shipping, scraper_datetime) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (   item['idd'],
                item['sku_id'],
                item['shop_id'],
                item['item_name'],
                item['category'],
                item['subCategory'],
                item['subSubCategory'],
                item['id_category'],
                item['url_category'],
                item['couriers'],
                item['created_at'],
                item['deal_applied_date'],
                item['deal_discount_price'],
                item['deal_expired_date'],
                item['deal_original_price'],
                item['deal_percentage'],
                item['description'],
                item['is_digital_product'],
                item['is_for_sale'],
                item['max_quantity'],
                item['merchant_return_insurance'],
                item['min_quantity'],
                item['rating'],
                item['rating_user_count'],
                item['rating_relisted_at'],
                item['rating_is_rush_delivery'],
                item['shipping_force_insurance'],
                item['stats_interest_count'],
                item['stats_sold_count'],
                item['stats_view_count'],
                item['stats_waiting_payment_count'],
                item['stock'],
                item['updated_at'],
                item['url_product'],
                item['warranty_cheapest'],
                item['product_weight'],
                item['without_shipping'],
                item['scraper_datetime']
                 ))
        self.connect.commit()


