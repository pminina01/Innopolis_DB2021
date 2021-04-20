import redis
r = redis.Redis(
host='redis-18256.c93.us-east-1-3.ec2.cloud.redislabs.com',
port="18256",
password='yiB5CuZ8K4rMoLB9V6JnR2jltd0xSfSH')

customers = (("001", 'Jane', 'Doe'),("002", 'John', 'Doe'),\
             ("003", 'Jane', 'Smith'),("004", 'John', 'Smith'),\
             ("005", 'Jane', 'Jones'),("006", 'John', 'Jones'))
orders = [("1001", "002", "10/10/09", 250.85),("1002", "002", "2/21/10", 150.89),\
          ("1003", "003", "11/15/09", 1567.99), ("1004", "004", "11/22/09", 180.92),\
          ("1005", "004", "12/15/09", 565.00), ("1006", "006", "11/22/09", 25.00),\
          ("1007", "006", "10/8/09", 85.00), ("1008", "006", "12/29/09", 109.12)]
#r.flushall()
for a, b, c in customers:
    r.hset(f"customer:{str(a)}", mapping={'id': a,'first_name': b,'last_name': c})
for a, b, c, d in orders:
    r.hset(f"order:{a}",mapping={'customer_id': b,'order_date': c,'order_total': d})