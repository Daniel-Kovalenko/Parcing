import collections
from datetime import datetime as dt

from pep_parse import constants as const
from pep_parse import settings, utils

BASE_DIR = settings.BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = collections.defaultdict(int)

    def close_spider(self, spider):
        filename = (
            f'{BASE_DIR}/results/status_summary_'
            f'{dt.now().strftime(const.STATUS_DT_FORMAT)}.csv'
        )
        utils.dict_to_csv(filename, self.statuses, ('Статус', 'Количество'))

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item
