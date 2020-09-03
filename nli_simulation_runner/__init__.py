from girder import getPlugin, plugin

from nli_simulation_runner.api import NLI


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'NLI Simulation Runner'

    def load(self, info):
        getPlugin('jobs').load(info)
        info['apiRoot'].nli = NLI()
