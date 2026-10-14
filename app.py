import streamlit as st
import ipaddress

st.set_page_config(
    page_title="Network Configuration Generator",
    page_icon="🌐"
)

st.title("Network Configuration Generator")

st.write("Generate Cisco Switch Configuration Commands")

vlan_id = st.number_input(
    "VLAN ID",
    min_value=1,
    max_value=4094,
    value=10
)

vlan_name = st.text_input("VLAN Name", "SALES")
interface = st.text_input("Switch Interface", "Fa0/1")

network = st.text_input(
    "Network",
    "192.168.10.0/24"
)

if st.button("Calculate Subnet"):
    try:
        net = ipaddress.ip_network(network, strict=False)

        st.write("Network Address:", net.network_address)
        st.write("Broadcast Address:", net.broadcast_address)
        st.write("Subnet Mask:", net.netmask)
        st.write("Total Addresses:", net.num_addresses)

    except ValueError:
        st.error("Please enter a valid network.")

if st.button("Generate Configuration"):
    if not vlan_name.strip() or not interface.strip():
        st.error("Please enter VLAN name and interface.")
    else:
        config = f"""enable
configure terminal
vlan {vlan_id}
name {vlan_name.strip()}
exit
interface {interface.strip()}
switchport mode access
switchport access vlan {vlan_id}
no shutdown
exit
end
"""

        st.code(config, language="text")

        st.download_button(
            "Download Configuration",
            data=config,
            file_name="switch_config.txt",
            mime="text/plain"
        )