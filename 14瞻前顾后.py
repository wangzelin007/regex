# https://blog.csdn.net/csm0912/article/details/81206848
# 前瞻：
# exp1(?=exp2) 查找exp2前面的exp1
# 后顾：
# (?<=exp2)exp1 查找exp2后面的exp1
# 负前瞻：
# exp1(?!exp2) 查找后面不是exp2的exp1
# 负后顾：
# (?<!exp2)exp1 查找前面不是exp2的exp1
# "中国人".replace(/(?<=中国)人/, "rr") // 匹配中国人中的人，将其替换为rr，结果为 中国rr
# "法国人".replace(/(?<=中国)人/, "rr") // 结果为 法国人，因为人前面不是中国，所以无法匹配到
# 数字格式化 1,123,000
# "1234567890".replace(/\B(?=(?:\d{3})+(?!\d))/g,",") // 结果：1,234,567,890，匹配的是后面是3*n个数字的非单词边界(\B)

# http://www.codebaoku.com/it-re/it-re-181088.html

# 1. (\w)((?=\1\1\1)(\1))+
# 最后的+号意思是一个或多个 意思就是 666666之匹配前四个6，而999999999只匹配前面7个，后面反正要留两个
# 因为用了(?=\1\1)，每次只匹配两个，但保证右侧有99，每次都取两个，每次都包括之前的一个
# (\w)((?=\1\1\1)(\1))+在999999999 中实际上是被匹配了6次。
# 第一次：(\w)取出第一个9，(?=\1\1\1)限定第2个9到第4个9，(\1)取出第2个9，得到99
# 第二次：(?=\1\1\1)限定第3个9到第5个9，(\1)取出第3个9，得到999
# 第三次：(?=\1\1\1)限定第4个9到第6个9，(\1)取出第4个9，得到9999
# 第四次：(?=\1\1\1)限定第5个9到第7个9，(\1)取出第5个9，得到99999
# 第五次：(?=\1\1\1)限定第6个9到第8个9，(\1)取出第6个9，得到999999
# 第六次：(?=\1\1\1)限定第7个9到第9个9，(\1)取出第7个9，得到9999999

# 2、(\w)((\1)(?=\1\1))+
# 第一次 \w取出第一个9，\1再取1个9就是 99 后面紧跟两个9才符合条件 所有第一次就是99
# 第二次 从第3个9到第四个9， 开始就\1 再取一个 999
# 第三次 匹配从第4-6个9 取一个 9999
# 第四次 从第5-7个9取一个 取一个99999
# 第五次 从第6-8个9 取一个 是 999999
# 第六次 从第7-9个9 后面仍满足取一个是 9999999
# 第七次 第8个开始右侧已经不够三个9了，所有取消匹配，匹配之前的7个9

# 3、(?<=<(\w+)>).*(?=<\/\1>)
# 详细解释下：?<=和?=都表示零宽断言，一个匹配后面一个匹配前面，
# 对应到上面的例子中，亦即.*前面必须要有<(\w+)>，后面必须要有<\/\1>。
# 零宽断言不体现到最终的匹配结果中。
# 再细看下，<(\w+)>匹配<tag>类型，\w表示数字、字母、下划线；<\/\1>中\/匹配斜杠/，
# \1表示捕获组，亦即从正则表达式左边开始的第一个小括号中的内容，注意这里不包含零宽断言的括号，在上例中表示(\w+)中的部分。
# 中间的.*表示任意多个非换行符。

# 正则表达式看懂的最好方法就是一步步分开解析：

# 1）以 '.*' 为分界，前面括号中的内容可以划分为 '？<=' 和 '<(\w+)>',其中'<(\w+)>'表示匹配尖括号里面是字母、数字或下划线的内容，类似<span>，外面还要加个括号是要实现分组；
# 而'？<='用到的是零宽断言语法，表示的是断定'<(\w+)>'后面有或没有内容，而且与内容的间隔宽度为零。
# 2）再看' .* '后面的部分，括号里面的内容可以分为 '？=' 和 '<(\/\1>',其中'？='用零宽断言表示匹配‘<(\/\1>'前面的部分，
# 而对于'<(\/\1>'，'\/'匹配‘/'符号，类似</span>,这里可能有些同学不太明白'\1'是什么意思？
# 这里用到的是捕获分组的思想，上述提到的'<(\w+)>'外面加个小括号就表示一个分组，
# 对于正则表达式的分组结果，索引 0表示匹配的整个内容，而1表示的是第1个子分组，所以这里的'\1'指向的就是前面的第一个分组'<(\w+)>'，\2表示重复第2个子项，\n表示重复第n个子项；
# 3）.* 就比较简单了，表示的是匹配 除了换行符意外的任意字符0次或多次。
# 综上，该表达式匹配的是类似html标签这种内容的，如<body>你好，正则！</body>

# 将不带style的span替换为空的正则。
# <span\s*?(?!:style)>(.[^<>]*)<\/span>
# 特殊符号："^"，"$"，"\b"。它们都有一个共同点，那就是：它们本身不匹配任何字符，只是对 "字符串的两头" 或者 "字符之间的缝隙" 附加了一个条件。
# 正向预搜索："(?=xxxxx)"，"(?!xxxxx)"
# 格式："(?=xxxxx)"，在被匹配的字符串中，它对所处的 "缝隙" 或者 "两头" 附加的条件是：所在缝隙的右侧，必须能够匹配上 xxxxx 这部分的表达式。
# 因为它只是在此作为这个缝隙上附加的条件，所以它并不影响后边的表达式去真正匹配这个缝隙之后的字符。
# 这就类似 "\b"，本身不匹配任何字符。"\b" 只是将所在缝隙之前、之后的字符取来进行了一下判断，不会影响后边的表达式来真正的匹配。
# 举例1：表达式 "Windows (?=NT|XP)" 在匹配 "Windows 98, Windows NT, Windows 2000" 时，将只匹配 "Windows NT" 中的 "Windows "，其他的 "Windows " 字样则不被匹配。
# 举例2：表达式 "(\w)((?=\1\1\1)(\1))+" 在匹配字符串 "aaa ffffff 999999999" 时，将可以匹配6个"f"的前4个，可以匹配9个"9"的前7个。
# 这个表达式可以读解成：重复4次以上的字母数字，则匹配其剩下最后2位之前的部分。当然，这个表达式可以不这样写，在此的目的是作为演示之用。
# 格式："(?!xxxxx)"，所在缝隙的右侧，必须不能匹配 xxxxx 这部分表达式。
# 举例3：表达式 "((?!\bstop\b).)+" 在匹配 "fdjka ljfdl stop fjdsla fdj" 时，将从头一直匹配到 "stop" 之前的位置，如果字符串中没有 "stop"，则匹配整个字符串。
# 举例4：表达式 "do(?!\w)" 在匹配字符串 "done, do, dog" 时，只能匹配 "do"。在本条举例中，"do" 后边使用 "(?!\w)" 和使用 "\b" 效果是一样的。

# 反向预搜索："(?<=xxxxx)"，"(?<!xxxxx)"
# 这两种格式的概念和正向预搜索是类似的，反向预搜索要求的条件是：所在缝隙的 "左侧"，两种格式分别要求必须能够匹配和必须不能够匹配指定表达式，而不是去判断右侧。
# 与 "正向预搜索" 一样的是：它们都是对所在缝隙的一种附加条件，本身都不匹配任何字符。
# 举例5：表达式 "(?<=\d{4})\d+(?=\d{4})" 在匹配 "1234567890123456" 时，将匹配除了前4个数字和后4个数字之外的中间8个数字。


chunks = { 
    "count": 10,
    "items": [
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-008",
            "score": 0.8216658,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--enable-vtpm\nEnable vTPM.\naccepted values: false, true\n\n--encryption-at-host\nEnable Host Encryption for the VM or VMSS. This will enable the encryption for all the disks including Resource/Temp disk at host itself.\naccepted values: false, true\n\n--ephemeral-os-disk\nAllows you to create an OS disk directly on the host node, providing local disk performance and faster VM/VMSS reimage time.\naccepted values: false, true\n\n--ephemeral-os-disk-placement --ephemeral-placement\nOnly applicable when used with --ephemeral-os-disk. Allows you to choose the Ephemeral OS disk provisioning location.\naccepted values: CacheDisk, ResourceDisk\n\n--eviction-policy\nThe eviction policy for the Spot priority virtual machine. Default eviction policy is Deallocate for a Spot priority virtual machine.\naccepted values: Deallocate, Delete\n\n--generate-ssh-keys\nGenerate SSH public and private key files if missing. The keys will be stored in the ~/.ssh directory.\ndefault value: False\n\n--host\nResource ID of the dedicated host that the VM will reside in. --host and --host-group can't be used together.\n\n--host-group\nName or resource ID of the dedicated host group that the VM will reside in. --host and --host-group can't be used together.",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        },
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-007",
            "score": 0.81135434,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--data-disk-delete-option\nSpecify whether data disk should be deleted or detached upon VM deletion. If a single data disk is attached, the allowed values are Delete and Detach. For multiple data disks are attached, please use &quot;&lt;data_disk&gt;=Delete &lt;data_disk2&gt;=Detach&quot; to configure each disk.\n\n--data-disk-encryption-sets\nNames or IDs (space delimited) of disk encryption sets for data disks.\n\n--data-disk-sizes-gb\nSpace-separated empty managed data disk sizes in GB to create.\n\n--disable-integrity-monitoring\nDisable the default behavior of installing guest attestation extension and enabling System Assigned Identity for Trusted Launch enabled VMs and VMSS.\ndefault value: False\n\n--disable-integrity-monitoring-autoupgrade\nDisable auto upgrade of guest attestation extension for Trusted Launch enabled VMs and VMSS.\ndefault value: False\n\n--disk-controller-type\nSpecify the disk controller type configured for the VM or VMSS.\naccepted values: NVMe, SCSI\n\n--edge-zone\nThe name of edge zone.\n\n--enable-agent\nIndicates whether virtual machine agent should be provisioned on the virtual machine. When this property is not specified, default behavior is to set it to true. This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later.\naccepted values: false, true\n\n--enable-auto-update\nIndicate whether Automatic Updates is enabled for the Windows virtual machine.\naccepted values: false, true\n\n--enable-hibernation\nThe flag that enable or disable hibernation capability on the VM.\naccepted values: false, true\n\n--enable-hotpatching\nPatch VMs without requiring a reboot. --enable-agent must be set and --patch-mode must be set to AutomaticByPlatform.\naccepted values: false, true\n\n--enable-secure-boot\nEnable secure boot.\naccepted values: false, true",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        },
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-011",
            "score": 0.8105075,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--os-disk-size-gb\nOS disk size in GB to create.\n\n--os-type\nType of OS installed on a custom VHD. Do not use when specifying an URN or URN alias.\naccepted values: linux, windows\n\n--patch-mode\nMode of in-guest patching to IaaS virtual machine. Allowed values for Windows VM: AutomaticByOS, AutomaticByPlatform, Manual. Allowed values for Linux VM: AutomaticByPlatform, ImageDefault. Manual - You control the application of patches to a virtual machine. You do this by applying patches manually inside the VM. In this mode, automatic updates are disabled; the paramater --enable-auto-update must be false. AutomaticByOS - The virtual machine will automatically be updated by the OS. The parameter --enable-auto-update must be true. AutomaticByPlatform - the virtual machine will automatically updated by the OS. ImageDefault - The virtual machine's default patching configuration is used. The parameter --enable-agent and --enable-auto-update must be true.\naccepted values: AutomaticByOS, AutomaticByPlatform, ImageDefault, Manual\n\n--plan-name\nPlan name.\n\n--plan-product\nPlan product.\n\n--plan-promotion-code\nPlan promotion code.\n\n--plan-publisher\nPlan publisher.\n\n--platform-fault-domain\nSpecify the scale set logical fault domain into which the virtual machine will be created. By default, the virtual machine will be automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the virtualMachineScaleSet property of this virtual machine is set. The virtual machine scale set that is referenced, must have platform fault domain count. This property cannot be updated once the virtual machine is created. Fault domain assignment can be viewed in the virtual machine instance view.\n\n--ppg\nThe name or ID of the proximity placement group the VM should be associated with.",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        },
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-006",
            "score": 0.80799973,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--capacity-reservation-group --crg\nThe ID or name of the capacity reservation group that is used to allocate. Pass in &quot;None&quot; to disassociate the capacity reservation group. Please note that if you want to delete a VM/VMSS that has been associated with capacity reservation group, you need to disassociate the capacity reservation group first.\n\n--computer-name\nThe host OS name of the virtual machine. Defaults to the name of the VM.\n\n--count\nNumber of virtual machines to create. Value range is [2, 250], inclusive. Don't specify this parameter if you want to create a normal single VM. The VMs are created in parallel. The output of this command is an array of VMs instead of one single VM. Each VM has its own public IP, NIC. VNET and NSG are shared. It is recommended that no existing public IP, NIC, VNET and NSG are in resource group. When --count is specified, --attach-data-disks, --attach-os-disk, --boot-diagnostics-storage, --computer-name, --host, --host-group, --nics, --os-disk-name, --private-ip-address, --public-ip-address, --public-ip-address-dns-name, --storage-account, --storage-container-name, --subnet, --use-unmanaged-disk, --vnet-name are not allowed.\n\n--custom-data\nCustom init script file or text (cloud-init, cloud-config, etc..).\n\n--data-disk-caching\nStorage caching type for data disk(s), including 'None', 'ReadOnly', 'ReadWrite', etc. Use a singular value to apply on all disks, or use &lt;lun&gt;=&lt;vaule1&gt; &lt;lun&gt;=&lt;value2&gt; to configure individual disk.",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        },
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-013",
            "score": 0.8079073,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--security-type\nSpecify the security type of the virtual machine.\naccepted values: ConfidentialVM, Standard, TrustedLaunch\n\n--size\nThe VM size to be created. See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.\ndefault value: Standard_DS1_v2\nvalue from: az vm list-sizes\n\n--specialized\nIndicate whether the source image is specialized.\naccepted values: false, true\n\n--ssh-dest-key-path\nDestination file path on the VM for the SSH key. If the file already exists, the specified key(s) are appended to the file. Destination path for SSH public keys is currently limited to its default value &quot;/home/username/.ssh/authorized_keys&quot; due to a known issue in Linux provisioning agent.\n\n--ssh-key-name\nUse it as public key in virtual machine. It should be an existing SSH key resource in Azure.\n\n--ssh-key-values\nSpace-separated list of SSH public keys or public key file paths.\n\n--storage-account\nOnly applicable when used with --use-unmanaged-disk. The name to use when creating a new storage account or referencing an existing one. If omitted, an appropriate storage account in the same resource group and location will be used, or a new one will be created.\n\n--storage-container-name\nOnly applicable when used with --use-unmanaged-disk. Name of the storage container for the VM OS disk. Default: vhds.",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        },
        {
            "id": "36a73dcf-783f-c429-7526-2c510b8c2fab-004",
            "score": 0.80739456,
            "title": "az vmware private-cloud create",
            "content": "### Command\naz vmware private-cloud create\n\n### Summary\nCreate a private cloud.\n\n### Required Parameters\n\n--cluster-size\nNumber of hosts for the default management cluster. Minimum of 3 and maximum of 16.\n\n--name -n\nName of the private cloud.\n\n--network-block\nA subnet at least of size /22. Make sure the CIDR format is conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is between 0 and 22.\n\n--resource-group -g\nName of resource group. You can configure the default group using az configure --defaults group=&lt;name&gt;.\n\n--sku\nThe product SKU.\n\n### Optional Parameters\n\n--accept-eula\nAccept the end-user license agreement without prompting.\ndefault value: False\n\n--internet\nConnectivity to internet. Specify &quot;Enabled&quot; or &quot;Disabled&quot;.\n\n--location -l\nLocation. Values from: az account list-locations. You can configure the default location using az configure --defaults location=&lt;location&gt;.\n\n--mi-system-assigned\nEnable a system assigned identity.\ndefault value: False\n\n--nsxt-password\nNSX-T Manager password.\n\n--secondary-zone\nThe secondary availability zone for the private cloud.\n\n--strategy\nThe availability strategy for the private cloud.\naccepted values: DualZone, SingleZone\n\n--tags\nSpace-separated tags: key[=value] [key[=value] ...]. Use &quot;&quot; to clear existing tags.\n\n--vcenter-password\nVCenter admin password.\n\n--yes\nDelete without confirmation.\ndefault value: False\n\n--zone\nThe primary availability zone for the private cloud.",
            "lastModifiedDateTime": "2023-08-22T21:32:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vmware/private-cloud?view=azure-cli-latest#az-vmware-private-cloud-create",
            "pageType": "azure-cli",
            "reportingMeta": []
        },
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-012",
            "score": 0.8059297,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--priority\nPriority. Use 'Spot' to run short-lived workloads in a cost-effective way. 'Low' enum will be deprecated in the future. Please use 'Spot' to deploy Azure spot VM and/or VMSS. Default to Regular.\naccepted values: Low, Regular, Spot\n\n--private-ip-address\nStatic private IP address (e.g. 10.0.0.5).\n\n--public-ip-address\nName of the public IP address when creating one (default) or referencing an existing one. Can also reference an existing public IP by ID or specify &quot;&quot; for None ('&quot;&quot;' in Azure CLI using PowerShell or --% operator). For Azure CLI using powershell core edition 7.3.4, specify  or &quot;&quot; (--public-ip-address  or --public-ip-address &quot;&quot;).\n\n--public-ip-address-allocation\naccepted values: dynamic, static\n\n--public-ip-address-dns-name\nGlobally unique DNS name for a newly created public IP.\n\n--public-ip-sku\nPublic IP SKU. It is set to Basic by default. The public IP is supported to be created on edge zone only when it is 'Standard'.\naccepted values: Basic, Standard\n\n--role\nRole name or id the system assigned identity will have.\n\n--scope\nScope that the system assigned identity can access.\n\n--secrets\nOne or many Key Vault secrets as JSON strings or files via @{path} containing [{ &quot;sourceVault&quot;: { &quot;id&quot;: &quot;value&quot; }, &quot;vaultCertificates&quot;: [{ &quot;certificateUrl&quot;: &quot;value&quot;, &quot;certificateStore&quot;: &quot;cert store name (only on windows)&quot;}] }].",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        },
        {
            "id": "5acade39-a3d8-174e-cbb2-ab894dd57682-002",
            "score": 0.8053367,
            "title": "az scvmm vm create",
            "content": "### Command\naz scvmm vm create\n\n### Summary\nCreate VM resource.\n\n### Optional Parameters\n\n--no-wait\nDo not wait for the long-running operation to finish.\ndefault value: False\n\n--tags\nSpace-separated tags: key[=value] [key[=value] ...]. Use &quot;&quot; to clear existing tags.\n\n--vm-template -t\nName or ID of the vm template for deploying the vm.\n\n--vmmserver -v\nName or ID of the vmmserver that is managing this resource.",
            "lastModifiedDateTime": "2023-08-22T21:32:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/scvmm/vm?view=azure-cli-latest#az-scvmm-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": []
        },
        {
            "id": "5acade39-a3d8-174e-cbb2-ab894dd57682-001",
            "score": 0.80468285,
            "title": "az scvmm vm create",
            "content": "### Command\naz scvmm vm create\n\n### Summary\nCreate VM resource.\n\n### Required Parameters\n\n--custom-location\nName or ID of the custom location that will manage this resource.\n\n--location -l\nLocation. Values from: az account list-locations. You can configure the default location using az configure --defaults location=&lt;location&gt;.\n\n--name -n\nName of the resource.\n\n--resource-group -g\nName of resource group. You can configure the default group using az configure --defaults group=&lt;name&gt;.\n\n### Optional Parameters\n\n--admin-password\nAdmin password for the vm.\n\n--availability-sets -a\nList of the name or the ID of the availability sets for the vm.\n\n--cloud -c\nName or ID of the cloud for deploying the vm.\n\n--cpu-count\nNumber of desired vCPUs for the vm.\n\n--disk\nDisk overrides for the vm.Usage: --disk name=&lt;&gt; disk-size=&lt;&gt; template-disk-id=&lt;&gt; bus-type=&lt;&gt; bus=&lt;&gt; lun=&lt;&gt; vhd-type=&lt;&gt; qos-name=&lt;&gt; qos-id=&lt;&gt;.\n\n--dynamic-memory-enabled\nIf dynamic memory should be enabled.\naccepted values: false, true\n\n--dynamic-memory-max\nDynamicMemoryMax in MBs for the vm.\n\n--dynamic-memory-min\nDynamicMemoryMin in MBs for the vm.\n\n--inventory-item -i\nName or ID of the inventory item.\n\n--memory-size\nDesired memory size in MBs for the vm.\n\n--nic\nNetwork overrides for the vm.Usage: --nic name=&lt;&gt; network=&lt;&gt; ipv4-address-type=&lt;&gt; ipv6-address-type=&lt;&gt; mac-address-type=&lt;&gt; mac-address=&lt;&gt;.",
            "lastModifiedDateTime": "2023-08-22T21:32:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/scvmm/vm?view=azure-cli-latest#az-scvmm-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": []
        },
        {
            "id": "29506b2a-2875-5e9f-308a-a6fe4653ae0d-009",
            "score": 0.8040971,
            "title": "az vm create",
            "content": "### Command\naz vm create\n\n### Summary\nCreate an Azure Virtual Machine.\n\n### Optional Parameters\n\n--image\nThe name of the operating system image as a URN alias, URN, custom image name or ID, custom image version ID, or VHD blob URI. In addition, it also supports shared gallery image. Please use the image alias including the version of the distribution you want to use. For example: please use Debian11 instead of Debian.' This parameter is required unless using --attach-os-disk. Valid URN format: &quot;Publisher:Offer:Sku:Version&quot;. For more information, see https://docs.microsoft.com/azure/virtual-machines/linux/cli-ps-findimage.\nvalue from: az sig image-version show-shared, az vm image list, az vm image show\n\n--license-type\nSpecifies that the Windows image or disk was licensed on-premises. To enable Azure Hybrid Benefit for Windows Server, use 'Windows_Server'. To enable Multi-tenant Hosting Rights for Windows 10, use 'Windows_Client'. For more information see the Azure Windows VM online docs.\naccepted values: None, RHEL_BASE, RHEL_BASESAPAPPS, RHEL_BASESAPHA, RHEL_BYOS, RHEL_ELS_6, RHEL_EUS, RHEL_SAPAPPS, RHEL_SAPHA, SLES, SLES_BYOS, SLES_HPC, SLES_SAP, SLES_STANDARD, UBUNTU, UBUNTU_PRO, Windows_Client, Windows_Server\n\n--location -l\nLocation in which to create VM and related resources. If default location is not configured, will default to the resource group's location.\n\n--max-price\nThe maximum price (in US Dollars) you are willing to pay for a Spot VM/VMSS. -1 indicates that the Spot VM/VMSS should not be evicted for price reasons.",
            "lastModifiedDateTime": "2023-09-05T05:16:00+00:00",
            "depotName": "Azure.azure-cli-docs",
            "contentUrl": "https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create",
            "pageType": "azure-cli",
            "reportingMeta": [
                "virtual-machines"
            ]
        }
    ]
}

data = [
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--enable-vtpm",
        "desc": "Enable vTPM.\naccepted values: false, true"
      },
      {
        "name": "--encryption-at-host",
        "desc": "Enable Host Encryption for the VM or VMSS. This will enable the encryption for all the disks including Resource/Temp disk at host itself.\naccepted values: false, true"
      },
      {
        "name": "--ephemeral-os-disk",
        "desc": "Allows you to create an OS disk directly on the host node, providing local disk performance and faster VM/VMSS reimage time.\naccepted values: false, true"
      },
      {
        "name": "--ephemeral-os-disk-placement --ephemeral-placement",
        "desc": "Only applicable when used with --ephemeral-os-disk. Allows you to choose the Ephemeral OS disk provisioning location.\naccepted values: CacheDisk, ResourceDisk"
      },
      {
        "name": "--eviction-policy",
        "desc": "The eviction policy for the Spot priority virtual machine. Default eviction policy is Deallocate for a Spot priority virtual machine.\naccepted values: Deallocate, Delete"
      },
      {
        "name": "--generate-ssh-keys",
        "desc": "Generate SSH public and private key files if missing. The keys will be stored in the ~/.ssh directory.\ndefault value: False"
      },
      {
        "name": "--host",
        "desc": "Resource ID of the dedicated host that the VM will reside in. --host and --host-group can't be used together."
      },
      {
        "name": "--host-group",
        "desc": "Name or resource ID of the dedicated host group that the VM will reside in. --host and --host-group can't be used together."
      }
    ],
    "score": 0.8216658
  },
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--data-disk-delete-option",
        "desc": "Specify whether data disk should be deleted or detached upon VM deletion. If a single data disk is attached, the allowed values are Delete and Detach. For multiple data disks are attached, please use &quot;&lt;data_disk&gt;=Delete &lt;data_disk2&gt;=Detach&quot; to configure each disk."
      },
      {
        "name": "--data-disk-encryption-sets",
        "desc": "Names or IDs (space delimited) of disk encryption sets for data disks."
      },
      {
        "name": "--data-disk-sizes-gb",
        "desc": "Space-separated empty managed data disk sizes in GB to create."
      },
      {
        "name": "--disable-integrity-monitoring",
        "desc": "Disable the default behavior of installing guest attestation extension and enabling System Assigned Identity for Trusted Launch enabled VMs and VMSS.\ndefault value: False"
      },
      {
        "name": "--disable-integrity-monitoring-autoupgrade",
        "desc": "Disable auto upgrade of guest attestation extension for Trusted Launch enabled VMs and VMSS.\ndefault value: False"
      },
      {
        "name": "--disk-controller-type",
        "desc": "Specify the disk controller type configured for the VM or VMSS.\naccepted values: NVMe, SCSI"
      },
      {
        "name": "--edge-zone",
        "desc": "The name of edge zone."
      },
      {
        "name": "--enable-agent",
        "desc": "Indicates whether virtual machine agent should be provisioned on the virtual machine. When this property is not specified, default behavior is to set it to true. This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later.\naccepted values: false, true"
      },
      {
        "name": "--enable-auto-update",
        "desc": "Indicate whether Automatic Updates is enabled for the Windows virtual machine.\naccepted values: false, true"
      },
      {
        "name": "--enable-hibernation",
        "desc": "The flag that enable or disable hibernation capability on the VM.\naccepted values: false, true"
      },
      {
        "name": "--enable-hotpatching",
        "desc": "Patch VMs without requiring a reboot. --enable-agent must be set and --patch-mode must be set to AutomaticByPlatform.\naccepted values: false, true"
      },
      {
        "name": "--enable-secure-boot",
        "desc": "Enable secure boot.\naccepted values: false, true"
      }
    ],
    "score": 0.81135434
  },
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--os-disk-size-gb",
        "desc": "OS disk size in GB to create."
      },
      {
        "name": "--os-type",
        "desc": "Type of OS installed on a custom VHD. Do not use when specifying an URN or URN alias.\naccepted values: linux, windows"
      },
      {
        "name": "--patch-mode",
        "desc": "Mode of in-guest patching to IaaS virtual machine. Allowed values for Windows VM: AutomaticByOS, AutomaticByPlatform, Manual. Allowed values for Linux VM: AutomaticByPlatform, ImageDefault. Manual - You control the application of patches to a virtual machine. You do this by applying patches manually inside the VM. In this mode, automatic updates are disabled; the paramater --enable-auto-update must be false. AutomaticByOS - The virtual machine will automatically be updated by the OS. The parameter --enable-auto-update must be true. AutomaticByPlatform - the virtual machine will automatically updated by the OS. ImageDefault - The virtual machine's default patching configuration is used. The parameter --enable-agent and --enable-auto-update must be true.\naccepted values: AutomaticByOS, AutomaticByPlatform, ImageDefault, Manual"
      },
      {
        "name": "--plan-name",
        "desc": "Plan name."
      },
      {
        "name": "--plan-product",
        "desc": "Plan product."
      },
      {
        "name": "--plan-promotion-code",
        "desc": "Plan promotion code."
      },
      {
        "name": "--plan-publisher",
        "desc": "Plan publisher."
      },
      {
        "name": "--platform-fault-domain",
        "desc": "Specify the scale set logical fault domain into which the virtual machine will be created. By default, the virtual machine will be automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the virtualMachineScaleSet property of this virtual machine is set. The virtual machine scale set that is referenced, must have platform fault domain count. This property cannot be updated once the virtual machine is created. Fault domain assignment can be viewed in the virtual machine instance view."
      },
      {
        "name": "--ppg",
        "desc": "The name or ID of the proximity placement group the VM should be associated with."
      }
    ],
    "score": 0.8105075
  },
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--capacity-reservation-group --crg",
        "desc": "The ID or name of the capacity reservation group that is used to allocate. Pass in &quot;None&quot; to disassociate the capacity reservation group. Please note that if you want to delete a VM/VMSS that has been associated with capacity reservation group, you need to disassociate the capacity reservation group first."
      },
      {
        "name": "--computer-name",
        "desc": "The host OS name of the virtual machine. Defaults to the name of the VM."
      },
      {
        "name": "--count",
        "desc": "Number of virtual machines to create. Value range is [2, 250], inclusive. Don't specify this parameter if you want to create a normal single VM. The VMs are created in parallel. The output of this command is an array of VMs instead of one single VM. Each VM has its own public IP, NIC. VNET and NSG are shared. It is recommended that no existing public IP, NIC, VNET and NSG are in resource group. When --count is specified, --attach-data-disks, --attach-os-disk, --boot-diagnostics-storage, --computer-name, --host, --host-group, --nics, --os-disk-name, --private-ip-address, --public-ip-address, --public-ip-address-dns-name, --storage-account, --storage-container-name, --subnet, --use-unmanaged-disk, --vnet-name are not allowed."
      },
      {
        "name": "--custom-data",
        "desc": "Custom init script file or text (cloud-init, cloud-config, etc..)."
      },
      {
        "name": "--data-disk-caching",
        "desc": "Storage caching type for data disk(s), including 'None', 'ReadOnly', 'ReadWrite', etc. Use a singular value to apply on all disks, or use &lt;lun&gt;=&lt;vaule1&gt; &lt;lun&gt;=&lt;value2&gt; to configure individual disk."
      }
    ],
    "score": 0.80799973
  },
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--security-type",
        "desc": "Specify the security type of the virtual machine.\naccepted values: ConfidentialVM, Standard, TrustedLaunch"
      },
      {
        "name": "--size",
        "desc": "The VM size to be created. See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.\ndefault value: Standard_DS1_v2\nvalue from: az vm list-sizes"
      },
      {
        "name": "--specialized",
        "desc": "Indicate whether the source image is specialized.\naccepted values: false, true"
      },
      {
        "name": "--ssh-dest-key-path",
        "desc": "Destination file path on the VM for the SSH key. If the file already exists, the specified key(s) are appended to the file. Destination path for SSH public keys is currently limited to its default value &quot;/home/username/.ssh/authorized_keys&quot; due to a known issue in Linux provisioning agent."
      },
      {
        "name": "--ssh-key-name",
        "desc": "Use it as public key in virtual machine. It should be an existing SSH key resource in Azure."
      },
      {
        "name": "--ssh-key-values",
        "desc": "Space-separated list of SSH public keys or public key file paths."
      },
      {
        "name": "--storage-account",
        "desc": "Only applicable when used with --use-unmanaged-disk. The name to use when creating a new storage account or referencing an existing one. If omitted, an appropriate storage account in the same resource group and location will be used, or a new one will be created."
      },
      {
        "name": "--storage-container-name",
        "desc": "Only applicable when used with --use-unmanaged-disk. Name of the storage container for the VM OS disk. Default: vhds."
      }
    ],
    "score": 0.8079073
  },
  {
    "command": "az vmware private-cloud create",
    "summary": "Create a private cloud.",
    "optional parameters": [
      {
        "name": "--accept-eula",
        "desc": "Accept the end-user license agreement without prompting.\ndefault value: False"
      },
      {
        "name": "--internet",
        "desc": "Connectivity to internet. Specify &quot;Enabled&quot; or &quot;Disabled&quot;."
      },
      {
        "name": "--location -l",
        "desc": "Location. Values from: az account list-locations. You can configure the default location using az configure --defaults location=&lt;location&gt;."
      },
      {
        "name": "--mi-system-assigned",
        "desc": "Enable a system assigned identity.\ndefault value: False"
      },
      {
        "name": "--nsxt-password",
        "desc": "NSX-T Manager password."
      },
      {
        "name": "--secondary-zone",
        "desc": "The secondary availability zone for the private cloud."
      },
      {
        "name": "--strategy",
        "desc": "The availability strategy for the private cloud.\naccepted values: DualZone, SingleZone"
      },
      {
        "name": "--tags",
        "desc": "Space-separated tags: key[=value] [key[=value] ...]. Use &quot;&quot; to clear existing tags."
      },
      {
        "name": "--vcenter-password",
        "desc": "VCenter admin password."
      },
      {
        "name": "--yes",
        "desc": "Delete without confirmation.\ndefault value: False"
      },
      {
        "name": "--zone",
        "desc": "The primary availability zone for the private cloud."
      }
    ],
    "required parameters": [
      {
        "name": "--cluster-size",
        "desc": "Number of hosts for the default management cluster. Minimum of 3 and maximum of 16."
      },
      {
        "name": "--name -n",
        "desc": "Name of the private cloud."
      },
      {
        "name": "--network-block",
        "desc": "A subnet at least of size /22. Make sure the CIDR format is conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is between 0 and 22."
      },
      {
        "name": "--resource-group -g",
        "desc": "Name of resource group. You can configure the default group using az configure --defaults group=&lt;name&gt;."
      },
      {
        "name": "--sku",
        "desc": "The product SKU."
      }
    ],
    "score": 0.80739456
  },
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--priority",
        "desc": "Priority. Use 'Spot' to run short-lived workloads in a cost-effective way. 'Low' enum will be deprecated in the future. Please use 'Spot' to deploy Azure spot VM and/or VMSS. Default to Regular.\naccepted values: Low, Regular, Spot"
      },
      {
        "name": "--private-ip-address",
        "desc": "Static private IP address (e.g. 10.0.0.5)."
      },
      {
        "name": "--public-ip-address",
        "desc": "Name of the public IP address when creating one (default) or referencing an existing one. Can also reference an existing public IP by ID or specify &quot;&quot; for None ('&quot;&quot;' in Azure CLI using PowerShell or --% operator). For Azure CLI using powershell core edition 7.3.4, specify  or &quot;&quot; (--public-ip-address  or --public-ip-address &quot;&quot;)."
      },
      {
        "name": "--public-ip-address-allocation",
        "desc": "accepted values: dynamic, static"
      },
      {
        "name": "--public-ip-address-dns-name",
        "desc": "Globally unique DNS name for a newly created public IP."
      },
      {
        "name": "--public-ip-sku",
        "desc": "Public IP SKU. It is set to Basic by default. The public IP is supported to be created on edge zone only when it is 'Standard'.\naccepted values: Basic, Standard"
      },
      {
        "name": "--role",
        "desc": "Role name or id the system assigned identity will have."
      },
      {
        "name": "--scope",
        "desc": "Scope that the system assigned identity can access."
      },
      {
        "name": "--secrets",
        "desc": "One or many Key Vault secrets as JSON strings or files via @{path} containing [{ &quot;sourceVault&quot;: { &quot;id&quot;: &quot;value&quot; }, &quot;vaultCertificates&quot;: [{ &quot;certificateUrl&quot;: &quot;value&quot;, &quot;certificateStore&quot;: &quot;cert store name (only on windows)&quot;}] }]."
      }
    ],
    "score": 0.8059297
  },
  {
    "command": "az scvmm vm create",
    "summary": "Create VM resource.",
    "optional parameters": [
      {
        "name": "--no-wait",
        "desc": "Do not wait for the long-running operation to finish.\ndefault value: False"
      },
      {
        "name": "--tags",
        "desc": "Space-separated tags: key[=value] [key[=value] ...]. Use &quot;&quot; to clear existing tags."
      },
      {
        "name": "--vm-template -t",
        "desc": "Name or ID of the vm template for deploying the vm."
      },
      {
        "name": "--vmmserver -v",
        "desc": "Name or ID of the vmmserver that is managing this resource."
      }
    ],
    "score": 0.8053367
  },
  {
    "command": "az scvmm vm create",
    "summary": "Create VM resource.",
    "optional parameters": [
      {
        "name": "--admin-password",
        "desc": "Admin password for the vm."
      },
      {
        "name": "--availability-sets -a",
        "desc": "List of the name or the ID of the availability sets for the vm."
      },
      {
        "name": "--cloud -c",
        "desc": "Name or ID of the cloud for deploying the vm."
      },
      {
        "name": "--cpu-count",
        "desc": "Number of desired vCPUs for the vm."
      },
      {
        "name": "--disk",
        "desc": "Disk overrides for the vm.Usage: --disk name=&lt;&gt; disk-size=&lt;&gt; template-disk-id=&lt;&gt; bus-type=&lt;&gt; bus=&lt;&gt; lun=&lt;&gt; vhd-type=&lt;&gt; qos-name=&lt;&gt; qos-id=&lt;&gt;."
      },
      {
        "name": "--dynamic-memory-enabled",
        "desc": "If dynamic memory should be enabled.\naccepted values: false, true"
      },
      {
        "name": "--dynamic-memory-max",
        "desc": "DynamicMemoryMax in MBs for the vm."
      },
      {
        "name": "--dynamic-memory-min",
        "desc": "DynamicMemoryMin in MBs for the vm."
      },
      {
        "name": "--inventory-item -i",
        "desc": "Name or ID of the inventory item."
      },
      {
        "name": "--memory-size",
        "desc": "Desired memory size in MBs for the vm."
      },
      {
        "name": "--nic",
        "desc": "Network overrides for the vm.Usage: --nic name=&lt;&gt; network=&lt;&gt; ipv4-address-type=&lt;&gt; ipv6-address-type=&lt;&gt; mac-address-type=&lt;&gt; mac-address=&lt;&gt;."
      }
    ],
    "required parameters": [
      {
        "name": "--custom-location",
        "desc": "Name or ID of the custom location that will manage this resource."
      },
      {
        "name": "--location -l",
        "desc": "Location. Values from: az account list-locations. You can configure the default location using az configure --defaults location=&lt;location&gt;."
      },
      {
        "name": "--name -n",
        "desc": "Name of the resource."
      },
      {
        "name": "--resource-group -g",
        "desc": "Name of resource group. You can configure the default group using az configure --defaults group=&lt;name&gt;."
      }
    ],
    "score": 0.80468285
  },
  {
    "command": "az vm create",
    "summary": "Create an Azure Virtual Machine.",
    "optional parameters": [
      {
        "name": "--image",
        "desc": "The name of the operating system image as a URN alias, URN, custom image name or ID, custom image version ID, or VHD blob URI. In addition, it also supports shared gallery image. Please use the image alias including the version of the distribution you want to use. For example: please use Debian11 instead of Debian.' This parameter is required unless using --attach-os-disk. Valid URN format: &quot;Publisher:Offer:Sku:Version&quot;. For more information, see https://docs.microsoft.com/azure/virtual-machines/linux/cli-ps-findimage.\nvalue from: az sig image-version show-shared, az vm image list, az vm image show"
      },
      {
        "name": "--license-type",
        "desc": "Specifies that the Windows image or disk was licensed on-premises. To enable Azure Hybrid Benefit for Windows Server, use 'Windows_Server'. To enable Multi-tenant Hosting Rights for Windows 10, use 'Windows_Client'. For more information see the Azure Windows VM online docs.\naccepted values: None, RHEL_BASE, RHEL_BASESAPAPPS, RHEL_BASESAPHA, RHEL_BYOS, RHEL_ELS_6, RHEL_EUS, RHEL_SAPAPPS, RHEL_SAPHA, SLES, SLES_BYOS, SLES_HPC, SLES_SAP, SLES_STANDARD, UBUNTU, UBUNTU_PRO, Windows_Client, Windows_Server"
      },
      {
        "name": "--location -l",
        "desc": "Location in which to create VM and related resources. If default location is not configured, will default to the resource group's location."
      },
      {
        "name": "--max-price",
        "desc": "The maximum price (in US Dollars) you are willing to pay for a Spot VM/VMSS. -1 indicates that the Spot VM/VMSS should not be evicted for price reasons."
      }
    ],
    "score": 0.8040971
  }
]

import re

def convert_chunks_to_json(chunks):
    data = []
    for chunk in chunks["items"]:
        chunk2json = {}
        chunk2json["command"] = chunk["title"]
        chunk2json["summary"] = re.search(r"### Summary\n([\s\S]*?)(?=\n\n###|\Z)", chunk["content"]).group(1)
        optional_params = []
        optional_params_content = re.search(r"### Optional Parameters\n\n([\s\S]*?)(?=\n\n###|\Z)", chunk["content"])
        optional_params_content = optional_params_content.group(1) if optional_params_content else ""
        params = re.findall(r"(--[\s\S]*?)(?=\n\n--|$)", optional_params_content)
        for param in params:
            item = {}
            item["name"] = param.split("\n")[0]
            item["desc"] = param[len(item["name"])+1:]
            optional_params.append(item)
        require_params = []
        require_params_desc = re.search(r"### Required Parameters\n\n([\s\S]*?)(?=\n\n###|\Z)", chunk["content"])
        require_params_desc = require_params_desc.group(1) if require_params_desc else ""
        params = re.findall(r"(--[\s\S]*?)(?=\n\n--|$)", require_params_desc)
        for param in params:
            item = {}
            item["name"] = param.split("\n")[0]
            item["desc"] = param[len(item["name"])+1:]
            require_params.append(item)
        if optional_params:
            chunk2json["optional parameters"] = optional_params
        if require_params:
            chunk2json["required parameters"] = require_params
        chunk2json["score"] = chunk["score"]
        data.append(chunk2json)
    print(data)
    return data


def test_convert_chunks_to_json(chunks):
    ref = convert_chunks_to_json(chunks)
    assert ref == data


if __name__ == '__main__':
    convert_chunks_to_json(chunks)
    test_convert_chunks_to_json