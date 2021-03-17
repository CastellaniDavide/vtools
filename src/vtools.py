"""vtools
"""
from sys import argv
import os
import subprocess
from csv import DictWriter
from tabular_log import tabular_log

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-3-16"

class vtools:
	def __init__ (self):
		"""Where it all begins
		"""
		self.setup()
		self.get_machines()
		try:
			self.core()
		except:
			print("Error: make sure you have installed vbox on your PC")
		print(self.vmachines)

	def setup(self):
		"""Setup
		"""
		# Define main variabiles
		self.verbose = True
		self.csv = True
		self.vboxmanage = "C:/Program Files/Oracle/VirtualBox/vboxmanage" if "--choco" in argv else "vboxmanage"

		# Define log
		self.log = tabular_log(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "log", "trace.log") if "--choco" in argv else "~/trace.log", title = "vtools" ,verbose = self.verbose)
		self.log.print("Created log")

		if self.csv:
			# Define files
			self.OS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "flussi", "OS.csv") if "--choco" in argv else "~/OS.csv"
			self.net = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "flussi", "net.csv") if "--choco" in argv else "~/net.csv"
			self.OSheader = "PC_name,OS"
			self.net_header = "PC_name,network_card_name,V4,MAC,Attachment"
			self.log.print("Defined CSV files' infos")

			# Create header if needed
			try:
				if open(self.OS, 'r+').readline() == "":
					assert(False)
			except:
				open(self.OS, 'w+').write(self.OSheader + "\n")

			try:
				if open(self.net, 'r+').readline() == "":
					assert(False)
			except:
				open(self.net, 'w+').write(self.net_header + "\n")
			
			self.log.print("Inizialized CSV files")

	def core(self):
		"""Core of all project
		"""
		for PC in self.vmachines:
			if self.csv:
				DictWriter(open(self.OS, 'a+', newline=''), fieldnames=self.OSheader.split(","), restval='').writerow({"PC_name": PC, "OS": self.get_os(PC)})
				for i in self.get_net(PC):
					net = {"PC_name": PC}
					for key, value in zip(self.net_header.split(",")[1:], i):
						net[key] = value
					DictWriter(open(self.net, 'a+', newline=''), fieldnames=self.net_header.split(","), restval='').writerow(net)

				self.log.print("Stored into csv file(s)")

	def get_machines(self):
		"""Get virtual machines' name
		"""
		self.vmachines = []
		temp=""
		take=False

		for i in self.get_output(["list", "vms"]):
			if i == "\"":
				if take == True:
					self.vmachines.append(temp)
					temp = ""
				take = not take
			elif take:
				temp += i

		self.log.print("Get VM names")

	def get_output(self, array):
		""" Gets the output by the shell
		"""
		return str(subprocess.Popen([self.vboxmanage] + array, stdout=subprocess.PIPE).communicate()[0])

	def get_os(self, machine_name):
		""" Gets the vitual machine os
		"""
		self.log.print("Getting OS")
		return vtools.remove_b(self.get_output(["guestproperty", "get", machine_name, "/VirtualBox/GuestInfo/OS/Product"]).replace("Value: ", "").replace("\\n", "").replace("\\r", ""))

	def remove_b(string):
		"""Removes b'' by string
		"""
		return str(string).replace("b'", "")[:-1:]
	
	def get_net(self, machine_name):
		""" Gets the vitual machine network's infos
		"""
		network = []
		temp = []
		attachments = self.get_attachments(machine_name)

		try:
			propriety = "Count"
			
			for i in range(int(str(self.get_output(["guestproperty", "get", machine_name, f"/VirtualBox/GuestInfo/Net/{propriety}"]).replace("Value: ", "").replace("\\n", "").replace("\\r", "").replace("b'", "")[:-1:]))):
				for propriety in ["Name", "V4/IP", "MAC"]:
					temp.append(vtools.remove_b(self.get_output(["guestproperty", "get", machine_name, f"/VirtualBox/GuestInfo/Net/{i}/{propriety}"]).replace("Value: ", "").replace("\\n", "").replace("\\r", "")))

				network.append(temp + [attachments[i]])
				temp = []
		except:
			pass

		self.log.print("Getted network infos")
		return network

	def get_attachments(self, machine_name):
		""" Gets the vitual machine attachment
		"""
		attachments = []

		for i in self.get_output(["showvminfo", machine_name]).replace("\\r", "").split("\\n"):
			if "NIC" in i and "disabled" not in i:
				for j in i[i.find('MAC'):].split(", "):
					if "Attachment" in j:
						attachments.append(j.replace("Attachment: ", ""))

		self.log.print("Getted attachments")
		return attachments

def laucher():
	"""Lanch all
	"""
	vtools()
		
if __name__ == "__main__":
	laucher()
