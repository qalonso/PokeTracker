@echo off
REM Vérifie si pyenv est installé
where pyenv >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO pyenv n'est pas installé. Veuillez l'installer d'abord.
    REM Continue l'exécution même si pyenv n'est pas installé
    GOTO END
) ELSE (
    ECHO pyenv est installé.
)

REM Vérifie si Python 3.10.4 est déjà installé
pyenv versions | findstr /C:"3.10.4" >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    ECHO Python 3.10.4 est déjà installé.
    REM Vérifie si la version locale est bien 3.10.4
    pyenv local | findstr /C:"3.10.4" >nul 2>nul
    IF %ERRORLEVEL% EQU 0 (
        ECHO La version locale est bien Python 3.10.4.
    ) ELSE (
        ECHO La version locale n'est pas Python 3.10.4.
        pyenv local 3.10.4
        IF %ERRORLEVEL% NEQ 0 (
            ECHO Erreur lors de la définition de la version locale.
        )
    )
) ELSE (
    REM Installe Python 3.10.4
    pyenv install 3.10.4
    IF %ERRORLEVEL% NEQ 0 (
        ECHO Erreur lors de l'installation de Python 3.10.4.
        REM Continue l'exécution même en cas d'erreur
    ) ELSE (
        ECHO Python 3.10.4 a été installé.
    )
)

REM Vérifie si l'environnement virtuel .env existe déjà
IF EXIST ".env" (
    ECHO L'environnement virtuel .env existe déjà.
) ELSE (
    REM Crée un environnement virtuel nommé .env
    python -m venv .env
    IF %ERRORLEVEL% NEQ 0 (
        ECHO Erreur lors de la création de l'environnement virtuel .env.
        REM Continue l'exécution même en cas d'erreur
    ) ELSE (
        ECHO Environnement virtuel .env créé avec Python 3.10.4.
    )
)

REM Active l'environnement virtuel et installe les dépendances
CALL .env\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    ECHO Erreur lors de l'activation de l'environnement virtuel.
    REM Continue l'exécution même en cas d'erreur
) ELSE (
    ECHO Environnement virtuel activé.
    REM Installe les dépendances à partir de requirements.txt
    pip install -r requirements.txt
    IF %ERRORLEVEL% NEQ 0 (
        ECHO Erreur lors de l'installation des dépendances.
    ) ELSE (
        ECHO Dépendances installées avec succès.
    )
)

:END
ECHO Script exécuté jusqu'au bout.
PAUSE
