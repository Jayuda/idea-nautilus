# IntelliJIDEA Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscode
INTELJIDEA = 'idea'

# what name do you want to see in the context menu?
INTELJIDEANAME = 'IntelliJ IDEA'

# always create new window?
NEWWINDOW = False


class IntelliJIDEAExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscode(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscode
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(INTELJIDEA + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='IntelliJIDEAOpen',
            label='Open in ' + INTELJIDEANAME,
            tip='Opens the selected files with IntelliJIDEA'
        )
        item.connect('activate', self.launch_vscode, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='IntelliJIDEAOpenBackground',
            label='Open in ' + INTELJIDEANAME,
            tip='Opens the current directory in IntelliJIDEA'
        )
        item.connect('activate', self.launch_vscode, [file_])

        return [item]
