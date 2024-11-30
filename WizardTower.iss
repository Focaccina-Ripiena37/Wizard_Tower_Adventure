[Setup]
AppName=Wizard Tower
AppVersion=1.0.0
AppPublisher=Your Name
DefaultDirName={commonpf}\Wizard Tower
DefaultGroupName=Wizard Tower
OutputDir=installer
OutputBaseFilename=WizardTower_Setup
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\WizardTower.exe
; Aggiornato da x64 a x64compatible come suggerito
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
; Aggiunto per chiarire i privilegi richiesti
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "dist\WizardTower\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "logging.conf"; DestDir: "{app}"; Flags: ignoreversion

[Dirs]
Name: "{app}\logs"; Permissions: users-full

[Icons]
Name: "{group}\Wizard Tower"; Filename: "{app}\WizardTower.exe"
Name: "{commondesktop}\Wizard Tower"; Filename: "{app}\WizardTower.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\WizardTower.exe"; Description: "{cm:LaunchProgram,Wizard Tower}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}\logs"
