# My personal variabiles
$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$ppath = "C:\Progra~1\vtools"
$exepath = "$ppath\vtools.exe"
echo "My personal path is: $ppath"
echo "My exe path id $exepath"

# Set folder
Remove-Item -LiteralPath $ppath -Force -Recurse

# Add Path
$new_path = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
if ($new_path -like "*$ppath*")
{
	echo "Delate unwanted path"
	$new_path = $new_path.Replace("$ppath", "").Replace(";;", ";")
	Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $new_path
}

# Installing pypi
pip.exe remove vtoolscd==0.1
