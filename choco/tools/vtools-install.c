#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	system("start powershell.exe $ppath = \"C:\\Program Files\\vtools\";pause");//;$exepath = \"$ppath\\vtools.exe\";echo \"My personal path is: $ppath\";echo \"My exe path id $exepath\";New-Item -ItemType Directory -Force -Path $ppath;Copy-Item \"$toolsDir\\vtools.exe\" \"$ppath\\vtools.exe\";$new_path = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Environment' -Name PATH).path;if ($new_path -notlike \"*$ppath*\"){$new_path += \";$ppath\";$new_path = $new_path.Replace(\";;\", \";\");Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Environment' -Name PATH -Value $new_path}");
}
