from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            pay_time_start = '2022-01-01 00:00:00'
            pay_time_end = '2022-12-31 23:59:59'
            cursor.callproc('GetShopSalesAmount', (pay_time_start, pay_time_end))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
