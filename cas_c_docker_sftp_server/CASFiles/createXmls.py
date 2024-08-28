from sys import argv

class CreateXML():

    def __init__(self):
        self.counter = 1
        

    def _getNmsFileContent(self, productNumber):
        nmsFileContent = '''<?xml version="1.0" encoding="UTF-8"?>
<UpgradePackage name="RadioNode R41A164 release upgrade package" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <!-- The list of all ME version to which this UP is applicable -->
  <ManagedElementTypes>
    <ManagedElementType platform="RadioNode" productDesignation="RadioNode" productNumber="CXP%s" productRevision="R41A164"/>
  </ManagedElementTypes>
  <UpgradePackageContent>
    <ProductData description="N/A" productName="BASEBAND" productNumber="CXP%s" productRevision="R41A164" productionDate="2018-04-17T14:47:22" type="RadioNode"/>
  </UpgradePackageContent>
</UpgradePackage>''' % (productNumber, productNumber)
        return nmsFileContent

    def _getSmoFileContent(self, productNumber):
        smoFileContent = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE SoftwarePackage SYSTEM "/opt/ericsson/nms_smo_srv/etc/smo_softwarepackage.dtd" >
<SoftwarePackage>
	<ProductData 
	Description="Upgrade package for CXP%s/18 R1A2" 
	Name="UTRAN ERBS" 
	Number="CXP%s/18" 
	ReleaseDate="20140110" 
	Revision="R1A2" 
	Type="upgrade"/>
<!--
   Type="update" is not allowed for this template !
-->
	<NodeType>
		<NodePlatform Type="CPP"/>
		<NodeFunction>
			<ERBS/>
		</NodeFunction>
	</NodeType>
	<CommonScriptParams>
		<JobParams>
			<Parameter Name="SMO_UPGRADE_CONTROL_FILE">
				<Enum Prompt="The name of upgrade control file" 
				      Value="CXP%s_R1A2.xml">
                                <Item>CXP%s_R1A2.xml</Item>


				</Enum>
			</Parameter>
		</JobParams>
	</CommonScriptParams>

	<Activity Name="Installation">
		<Startup>
			<Immediate Default="true"/>
			<Manual/>
			<Scheduled/>
		</Startup>
		<JobParams>
			<Parameter Name="SMO_INSTALL_TRANSFER_TYPE">
				<Enum Prompt="Load Module transfer type" Value="delta">
					<Item>delta</Item>
					<Item>full</Item>
				</Enum>
			</Parameter>
			<Parameter Name="SMO_INSTALL_SELECT_TYPE">
				<Enum Prompt="Load module selection at install" Value="not selective">
					<Item>not selective</Item>
				</Enum>
			</Parameter>
		</JobParams>
	</Activity>
	<Activity Name="Verify Upgrade">
		<Startup>
			<Immediate Default="true"/>
			<Manual/>
			<Scheduled/>
		</Startup>
	</Activity>
	<Activity Name="Upgrade">
		<Startup>
			<Immediate Default="true"/>
			<Manual/>
			<Scheduled/>
		</Startup>
		<JobParams>
			<Parameter Name="SMO_UPGRADE_REBOOT">
				<Boolean Prompt="Reboot node upgrade?" Value="true"/>
			</Parameter>
		</JobParams>
	</Activity>
	<Activity Name="Confirm Upgrade">
		<Startup>
			<Immediate Default="true"/>
			<Manual/>
			<Scheduled/>
		</Startup>
	</Activity>
	<Activity Name="SWAdjust">
		<Startup>
			<Immediate Default="true"/>
			<Manual/>
			<Scheduled/>
		</Startup>
	</Activity>
        <Activity Name="20MHz Performance" Selected="false">
                <Startup>
                        <Immediate Default="true"/>
                        <Manual/>
                        <Scheduled/>
                </Startup>
                <Script RelativeFileName="cellotest2.py"/>
        </Activity>
</SoftwarePackage>
''' % (productNumber, productNumber, productNumber, productNumber)

        return smoFileContent

    def _createFile(self, productNumber, nodeType):
        fileContent = ""

        if nodeType == "NMS":
            fileContent = self._getNmsFileContent(productNumber)
        elif nodeType == "SMO":
            fileContent = self._getSmoFileContent(productNumber)

        with open("%s_CXP%s_R1A2.xml" % (nodeType, productNumber), "w") as xmlFile:
            xmlFile.write(fileContent)

    def _createProductNumber(self):
        productNumber = '%07d' % self.counter
        self.counter += 1

        return productNumber

    def run(self, nodeType, numberOfFilesToGenerate):
        
        for fileNumber in range(0, numberOfFilesToGenerate):                
            productNumber = self._createProductNumber()
            self._createFile(productNumber, nodeType)

def main(numberOfFilesToGenerate):
    createXML = CreateXML()
    nodeTypes = ["NMS", "SMO"]

    numberOfFilesForEachNodeType = numberOfFilesToGenerate/len(nodeTypes)
    for nodeType in nodeTypes:
      createXML.run(nodeType, numberOfFilesForEachNodeType)

if __name__ == "__main__":
    numberOfFilesToGenerate = int(argv[1])
    main(numberOfFilesToGenerate)
