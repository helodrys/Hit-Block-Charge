from PyInstaller.utils.hooks import collect_submodules

# Collect all submodules of pywin32
hiddenimports = collect_submodules('win32')
hiddenimports += collect_submodules('win32com')
