# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_dynamic_libs

import os
cmdline_name = os.environ.get("ELECTRUM_CMDLINE_NAME")
if not cmdline_name:
    raise Exception('no name')

home = 'C:\\electrum-ltc\\'

# see https://github.com/pyinstaller/pyinstaller/issues/2005
hiddenimports = []
hiddenimports += collect_submodules('pkg_resources')  # workaround for https://github.com/pypa/setuptools/issues/1963
hiddenimports += collect_submodules('trezorlib')
hiddenimports += collect_submodules('safetlib')
hiddenimports += collect_submodules('btchip')
hiddenimports += collect_submodules('keepkeylib')
hiddenimports += collect_submodules('websocket')
hiddenimports += collect_submodules('ckcc')
hiddenimports += collect_submodules('bitbox02')
hiddenimports += ['electrum_ltc.plugins.jade.jade']
hiddenimports += ['electrum_ltc.plugins.jade.jadepy.jade']
hiddenimports += ['_scrypt', 'PyQt5.QtPrintSupport']  # needed by Revealer


binaries = []

# Workaround for "Retro Look":
binaries += [b for b in collect_dynamic_libs('PyQt5') if 'qwindowsvista' in b[0]]

binaries += [('C:/tmp/libsecp256k1-0.dll', '.')]
binaries += [('C:/tmp/libusb-1.0.dll', '.')]
binaries += [('C:/tmp/libzbar-0.dll', '.')]
binaries += [(home+'mwebd.exe', '.')]

datas = [
    (home+'electrum_ltc/*.json', 'electrum_ltc'),
    (home+'electrum_ltc/lnwire/*.csv', 'electrum_ltc/lnwire'),
    (home+'electrum_ltc/wordlist/english.txt', 'electrum_ltc/wordlist'),
    (home+'electrum_ltc/wordlist/slip39.txt', 'electrum_ltc/wordlist'),
    (home+'electrum_ltc/locale', 'electrum_ltc/locale'),
    (home+'electrum_ltc/plugins', 'electrum_ltc/plugins'),
    (home+'electrum_ltc/gui/icons', 'electrum_ltc/gui/icons'),
]
datas += collect_data_files('trezorlib')
datas += collect_data_files('safetlib')
datas += collect_data_files('btchip')
datas += collect_data_files('keepkeylib')
datas += collect_data_files('ckcc')
datas += collect_data_files('bitbox02')

# We don't put these files in to actually include them in the script but to make the Analysis method scan them for imports
a = Analysis([home+'run_electrum',
              home+'electrum_ltc/gui/qt/main_window.py',
              home+'electrum_ltc/gui/qt/qrreader/qtmultimedia/camera_dialog.py',
              home+'electrum_ltc/gui/text.py',
              home+'electrum_ltc/util.py',
              home+'electrum_ltc/wallet.py',
              home+'electrum_ltc/simple_config.py',
              home+'electrum_ltc/bitcoin.py',
              home+'electrum_ltc/blockchain.py',
              home+'electrum_ltc/dnssec.py',
              home+'electrum_ltc/commands.py',
              home+'electrum_ltc/plugins/cosigner_pool/qt.py',
              home+'electrum_ltc/plugins/trezor/qt.py',
              home+'electrum_ltc/plugins/safe_t/client.py',
              home+'electrum_ltc/plugins/safe_t/qt.py',
              home+'electrum_ltc/plugins/keepkey/qt.py',
              home+'electrum_ltc/plugins/ledger/qt.py',
              home+'electrum_ltc/plugins/coldcard/qt.py',
              home+'electrum_ltc/plugins/jade/qt.py',
              #home+'packages/requests/utils.py'
              ],
             binaries=binaries,
             datas=datas,
             #pathex=[home+'lib', home+'gui', home+'plugins'],
             hiddenimports=hiddenimports,
             hookspath=[])


# http://stackoverflow.com/questions/19055089/pyinstaller-onefile-warning-pyconfig-h-when-importing-scipy-or-scipy-signal
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

# Strip out parts of Qt that we never use. Reduces binary size by tens of MBs. see #4815
qt_bins2remove=('qt5web', 'qt53d', 'qt5game', 'qt5designer', 'qt5quick',
                'qt5location', 'qt5test', 'qt5xml', r'pyqt5\qt\qml\qtquick')
print("Removing Qt binaries:", *qt_bins2remove)
for x in a.binaries.copy():
    for r in qt_bins2remove:
        if x[0].lower().startswith(r):
            a.binaries.remove(x)
            print('----> Removed x =', x)

qt_data2remove=(r'pyqt5\qt\translations\qtwebengine_locales',)
print("Removing Qt datas:", *qt_data2remove)
for x in a.datas.copy():
    for r in qt_data2remove:
        if x[0].lower().startswith(r):
            a.datas.remove(x)
            print('----> Removed x =', x)

# not reproducible (see #7739):
print("Removing *.dist-info/ from datas:")
for x in a.datas.copy():
    if ".dist-info\\" in x[0].lower():
        a.datas.remove(x)
        print('----> Removed x =', x)


# hotfix for #3171 (pre-Win10 binaries)
a.binaries = [x for x in a.binaries if not x[1].lower().startswith(r'c:\windows')]

pyz = PYZ(a.pure)


#####
# "standalone" exe with all dependencies packed into it

exe_standalone = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name=os.path.join('build\\pyi.win32\\electrum-ltc', cmdline_name + ".exe"),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'electrum_ltc/gui/icons/electrum.ico',
    console=False)
    # console=True makes an annoying black box pop up, but it does make Electrum output command line commands, with this turned off no output will be given but commands can still be used

exe_portable = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas + [('is_portable', 'README.md', 'DATA')],
    name=os.path.join('build\\pyi.win32\\electrum-ltc', cmdline_name + "-portable.exe"),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'electrum_ltc/gui/icons/electrum.ico',
    console=False)

#####
# exe and separate files that NSIS uses to build installer "setup" exe

exe_inside_setup_noconsole = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name=os.path.join('build\\pyi.win32\\electrum-ltc', cmdline_name),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'electrum_ltc/gui/icons/electrum.ico',
    console=False)

exe_inside_setup_console = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name=os.path.join('build\\pyi.win32\\electrum-ltc', cmdline_name+"-debug"),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'electrum_ltc/gui/icons/electrum.ico',
    console=True)

coll = COLLECT(
    exe_inside_setup_noconsole,
    exe_inside_setup_console,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=None,
    upx=True,
    debug=False,
    icon=home+'electrum_ltc/gui/icons/electrum.ico',
    console=False,
    name=os.path.join('dist', 'electrum-ltc'))
