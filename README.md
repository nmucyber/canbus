# NMU Cybersecurity: CANBUS

This section contains documentation and sample code for working with CANBUS networks used in cars, boats, and other systems.

The focus will be on setting up and using the following tools in Linux:

- ICSim
- can-utils

See the [cheat sheet](cheat_sheet.md) for tips to get started.

The python program [cansend_sample.py](cansend_sample.py) sends data using cansend.

The file [sample_icsim_candump.txt](sample_icsim_candump.txt) contains data captured while running ICSim. It includes the CAN messages to turn on the left blinker.

The python program [dump_finder.py](dump_finder.py) is a small program for sifting through a candump file.

Clone this repository from Linux using the following command:

```sh
git clone https://github.com/nmucyber/canbus
```
