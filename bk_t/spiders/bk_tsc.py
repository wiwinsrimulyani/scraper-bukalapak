import logging
import scrapy
import requests
import json
from bk_t.items import BkTItem
from datetime import datetime

class BkTscSpider(scrapy.Spider):
    name = 'bk_tsc'
    allowed_domains = ['api.bukalapak.com']
    start_urls = ['http://www.bukalapak.com/']

    url = "https://www.bukalapak.com/westeros_auth_proxies"
    handle_httpstatus_list = [401, 502]
    payload = json.dumps({
    "application_id": 1,
    "authenticity_token": ""
    })

    headers = {
    'user-agent': 'my-cool-project (http://example.com)',
    'Content-Type': 'application/json',
    'Cookie': 'browser_id=686643c3a11700cefedfd2bc298bb960; identity=8b248d1761c5b6389d70a8aec76a6a7a; lskjfewjrh34ghj23brjh234=dUNEa0hRRUU5cEhxZ3p0VmlmOVlpdC9EMzdSUXVaSHRBMzNTRGpvY083QVZYM2Rzcnh0ZDRsMzB5Mm5FQzROREgveGhPWVRGNWlmTHBKV2FiUkVyK0E9PS0tZmlOS1JaWUhtbGxsRU5kYVp2TU9wZz09--7e8247865fff69945957ffc7578e22a422a411fd; session_id=acd39d7a78006870ff660632127867dc; __cf_bm=AiMyvNzlbNVdO9KQ3h3JG4KkQs2XV79WqWkwunYQ4RU-1643089396-0-ARVWlcDE/DJ30abbqYPtbMmP1kMuN+XC0ylqyCNBZQbXe1ORXwEEAZflo21GqO1F1fFIo4u5VUyUAOBn/jThWWU=; __cfruid=3aabb83091cabb29341adf9202cc4522394b836d-1643089396'
    }


    def __init__(self):
        #run time
        self.runtime = datetime.now()#.strftime('%Y-%m-%d')


    def parse(self, response):
        
        #offset start from 0, limit always 16
        start_url = 'https://api.bukalapak.com/stores/2795056/products?offset=0&limit=16&sort=bestselling&access_token=' + str(self.access_tkn())
        request = scrapy.Request(url = start_url, callback =self.parse_getData, meta = {'shop_id': 2795056, 'offset' :0, 'sku_id1': '0'})
        yield request

    def access_tkn(self):
        try:
            response = requests.request("POST", self.url, headers=self.headers, data=self.payload, verify=False)
            tmp_var = json.loads(response.text)
            acc_tkn = tmp_var.get('access_token')
            return acc_tkn
        except:
            self.access_tkn()

    def parse_getData(self, response):
        shop_id = response.request.meta['shop_id']
        offset = response.request.meta['offset']
        sku_id1 = response.request.meta['sku_id1']
        try:

            productList_text = response.text
            productj = json.loads(productList_text)
            productData = productj.get('data')
            item = BkTItem()
            try: 
                temp_sku_id = productData[len(productData)-1].get('sku_id')
            except:
                temp_sku_id = '1'

            if(shop_id <= 999999999):
                if(productData):
                    temp_bol = True
                else:
                    temp_bol = False
                if(temp_sku_id != sku_id1):
                    temp_bol1 = True
                else:
                    temp_bol1 = False
                if(temp_bol and temp_bol1):
                                      #do not need sku id, limit = 10000 products in shop
                    for prod in productData:
                        item['idd'] = prod.get('id')
                        item['sku_id'] = prod.get('sku_id')
                        item['shop_id'] = prod.get('store').get('id')
                        item['item_name'] = prod.get('name')
                        try: 
                            item['category'] = prod.get('category').get('structure')[0]
                        except:
                            item['category'] = ''
                        try:
                            item['subCategory'] = prod.get('category').get('structure')[1]
                        except:
                            item['subCategory'] = ''
                        try:
                            item['subSubCategory'] = prod.get('category').get('structure')[2]
                        except:
                            item['subSubCategory'] = ''
                        item['id_category'] = prod.get('category').get('id')
                        item['url_category'] = prod.get('category').get('url')
                        item['couriers'] = ','.join(prod.get('couriers'))
                        item['created_at'] = prod.get('created_at')
                        item['deal_applied_date'] = prod.get('deal').get('applied_date')
                        item['deal_discount_price'] = prod.get('deal').get('discount_price')
                        item['deal_expired_date'] = prod.get('deal').get('expired_date')
                        item['deal_original_price'] = prod.get('deal').get('original_price')
                        item['deal_percentage'] = prod.get('deal').get('percentage')
                        item['description'] = prod.get('description')
                        item['is_digital_product'] = prod.get('digital_product')
                        item['is_for_sale'] = prod.get('for_sale')
                        item['max_quantity'] = prod.get('max_quantity')
                        item['merchant_return_insurance'] = prod.get('merchant_return_insurance')
                        item['min_quantity'] = prod.get('min_quantity')
                        item['rating'] = prod.get('rating').get('average_rate')
                        item['rating_user_count'] = prod.get('rating').get('user_count')
                        item['rating_relisted_at'] = prod.get('relisted_at')
                        item['rating_is_rush_delivery'] = prod.get('rush_delivery')
                        item['shipping_force_insurance'] = prod.get('shipping').get('force_insurance')

                        item['stats_interest_count'] = prod.get('stats').get('interest_count')
                        item['stats_sold_count'] = prod.get('stats').get('sold_count')
                        item['stats_view_count'] = prod.get('stats').get('view_count')
                        item['stats_waiting_payment_count'] = prod.get('stats').get('waiting_payment_count')
                        item['stock'] = prod.get('stock')
                        item['updated_at'] = prod.get('updated_at')
                        item['url_product'] = prod.get('url')
                        item['warranty_cheapest'] = prod.get('warranty').get('cheapest')
                        item['product_weight'] = prod.get('weight')
                        item['without_shipping'] = prod.get('without_shipping')

                        #collect store data
                        item['city'] = prod.get('store').get('address').get('city')
                        item['province'] = prod.get('store').get('address').get('province')
                        item['is_brand_seller'] = prod.get('store').get('brand_seller')
                        item['is_shop_closed'] = prod.get('store').get('closing').get('closed')
                        item['delivery_time'] = prod.get('store').get('delivery_time')
                        #item['shop_description'] = prod.get('store').get('description')
                        item['first_upload_product_at'] = prod.get('store').get('first_upload_product_at')
                        item['is_shop_inactive'] = prod.get('store').get('inactivity').get('inactive')
                        item['last_appear_at'] = prod.get('store').get('inactivity').get('last_appear_at')
                        item['last_order_schedule'] = ','.join(['%s:%s' % (key, value) for (key, value) in prod.get('store').get('last_order_schedule').items()])
                        item['shop_level'] = prod.get('store').get('level').get('name')
                        item['shop_name'] = prod.get('store').get('name')
                        item['shop_premium_level'] = prod.get('store').get('premium_level')
                        item['is_shop_premium_top_seller'] = prod.get('store').get('premium_top_seller')
                        item['recent_rejection_transaction'] = prod.get('store').get('rejection').get('recent_transactions')
                        item['rejected_count'] = prod.get('store').get('rejection').get('rejected')
                        item['negative_reviews'] = prod.get('store').get('reviews').get('negative')
                        item['positive_reviews'] = prod.get('store').get('reviews').get('positive')
                        item['sla_type'] = prod.get('store').get('sla').get('type')
                        item['sla_value'] = prod.get('store').get('sla').get('value')
                        item['subscribers_amount'] = prod.get('store').get('subscriber_amount')
                        #item['term_and_condition'] = prod.get('store').get('term_and_condition')
                        item['shop_url'] = prod.get('store').get('url')
                        item['scraper_datetime'] = self.runtime


                        yield item
                    sku_id1 = productData[len(productData)-1].get('sku_id')

                        #next offset, same shop_id
                    try:
                        next_url_offset = 'https://api.bukalapak.com/stores/' + str(shop_id) + '/products?offset=' + str(offset+16) + '&limit=16&sort=bestselling&access_token=' + str(self.access_tkn())
                        request = scrapy.Request(url = next_url_offset, callback =self.parse_getData, meta = {'shop_id': shop_id, 'offset': offset+16, 'sku_id1': sku_id1})
                        yield request
                    except:
                        try:
                            next_url_offset = 'https://api.bukalapak.com/stores/' + str(shop_id) + '/products?offset=' + str(offset+16) + '&limit=16&sort=bestselling&access_token=' + str(self.access_tkn())
                            request = scrapy.Request(url = next_url_offset, callback =self.parse_getData, meta = {'shop_id': shop_id, 'offset': offset+16, 'sku_id1': sku_id1}, headers={'user-agent':'my-cool-project (http://example.com)'})
                            yield request
                        except:
                        #request access token
                            tmp_url = response.request.url
                            split_url = tmp_url.split('access_token=')[0]
                            req_tkn_url = split_url + 'access_token=' + str(self.access_tkn())
                            request = scrapy.Request(url = req_tkn_url, callback= self.parse_getData, meta = {'shop_id':shop_id, 'offset': offset+16, 'sku_id1' : sku_id1})



                else:
                #shop_id + 1
                    print('item_max : ' + str(productj.get('meta').get('total')))
                    try:
                        #print("-----shop ID : " + str(shop_id) + " ----- is empty")
                        #next shop_id
                        next_url_empty = 'https://api.bukalapak.com/stores/' + str(shop_id+1) + '/products?offset=0&limit=16&sort=bestselling&access_token=' + str(self.access_tkn())
                        request = scrapy.Request(url = next_url_empty, callback =self.parse_getData, meta = {'shop_id': shop_id+1, 'offset': 0, 'sku_id1' : '0'})
                        yield request
                    except:

                        #request access token
                        tmp_url = response.request.url
                        split_url = tmp_url.split('access_token=')[0]
                        req_tkn_url = split_url + 'access_token=' + str(self.access_tkn())
                        request = scrapy.Request(url = req_tkn_url, callback= self.parse_getData, meta = {'shop_id':shop_id+2, 'offset': 0, 'sku_id1' : '0'})
        except:
            try:
                try:
                    next_url_empty = 'https://api.bukalapak.com/stores/' + str(shop_id+1) + '/products?offset=0&limit=16&sort=bestselling&access_token=' + str(self.access_tkn())
                    request = scrapy.Request(url = next_url_empty, callback =self.parse_getData, meta = {'shop_id': shop_id+3, 'offset': 0, 'sku_id1' : '0'})
                    yield request
                except:
                    #request access token
                    tmp_url = response.request.url
                    split_url = tmp_url.split('access_token=')[0]
                    req_tkn_url = split_url + 'access_token=' + str(self.access_tkn())
                    request = scrapy.Request(url = req_tkn_url, callback= self.parse_getData, meta = {'shop_id':shop_id+4, 'offset' : 0, 'sku_id1' : '0'})
            except:
                try:
                    next_url_empty = 'https://api.bukalapak.com/stores/' + str(shop_id+1) + '/products?offset=0&limit=16&sort=bestselling&access_token=' + str(self.access_tkn())
                    request = scrapy.Request(url = next_url_empty, callback =self.parse_getData, meta = {'shop_id': shop_id+5, 'offset': 0, 'sku_id1' : '0'})
                    yield request
                except:
                    #request access token
                    tmp_url = response.request.url
                    split_url = tmp_url.split('access_token=')[0]
                    req_tkn_url = split_url + 'access_token=' + str(self.access_tkn())
                    request = scrapy.Request(url = req_tkn_url, callback= self.parse_getData, meta = {'shop_id':shop_id+6, 'offset' : 0, 'sku_id1' : '0'})




