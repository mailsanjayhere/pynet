$ cat config_test.py
import cli

mac_to_name={
"abcd_0001_efab":"switch1",
"defg_dfad_0123":"switch2"
}

# if some sample config to be applied
cli.configurep(["hostname switch_test"])
cli.configurep(["!"])
cli.configurep(["end"])

# Determine the hardware address of the device
output=cli.cli('show interface Gi0/0 | include Hardware')
mac=str(output).split()[-1].strip(")").replace(".","_")

# Download teh specific config and apply it to the device
filename=mac_to_name[mac]+"_"+mac+".cfg"
cli.execute("copy tftp://10.15.52.14/"+filename+" running-config\n")
