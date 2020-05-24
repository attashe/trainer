# Trainer

Небольшая библиотека для перебора параметров моделей машинного обучения

```python
import sys
import subprocess
from trainer import UpdateRule, Trainer, Model
class ModelTest(Model):
  def _internal_run(self):
    sp = subprocess.Popen(['cat', 'config.yaml'], cwd=self.folder,
                          stdout=sys.stdout)
    sp.wait()

cfg = {
  'arch': 'unet',
  'test': True
}
rule = UpdateRule({
  "bs": [1, 2],
  "lr": [0.1, 0.01, 0.001]
})

trainer = Trainer(cfg, ModelTest, )
trainer.add_rule(rule)
trainer.run()
```