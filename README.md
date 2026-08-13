## Table of UART pin on RPI4
                    TXD             RXD                   Communication Port
uart0 :          GPIO 14          GPIO 15                   /dev/ttyAMA0
uart1 :          GPIO 0           GPIO 1                    /dev/ttyAMA1
uart2 :          GPIO 4           GPIO 5                    /dev/ttyAMA2
uart3 :          GPIO 8           GPIO 9                    /dev/ttyAMA3
uart4 :          GPIO 12          GPIO 13                   /dev/ttyAMA4

after knowing all of this possibilities you need to add permissions on your os so that your code can write and read data trougth these communication port you can do that by typing this comand

    sudo usermod -aG dialout $USER

after that reboot your computer and check if any program use the same port by this command

    sudo lsof /dev/ttyAMA2 (chose the right port in your case)