import tablib

from django.core.management.base import BaseCommand
from goods.admin import SpecGoodsResource

class Command(BaseCommand):
    def handle(self, *args, **options):
        # resource = SpecGoodsResource()
        # dataset = tablib.Dataset(['101', '202', '测试'], headers=['spec_no', 'goods_no', 'goods_name'])
        # result = resource.import_data(dataset, dry_run=True)
        # print(result.has_errors())
        # False
        # result = resource.import_data(dataset, dry_run=False)
        # print(result)

        dataset = SpecGoodsResource().export()
        print(dataset.csv)
