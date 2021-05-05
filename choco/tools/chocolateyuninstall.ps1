# My personal variabiles
$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$ppath = "C:\Progra~1\vtools"
$localppath = $env:LOCALAPPDATA + "\vtools"

# Set folder
Remove-Item -LiteralPath $ppath -Force -Recurse
Remove-Item -LiteralPath $localppath -Force -Recurse

# Add Path
$new_path = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
if ($new_path -like "*$ppath*" -or $new_path -like "*$localppath*")
{
	echo "Delate unwanted path"
	$new_path = $new_path.Replace("$ppath", "").Replace("$localppath", "").Replace(";;", ";")
	Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $new_path
}
