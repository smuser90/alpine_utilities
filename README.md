# alpine_utilities

Production & Operations utilities for Alpine Labs


There are two branches in this repo.
'master' is for the Programming Fixtures,
'BLE-Scanner' is for the Upload Fixtures.

For the BLE_Scanner repository, the pulse-script.sh file needs to be updated for each fixture to ensure that the fixture number is correctly set. That way the fixture will scan for the correct daughter board.

This repository is designed to be pulled into the default level of a Raspberry Pi 3 Model B V1.2 that has already been set up with the correct version of raspbian. I don't think there is anything too fancy that is needed for the Upload repos, but I do recall there being some annoying BLE setup for the scanner application. To keep things simple, this repo should be pulled from a raspi that already has the correct image running. That image is stored on Steve's computer at /Users/stephenhibbs/Documents/Work/AlpineLabs/Engineering/Pulse/Manufacturing/Test_&_Prog
