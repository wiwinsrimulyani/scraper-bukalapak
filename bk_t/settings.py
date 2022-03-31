# Scrapy settings for bk_t project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bk_t'

SPIDER_MODULES = ['bk_t.spiders']
NEWSPIDER_MODULE = 'bk_t.spiders'

USER_AGENT = 'my-cool-project (http://example.com)'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bk_t (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

#ITEM_PIPELINES = {
#  'bk_t.pipelines.BkTPipeline': 300,
#}

#DOWNLOAD_DELAY = 0.1

AUTOTHROTTLE_ENABLED = False


#AUTOTHROTTLE_START_DELAY = 0.75
#AUTOTHROTTLE_MAX_DELAY = 2

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bk_t.middlewares.BkTSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bk_t.middlewares.BkTDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bk_t.pipelines.BkTPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_HOST   = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER   = 'root'
MYSQL_PASSWD = ''

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = [
    'idd',
    'sku_id',
    'shop_id',
    'item_name',
    'category',
    'subCategory',
    'subSubCategory',
    'id_category',
    'url_category',
    'couriers',
    'created_at',
    'deal_applied_date',
    'deal_discount_price',
    'deal_expired_date',
    'deal_original_price',
    'deal_percentage',
    'description',
    'is_digital_product',
    'is_for_sale',
    'max_quantity',
    'merchant_return_insurance',
    'min_quantity',
    'rating',
    'rating_user_count',
    'rating_relisted_at',
    'rating_is_rush_delivery',
    'shipping_force_insurance',
    'stats_interest_count',
    'stats_sold_count',
    'stats_view_count',
    'stats_waiting_payment_count',
    'stock',
    'updated_at',
    'url_product',
    'warranty_cheapest',
    'product_weight',
    'without_shipping',
    'city',
    'province',
    'is_brand_seller',
    'is_shop_closed',
    'delivery_time',
    'first_upload_product_at',
    'is_shop_inactive',
    'last_appear_at',
    'last_order_schedule',
    'shop_level',
    'shop_name',
    'shop_premium_level',
    'is_shop_premium_top_seller',
    'recent_rejection_transaction',
    'rejected_count',
    'negative_reviews',
    'positive_reviews',
    'sla_type',
    'sla_value',
    'subscribers_amount',
    'shop_url',
    'scraper_datetime',
    ]
