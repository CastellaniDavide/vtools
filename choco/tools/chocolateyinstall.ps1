 param (
    [switch]$local = $false
 )

# Variabiles
$toolsDir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"

if ($local) {
	$ppath = $env:LOCALAPPDATA + "\vtools"
} else {
	$ppath = "C:\Progra~1\vtools"
}

$path = "$ppath\__init__"

# Set folder and rename exe file
New-Item -ItemType Directory -Force -Path $ppath
Copy-Item -Path "$toolsDir\dist\__init__\*" -Destination "$ppath\" -Recurse
Rename-Item -Path "$ppath\__init__.exe" -NewName "$ppath\vtools.exe"

# Add Path
$new_path = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
if ($new_path -notlike "*$ppath*")
{
	$new_path += ";$ppath"
	$new_path = $new_path.Replace(";;", ";")
	Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $new_path
}