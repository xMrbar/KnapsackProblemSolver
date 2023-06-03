# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['KnapsackSolver.py', 'Crosser.py', 'GeneticAlgorithm.py', 'GUILogic.py', 'ICrossable.py', 'IGeneticAlgorithm.py', 'IIndividual.py', 'IIndividualCreator.py', 'IKnapsackProblem.py', 'ILogger.py', 'IMutable.py', 'Individual.py', 'IndividualCreator.py', 'IReader.py', 'ISolutionCounter.py', 'ItemCreator.py', 'IValidator.py', 'IWritableKnapsack.py', 'IWritableSolution.py', 'KnapsackItem.py', 'KnapsackProblem.py', 'Logger.py', 'Mutation.py', 'MyExceptions.py', 'MyGUI.py', 'Reader.py', 'SolutionCounter.py', 'Validator.py', 'WriteKnapsack.py', 'WriteSolution.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='KnapsackSolver',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
