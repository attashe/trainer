from .update_rule import UpdateRule

import time
import warnings
import numpy as np
warnings.filterwarnings('ignore', message='numpy.dtype size changed')
import subprocess
import sys


class Model:
    def __init__(self, folder, config: dict = None):
        print("Model was initialized")
        self.config = config
        self.trained = False
        self.folder = folder

    def set_config(self, config):
        print("Config was set")
        self.config = config

    def _internal_run(self):
        # stiching ir
        # change_value_in_config(geo_config_path, 'paths', 'start_dir', ir_dataset_dir)
        # change_value_in_config(geo_config_path, 'paths', 'coord_csv_path', ir_coords_cache)
        # sp = subprocess.Popen(['python3', 'bbox.py', '--elev_flg', '--coord_flg', '--norm'], cwd='geo',
        #                       stdout=sys.stdout)
        # sp.wait()
        print('Internal run')

    def train(self):
        print("Model training is started")
        self._internal_run()
        # создать новый тред и в нем запустить  sleep, а здесь поставить wait/join, чтобы проверить
        # ошибку для преждевременного вызова calc_metric
        time.sleep(1)
        self.trained = True

    def calc_metric(self):
        if self.trained:
            print("Model training is successful")
            return np.random.rand()
        else:
            raise Exception("Model training is unsuccessful")