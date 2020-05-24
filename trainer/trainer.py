import os
import shutil
import yaml
from copy import deepcopy
from datetime import datetime
from .update_rule import UpdateRule
from .model import Model


class Trainer:
    def __init__(self, init_cfg, model: type(Model), workdir='./workdir'):
        self.config: dict = init_cfg
        self.results: dict = {}
        self.rules: [UpdateRule] = []
        self.model_class = model

        if os.path.exists(workdir):
            shutil.rmtree(workdir)
        os.mkdir(workdir)
        self.workdir = workdir

        with open(os.path.join(workdir, 'config.yaml'), 'w') as f:
            yaml.dump(init_cfg, f)

    @staticmethod
    def update_cfg(config: dict, update_rule: UpdateRule):
        new_cfg = deepcopy(config)
        if update_rule is None:
            return new_cfg

        for k in update_rule.keys:
            new_cfg[k] = update_rule[k]

        update_rule.next_state()
        return new_cfg

    def add_rule(self, rule: UpdateRule):
        self.rules.append(rule)

    def get_result(self):
        pass

    def run(self):
        for rule in self.rules:
            for t in rule.states():
                now = datetime.now()
                # t = now.strftime("%d-%m-%Y_%H-%M")
                t = now.ctime()
                out_folder = os.path.join(self.workdir, t)
                if os.path.exists(out_folder):
                    shutil.rmtree(out_folder)
                os.mkdir(out_folder)

                config = rule.get_config(self.config)
                # print(config)
                # Trainer.update_cfg(self.config, rule)
                with open(os.path.join(out_folder, 'config.yaml'), 'w') as f:
                    yaml.dump(config, f)

                model = self.model_class(out_folder, config)
                model.train()