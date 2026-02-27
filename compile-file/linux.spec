# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os

# ========= CONFIG =========
APP_NAME = "Arrera Six"
ENTRY_SCRIPT = "main.py"
ICON_FILE = "asset/icon/linux/icon.png"
UPX_ENABLED = False
DEBUG_BUILD = False

# AJOUT : Force l'inclusion du finder de Pillow pour Tkinter
HIDDENIMPORTS = ['PIL._tkinter_finder']
EXCLUDES = []
# ========= FIN CONFIG =========

block_cipher = None
PROJECT_ROOT = os.path.abspath(".")

# --- Récupération de llama_cpp ET customtkinter ---
# On combine les collectes pour s'assurer que les thèmes JSON et binaires sont là
tmp_llama = collect_all('llama_cpp')
tmp_ctk = collect_all('customtkinter')

# Fusion des données, binaires et imports cachés
combined_datas = tmp_llama[0] + tmp_ctk[0]
combined_binaries = tmp_llama[1] + tmp_ctk[1]
combined_hidden = tmp_llama[2] + tmp_ctk[2]

final_hiddenimports = list(set(HIDDENIMPORTS + combined_hidden))

# --- Ajout des dossiers asset, config, keyword, language ---
extra_datas = []
for folder in ['asset', 'config', 'keyword', 'language']:
    source_path = os.path.join(PROJECT_ROOT, folder)
    if os.path.exists(source_path):
        extra_datas.append((source_path, folder))

final_datas = combined_datas + extra_datas

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=combined_binaries,
    datas=final_datas,
    hiddenimports=final_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True, # Garde la console pour voir si l'erreur audio persiste
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_FILE,
)