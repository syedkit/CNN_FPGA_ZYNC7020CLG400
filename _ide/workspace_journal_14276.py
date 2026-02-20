# 2026-02-10T13:51:05.823734500
import vitis

client = vitis.create_client()
client.set_workspace(path="hls")

comp = client.create_hls_component(name = "depth",cfg_file = ["hl_co.cfg"],template = "empty_hls_component")

comp = client.get_component(name="depth")
comp.run(operation="C_SIMULATION")

comp.run(operation="SYNTHESIS")

comp.run(operation="SYNTHESIS")

comp.run(operation="SYNTHESIS")

comp.run(operation="SYNTHESIS")

comp.run(operation="C_SIMULATION")

comp.run(operation="SYNTHESIS")

comp.run(operation="PACKAGE")

vitis.dispose()

