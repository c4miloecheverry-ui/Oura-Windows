# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

hiddenimports = [
    # --- uvicorn ---
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    # --- fastapi / starlette ---
    'fastapi',
    'fastapi.middleware',
    'fastapi.middleware.cors',
    'fastapi.staticfiles',
    'fastapi.responses',
    *collect_submodules('starlette'),
    # --- pydantic ---
    *collect_submodules('pydantic'),
    *collect_submodules('pydantic_core'),
    # --- sqlalchemy ---
    'sqlalchemy',
    'sqlalchemy.orm',
    'sqlalchemy.dialects.sqlite',
    *collect_submodules('sqlalchemy.engine'),
    *collect_submodules('sqlalchemy.sql'),
    # --- pandas ---
    'pandas',
    'pandas.io.formats.style',
    # --- async / http ---
    'anyio',
    'anyio._backends',
    'anyio._backends._asyncio',
    'sniffio',
    'h11',
    'httpx',
    'httpcore',
    'httpcore._async',
    'httpcore._sync',
    # --- multipart (file uploads) ---
    'multipart',
    'multipart.multipart',
    # --- playwright ---
    'playwright',
    'playwright.async_api',
    'playwright._impl',
    'playwright._impl._driver',
    # --- langchain ---
    'langchain_ollama',
    'langchain_community',
    'langchain_community.utilities',
    'langchain_community.agent_toolkits',
    'langchain_core',
    'langchain_core.callbacks',
    # --- other ---
    'email_validator',
]

# Collect playwright driver data files
playwright_datas = collect_data_files('playwright')

a = Analysis(
    ['src/api/main.py'],
    pathex=['..'],
    binaries=[],
    datas=[
        ('src', 'backend/src'),
        ('__init__.py', 'backend'),
        *playwright_datas,
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='backend',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='backend',
)
