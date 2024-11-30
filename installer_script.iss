; filepath: /c:/Users/Lorenzo/Desktop/Progettone/wizard_tower/installer_script.iss
[Setup]
AppName=Wizard Tower
AppVersion=1.0.0
DefaultDirName={pf}\WizardTower
DefaultGroupName=Wizard Tower
OutputDir=installer
OutputBaseFilename=WizardTowerInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\WizardTower\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Dirs]
Name: "{app}\logs"; Permissions: users-full

[Icons]
Name: "{group}\Wizard Tower"; Filename: "{app}\WizardTower.exe"
Name: "{group}\Uninstall Wizard Tower"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\WizardTower.exe"; Description: "{cm:LaunchProgram,Wizards Tower}"; Flags: nowait postinstall skipifsilent