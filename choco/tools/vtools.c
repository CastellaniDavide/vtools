#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	system("python.exe -c \"exec(\\\"from vtools import vtools;vtools('--choco')\\\")\"");
}