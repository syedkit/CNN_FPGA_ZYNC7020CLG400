# 2026-02-19T21:25:16.018630400
import vitis

client = vitis.create_client()
client.set_workspace(path="hls")

vitis.dispose()

