class UpdateRule:
    def __init__(self, values, variants: list = None):
        """
        Rules for changing values in config

        @param values: string with param name or dictionary like { param: [values] }
        @param variants: if values is string variants contain list with possible values for selected param
        """
        self.dict = {}

        if type(values) is str and type(variants) is list:
            self.dict[values] = variants
        elif type(values) is dict:
            self.dict.update(values)
        else:
            raise Exception("Arguments aren't recognized")

        self.counters = [len(v) for k, v in self.dict.items()]
        print(self.counters)
        self.state = [0 for c in self.counters]

    @property
    def keys(self):
        return list(self.dict.keys())

    def __getitem__(self, key):
        pass

    def next_state(self, ):
        pass

    def get_config(self, config):
        for i, k in enumerate(self.keys):
            config[k] = self.dict[k][self.state[i]]
        # print(config)

        return config

    def states(self):
        t = 0
        while True:
            yield t
            for i in range(len(self.state)):
                self.state[i] += 1
                if self.state[i] == self.counters[i]:
                    self.state[i] = 0
                    if i == len(self.state) - 1:
                        # raise StopIteration
                        return
                    else:
                        self.state[i] = 0
                else:
                    # yield t
                    break
            t += 1
            # print(self.state)

            t += 1
