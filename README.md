# mac_changer is a python based tool which allows to change mac address of a linux environment
 .




#  How to use:

Pre requiste: Python3 and pip3 installed 

	      sudo apt-get install python3 
	      
	      sudo apt-get install python3-pip
	      
	      sudo pip3 install get-nic		
	      
**********************         Installation *************************

git-clone https://github.com/UjjwalSaini/mac_changer.git

cd mac_changer

python3 mac_changer.py -options


Usage: mac_changer.py [options]

Options:

  -h, --help            show this help message and exit
  
  -i INTERFACE, --interface=INTERFACE
  
                        Enter the interface to change its mac value
			
  -m NEW_MAC, --mac=NEW_MAC
  
                        Enter the new mac address for the interface

   Omit the New_Mac option if you want a random mac address	
