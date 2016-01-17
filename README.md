# cq-formation-spark

Information for setting up for Calcul Québec's Spark workshop.

## Software Requirements

- [Git](https://git-scm.com/downloads)
- [Virtualbox 5.x](https://www.virtualbox.org/download)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- **Windows only**: [Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-ca/download/details.aspx?id=40784)

## Setup

### A few days before the workshop

In a terminal / command prompt:

1. Clone the workshop's repo:  
```git clone https://git.io/vz3sJ```
2. Download the virtual machine:
```vagrant box add calculquebec/spark```

### On the day of the workshop

In a terminal / command prompt:
1. Change directory to where you cloned thwe course repo:
`cd <FILL IN>/cq-formation-spark`
2. Pull any recent changes from the repo:
`git pull`
3. Launch the virtual machine:  
`vagrant up`
4. Access the notebook URL : [http://localhost:8001/tree]
