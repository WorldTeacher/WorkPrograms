#ask if user uses the program for the first time
$url = "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe"
$outpath = "$PSScriptRoot/pythoninstaller.exe"
$appdata = $env:LOCALAPPDATA
#$python = "$appdata\Programs\Python\Python310\python.exe"
$path = $PSScriptRoot 
$persistent=Get-Variable -Name Pythoninstalled -Value -ErrorAction SilentlyContinue
#$pippath = "$appdata\Programs\Python\Python310\Scripts\pip.exe"
#Write-Host "Install Path: $python"
Write-Host "Willkommen im Installer fuer 'TEMPNAME'!"
Write-Host "Dieser Installer wird Ihnen helfen, Python, die benoetigten Module, sowie das Program 'TEMPNAME' zu installieren und starten."
Set-Variable -Name Pythoninstalled -Description "check if python is installed" -Value 0
#if variable is 0, install python
#use persistent mode?
if ($persistent -eq "0"){
$persistentstate= Read-Host -Prompt "Moechten Sie die komplette Installation immer wieder starten? (j/n)"
}
if ($persistentstate -eq "n"){

    if ($Pythoninstalled -eq 0) {
        Write-Host "Python 3.10.4 wird heruntergeladen, bitte warten..."
        Invoke-WebRequest -Uri $url -OutFile $outpath
        #wait 0,5sec
        Start-Sleep -s 0.5
        Write-Host "Download abgeschlossen, bitte warten..."
        Set-Variable -Name Pythoninstalled -Description "check if python is installed" -Value 1
        Start-Sleep -s 2
        Write-host "In ein paar Sekunden wird Python den Installer starten," -ForegroundColor Red
        Start-Sleep -s 2
        Write-Host "hier muessen dann einige Eingaben gemacht werden:" -ForegroundColor Red
        Start-Sleep -s 2
        Write-Host "Das Feld 'Fuer alle Nutzer installieren' muss deaktiviert werden, das Feld 'Add Python to PATH' muss aktiviert werden" -ForegroundColor Red
        Start-Sleep -s 2
        Write-Host "Nachdem die Nachricht 'Installation was successfull' erscheint, kann der Installer mit 'Close' geschlossen werden" -ForegroundColor Red
        #start the installer
        Start-Process -FilePath $outpath 
        #ask if Python is installed
        $PYTHON_INSTALLED = Read-Host -Prompt "Ist Python installiert? (j/n) "
        if ($PYTHON_INSTALLED -eq "j") {
            Write-Host "Die Python Installation ist abgeschlossen"
            Write-Host "PIP wird zum PATH hinzugefuegt"
            setx PATH "%PATH%;$appdata\Programs\Python\Python310\Scripts" 
            Write-Host "Python installiert nun zusaetzliche Module"
            #using python pip, install pandas
            pip install -r $path/requirements.txt	
            Write-Host "Alle Module wurden installiert"
            #ask if they want to start the launcher
            $LAUNCHER_START = Read-Host -Prompt "Soll der Launcher gestartet werden? (j/n) "
                if ($LAUNCHER_START -eq "j") {
                #start the launcher
                Write-Host "Launcher wird gestartet, bitte warten..."
                #python.exe $PSScriptRoot/launcher.py #might need changes, if folder structure changes
                }
            }
        }
    }

if($persistentstate -eq "j") {
    Write-Host "Python 3.10.4 wird heruntergeladen, bitte warten..."
    #Invoke-WebRequest -Uri $url -OutFile $outpath
    #wait 0,5sec
    Start-Sleep -s 0.5
    Write-Host "Download abgeschlossen, bitte warten..."
    #inform user about the next steps
    Start-Sleep -s 2
    Write-host "In ein paar Sekunden wird Python den Installer starten," -ForegroundColor Red
    Start-Sleep -s 2
    Write-Host "hier muessen dann einige Eingaben gemacht werden:" -ForegroundColor Red
    Start-Sleep -s 2
    Write-Host "Das Feld 'Fuer alle Nutzer installieren' muss deaktiviert werden, das Feld 'Add Python to PATH' muss aktiviert werden" -ForegroundColor Red
    Start-Sleep -s 2
    Write-Host "Nachdem die Nachricht 'Installation was successfull' erscheint, kann der Installer mit 'Close' geschlossen werden" -ForegroundColor Red
    #start the installer
    Start-Process -FilePath $outpath 

    #ask if Python is installed
    $PYTHON_INSTALLED = Read-Host -Prompt "Ist Python installiert? (j/n) "
    if ($PYTHON_INSTALLED -eq "j") {
        Write-Host "Die Python Installation ist abgeschlossen"
        Write-Host "PIP wird zum PATH hinzugefuegt"
        setx PATH "%PATH%;$appdata\Programs\Python\Python310\Scripts" 
        Write-Host "Python installiert nun zusaetzliche Module"
        #using python pip, install pandas
        pip install pandas	
        #python.exe -m pip install -r $path/requirements.txt
        #pip.exe install pandas
        Write-Host "Alle Module wurden installiert"
        #ask if they want to start the launcher
        $LAUNCHER_START = Read-Host -Prompt "Soll der Launcher gestartet werden? (j/n) "
            if ($LAUNCHER_START -eq "j") {
            #start the launcher
            Write-Host "Launcher wird gestartet, bitte warten..."
            #python.exe $PSScriptRoot/launcher.py #might need changes, if folder structure changes
        }
    }
    else{
       Write-Host "Launcher wird nicht gestartet"
       Write-Host "Programm wird beendet"   
       Start-Sleep -s 1
         exit 
    }
}
#if ($PYTHON_INSTALLED -eq "n") {
#    Write-Host "Please install Python first"
#}
#if($First_Time -eq "n"){
#   $LaunchScript = Read-Host -Prompt "Would you like to launch the script? (y/n) "
#    if ($LaunchScript -eq "y") {
#         python.exe $PSSCRIPTROOT/Launcher.py
#    else {
#        Write-Host "Thank you for using the program"
#        Write-Host "Goodbye"
#        Start-Sleep -s 5
#        exit
#        }
#    }
#}


