## Enabling UART port on raspbery pi4
Basically UART's port are used for other purposes such as bluetooth communivcation. So for some raison if you want to use them on your project you'll need to activate them by adding few things on the config file.

### step 1: Access to the config file
Type this on your terminal to access to the config file

    sudo nano /boot/config.txt

### step 2 : Enabling UART port
Depending on the port you wish to enable, add this to the end of your config file

    dtoverlay=vc4-fkms-v3d
    dtoverlay=uart1
    dtoverlay=uart2
    dtoverlay=uart3
    dtoverlay=uart4

i recommand you to just activate the port your wish tu use and follow the table bellow to find the correct GPIO 

### Table of UART pin on RPI4
| uart port  |     TXD      |     RXD      | Communication Port  |
|:-----------|:------------:|:------------:|:-------------------:|
| uart0 :    |    GPIO 14   |    GPIO 15   |     /dev/ttyAMA0    |
| uart1 :    |    GPIO 14   |    GPIO 15   |     /dev/ttyAMA1    |
| uart2 :    |    GPIO 0    |    GPIO 1    |     /dev/ttyAMA2    |
| uart3 :    |    GPIO 4    |    GPIO 5    |     /dev/ttyAMA3    |
| uart4 :    |    GPIO 8    |    GPIO 9    |     /dev/ttyAMA4    |

### step 3 : Save the change with ctrl+S and exit 

### step 4 : Adding permissions

NOTE: 
In this step, you need to add permissions on your OS so that your code can write and read data trougth these communication port you can do that by typing this comand through the terminal

    sudo usermod -aG dialout $USER

after that reboot your computer and check if any program use the same port as you by this command (choose the right port in your case)

    sudo lsof /dev/ttyAMA3 