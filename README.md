# objectDuplication

This API based tool helps in detecting duplicate network hosts and network objects configured on the FMC. Currently the tool only helps detect duplicates, there is no remediation done programatically. This feature would be added in subsequent versions.

 
## Use Case Description

The tool is developed to address the concern of identification of duplicates in network hosts and objects present on the FMC. Over period of time, the objects grow exponentially and identification of objects that are duplicate becomes a daunting task. This utility will help address the concern by accessing the network objects over API and identifying the duplicates. The results are stored in a CSV file.

## Installation

Requirements for installation:

 1. pip3 install fireREST
 2. pip3 install netaddr
 3. pip3 install datetime
 4. pip3 install ipaddress
 
Or alternatively you can the command below to download dependencies via the requirements.txt file, this has to be executed from the downloaded script directory.

pip3 install -r ./requirements.txt


## Usage

Once the dependencies are installed and the code is pulled from GitHub, it is good to go.
Below mentioned are the steps to follow in order to execute it:

First thing to ensure is, the machine where the code will be installed should have connectivity with the FMC under concern.
It is recommended to create a different user for the tool, so that it does not block existing users from logging into the FMC for operational changes.
Navigate to the location where the script is installed.
In order to execute the script, run the below command:

python3 objectDuplicationFirepower.py 
	Enter the IP Address of the FMC: 
	Enter the username for the FMC: 
	Enter the password associated with the username entered: 
 
Once this is entered, the script logs into the FMC to pull all the network objects configured in the global domain. Once the objects are pulled, the script works through this to identification of duplicates.

Once the logic is executed, you would see the below:

Total Host Duplicates 7
Writing host duplicate 1 to CSV...
Writing host duplicate 2 to CSV...
Writing host duplicate 3 to CSV...
Writing host duplicate 4 to CSV...
Writing host duplicate 5 to CSV...
Writing host duplicate 6 to CSV...
Writing host duplicate 7 to CSV...
Total Network Duplicates 2
Writing network duplicates 1 to CSV ...
Writing network duplicates 2 to CSV ...


The CSV file is located in the same folder as that of script. You will observe 2 CSV files generated:

 1. hostDuplicates.csv  -> Contains duplicates at network hosts
 2. networkDuplicates.csv  -> Contains duplicates at network objects
 
The output generated in the CSV has the below mentioned format:

IP Network, Duplicates, Count of Duplicates

Column 1: Specifies the IP Address/Network that is under duplication
Column 2: Lists the objects that are duplicating the value.
Column 3: Count of number of objects that are duplicating the said value.

## Known issues

The tool currently works for objects created in Global domain, the duplicate identification is limited to network hosts and network objects. Network Groups and network range objects are not supported in this release and would be made available in subsequent build.

## Getting help
If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## DevNet Learning Lab
Please go to the DevNet Learning Lab for Firepower Management Center (FMC) to learn how to use these scripts:
https://developer.cisco.com/learning/modules/fmc-api

## DevNet Sandbox
The Sandbox which can implement this script is at: https://devnetsandbox.cisco.com/RM/Diagram/Index/1228cb22-b2ba-48d3-a70a-86a53f4eecc0?diagramType=Topology

## Author(s)

This project was written and is maintained by the following individuals:

* Raghunath Kulkarni <raghukul@cisco.com>
