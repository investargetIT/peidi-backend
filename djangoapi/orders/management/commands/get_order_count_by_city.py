import os, time, requests

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstKGjrJd6KjxyxKCy/records"
        token = os.getenv("APITABLE_TOKEN")
        records = []

        with connection.cursor() as cursor:
            time_start = '2024-01-01 00:00:00'
            time_end = '2024-01-31 23:59:59'
            cursor.callproc('GetOrderCountByCity', (time_start, time_end))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                r = {
                    "省市": row[0],
                    "订单数量": float(row[1]),
                    "时间": time_start[:7]
                }
                records.append({ "fields": r })

        print(len(records))
        for i in range(int(len(records)/30)+1):
            s = 30 * i
            e = 30 * (i + 1)
            if i == int(len(records)/30):
                e = len(records)
            res = requests.post(
                url=url,
                json={"records": records[s:e]},
                headers={"Authorization": f"Bearer {token}"},
            )
            res.raise_for_status()
            time.sleep(1)
