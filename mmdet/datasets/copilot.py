import numpy as np
from pycocotools.coco import COCO

from .coco import CocoDataset
from .registry import DATASETS

@DATASETS.register_module
class CopilotDataset(CocoDataset):

    CLASSES = ('panel', 'cropped_panel')