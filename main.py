import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):

    def delete_item(self, item):
        item.delete()

        print('Successfully deleted the item')
